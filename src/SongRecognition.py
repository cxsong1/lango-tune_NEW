import json
from acrcloud.recognizer import ACRCloudRecognizer

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

getTitle(r"C:\Users\cxson\OneDrive\Documents\song1_4.wav")


