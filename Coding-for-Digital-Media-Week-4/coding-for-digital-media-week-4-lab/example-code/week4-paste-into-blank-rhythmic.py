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
        drum_track = np.zeros(sr*20)

        beats_per_minute = 90
        beats_per_second = beats_per_minute/60
        samples_per_beat = int(sr // beats_per_second)

        #pull out the first kick
        kick = drums[:sr//4]
        
        #Lets make a drop starting at the beginning and getting progressively faster 
        start = 0
        #4 beats
        division = samples_per_beat
        for i in range(4):
            self.replace(drum_track, kick, start+(division*i))

        #start a 4 beats later
        start += samples_per_beat*4
        #8 half beats
        division = samples_per_beat//2 
        for i in range(8):
            self.replace(drum_track, kick, start+(division*i))

        #start a 4 beats later (8 in total)
        start += samples_per_beat*4
        #16 quarter beats
        division = samples_per_beat//4
        for i in range(16):
            self.replace(drum_track, kick, start+(division*i))

        #start a 4 beats later (12 in total)
        start += samples_per_beat*4
        #16 eighth beats
        division = samples_per_beat//8 
        for i in range(16):
            self.replace(drum_track, kick, start+(division*i))

        #start a 2 beats later (14 in total)
        start += samples_per_beat*2
        #32 1/16 beats
        division = samples_per_beat//16 
        for i in range(32):
            self.replace(drum_track, kick, start+(division*i))
        
        dot.music.start_sample_stream(drum_track, sr=sr)

    def replace(self, timeline, to_paste, pos):
        start = pos
        #How long is our audio to paste in?
        end = start + len(to_paste)
        #paste over existing audio
        timeline[start:end] = to_paste
        print(pos)
        return timeline

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(col=dot.black, with_playhead=True)
               
MySketch() 