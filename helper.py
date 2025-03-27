import openai
import io
import tempfile
import os
from dotenv import load_dotenv

def create_openai_client(api_key):
    """Initialize and return an OpenAI client with the provided API key."""
    return openai.OpenAI(api_key=api_key)

load_dotenv()
api_key = os.getenv("OPENAI_APIKEY")
client = create_openai_client(api_key)

def transcribe_audio(file):
    """Convert an in-memory audio file to text using OpenAI's Whisper API."""
    temp_audio_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(file.read())  
            temp_audio_path = temp_audio.name

        with open(temp_audio_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response.text
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}")
    finally:
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)

conversation_history = []

def get_chatgpt_response(prompt):
    """Get response from OpenAI's ChatGPT API with memory support."""
    try:
        conversation_history.append({"role": "user", "content": prompt})
        max_history_length = 10 
        if len(conversation_history) > max_history_length:
            conversation_history.pop(0)  

        response = client.chat.completions.create(
            model="gpt-4",
            messages=conversation_history  
        )
        assistant_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_response})

        return assistant_response
    except openai.OpenAIError as e:
        raise RuntimeError(f"OpenAI API Error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"ChatGPT response failed: {str(e)}")

def text_to_speech(text):
    """Convert text to speech using OpenAI's TTS API and return an MP3 audio byte stream."""
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        audio_io = io.BytesIO(response.content)
        audio_io.seek(0)
        return audio_io.getvalue()
    except Exception as e:
        raise Exception(f"Text-to-speech conversion failed: {str(e)}")