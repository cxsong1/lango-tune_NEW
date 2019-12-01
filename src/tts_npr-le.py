import text_to_song as tts
import lyric_extractor as le

song = "It's beggining to look a lot like christmas"
lyrics = le.song_lyric_extract(song)

time = 207

new_path_1 = tts.generate_speech(lyrics, "en")

new_path_2 = tts.squish_audio(new_path_1, time)

