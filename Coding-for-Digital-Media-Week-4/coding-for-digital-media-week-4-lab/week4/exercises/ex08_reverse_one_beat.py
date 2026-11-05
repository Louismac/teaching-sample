# ----------------------------------------------------------------------
# Week 4 · Exercise 08 · MODIFY    Concept: np.flip() on a slice
# ----------------------------------------------------------------------
# PREDICT  np.flip() reverses a whole list. What will this drum loop
#          sound like?
# RUN      python week4/exercises/ex08_reverse_one_beat.py
# TASK     Only reverse the LAST BEAT of the loop. Everything else should
#          play forwards. Change one line.
# HINT     audio[-samples_in_beat:] is the last beat. Flip that slice and
#          write it back into the same place.
# CHECK    The loop plays normally, then the very last hit swooshes
#          backwards.
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
        samples_in_beat = (len(audio) // 2) // 4
        audio = np.flip(audio)
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
