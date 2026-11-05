# ----------------------------------------------------------------------
# Week 4 · Exercise 02 · MODIFY    Concept: slicing with [start:end]
# ----------------------------------------------------------------------
# PREDICT  sr is the number of samples in ONE second. How much audio is
#          audio[:sr]?
# RUN      python week4/exercises/ex02_the_last_two_seconds.py
# TASK     At the moment it plays the first second. Change the slice so
#          it plays only the LAST TWO seconds of the file.
# HINT     A negative number counts back from the end: audio[-n:] means
#          "the last n items".
# CHECK    The waveform is the end of the drum loop and the terminal says
#          2.00 seconds.
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
        clip = audio[:sr]
        print(f"clip lasts {len(clip) / sr:.2f} seconds")
        dot.music.start_sample_stream(clip, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
