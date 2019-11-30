from googletrans import Translator


def translate(lyrics, destination_lang):
    translator = Translator()
    translated = translator.translate(lyrics, dest=destination_lang)
    return translated.text

def linebreak(lyrics):
    translatedLyrics = ''
    i = 0
    startIndex = 0
    while i <len(lyrics):
        endIndex = i
        if lyrics[i] == '\n' or i == (len(lyrics)-1):
            line = translate(lyrics[startIndex:endIndex+1], 'ru')
            #line.replace('\n', '')
            translatedLyrics = translatedLyrics + ' ' + line
            startIndex = i+1
        i += 1
    return translatedLyrics

print(linebreak("你好 \n my \n name \n is \n el diablo"))

