import sys
from aubio import source, pitch
import soundfile as sf

def get_pitches(filename):

    """
    Take in the filename (was audio file) as a string ex: "song1.wav"

    Returns [(time is seconds, pitch in frequency I think)], total time
    """

    #def get_pitches(filename):
        

    downsample = 1
    samplerate = 44100 // downsample
    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

    win_s = 4096 // downsample # fft size
    hop_s = 512  // downsample # hop size

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    pitch_tuple=[]

    #getting overall song length
    file = sf.SoundFile(filename)
    total_time = len(file) / file.samplerate
    
    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        pt = pitch_o(samples)[0]
        pt = int(round(pt))
        confidence = pitch_o.get_confidence()
        pitch_tuple.append((total_frames / float(samplerate),pt))
        #if confidence < 0.8: pitch = 0.
        #print("%f %f %f" % (total_frames / float(samplerate), pt, confidence))
        pitches += [pitch]
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break
        
    return pitch_tuple,total_time
    

print(get_pitches("song1_4.wav"))


