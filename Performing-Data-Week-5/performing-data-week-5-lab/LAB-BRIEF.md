# Lab: Performing with Diffusion Models

← [Week 5 overview](../README.md) · [All teaching samples](../../README.md) · [SD Turbo tuning notes](sd_turbo_tuning_notes.md)

**Dorothy + Stable Diffusion (img2img)**

This lab takes the ideas from the lecture — denoise strength, prompt manipulation, structural control, feedback loops. By the end you'll have a working real-time-ish AI visual instrument running on your laptop, controlled by webcam, mouse, and audio.

We'll use **Dorothy** for the draw loop, windowing, audio analysis, and interaction, and **Stable Diffusion Turbo** (via Hugging Face Diffusers) for fast(er) img2img generation on laptops and GPUs.

---

## Before you start 

Make sure you have a working environment. In a fresh conda env:

**Apple Silicon / CPU (most laptops):**
```bash
pip install dorothy-cci diffusers transformers accelerate torch opencv-python
```

**NVIDIA GPU (CUDA):**
```bash
pip install dorothy-cci diffusers transformers accelerate opencv-python
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

The first time you run a sketch with diffusion, it will download the SD Turbo model (~2GB). Do this now while we're talking through the lab outline.

The device is **auto-detected** — `diffusion_utils.get_device()` picks `cuda` if you have an NVIDIA GPU, `mps` on Apple Silicon, and falls back to `cpu` otherwise. Each sketch sets this at the top:

```python
from diffusion_utils import load_pipe, get_device
device = get_device()   # auto: cuda / mps / cpu
```

You only need to change this line if you want to force a specific device.

---
## Troubleshooting

* **I cant see the webcam**
  * Try changing `self.cap = cv2.VideoCapture(1)` to `self.cap = cv2.VideoCapture(0)`. The number in the argument determines which webcam to connect to, starting at 0.
 
* **Output is only top quadrant**
  * This is an issue with Dorothy getting the resolution. You can fix by pasting the output twice as large at the bottom of the `draw()` loop
    ```python
    if result is not None:
            dot.paste(result, (0, 0), (dot.width*2, dot.height*2))
    ```
* **Window not responsive to mouse or keyboard**
    * Sometimes to get the window in focus to accept input events you need to click away and bring something else into focus (e.g. VSCode), then click back to the window. You can tell what is in focus as the title of the window will not be greyed out and it will say "python" in the top left (where it tells you what program is currently being used)
---

## Activity 1 — A Dorothy webcam baseline 

**Goal:** get comfortable with the Dorothy draw loop and webcam input *before* adding the model. If something breaks later, you want to know whether it's Dorothy or diffusion.

**Try it.** You should see your webcam in a 512×512 window.

**Tweaks to play with:**
- Mirror the image: `frame = cv2.flip(frame, 1)`
- Apply a Dorothy effect: add `dot.pixelate(8.0)` after the paste
- Add `dot.feedback(0.98)` (and remove `dot.background()`) for a trail effect

**Discuss:** Dorothy's `feedback` already does something the lecture talked about — frame-to-frame compounding. We're going to do the same thing but with a diffusion model in the middle.

---

## Activity 2 — Single-shot img2img 

**Goal:** generate one transformed image from your webcam feed and display it. Slow, but it proves the wiring works.

Press **SPACE**, wait a second or two, see your face transformed.

**Important things to notice:**
- `num_inference_steps=2` and `guidance_scale=0.0` — this is SD Turbo's "trick." Normal SD wants 20+ steps and guidance 7+. Turbo is distilled to 1–4 steps with no CFG.
- `strength` is the parameter the lecture called "the AI whispers / the AI screams." 0.0 = unchanged, 1.0 = ignore the input. SD Turbo behaves well from about 0.4 to 0.9.

**Try:** edit the prompt and re-run. Try `"a charcoal sketch"`, `"underwater photograph, bioluminescent"`, `"renaissance fresco"`.

---
## Aside on Live Coding in Dorothy

You will see that the real time sketches have this code at the bottom. This is a small adjustment in `Dorothy` that tells us we want it to check for updates to file as we are running, then incorporate any changes to the draw function without re-running the sketch.

Any time you save the project after changig code in the draw loop (e.g. the prompt or other settings), you should see them immediately brought in to the next frame.

```python
if __name__ == '__main__':
    import __main__
    dot.start_livecode_loop(__main__)
