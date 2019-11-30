"""
Functions to generate and manipulate spoken audio files
from multi-lingual text
"""
import os

import librosa
import soundfile as sf
from gtts import gTTS

DEFAULT_DIR = "temp/"
DEFAULT_FILE = "tts_audio"
FILE_TYPE = ".wav"
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
        num = str((max(existing_nums) if existing_nums else -1) + 1)
        out_path = os.path.join(DEFAULT_DIR, f"{DEFAULT_FILE}{SEP}{num}{FILE_TYPE}")
    # Use gTTS module functions lol
    tts = gTTS(message, lang=lang)
    tts.save(out_path)

def squish_audio(file_path, duration, overwrite=False):
    """
    Squeezes (or stretches) an audio file to match the desired duration

    file_path: path to audio file
    duration: desired duration in seconds
    overwrite: whether or not to override the file
    """
    try:
        time_series, sample_rate = librosa.load(file_path)
    except FileNotFoundError:
        print(f"squish_audio: provided file does not exist: {file_path}")
    else:
        old_duration = librosa.get_duration(time_series)
        desired_ratio = duration/old_duration
        new_ts = librosa.effects.time_stretch(time_series, desired_ratio)
        # Rename output file if do not wish to overwrite
        if not overwrite:
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}{SEP}{duration}{file_extension}"
        # Save output file
        sf.write(file_path, new_ts, sample_rate)
