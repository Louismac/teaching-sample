# ----------------------------------------------------------------------
# Week 4 · Exercise 09 · FIX       Concept: pasting (overwriting a slice)
# ----------------------------------------------------------------------
# PREDICT  cut is 2 beats long. The slice it's being pasted into goes
#          from beat 1 to beat 4. Are they the same size?
# RUN      python week4/exercises/ex09_paste_must_fit.py
# TASK     It crashes with a ValueError. Read the error, then fix the END
#          of the slice being pasted into, so the 2-beat harp fits
#          exactly.
# HINT     When you overwrite a slice, the new piece must be EXACTLY the
#          same length as the slice. 2 beats that start at beat 1 end at
#          beat 3.
# CHECK    No crash. You hear keys, then a burst of harp in the middle of
#          bar 1, then keys again.
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
        harp, sr = librosa.load("week4/audio/harp1.wav")
        samples_in_beat = (len(audio) // 2) // 4

        cut = harp[0:samples_in_beat * 2]
        audio[samples_in_beat:samples_in_beat * 4] = cut
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
