"""
Native Audio Speech Synthesis for DharaniAI.
Supports Telugu (te), Hindi (hi), Marathi (mr), Kannada (kn), and English (en).
Generates audio files that play directly in the Streamlit UI.
"""

import os
import re
import tempfile
from typing import Optional

def generate_native_speech(text: str, lang: str = "te") -> Optional[str]:
    """
    Synthesizes speech into an MP3 file using gTTS.
    Falls back gracefully to offline pyttsx3 if internet is absent.
    Returns the filepath of the generated audio.
    """
    # Clean markdown headers, asterisks, and emojis for clear voice synthesis
    clean_text = re.sub(r'[*#_`>~]', '', text)
    clean_text = re.sub(r'[^\w\s.,;:?!()-]', ' ', clean_text)
    clean_text = ' '.join(clean_text.split())
    
    # Limit speech length for responsive voice playback (~first 600 chars of actionable summary)
    if len(clean_text) > 700:
        clean_text = clean_text[:700] + "..."

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = tmp_file.name
    tmp_file.close()

    try:
        from gtts import gTTS
        tts = gTTS(text=clean_text, lang=lang, slow=False)
        tts.save(tmp_path)
        return tmp_path
    except Exception:
        # Fallback to local Windows offline speech engine (SAPI5 via pyttsx3)
        try:
            import pyttsx3
            wav_path = tmp_path.replace(".mp3", ".wav")
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.save_to_file(clean_text, wav_path)
            engine.runAndWait()
            return wav_path
        except Exception:
            return None
