import text_to_song as tts
import lyric_extractor as le
from pydub import AudioSegment

song = "It's beggining to look a lot like christmas"
lyrics = le.song_lyric_extract(song)


time = 90

#time = 207


new_path_1 = tts.generate_speech(lyrics, "fr")

new_path_2 = tts.squish_audio(new_path_1, time)


sound1 = AudioSegment.from_file(new_path_2)

sound2 = AudioSegment.from_file(r"C:\Users\eagub\Documents\GitHub\lango-tune\src\temp\song1_inst.wav")

one_sec_segment = AudioSegment.silent(duration=4000)

sound3 = one_sec_segment + sound1

song_10_db_quierter = sound2 - 15

combined = sound3.overlay(song_10_db_quierter)

combined.export(r"C:\Users\eagub\Documents\GitHub\lango-tune\src\temp\new_song.wav", format='wav')

