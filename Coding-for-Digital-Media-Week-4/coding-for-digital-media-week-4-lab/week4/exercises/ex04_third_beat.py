# ----------------------------------------------------------------------
# Week 4 · Exercise 04 · MODIFY    Concept: slicing by musical time
# ----------------------------------------------------------------------
# PREDICT  The loop is 2 bars of 4 beats. samples_in_beat is how many
#          samples one beat lasts. Which beat does
#          audio[0:samples_in_beat] cut out?
# RUN      python week4/exercises/ex04_third_beat.py
# TASK     Change the slice so it cuts out the THIRD beat instead of the
#          first.
# HINT     Beat 1 starts at 0 x samples_in_beat. Beat 2 starts at 1 x
#          samples_in_beat. So where do beat 3's start and end go?
# CHECK    You hear a different single hit looping, and the terminal
#          still shows the same number of samples.
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
        samples_in_bar = len(audio) // 2
        samples_in_beat = samples_in_bar // 4
        beat = audio[0:samples_in_beat]
        print(f"one beat is {len(beat)} samples")
        dot.music.start_sample_stream(beat, sr=sr)

    def draw(self):
        dot.background(dot.white)
        dot.draw_waveform(col=dot.black, with_playhead=True)

MySketch()