```

---

## Activity 3 — Continuous generation 

**Goal:** generate every frame instead of on keypress. More performance like!

The naive version blocks the draw loop while generating, which makes the window feel frozen. We'll use a simple pattern: generate in the draw loop, but only the latest frame, and show whatever's most recent.

You should see roughly **3 fps** on Apple Silicon depending on the chip. M2/M3/M4 Pro/Max will feel responsive; base M1 will be sluggish but workable.

**Key observation:** this is the heart of the lecture's "frame rate spectrum." 

**Try `num_inference_steps=4`** — about half the speed, noticeably better quality. This is your first speed/quality dial

---

## Activity 3b — Canvas as input (no webcam needed)

**Goal:** replace the webcam with a procedural Dorothy canvas as the model's input. Anything you draw in code — shapes, particles, text — becomes the structure the model interprets.

The sketch draws offscreen into a Dorothy layer, reads those pixels back, and feeds them to the diffusion model. Because the input is synthetic, the model is working entirely from code-generated structure — no camera required.

Open `week5-3-continuous-canvas.py`. An LFO drives an animated circle, styled with the disco ball prompt from earlier.

**Key differences from Activity 3:**
- No `cv2.VideoCapture` — the input is whatever you draw
- `dot.get_layer()` creates an offscreen buffer; `with dot.layer(...)` draws into it
- `dot.renderer.get_pixels(layer, bgr=False)` reads pixels without BGR conversion
- `dot.get_lfo("sine", 0.125)` drives the animation automatically

**Try:**
- Replace the circle with `dot.rectangle()`, `dot.line()`, or `dot.text()` — the model interprets typographic structure too
- Use `dot.mouse_x / dot.width` to control the shape size live
- Change the prompt to something that interacts interestingly with simple geometry (`"city plan, aerial view"`, `"topographic map"`, `"circuit board"`)
- Stack multiple shapes in the layer for more complex inputs

**Discuss:** the webcam grounds the model in a human body. What changes when the input is purely generative? Who (or what) is performing?

---

## Activity 4 — Mapping the denoise strength 

**Goal:** put strength on the mouse. This is the easiest one to control from your laptop, if limited

Add to exercise 3, or start new

```python
def draw(self):
    # Map mouse_x to strength range
    self.strength = 0.3 + (dot.mouse_x / dot.width) * 0.6   # 0.3 to 0.9
    # ... rest the same
