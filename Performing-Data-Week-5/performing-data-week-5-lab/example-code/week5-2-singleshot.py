import cv2
import numpy as np
from PIL import Image
from dorothy import Dorothy
from diffusion_utils import load_pipe, grab_webcam

dot = Dorothy(width=512, height=512, title="Single-shot img2img")
device = "mps"

class Sketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.cap = cv2.VideoCapture(0)
        print("Loading model...")
        self.pipe = load_pipe(device=device)
        print("Ready. Press SPACE to generate.")

        self.prompt = "an oil painting of a person, dramatic lighting, swirling brushstrokes"
        self.output = None
        dot.on_key_press = self.on_key

    def on_key(self, key, action, mods):
        if key == dot.keys.SPACE and action == dot.keys.ACTION_PRESS:
            self.generate()

    def generate(self):
        frame = grab_webcam(self.cap, 512)
        if frame is None:
            return
        self.output = np.array(self.pipe(
            prompt=self.prompt,
            image=Image.fromarray(frame),
            num_inference_steps=2,
            strength=0.6,
            guidance_scale=0.0,
        ).images[0])

    def draw(self):
        dot.background((0, 0, 0))
        if self.output is not None:
            dot.paste(self.output, (0, 0))

Sketch()
