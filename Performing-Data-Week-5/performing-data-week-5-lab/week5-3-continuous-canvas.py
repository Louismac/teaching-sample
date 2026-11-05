import torch
from dorothy import Dorothy
from diffusion_utils import load_pipe, LivePipe
import numpy as np

dot = Dorothy(width=512, height=512, title="Continuous img2img - canvas")
device = "mps"

class Sketch:

    def setup(self):
        self.live = LivePipe(load_pipe(device=device), gen_size=384)
        self.live.warmup()

        self.generator = torch.Generator(device=device).manual_seed(42)
        self.layer = dot.get_layer()
        self.lfo = dot.get_lfo("sine", 0.125)

    def draw(self):
        dot.background((0, 0, 0))
        with dot.layer(self.layer):
            r = dot.lfo_value(self.lfo) / 2
            #dot.background(dot.black)
            dot.fill(dot.green)
            dot.circle((dot.width // 2, dot.height // 2), 1 + int(r * dot.height))
            dot.tile(np.random.randint(2), np.random.randint(2), bake=True)
            dot.feedback(zoom=1-((1-r))/10, bake=True)


        frame = dot.renderer.get_pixels(self.layer, bgr=False)
        # self.prompt = ("a disco ball, mirror tiles, reflective silver spherical surface, specular highlights, photorealistic")
        self.prompt = ("cat clown photo")
        self.strength = 0.9
        
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
            dot.paste(result, (0, 0), (dot.width, dot.height))

        
        fps = dot.frames * 1000.0 / max(dot.millis, 1)
        dot.fill(dot.white)
        dot.text(f"display {fps:.1f} fps  |  diffuse {self.live.diffuse_fps:.1f} fps", 10, 30, 18)

if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
