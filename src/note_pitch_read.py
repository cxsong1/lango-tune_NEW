import sys
from aubio import source, notes


def note_read(filename):
    """
    Take in the filepath to an audio file as a string
    

    Returns [(time in seconds divided by total time,
    note in frequency I think)], total time
    """
        
    downsample = 1
    samplerate = 44100 // downsample
    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

    win_s = 512 // downsample # fft size
    hop_s = 256 // downsample # hop size

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    total_time = s.duration/float(samplerate)

    tolerance = 0.8

    notes_o = notes("default", win_s, hop_s, samplerate)

    pitch_tuple=[]

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        new_note = notes_o(samples)
        if (new_note[0] != 0):
            note_str = ' '.join(["%.2f" % i for i in new_note])
            pitch_tuple.append(((total_frames/float(samplerate))/total_time ,
                               new_note[0]))
            #for debugging purposes
            #print("%.6f" % (total_frames/float(samplerate)), new_note[0])
        total_frames += read
        if read < hop_s: break
    return pitch_tuple, total_time

#example call
#print(note_read(r"C:\Users\eagub\Desktop\songstuff\song1_4.wav"))
#r'C:\Users\eagub\Desktop\songstuff\song1_4.wav'


def get_pitches(filename):

    """
    Take in the filepath to an audio file as a string ex: "song1.wav"

    Returns [(time is seconds divided by total time, pitch in frequency I think)], total time
    """
        
    downsample = 1
    samplerate = 44100 // downsample
    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

    win_s = 4096 // downsample # fft size
    hop_s = 512  // downsample # hop size

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    total_time = s.duration/float(samplerate)

    tolerance = 0.8

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)


    pitch_tuple=[]
    
    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        pt = pitch_o(samples)[0]
        pt = int(round(pt))
        total_frames += read
        pitch_tuple.append(((total_frames / float(samplerate))/total_time,pt))
        #for debugging purposes
        #print("%f %f %f" % (total_frames / float(samplerate), pt))
        
        if read < hop_s: break
        
    return pitch_tuple,total_time
    
#example call
#print(get_pitches(r"C:\Users\eagub\Desktop\songstuff\song1_4.wav"))

