"""
Functions to generate and manipulate spoken audio files
from multi-lingual text
"""
import math
import os

import librosa
import numpy as np
import soundfile as sf
from gtts import gTTS

DEFAULT_DIR = "temp/"
if not os.path.isdir(DEFAULT_DIR):
    os.mkdir(DEFAULT_DIR)

DEFAULT_FILE = "tts_audio"
FILE_TYPE = ".wav"
SEP = '_'
COPY = 'copy'

def parse_name(file_path):
    file_name.split(SEP)

def generate_speech(message, lang, out_path=None):
    """
    Saves text-to-speech audio interpretation of <message>
    via Google Text to Speech

    message: string to speak
    lang: language of message if known (IETF language tag)
    out_path: where to save file

    returns: output file path
    """
    out_path = os.path.join(DEFAULT_DIR, out_path or f"{DEFAULT_FILE}{SEP}{COPY}{FILE_TYPE}")
    # Use gTTS module functions lol
    tts = gTTS(message, lang=lang)
    tts.save(out_path)
    return out_path

def squish_audio(file_path, duration, overwrite=False):
    """
    Squeezes (or stretches) an audio file to match the desired duration

    file_path: path to audio file
    duration: desired duration in seconds
    overwrite: whether or not to override the file

    returns: output file path
    """
    try:
        time_series, sample_rate = librosa.load(file_path)
    except FileNotFoundError:
        print(f"squish_audio: provided file does not exist: {file_path}")
        return None
    else:
        old_duration = librosa.get_duration(time_series)
        speed = old_duration/duration
        new_ts = librosa.effects.time_stretch(time_series, speed)
        # Rename output file if do not wish to overwrite
        if not overwrite:
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}{SEP}{int(round(duration))}{file_extension}"
        # Save output file
        sf.write(file_path, new_ts, sample_rate)
        return file_path

def pitch_audio(file_path, pitch_data, overwrite=False):
    """
    Applies pitches to audio data

    file_path: path to audio file
    pitch_data: list of (<relative time (t/duration)>, <pitch (Hz)>)
    overwrite: whether or not to override the file

    returns: output file path
    """
    try:
        time_series, sample_rate = librosa.load(file_path)
    except FileNotFoundError:
        print(f"pitch_audio: provided file does not exist: {file_path}")
        return None
    else:
        print(f"pitch_audio: parsing pitch_data containing {len(pitch_data)} notes with time_series of shape {time_series.shape}")
        duration = librosa.get_duration(time_series)
        pitch_time_bins = []
        prev_idx = 0
        num_bins = time_series.size
        # Add final data point matching last data point in time series at end of duration
        pitch_data = [pitch_data[i] for i in range(len(pitch_data)) if i % 5 == 0]
        pitch_data.append((1, pitch_data[-1][1]))
        # Slice audio time series into bins based on pitch_data
        for rel_t, pitch in pitch_data:
            curr_idx = int(math.floor(rel_t*num_bins))
            pitch_time_bins.append((
                pitch,
                time_series[prev_idx:curr_idx]))
            prev_idx = curr_idx
        # Apply pitching to individual bins
        pitched_audio_ts = np.asarray([])
        for pitch, ts in pitch_time_bins:
            # Estimate current pitch of bin (find largest peak in FFT)
            pt, mg = librosa.piptrack(ts, sample_rate)
            pt = np.sum(pt, axis=1)
            mg = np.sum(mg, axis=1)
            curr_p = pt[np.where(mg == np.max(mg))[0]][0]
            # Find number of steps to requested pitch (in semitones)
            if curr_p:
                delta = 12 * math.log2(8*pitch/curr_p)
            else:
                delta = 0 # Avoid division by 0 for silence
            print(delta)
            # Shift pitch and append to new time series
            pitched_audio_ts = np.append(
                pitched_audio_ts,
                librosa.effects.pitch_shift(
                    ts,
                    sample_rate,
                    delta
                )
            )
        if not overwrite:
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}{SEP}pitched{file_extension}"
        # Save output file
        sf.write(file_path, pitched_audio_ts, sample_rate)
        return file_path
