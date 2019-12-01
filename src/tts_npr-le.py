import note_pitch_read as npr
import text_to_song as tts
import lyric_extractor as le

song = "It's beggining to look a lot like christmas"
lyrics = le.song_lyric_extract(song)

notes, time = npr.note_read(r"C:\Users\eagub\Desktop\songstuff\song1.wav")
print(time)

new_path_1 = tts.generate_speech(lyrics, "en")

new_path_2 = tts.squish_audio(new_path_1, time)

new_song= tts.pitch_audio(new_path_2, notes)

