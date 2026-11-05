from dorothy import Dorothy 
import librosa
from util import draw_bars
import numpy as np

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/drums.wav")
        #Make 60 of silence
        samples_in_bar = len(audio) // 2
        samples_in_beat = samples_in_bar // 4
        #This is the first beat
        beginning = audio[:samples_in_beat]
        print(len(beginning)) 
        #This is the last beat
        end = audio[-samples_in_beat:]
        print(len(end)) 
        #This is the middle of bar 1, the second and third beats
        mid = audio[samples_in_beat:samples_in_beat*3]
        print(len(mid)) 
        dot.music.start_sample_stream(audio, sr=22050, buffer_size = 2048)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(col=dot.black, with_playhead=True)
        draw_bars(dot)
               
MySketch() 