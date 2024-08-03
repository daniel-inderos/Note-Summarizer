from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pydub import AudioSegment
import openai
import os
import yt_dlp
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB

def split_audio(audio_path, max_size):
    logging.debug(f"Splitting audio: {audio_path}")
    audio = AudioSegment.from_file(audio_path)
    chunks = []
    current_chunk = AudioSegment.empty()
    current_size = 0

    for i in range(0, len(audio), 1000):  # Iterate over audio in 1-second intervals
        chunk = audio[i:i + 1000]
        chunk_size = len(chunk.raw_data)

        if current_size + chunk_size > max_size:
            chunks.append(current_chunk)
            current_chunk = chunk
            current_size = chunk_size
        else:
            current_chunk += chunk
            current_size += chunk_size

    # Append the last chunk if it's not empty
    if len(current_chunk) > 0:
        chunks.append(current_chunk)

    logging.debug(f"Number of chunks created: {len(chunks)}")
    return chunks

def transcribe_audio_chunk(audio_chunk, api_key):
    with open('temp_chunk.wav', 'wb') as f:
        audio_chunk.export(f, format='wav')
    
    with open('temp_chunk.wav', 'rb') as audio_file:
        response = requests.post(
            'https://api.openai.com/v1/audio/transcriptions',
            headers={
                'Authorization': f'Bearer {api_key}',
            },
            files={
                'file': audio_file,
                'model': (None, 'whisper-1'),
            }
        )
    transcription_data = response.json()
    logging.debug(f"Transcription response: {transcription_data}")
    return transcription_data.get('text', '')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    api_key = request.headers.get('Authorization').split(' ')[1]
    audio_file = request.files['audio']
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)

    logging.debug("Audio file saved, starting transcription")
    chunks = split_audio(audio_path, MAX_FILE_SIZE)
    transcription = ""

    for chunk in chunks:
        transcription += transcribe_audio_chunk(chunk, api_key) + " "

    logging.debug("Transcription complete")
    return jsonify({'transcription': transcription.strip()})

@app.route('/transcribe_youtube', methods=['POST'])
def transcribe_youtube():
    data = request.get_json()
    url = data.get('url', '')
    api_key = request.headers.get('Authorization').split(' ')[1]

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    logging.debug(f"Downloading audio from YouTube URL: {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(id)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        audio_path = ydl.prepare_filename(info_dict).replace('webm', 'wav')

    logging.debug(f"Audio downloaded to: {audio_path}")
    chunks = split_audio(audio_path, MAX_FILE_SIZE)
    transcription = ""

    for chunk in chunks:
        transcription += transcribe_audio_chunk(chunk, api_key) + " "

    logging.debug("Transcription complete")
    return jsonify({'transcription': transcription.strip()})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    api_key = request.headers.get('Authorization').split(' ')[1]

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    logging.debug("Starting summarization")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text into Cornell notes format:\n\n{text}"}
        ],
        max_tokens=150,
        temperature=0.5
    )

    summary = response.choices[0].message['content'].strip()
    logging.debug("Summarization complete")
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
