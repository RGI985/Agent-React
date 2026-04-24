# Agent

A simple chatbot application built with Streamlit and Google's Gemini AI.

## Description

This project implements a basic chatbot interface using Streamlit for the frontend and Google's Generative AI (Gemini) for generating responses. It supports text-based conversations and includes a placeholder for future image generation features.

## Features

- Interactive chat interface
- Streaming responses from Gemini AI
- Session-based chat history
- Text-to-speech capabilities (via gTTS, though not fully implemented in the current code)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd agent
   ```

2. Install dependencies:
   ```
   pip install -r requirement.txt
   ```
   Or if using modern Python packaging:
   ```
   pip install .
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your Google AI API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app:
```
streamlit run agent.py
```

Open your browser to the provided URL and start chatting with the bot.

## Dependencies

- google-generativeai >= 0.8.6
- gtts >= 2.5.4
- python-dotenv >= 1.2.2
- streamlit >= 1.56.0

## License

[Add license information here]