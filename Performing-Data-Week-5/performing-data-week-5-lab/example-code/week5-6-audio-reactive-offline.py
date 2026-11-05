import cv2
import numpy as np
import torch
import librosa
import subprocess
import os
import imageio_ffmpeg
from PIL import Image
from diffusion_utils import load_pipe

# ── config ────────────────────────────────────────────────────────────────────
VIDEO_IN      = "/Users/lmccallum/Downloads/louis.mov"          # pre-recorded webcam footage
AUDIO_IN      = "audio/disco.wav"
VIDEO_OUT     = "output.mp4"
FPS           = 24
GEN_SIZE      = 512                  # can go larger offline
STEPS         = 4
STRENGTH_MIN  = 0.4
STRENGTH_MAX  = 0.9

PROMPTS = [
    "an oil painting, thick brushstrokes",
    "neon cyberpunk, glowing edges",
    "charcoal sketch, expressive lines",
    "underwater, bioluminescent",
]
# ─────────────────────────────────────────────────────────────────────────────

# Pre-analyse audio at the target FPS so we get one value per output frame
hop = None   # computed below after loading
y, sr = librosa.load(AUDIO_IN)
hop = int(sr / FPS)

rms = librosa.feature.rms(y=y, hop_length=hop)[0]
rms_norm = rms / (rms.max() + 1e-8)

onset_frames = set(
    librosa.onset.onset_detect(y=y, sr=sr, hop_length=hop).tolist()
)

# Video input
cap = cv2.VideoCapture(VIDEO_IN)
n_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
n_frames = min(n_video, len(rms_norm))
print(f"Rendering {n_frames} frames  ({n_frames / FPS:.1f}s)")

# Video output (mp4v writes .mp4 on macOS; use avc1 if you need H.264)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(VIDEO_OUT, fourcc, FPS, (GEN_SIZE, GEN_SIZE))

device = "mps"
pipe = load_pipe(device = device)
generator = torch.Generator(device=device).manual_seed(42)

prompt_idx = 0
for i in range(n_frames):
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (GEN_SIZE, GEN_SIZE))

    amp = float(rms_norm[i])
    strength = STRENGTH_MIN + amp * (STRENGTH_MAX - STRENGTH_MIN)
    strength = max(strength, 1.0 / STEPS)   # guard against 0-step error

    if i in onset_frames:
        prompt_idx = (prompt_idx + 1) % len(PROMPTS)

    generator.manual_seed(42)
    result = pipe(
        prompt=PROMPTS[prompt_idx],
        image=Image.fromarray(frame),
        num_inference_steps=STEPS,
        strength=strength,
        guidance_scale=0.0,
        generator=generator,
    ).images[0]

    out.write(cv2.cvtColor(np.array(result), cv2.COLOR_RGB2BGR))

    pct = (i + 1) / n_frames * 100
    print(f"\r{i+1}/{n_frames} ({pct:.0f}%)  amp={amp:.2f}  "
          f"strength={strength:.2f}  [{PROMPTS[prompt_idx][:30]}]", end="", flush=True)

cap.release()
out.release()
print(f"\nSaved silent video → {VIDEO_OUT}")

# Mux audio into the rendered video using ffmpeg
VIDEO_OUT_FINAL = VIDEO_OUT.replace(".mp4", "_audio.mp4")
subprocess.run([
    imageio_ffmpeg.get_ffmpeg_exe(), "-y",
    "-i", VIDEO_OUT,
    "-i", AUDIO_IN,
    "-c:v", "copy",
    "-c:a", "aac",
    "-shortest",
    VIDEO_OUT_FINAL,
], check=True)
os.remove(VIDEO_OUT)
print(f"Saved with audio → {VIDEO_OUT_FINAL}")