```

Sweep your mouse left-to-right slowly. Watch what happens:
- **Far left (~0.3):** the model barely intervenes
- **Middle (~0.5):** the model is clearly reinterpreting you.
- **Far right (~0.9):** the model is hallucinating freely; the input is just a vague structural hint.

**Performance exercise:** try to make a 30-second arc — start grounded (low strength), build to chaos (high), return to clarity (low). You're playing one parameter, but it's already a usable performance gesture.

**Discuss:**
- Where do *you* find the most interesting territory? Many people end up preferring a narrow band around 0.55–0.7.
- The model "screams" past 0.85, but it also loses connection to the input. There's a sweet spot.

---

## Activity 5 — Prompt switching and blending 

**Goal:** treat prompts as scenes. Trigger them with keys and blend between them.

A key thing about SD Turbo: it accepts pre-computed prompt embeddings, so you can interpolate between two prompts in embedding space. That gives smooth crossfades instead of hard cuts.

Press **1–5** to switch prompts. The blend takes about a second.

**Things to try:**
- Make the blend slower (`self.blend += 0.005`) — the prompt drift becomes a slow musical gesture.
- Add a 6th prompt using completely different vocabulary. Notice which transitions are smooth and which are jarring (style→style is smooth; subject→subject is rougher).
- Set `self.blend += 0.001`. Now it takes ~30 seconds to crossfade between two prompts

**Discuss:** Do we still free control even at choppy latency?

---

## Activity 6 — Audio reactivity

**Goal:** plug audio analysis into the visual parameters. 

Either play a music file through Dorothy or use the microphone

**Tuning notes:**
- The `* 4` multiplier on amplitude is empirical. If you're loud, the strength saturates instantly. If you're quiet, drop to `* 8`.
- Onsets are a binary trigger — single events, like a beat. If they're firing too often, raise `threshold`. Too rarely, lower it.
- The smoother (`get_window(8)`) is doing real work. Without it, amplitude is jittery and the strength flickers visually.

**Try:**
- Map FFT bands instead of amplitude: `bass = np.mean(dot.music.fft(self.mic)[:10])` and use that for strength.
- Use beats instead of onsets if you have a music file: switch to `start_file_stream("song.wav")` and use `dot.music.is_beat()`.
- Stack with the keyboard prompt switching from Activity 5 — performer can override the audio-driven choice.

---

## Extension — Offline rendering to video

**Goal:** render a high-quality version of the audio-reactive sketch to a video file, with no real-time constraint.

This requires you to `pip install imageio-ffmpeg` to add the audio back into the rendered output.

The live sketch runs at 3–5 fps and uses threading tricks to hide latency. Offline rendering removes all of that — you process every frame sequentially, wait for the GPU to finish, and write the result to disk. This means you can afford:
- `num_inference_steps=4` (noticeably better quality than the live 2-step version)
- `GEN_SIZE=512` (larger than the live 256–384)
- Perfect audio sync (pre-analysed with librosa at the exact target fps)

**You'll need:**
- A video file as input — record webcam footage with QuickTime, or screen-record your live sketch (`VIDEO_IN = "input.mp4"`)
- `pip install librosa`

Open `week5-6-audio-reactive-offline.py`, set `VIDEO_IN` and `AUDIO_IN` at the top, then run from the terminal. It prints progress and saves `output.mp4`.

```bash
python week5-6-audio-reactive-offline.py
```

Expect roughly **2–5 seconds per frame** on Apple Silicon depending on chip and `GEN_SIZE`. A 30-second clip at 24fps = 720 frames ≈ 30–60 minutes to render. Leave it running overnight for longer pieces.

**Things to try:**
- Use `GEN_SIZE=768` for sharper output (slower — test with a short clip first)
- Lower `STRENGTH_MIN` to `0.25` with `STEPS=4` — the quiet sections are much more subtle offline
- Change the prompt bank to follow the narrative arc of the audio
- Use `librosa.beat.beat_track()` instead of onset detection for a more musical trigger

**Codec note:** `mp4v` is the safe default on macOS. Change to `avc1` for H.264 if you need to import into Final Cut or Premiere.

---

## Activity 7 — Feedback loop ("I am sitting in a model") 

**Goal:** feed the model's output back in as next frame's input. 

Mouse-X is strength (left = subtle, right = wild). Mouse-Y is feedback amount (top = pure webcam, bottom = pure feedback). Press **R** to reset the loop.

**What to look for:**
- Pure feedback (mouse at the bottom): the image drifts away from reality entirely. After ~10 seconds it's a fully synthetic visual that has no connection to the camera.
- Mid feedback (~50%): the camera anchors the loop just enough. You see yourself, but you're being pulled into the model's hallucination.
- The feedback loop has a *direction*. It tends toward whatever the prompt describes. Change the prompt while feedback is high and watch the image migrate.

**Discuss:** what does it mean that the camera is no longer the subject? 


---

## Wrap-up discussion 

- Where on the frame-rate spectrum did your favourite outputs sit? Did "slower" work better than "faster" for some pieces?
- Did the audio-reactive version feel like a *performance* or an *automation*? What's the difference?
- When you put strength on the mouse, did you feel like you were performing the model, or being performed by it?

---

## Reference card

A few things worth remembering after the lab.

| What | Setting | Why |
|---|---|---|
| SD Turbo steps | 1–4 | Distilled for few-step generation; more steps ≠ much better |
| SD Turbo guidance | 0.0 | The model wasn't trained with CFG; non-zero ruins it |
| img2img strength | 0.4–0.9 | Below 0.4 the model barely engages; above 0.9 input is ignored |
| Resolution | 384×384 | SD 1.5 base; quality drops sharply elsewhere, 512 x 512 is available |
| Device | `"cuda"` / `"mps"` / `"cpu"` | Auto-detected; CUDA and MPS use float16 for speed |
| dtype | `float16` | Half the memory, ~2× faster on GPU; CPU falls back to float32 |

**The dials of an img2img performance instrument:**

1. **Strength** — how much the AI intervenes
2. **Prompt** — what aesthetic territory we're in
3. **Prompt blend rate** — how fast we move between territories
4. **Feedback amount** — how self-referential the system is
5. **Seed** — which interpretation of the prompt we get
6. **Steps** — speed/quality tradeoff (also affects character of output)

Map any of these to anything (mouse, audio, MIDI, sensors) and you have a piece.
