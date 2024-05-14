# Note Summarizer

Note Summarizer is a web application that allows users to transcribe audio recordings and YouTube videos into text, and then summarize the text into Cornell notes format. Users can input their own OpenAI API key to use the transcription and summarization services.

## Features

- Record audio directly in the browser and transcribe it.
- Transcribe audio from YouTube videos.
- Summarize transcriptions into Cornell notes format.
- Save and load notes locally using browser storage.
- User-provided OpenAI API key for personalization.

## Technologies Used

- Flask
- Pydub
- yt-dlp
- OpenAI API
- HTML/CSS/JavaScript

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. Set your OpenAI API key in an environment variable:

   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `your-username` and `your-repository` with your GitHub username and repository name, and `your_openai_api_key` with your actual OpenAI API key when testing locally.

This `README.md` provides a comprehensive guide to setting up, running, and deploying your application. It should be helpful for other developers or users who want to understand and use your project.
