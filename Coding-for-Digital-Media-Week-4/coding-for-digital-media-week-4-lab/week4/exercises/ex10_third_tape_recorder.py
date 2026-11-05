# ----------------------------------------------------------------------
# Week 4 · Exercise 10 · FIX       Concept: pasting into a blank timeline and mixing
# ----------------------------------------------------------------------
# PREDICT  timeline starts as 12 seconds of silence (zeros). The drums go
#          in at 0 seconds. Where does the harp go, and what happens to
#          the drums underneath it?
# RUN      python week4/exercises/ex10_third_tape_recorder.py
# TASK     (1) Make the harp start at 4 seconds instead of 0. (2) MIX the
#          harp in with what's already there, instead of replacing it.
# HINT     Mixing is adding: timeline[start:end] + harp. Then put the
#          result back into timeline[start:end].
# CHECK    Drums on their own, then the harp comes in at 4 seconds while
#          the last of the drums is still playing.
# ----------------------------------------------------------------------

from dorothy import Dorothy
import librosa
import numpy as np

dot = Dorothy(1000, 250)

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        drums, sr = librosa.load("week4/audio/drums.wav")
        harp, sr = librosa.load("week4/audio/harp1.wav")
        timeline = np.zeros(sr * 12, dtype=np.float32)

        # paste the drums at 0 seconds
        timeline[0:len(drums)] = drums

        # paste the harp
        start = sr * 0
        end = start + len(harp)
        timeline[start:end] = harp

        dot.music.start_sample_stream(timeline, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
