import cv2
import torch
from dorothy import Dorothy
from diffusion_utils import load_pipe, grab_webcam, LivePipe

dot = Dorothy(width=512, height=512, title="Continuous img2img")
device = "mps"

class Sketch:

    def setup(self):
        self.cap = cv2.VideoCapture(1)
        self.live = LivePipe(load_pipe(device=device), gen_size=256)
        self.live.warmup()        
        self.generator = torch.Generator(device=device).manual_seed(42)

    def draw(self):
        dot.background((0, 0, 0))
        frame = grab_webcam(self.cap, dot.width)
        if frame is None: return
        
        self.prompt = "warriors of pasta"
        self.strength = 0.7
        self.generator.manual_seed(42)
        self.live.push(
            frame,
            prompt=self.prompt,
            num_inference_steps=2,
            strength=self.strength,
            guidance_scale=0.0,
            generator=self.generator,
        )

        result = self.live.get_frame()
        if result is not None:
            dot.paste(result, (0, 0), (dot.width*2, dot.height*2))

        fps = dot.frames * 1000.0 / max(dot.millis, 1)
        dot.fill(dot.white)
        dot.text(f"display {fps:.1f} fps  |  diffuse {self.live.diffuse_fps:.1f} fps", 10, 30, 18)

if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
