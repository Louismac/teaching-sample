from dorothy import Dorothy 
import librosa
from util import draw_bars
import numpy as np

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        bpm = 106
        bpm2 = 75
        audio, sr = librosa.load("week4/audio/drums.wav")
        audio2, sr = librosa.load("week4/audio/drums75.wav")
        #adjust sample rate based on ratio of bpms
        audio2 = librosa.resample(audio2, orig_sr=sr, target_sr= int(sr * (bpm2/bpm)))
        diff = len(audio) - len(audio2)
        #diff should be close to 0, pad to make same lengths if slightly off (rounding errors)
        if diff > 0:
            audio2 = np.pad(audio2, (0,diff))
        else:
            audio = np.pad(audio, (0,diff))
        print(len(audio), len(audio2))
        dot.music.start_sample_stream(audio+audio2, sr=sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(col=dot.black, with_playhead=True)
        draw_bars(dot, 2, 4)
    
        
MySketch() 