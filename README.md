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
- Git
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) (if deploying to Heroku)
- [Vercel CLI](https://vercel.com/docs/cli) (if deploying to Vercel)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/) (if deploying to Netlify)

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

### Deployment

#### Deploying to Vercel

1. Install Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Create a `vercel.json` configuration file:

   ```json
   {
     "version": 2,
     "builds": [
       { "src": "app.py", "use": "@vercel/python" }
     ],
     "routes": [
       { "src": "/(.*)", "dest": "app.py" }
     ]
   }
   ```

3. Deploy to Vercel:

   ```bash
   vercel
   ```

4. Set the environment variable in Vercel:

   - Go to your project dashboard on Vercel.
   - Navigate to "Settings" > "Environment Variables".
   - Add your `OPENAI_API_KEY` environment variable.

#### Deploying to Netlify

1. Install Netlify CLI:

   ```bash
   npm install -g netlify-cli
   ```

2. Create a `netlify.toml` configuration file:

   ```toml
   [build]
     command = "pip install -r requirements.txt && python app.py"
     publish = "."

   [[redirects]]
     from = "/*"
     to = "/index.html"
     status = 200
   ```

3. Deploy to Netlify:

   ```bash
   netlify deploy --prod
   ```

4. Set the environment variable in Netlify:

   - Go to your project dashboard on Netlify.
   - Navigate to "Site settings" > "Build & deploy" > "Environment".
   - Add your `OPENAI_API_KEY` environment variable.

## Usage

1. Open the application in your web browser.
2. Enter your OpenAI API key.
3. Record audio or enter a YouTube URL to transcribe.
4. Click "Summarize" to get a summary in Cornell notes format.
5. Save and load your notes using the provided buttons.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `your-username` and `your-repository` with your GitHub username and repository name, and `your_openai_api_key` with your actual OpenAI API key when testing locally.

This `README.md` provides a comprehensive guide to setting up, running, and deploying your application. It should be helpful for other developers or users who want to understand and use your project.
