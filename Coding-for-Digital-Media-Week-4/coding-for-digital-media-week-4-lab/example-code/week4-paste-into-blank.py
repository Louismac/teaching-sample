from dorothy import Dorothy 
import librosa
from util import draw_bars
import numpy as np

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        drums, sr = librosa.load("week4/audio/drums.wav")
        harp, sr = librosa.load("week4/audio/harp1.wav")
        #Make 60 of silence
        timeline = np.zeros(sr*60)
        #overwrite timeline with drums
        self.replace(timeline, drums, 0)
        #mix in (not replace) with existing timeline
        self.mix(timeline, harp, 0)
        dot.music.start_sample_stream(timeline, sr=22050, buffer_size = 2048)

    def replace(self, timeline, to_paste, pos):
        start = pos
        #How long is our audio to paste in?
        end = start + len(to_paste)
        #paste over existing audio
        timeline[start:end] = to_paste

    def mix(self, timeline, to_paste, pos):
        start = pos
        #How long is our audio to paste in?
        end = start + len(to_paste)
        # mix with existing section on online
        mix = timeline[start:end] + to_paste
        #paste mix back in
        timeline[start:end] = mix

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(col=dot.black, with_playhead=True)
               
MySketch() 