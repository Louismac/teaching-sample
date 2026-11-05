# ----------------------------------------------------------------------
# Week 4 · Exercise 01 · FIX       Concept: f-strings
# ----------------------------------------------------------------------
# PREDICT  Read the print() line. What do you think will appear in the
#          terminal?
# RUN      python week4/exercises/ex01_format_strings.py
# TASK     The terminal shows the curly brackets instead of the numbers.
#          (1) Make it a format string. (2) Show the seconds with only 2
#          decimal places.
# HINT     A format string has an f just before the opening quote:
#          f"...". Inside {}, add :.2f after a number to round it to 2
#          decimal places.
# CHECK    The terminal says: 99849 samples at 22050Hz lasts for 4.53
#          seconds
# ----------------------------------------------------------------------

from dorothy import Dorothy
import librosa
import numpy as np

dot = Dorothy(1000, 250)

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        audio, sr = librosa.load("week4/audio/drums.wav")
        num_samples = len(audio)
        print("{num_samples} samples at {sr}Hz lasts for {num_samples / sr} seconds")
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
