from dorothy import Dorothy 
import librosa
from util import draw_bars
from soundfile import SoundFile

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/keys4.wav")
        audio = librosa.resample(audio, orig_sr=sr, target_sr= sr//2)
        dot.music.start_sample_stream(audio, sr = sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(col=dot.black, with_playhead=True)
        draw_bars(dot, 2, 4)
    
        
MySketch() 