import sys

import crepe
import numpy as np
from scipy.io import wavfile


def note_read(filename, interval=20, delta=2):
    """
    Take in the filepath to an audio file as a string

    Returns [(time in seconds divided by total time,
    note in frequency I think)], total time
    """
    sr, audio = wavfile.read(filename)
    time, frequency, _, _, = crepe.predict(audio, sr, model_capacity='small')
    notes = []
    avg_f = 1
    prev_idx = 0
    curr_idx = min(interval, frequency.size)
    while curr_idx < frequency.size:
        new_f = np.sum(frequency[prev_idx:curr_idx])
        if new_f/avg_f > delta:
            notes.append(time[prev_idx], new_f)
            avg_f = new_f
        prev_idx = curr_idx
        curr_idx += interval
    
    return notes, time[-1]
