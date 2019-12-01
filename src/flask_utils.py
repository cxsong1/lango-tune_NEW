"""
Functions for handling Flask web interface functions
"""
import os
from urllib.request import urlretrieve

from flask import request
from werkzeug import abort

from .lyric_extractor import song_lyric_extract
from .note_pitch_read import note_read
from .text_to_song import *
from .translation import translate

NAME = 'song'
LANG = 'lang'
AUDIO = 'path'
TEMP_DIR = 'temp/'

def api_call():
    song_name = request.args.get(NAME, None)
    song_lang = request.args.get(LANG, None)
    audio_file = request.args.get(AUDIO, None)
    error_str = "{}{}{}".format(
        "Missing song title. " if not song_lang else '',
        "Missing translation language. " if not song_lang else '',
        "Missing audio file path. " if not audio_file else ''
    )
    if len(error_str) > 0:
        abort(400, desc=error_str)
    lyrics = song_lyric_extract(song_name)
    # Generate lyric audio from Google Translate and Google TTS
    new_lyrics = translate(lyrics, song_lang)
    outfile_path = generate_speech(new_lyrics, song_lang, out_path=song_name+".wav")
    # Parse note information from audio file
    file_name = os.path.join(TEMP_DIR, 'song.wav')
    urlretrieve(audio_file)
    pitch_data, duration = note_read(file_name)
    outfile_path = squish_audio(outfile_path, duration, overwrite=True)
    outfile_path = pitch_audio(outfile_path, pitch_data, overwrite=True)
    # Format output
    info = {
        NAME: song_name,
        LANG: song_lang,
        AUDIO: audio_file,
        "raw_output": open(outfile_path, 'rb').read(),
        "filetype": ".wav"
    }
    return info
    