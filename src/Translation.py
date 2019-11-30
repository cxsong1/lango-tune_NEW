from googletrans import Translator

"""
Translates a line of song lyrics using the googletrans API

@:param 
    lyrics: the current line of lyrics to translate
    destination_lang: the language to be translated to 
@:return
    the translated line of lyrics
"""
def translate(lyrics, destination_lang):
    translator = Translator()
    translated = translator.translate(lyrics, dest=destination_lang)
    return translated.text
""""
Breaks down the lyrics of a song into individual lines to be translated, then concatenates all the
translated strings to produce the translated lyrics of the entire song. 

@:param 
    lyrics: all the lyrics in a string from the song that we wish to translate
@:return
    string with translated lyrics for the entire song
"""
def linebreak(lyrics):
    translatedLyrics = ''
    i = 0
    startIndex = 0
    while i <len(lyrics):
        endIndex = i
        if lyrics[i] == '\n' or i == (len(lyrics)-1):
            line = translate(lyrics[startIndex:endIndex+1], 'fr')
            #line.replace('\n', '')
            translatedLyrics = translatedLyrics + ' ' + line
            startIndex = i+1
        i += 1
    return translatedLyrics


linebreak("""I love it when you call me señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true, la-la-la
Ooh, I should be runnin'
Ooh, you keep me coming for ya


Land in Miami
The air was hot from summer rain
Sweat drippin' off me
Before I even knew her name, la-la-la
It felt like ooh-la-la-la, yeah, no
Sapphire moonlight
We danced for hours in the sand
Tequila Sunrise
Her body fit right in my hands, la-la-la
It felt like ooh-la-la-la, yeah


I love it when you call me señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true, la-la-la
Ooh, I should be runnin'
Ooh, you know I love it when you call me señorita
I wish it wasn't so damn hard to leave ya
But every touch is ooh-la-la-la
It's true, la-la-la
Ooh, I should be runnin'
Ooh, you keep me coming for ya


Locked in the hotel
There's just some things that never change
You say we're just friends
But friends don't know the way you taste, la-la-la
'Cause you know it's been a long time coming
Don't ya let me fall, oh
Ooh, when your lips undress me, hooked on your tongue
Ooh, love, your kiss is deadly, don't stop


I love it when you call me señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true, la-la-la
Ooh, I should be runnin'
Ooh, you know I love it when you call me señorita
I wish it wasn't so damn hard to leave ya
But every touch is ooh-la-la-la
It's true, la-la-la
Ooh, I should be runnin'
Ooh, you keep me coming for ya


All along, I've been coming for ya
And I hope it meant something to you
Call my name, I'll be coming for ya
Coming for ya
For ya
For ya
For ya
Ooh, I should be runnin'
Ooh, you keep me coming for ya""")

