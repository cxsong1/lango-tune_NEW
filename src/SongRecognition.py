import json
from acrcloud.recognizer import ACRCloudRecognizer

"""
Recognizes and returns the name of a song given an audio/media file (ex. mp3, mp4, wav etc.)

@:param 
    filePath: string with the location of the audio file on your computer
@:return 
    The title of the song contained in the file
"""
def getTitle(filePath):
    if __name__ == '__main__':
        config = {
            'host':'identify-us-west-2.acrcloud.com',
            'access_key':'5b3f425b3e7dd719669f681b3a89193c',
            'access_secret':'pZxRsVGVIXXjZ4GPiX4nb7v33sRsTKBX2ejdlORk',
            'timeout':10 # seconds
        }
        re = ACRCloudRecognizer(config)

        songInfo = re.recognize_by_file(filePath, 0)
        songJson =json.loads(songInfo)
        print(songJson["metadata"]["music"][0]["title"])

#example call:
#getTitle(r"C:\Users\cxson\OneDrive\Documents\coeur-de-pirate-place-de-la-republique.mp3")


