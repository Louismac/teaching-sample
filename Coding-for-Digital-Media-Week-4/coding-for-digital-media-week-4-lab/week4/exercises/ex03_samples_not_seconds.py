# ----------------------------------------------------------------------
# Week 4 · Exercise 03 · FIX       Concept: indexes are samples, not seconds
# ----------------------------------------------------------------------
# PREDICT  This is meant to cut from 1 second to 3 seconds. Look at what
#          the print() says. How many samples is audio[1:3]?
# RUN      python week4/exercises/ex03_samples_not_seconds.py
# TASK     It plays (almost) nothing. Fix the slice so it really cuts out
#          second 1 to second 3.
# HINT     Slice numbers count SAMPLES. One second is sr samples, so 3
#          seconds is sr * 3 samples.
# CHECK    The terminal says the clip is 44100 samples (2.00 seconds) and
#          you hear drums.
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
        clip = audio[1:3]
        print(f"clip is {len(clip)} samples, {len(clip) / sr:.2f} seconds")
        dot.music.start_sample_stream(clip, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
