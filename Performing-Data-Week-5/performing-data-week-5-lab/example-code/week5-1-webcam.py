import cv2
from dorothy import Dorothy

dot = Dorothy(width=512, height=512, title="Webcam baseline")

class Sketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.cap = cv2.VideoCapture(0)
        # OpenCV gives BGR; we'll convert each frame
        self.frame = None

    def draw(self):
        dot.background((0, 0, 0))
        ret, frame = self.cap.read()
        if ret:
            # BGR -> RGB, resize to canvas
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (dot.width*2, dot.height*2))
            self.frame = frame
            dot.paste(self.frame, (0, 0))

Sketch()