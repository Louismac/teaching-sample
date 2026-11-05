import cv2
from dorothy import Dorothy
from diffusion_utils import load_pipe, grab_webcam, LivePipe
import torch

dot = Dorothy(width=512, height=512, title="Audio-reactive img2img")
device = "mps"

class Sketch:

    def setup(self):
        self.cap = cv2.VideoCapture(0)

        self.mic = dot.music.start_file_stream("audio/disco.wav")
        dot.music.audio_outputs[self.mic].analyse_onsets = True

        self.live = LivePipe(load_pipe(device=device), gen_size=256)
        self.live.warmup()

        self.smoother = dot.get_window(8)

        self.prompts = [
            "an oil painting, thick brushstrokes",
            "neon cyberpunk, glowing edges",
            "charcoal sketch, expressive lines",
            "underwater, bioluminescent",
        ]
        self.prompt_idx = 0
        self.generator = torch.Generator(device=device).manual_seed(42)

    def draw(self):
        dot.background((0, 0, 0))
        frame = grab_webcam(self.cap, 512)
        if frame is None: return

        amp = self.smoother.add(dot.music.amplitude(self.mic))
        strength = 0.4 + min(amp * 4, 1.0) * 0.5

        if dot.music.is_onset(self.mic):
            self.prompt_idx = (self.prompt_idx + 1) % len(self.prompts)

        self.generator.manual_seed(42)
        self.live.push(
            frame,
            prompt=self.prompts[self.prompt_idx],
            num_inference_steps=2,
            strength=strength,
            guidance_scale=0.0,
            generator = self.generator
        )

        result = self.live.get_frame()
        if result is not None:
            dot.paste(result, (0, 0), (dot.width, dot.height))
        else:
            dot.paste(frame, (0, 0), (dot.width, dot.height))

        dot.fill(dot.white)
        dot.text(f"amp={amp:.2f}  strength={strength:.2f}", 10, 30, 16)
        dot.text(f"{self.prompts[self.prompt_idx][:40]}", 10, 50, 14)

if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
