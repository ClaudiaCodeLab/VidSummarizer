# VidSummarizer

[![Sync to Hugging Face hub](https://github.com/ClaudiaCodeLab/VidSummarizer/tree/main/.github/workflows/main.yml/badge.svg)](https://github.com/ClaudiaCodeLab/VidSummarizer/tree/main/.github/workflows/main.yml)

VidSummarizer is a YouTube video summarization app using the OpenAI API.

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python app.py
```

## Features
- OpenAI API (via LangChain)
- Separate buttons to get transcript and summarize
- Auto-fallback to Spanish if English is unavailable
- Smaller, app-style buttons with exact label fit
- Compatible with Gradio 4.44.1

## API Key Management
Do **not** commit `.env` files containing your API keys to version control.
- Use environment variables in production.
- In Hugging Face Spaces, set the `OPENAI_API_KEY` in the **Settings** tab.

## Deployment
Deploy on Hugging Face Spaces for public access.
