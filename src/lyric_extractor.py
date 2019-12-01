from lyrics_extractor import Song_Lyrics
import re


def song_lyric_extract(songtitle):
    """
    Takes in a song name as a string, searches through
    cutom engine and produces the lyrics as a string. 
    """

    extract_lyrics = Song_Lyrics("AIzaSyCtjCkXwCKC5ZPMSVk6UMvBC4kbsm-QaSE",
                                 "003304024142726018998:qpokd7ayxyi" )

    song_title, song_lyrics = extract_lyrics.get_lyrics(songtitle)

    parsed_song = re.sub("[\(\[].*?[\)\]]",  '', song_lyrics)

    return parsed_song


#example call
#print(song_lyric_extract("despacito"))
