import cv2
import numpy as np
import torch
from dorothy import Dorothy
from diffusion_utils import load_pipe, grab_webcam, LivePipe

dot = Dorothy(width=384, height=384, title="Feedback")
device = "mps"

class Sketch:

    def setup(self):
        self.cap = cv2.VideoCapture(0)
        self.live = LivePipe(load_pipe(device=device), gen_size=384)
        self.live.warmup()

        self.prompt = "an oil painting, dramatic light, thick brushstrokes"
        self.generator = torch.Generator(device=device).manual_seed(42)
        dot.on_key_press = self.on_key

    def on_key(self, key, action, mods):
        if action != dot.keys.ACTION_PRESS: return
        if key == dot.keys.R:
            self.live._last_output = None   # reset feedback loop

    def draw(self):
        dot.background((0, 0, 0))
        frame = grab_webcam(self.cap, 384)
        if frame is None: return

        feedback_amount = dot.mouse_y / dot.height
        last = self.live.result   # completed output, not interpolated
        if last is not None:
            last_resized = cv2.resize(last, (384, 384))
            mix = (frame * (1 - feedback_amount)
                   + last_resized * feedback_amount).astype(np.uint8)
        else:
            mix = frame
        s = min(1.0, max(0.0, 0.4 + (dot.mouse_x / dot.width) * 0.4))
        # self.generator.manual_seed(42)
        self.live.push(
            mix,
            prompt=self.prompt,
            num_inference_steps=4,
            strength=s,
            guidance_scale=0.0,
            generator=self.generator,
        )

        result = self.live.get_frame()
        if result is not None:
            dot.paste(result, (0, 0), (dot.width*2, dot.height*2))
        
        dot.fill(dot.white)
        dot.text(f"strength={s:.2f}  feedback amount={feedback_amount:.2f}", 10, 30, 16)

if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
