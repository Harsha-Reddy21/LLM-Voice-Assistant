# AI Voice Chatbot

## Summary
This AI Voice Chatbot is an interactive voice-based assistant built using Streamlit, OpenAI's Whisper API for speech-to-text, ChatGPT for conversational AI, and OpenAI's TTS for text-to-speech conversion. Users can speak to the chatbot, which transcribes their speech, processes the input through ChatGPT, and responds with generated speech.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- A valid OpenAI API key

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key:
   - Create a `.env` file in the project root and add:
     ```
     OPENAI_APIKEY=your_api_key_here
     ```

## Running the Chatbot
1. Start the chatbot:
   ```bash
   streamlit run app.py
   ```
2. Click on **Start Recording**, speak into your microphone, and wait for the response.
3. Click **Stop Recording** when done.
4. View conversation history on the Streamlit interface.

## Approach Explanation (Step-by-Step)

### 1. Recording User Audio
- When the user clicks **Start Recording**, the `record_audio` function records audio for a fixed duration.
- The recorded audio is saved in a temporary buffer in WAV format.

### 2. Speech-to-Text Conversion
- The recorded audio is sent to OpenAI's Whisper API via `transcribe_audio`.
- Whisper transcribes the spoken words into text.

### 3. Generating Chatbot Response
- The transcribed text is sent to ChatGPT via `get_chatgpt_response`.
- The response is generated while maintaining conversation history.

### 4. Text-to-Speech Conversion
- The chatbot's response is converted into speech using OpenAI's TTS API.
- The MP3 audio is played back to the user.

### 5. Conversation History
- Each interaction (user speech and chatbot response) is stored in `st.session_state.history`.
- The history is displayed in the Streamlit interface.

## Features
✅ Real-time speech recognition
✅ AI-generated responses using ChatGPT
✅ Text-to-speech conversion for audio playback
✅ Conversation history tracking
✅ Interactive Streamlit UI

## Future Enhancements
- Support for multiple languages
- Custom voice options for responses
- Adjustable recording duration

## Troubleshooting
- If audio recording doesn't work, check microphone permissions.
- Ensure the OpenAI API key is correctly set up in `.env`.
- If responses take too long, verify internet connectivity and API availability.

---
Enjoy using the AI Voice Chatbot! 🎙️🤖

