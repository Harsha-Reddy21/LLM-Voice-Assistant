import streamlit as st
import io
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from helper import transcribe_audio, get_chatgpt_response, text_to_speech
import time

st.title("🎙️ AI Voice Chatbot")
st.write("Ask me anything, and I'll respond with my voice!")

def record_audio(duration=10, samplerate=44100):
    """Record audio for a fixed duration."""
    st.write("🎤 Recording... Speak now!")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    st.write("✅ Recording complete!")
    
    buffer = io.BytesIO()
    wav.write(buffer, samplerate, audio_data)
    buffer.seek(0)
    return buffer


if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'history' not in st.session_state:
    st.session_state.history = []

if st.button("🎙️ Start Recording"):
    st.session_state.recording = True
    while st.session_state.recording:
        audio_file = record_audio()
        st.audio(audio_file, format="audio/wav")
        transcript_text = transcribe_audio(audio_file)
        st.write(f"📝 You said: **{transcript_text}**")

        bot_reply = get_chatgpt_response(transcript_text)
        st.write(f"🤖 Chatbot: **{bot_reply}**")

        audio_response = text_to_speech(bot_reply)
        st.audio(audio_response, format="audio/mp3")

        st.session_state.history.append({
            "You said": transcript_text,
            "Chatbot": bot_reply
        })

        time.sleep(30)

if st.session_state.history:
    st.write("### Conversation History")
    for i, entry in enumerate(st.session_state.history, 1):
        st.write(f"**Turn {i}**")
        st.write(f"📝 You said: **{entry['You said']}**")
        st.write(f"🤖 Chatbot: **{entry['Chatbot']}**")
        st.write("---")

if st.button("🎤 Stop Recording"):
    st.session_state.recording = False
    st.write("🛑 Recording stopped.")

st.write(f"Recording Status: {'Active' if st.session_state.recording else 'Inactive'}")