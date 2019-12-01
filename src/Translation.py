from googletrans import Translator

"""
Translates a line of song lyrics using the googletrans API

@:param 
    lyrics: the current line of lyrics to translate
    destination_lang: the language we want to translate to 
@:return
    the translated line of lyrics
"""
def translate(lyrics, destination_lang):
    translator = Translator()
    translated = translator.translate(lyrics, dest=destination_lang)
    return translated.text
"""
Breaks down the lyrics of a song into individual lines to be translated, then concatenates all the
translated strings to produce the translated lyrics of the entire song. 

@:param 
    lyrics: all the lyrics in a string from the song that we wish to translate
    destination_lang: the language we want to translate to
@:return
    string with translated lyrics for the entire song
"""
def linebreak(lyrics, destination_lang):
    translatedLyrics = ''
    i = 0
    startIndex = 0
    while i <len(lyrics):
        endIndex = i
        if lyrics[i] == '\n' or i == (len(lyrics)-1):
            line = translate(lyrics[startIndex:endIndex+1], destination_lang)
            #line.replace('\n', '')
            translatedLyrics = translatedLyrics + ' ' + line
            startIndex = i+1
        i += 1
    return translatedLyrics