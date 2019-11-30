import speech_recognition as sr
from pydub import AudioSegment

from lyrics_extractor import Song_Lyrics
import re



##
##sound_file = "song1_4.wav"
##
### use sound_file as source
##r = sr.Recognizer()
##with sr.AudioFile(sound_file) as source:
##    audio = r.record(source)  # read the entire audio file
##
##
##print("Transcription: " + r.recognize_google(audio))
##


def song_lyric_extract(songtitle):
    

    extract_lyrics = Song_Lyrics("AIzaSyCtjCkXwCKC5ZPMSVk6UMvBC4kbsm-QaSE",
                                 "003304024142726018998:qpokd7ayxyi" )

    song_title, song_lyrics = extract_lyrics.get_lyrics(songtitle)

    parsed_song = re.sub("[\(\[].*?[\)\]]",  '', song_lyrics)

    return parsed_song



