import cv2
import torch
from dorothy import Dorothy
from diffusion_utils import load_pipe, grab_webcam, LivePipe

dot = Dorothy(width=512, height=512, title="Prompt blending")
device = "mps"

PROMPTS = [
    "an oil painting, dramatic light, thick brushstrokes",
    "underwater photograph, bioluminescent, deep sea",
    "neon cyberpunk portrait, glowing wires, rain",
    "renaissance fresco, faded pigment, cracked plaster",
    "charcoal sketch on rough paper, expressive lines",
]

class Sketch:

    def setup(self):
        self.cap = cv2.VideoCapture(0)
        pipe = load_pipe(device=device)
        self.live = LivePipe(pipe, gen_size=384)
        self.live.warmup()

        # Pre-compute embeddings for all prompts so blending is free at runtime
        self.embeddings = [
            pipe.encode_prompt(p, device="mps", num_images_per_prompt=1,
                               do_classifier_free_guidance=False)[0]
            for p in PROMPTS
        ]

        self.current_idx = 0
        self.target_idx = 0
        self.blend = 1.0
        self.generator = torch.Generator(device=device).manual_seed(42)
        dot.on_key_press = self.on_key

    def on_key(self, key, action, mods):
        if action != dot.keys.ACTION_PRESS: return
        for i, k in enumerate([dot.keys.NUMBER_1, dot.keys.NUMBER_2,
                               dot.keys.NUMBER_3, dot.keys.NUMBER_4,
                               dot.keys.NUMBER_5]):
            if key == k and i < len(PROMPTS):
                self.current_idx = self.target_idx
                self.target_idx = i
                self.blend = 0.0

    def draw(self):
        dot.background((0, 0, 0))
        frame = grab_webcam(self.cap, 384)
        if frame is None: return

        self.blend = min(1.0, self.blend + 0.03)
        emb = ((1 - self.blend) * self.embeddings[self.current_idx]
               + self.blend * self.embeddings[self.target_idx])
        s = min(1.0, max(0.0, 0.55 + (dot.mouse_x / dot.width) * 0.35))
        print(s)
        self.generator.manual_seed(42)
        self.live.push(
            frame,
            prompt_embeds=emb,
            num_inference_steps=2,
            strength=s,
            guidance_scale=0.0,
            generator=self.generator,
        )

        result = self.live.get_frame()
        if result is not None:
            dot.paste(result, (0, 0), (dot.width*2, dot.height*2))
        dot.fill(dot.white)
        dot.text(f"{PROMPTS[self.target_idx][:40]}", 10, 30, 14)

if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
