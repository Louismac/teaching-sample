# ----------------------------------------------------------------------
# Week 4 · Exercise 07 · MODIFY    Concept: item-wise multiplication with a ramp
# ----------------------------------------------------------------------
# PREDICT  ramp goes smoothly from 0 to 1 and is the same length as
#          audio. What happens when you multiply the two together?
# RUN      python week4/exercises/ex07_fade_out.py
# TASK     This makes a fade IN. Change ONE line to make it fade OUT
#          instead.
# HINT     np.linspace(start, end, how_many). Which way does the ramp
#          need to go?
# CHECK    The waveform starts big and shrinks to nothing at the end.
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
        ramp = np.linspace(0, 1, len(audio), dtype=np.float32)
        audio = audio * ramp
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
