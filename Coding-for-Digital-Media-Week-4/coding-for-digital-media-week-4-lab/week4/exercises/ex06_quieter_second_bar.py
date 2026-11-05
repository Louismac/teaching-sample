# ----------------------------------------------------------------------
# Week 4 · Exercise 06 · MODIFY    Concept: maths on part of a list
# ----------------------------------------------------------------------
# PREDICT  audio * 0.2 multiplies EVERY sample by 0.2. What will the
#          whole waveform look like?
# RUN      python week4/exercises/ex06_quieter_second_bar.py
# TASK     Make only the SECOND bar quieter and leave the first bar at
#          full volume. Change one line.
# HINT     You can do maths on a slice and put it back into the same
#          slice: audio[a:b] = audio[a:b] * 0.2
# CHECK    The left half of the waveform is tall and the right half is
#          small.
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
        half = len(audio) // 2
        audio = audio * 0.2
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
