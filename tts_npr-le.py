import src.text_to_song as tts
import src.lyric_extractor as le
import src.note_pitch_read as npr

filename = ""

song = "It's beginning to look a lot like christmas"
lyrics = le.song_lyric_extract(song)
pitch_data, time = npr.note_read(filename)
new_path_1 = tts.generate_speech(lyrics, "en")
new_path_2 = tts.squish_audio(new_path_1, time)
new_song= tts.pitch_audio(new_path_2, pitch_data)
