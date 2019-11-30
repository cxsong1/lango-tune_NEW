"""
Functions to generate and manipulate spoken audio files
from multi-lingual text
"""
import os
from gtts import gTTS

DEFAULT_DIR = "temp/"
DEFAULT_FILE = "tts_audio"
FILE_TYPE = ".mp3"
SEP = '_'

def generate_speech(message, lang, out_path=None):
    """
    Saves text-to-speech audio interpretation of <message>
    via Google Text to Speech

    message: string to speak
    lang: language of message if known (IETF language tag)
    out_path: where to save file
    """
    if not out_path:
        existing_nums = [
            int(os.path.splitext(f.split(SEP)[-1])[0])
            for f in os.listdir(DEFAULT_DIR)]
        num = str((max(existing_nums) if existing_nums else 0) + 1)
        out_path = os.path.join(DEFAULT_DIR, f"{DEFAULT_FILE}{SEP}{num}{FILE_TYPE}")
    # Use gTTS module functions lol
    tts = gTTS(message, lang=lang)
    tts.save(out_path)