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
DEFAULT_FILE = "tts_audio"
FILE_TYPE = ".wav"
SEP = '_'

def generate_speech(message, lang, out_path=None):
    """
    Saves text-to-speech audio interpretation of <message>
    via Google Text to Speech

    message: string to speak
    lang: language of message if known (IETF language tag)
    out_path: where to save file

    returns: output file path
    """
    if not out_path:
        existing_nums = [
            int(os.path.splitext(f.split(SEP)[-1])[0])
            for f in os.listdir(DEFAULT_DIR)]
        num = str((max(existing_nums) if existing_nums else -1) + 1)
        out_path = os.path.join(DEFAULT_DIR, f"{DEFAULT_FILE}{SEP}{num}{FILE_TYPE}")
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
        desired_ratio = duration/old_duration
        new_ts = librosa.effects.time_stretch(time_series, desired_ratio)
        # Rename output file if do not wish to overwrite
        if not overwrite:
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}{SEP}{duration}{file_extension}"
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
        print(f"pitch_audio: parsing pitch_data containing {len(pitch_data)} notes with time_series of length{time_series.shape[1]}")
        duration = librosa.get_duration(time_series)
        pitch_time_bins = []
        prev_t = 0
        # Add final data point matching last data point in time series at end of duration
        pitch_data.append((1, pitch_data[-1][1]))
        # Slice audio time series into bins based on pitch_data
        for rel_t, pitch in pitch_data:
            curr_t = rel_t * duration
            pitch_time_bins.append((
                pitch,
                time_series[:][prev_t:curr_t]))
            prev_t = curr_t
        # Apply pitching to individual bins
        pitched_audio_ts = []
        for pitch, ts in pitch_time_bins:
            # Estimate current pitch of bin (find largest peak in FFT)
            pt, mg = librosa.piptrack(ts, sample_rate)
            pt = np.sum(pt, axis=1)
            mg = np.sum(mg, axis=1)
            curr_p = pt[np.where(mg == np.max(mg))[0]]
            # Find number of steps to requested pitch (in semitones)
            delta = 12 * math.log2(pitch/curr_p)
            # Shift pitch and append to new time series
            pitched_audio_ts.append(librosa.effects.pitch_shift(
                ts,
                sample_rate,
                delta
            ))
        pitched_audio_ts = np.asarray(pitched_audio_ts)
        if not overwrite:
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}{SEP}pitched{file_extension}"
        # Save output file
        sf.write(file_path, pitched_audio_ts, sample_rate)
        return file_path
