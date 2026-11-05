import cv2
import torch
import time
from dorothy import Dorothy
from diffusion_utils import (
    load_pipe, grab_webcam, LivePipe, encode_prompts, slerp_embeds
)

dot = Dorothy(width=512, height=512, title="Prompt interpolation")
device = "mps"


class Sketch:
    def setup(self):
        self.cap = cv2.VideoCapture(0)
        self.pipe = load_pipe(device=device)
        self.live = LivePipe(self.pipe, gen_size=384)
        self.live.warmup()
        self.generator = torch.Generator(device=device).manual_seed(42)

        self.prompts = [
            "a smooth river stone, wet, grey, photorealistic",
            "a cracked dry clay vessel, earthy, ancient",
            "a glowing ember, orange light, smoke",
            "a wisp of pale smoke against black, ethereal",
        ]
        self.embeds = encode_prompts(self.pipe, self.prompts, device=device)
        self.duration_s = 30.0
        self.start_time = time.perf_counter()

        # the prompt is moving every frame — don't let the filter skip
        self.live.skip_filter = False

    def _embed_at(self, progress):
        progress = max(0.0, min(1.0, progress))
        n_legs = len(self.embeds) - 1
        scaled = progress * n_legs
        i = min(int(scaled), n_legs - 1)
        local_t = scaled - i
        local_t = local_t * local_t * (3 - 2 * local_t)   # smoothstep
        return slerp_embeds(local_t, self.embeds[i], self.embeds[i + 1])

    def draw(self):
        dot.background((0, 0, 0))
        frame = grab_webcam(self.cap, dot.width)
        if frame is None:
            return

        progress = (time.perf_counter() - self.start_time) / self.duration_s

        # once the journey ends, let the filter idle the GPU on static input
        if progress >= 1.0 and not self.live.skip_filter:
            self.live.skip_filter = True

        embed = self._embed_at(progress)

        self.generator.manual_seed(42)
        self.live.push(
            frame,
            prompt_embeds=embed,
            num_inference_steps=2,
            strength=0.7,
            guidance_scale=0.0,
            generator=self.generator,
        )

        result = self.live.get_frame()
        if result is not None:
            dot.paste(result, (0, 0), (dot.width*2, dot.height*2))

        # HUD
        fps = dot.frames * 1000.0 / max(dot.millis, 1)
        n_legs = len(self.prompts) - 1
        leg_idx = min(int(progress * n_legs), n_legs - 1) if progress < 1.0 else n_legs - 1
        dot.fill(dot.white)
        dot.text(f"display {fps:.1f}  |  diffuse {self.live.diffuse_fps:.1f}", 10, 30, 18)
        dot.text(f"progress {min(progress, 1.0)*100:.0f}%  |  {self.prompts[leg_idx][:30]}...",
                 10, 55, 14)


if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)