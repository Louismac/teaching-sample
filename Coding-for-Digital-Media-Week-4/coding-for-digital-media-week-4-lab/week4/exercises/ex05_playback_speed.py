# ----------------------------------------------------------------------
# Week 4 · Exercise 05 · FIX       Concept: sample rate controls speed and pitch
# ----------------------------------------------------------------------
# PREDICT  speed is 2, so the samples play back at sr * 2. Will it sound
#          higher or lower? Longer or shorter?
# RUN      python week4/exercises/ex05_playback_speed.py
# TASK     (1) Make it play at HALF speed. (2) The printed length is
#          wrong because it ignores speed. Fix it so it prints how long
#          it really plays for.
# HINT     If you play the same samples at a different rate, the time it
#          takes is samples / (sr * speed).
# CHECK    It sounds slower and deeper, and the terminal says 12.80
#          seconds.
# ----------------------------------------------------------------------

from dorothy import Dorothy
import librosa
import numpy as np

dot = Dorothy(1000, 250)

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        audio, sr = librosa.load("week4/audio/keys4.wav")
        speed = 2
        print(f"this will play for {len(audio) / sr:.2f} seconds")
        dot.music.start_sample_stream(audio, sr=sr * speed)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
