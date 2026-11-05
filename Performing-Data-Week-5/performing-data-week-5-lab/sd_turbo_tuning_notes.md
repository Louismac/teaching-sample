# SD-Turbo img2img: tuning notes

← [Lab guide](README.md) · [Week 5 overview](../README.md)

Notes on the relationship between `strength`, `num_inference_steps`, and resolution for real-time img2img with SD-Turbo. Focus is on efficiency, output quality, prompt adherence, and how clearly the input image reads through.

## The core formula

```
effective_steps = int(num_inference_steps * strength)   # must be >= 1
```

This is the actual UNet work done per frame. Halve it, roughly halve the compute. `steps=2, strength=0.5` → 1 step (Turbo's sweet spot for img2img).

A consequence worth internalising: `steps=10, strength=0.1` and `steps=2, strength=0.5` both do **1 actual denoise step** and run at the same speed. They are not independent knobs — they multiply. The only reason to pick a higher `num_inference_steps` while keeping effective steps low is that it gives the scheduler a finer noise schedule, which can *slightly* improve quality. In practice with Turbo, just pick the smallest pair that yields the effective steps you want.

## Strength (0.0 – 1.0)

How much noise is added to the input before denoising starts.

- **Low (0.3 – 0.5)** — output stays close to input. Composition, shapes, and silhouettes survive. Prompt has less influence. Best for live video, sketch-to-image, or anything where the input needs to read through clearly. Lower strength also means less flicker frame-to-frame, since each frame stays anchored to its source.
- **High (0.8 – 1.0)** — input is mostly destroyed by noise. Prompt dominates. Output is more "hallucinated" and less faithful to the source, with more frame-to-frame flicker. Use when the input is just a rough guide for composition and you want strong stylization.

## Number of inference steps

Granularity of denoising. With Turbo, more steps = slightly cleaner detail and better prompt adherence, but with strongly diminishing returns past 4. Each extra effective step is a full UNet forward pass — linear cost.

- **1 step** — fastest, slightly soft, prompt adherence okay
- **2 steps** — noticeably sharper, better prompt adherence, ~2× slower
- **4 steps** — near-best Turbo quality, ~4× slower. Rarely worth it real-time.

## Resolution

Cost scales roughly **quadratically** with resolution (latent area). 512² is 4× the work of 256². SD-Turbo was trained at 512², so:

- **256²** — fastest, softer detail, occasional artifacts. Fine for abstract input.
- **384²** — good balance, mild quality hit.
- **512²** — best quality and prompt adherence, native training resolution.
- **>512²** — quality often *degrades* (model wasn't trained for it) and it's slower. Avoid.

## Guidance scale

Keep at `0.0` for Turbo. Anything else doubles UNet cost (classifier-free guidance = 2 forward passes) for no quality gain — Turbo was distilled without it.

## The asymmetric tradeoff

Resolution-vs-steps isn't symmetric, and this is useful:

- Dropping 512 → 384 saves **~45% compute**
- Dropping 2 effective steps → 1 saves **~50% compute**

Similar magnitude, but the resolution drop tends to hurt quality less than the step drop **for img2img specifically**. The input image is providing the structure, so the model needs fewer "pixels of imagination space" than for txt2img where it's inventing everything from noise.

**If you have to choose, lower resolution before lowering steps.**

## Rules of thumb for live img2img

| Goal | Action |
|---|---|
| Want input to read clearly? | Lower strength, keep steps low |
| Want strong stylization? | Higher strength, maybe +1 step |
| Need more fps? | Drop resolution before dropping steps |
| Flicker between frames? | Lower strength, fix the seed |
| Prompt being ignored? | Raise strength before raising steps |

## Quick recipes

- **Webcam → stylized video, smooth and faithful**: `gen_size=384, steps=2, strength=0.5` (1 effective step)
- **Sketch → image, more interpretation**: `gen_size=512, steps=2, strength=0.7` (1 effective step, slightly more freedom)
- **Maximum fps, abstract input**: `gen_size=256, steps=2, strength=0.5` (1 effective step at small res)
- **Best quality, willing to accept ~5 fps on M-series**: `gen_size=512, steps=4, strength=0.5` (2 effective steps)

---

# Pipeline-level speedups

The model parameters above control how expensive *one* diffusion pass is. The techniques below control how often we run a pass at all, how much the user has to wait for one, and how smooth the result feels in between. They're stackable and largely independent of the tuning above.

## Tiny VAE (TAESD)

The VAE decodes the final latent back into pixels at the end of every frame. The standard SD VAE is surprisingly expensive — on Apple Silicon it can eat 30-50% of a fast img2img frame. **TAESD** (`madebyollin/taesd`) is a tiny distilled replacement: roughly 10× faster decode, with a minor quality hit that's invisible at real-time resolutions. Drop-in via `pipe.vae = AutoencoderTiny.from_pretrained(...)`. Free win, always on.

## Warm-up passes

The first 1–2 inference calls on MPS (and CUDA) are 2–5× slower than steady-state because kernels are still compiling and caches are cold. Doing two throwaway passes in `setup()` means the first user-visible frame isn't a stutter. Costs you ~1 second at startup, saves a visible glitch.

## Async diffusion (the big one)

In a naive loop, the draw thread *waits* on the GPU every frame, so display fps == diffusion fps. Move the pipeline call into a background worker thread and let the draw loop run at display rate, painting whatever the latest completed output is.

Effect: display goes from being locked to ~3 fps (whatever diffusion can manage) up to 30+ fps, while diffusion happens in the background at its own pace. The user sees motion, input, and HUD updates immediately even when a frame is mid-generation.

This is also what makes the next two techniques possible — they only help if the display loop isn't blocked.

## Similarity filter

Compare a tiny (32×32) version of the current input to the previous one with cosine similarity. If they're nearly identical (threshold ~0.985), skip the diffusion call entirely and reuse the last output.

The 32×32 downsample makes the comparison effectively free (microseconds), and on typical input — webcam, sketch, slow LFO — large stretches of frames are near-duplicates. In practice this cuts compute by 30–80% with zero visible quality loss.

Tuning notes:
- **Higher threshold (0.99+)** — almost never skips, safe but minimal savings
- **Lower threshold (0.95)** — aggressive skipping, can feel "frozen" on subtle motion
- **`max_skips` cap** — force a refresh every N skips so slow drift still gets re-rendered eventually

This is borrowed directly from StreamDiffusion, where it's called the "stochastic similarity filter."

## Temporal interpolation (frame blending)

While the worker is grinding out diffusion frame N+1, cross-fade from frame N-1 to frame N in the display loop based on how far through the expected frame duration we are.

Effect: motion at display rate looks smooth even when the underlying diffusion rate is 3–5 fps. Without this, you see the same diffusion frame held for ~250ms then snap to the next one — very noticeable, very ugly. With it, you get continuous-looking motion.

Implementation: `cv2.addWeighted(prev, 1-t, cur, t, 0)` where `t = elapsed / frame_duration`. `cv2.addWeighted` is meaningfully faster than the equivalent numpy float math.

The `frame_duration` is auto-estimated as an exponential moving average of recent diffusion-pass times, so it adapts as conditions change (prompt complexity, system load).

For higher-quality interpolation you can swap in optical-flow-based methods (RIFE, FILM), but linear blending is hard to beat at this latency budget.

## Fixed seed for temporal coherence

Reuse the same `torch.Generator` across frames instead of re-seeding each time. Different seeds produce wildly different denoising paths even from near-identical inputs, which manifests as flicker. Locking the seed means consecutive frames share a denoising trajectory, so frame-to-frame changes come almost entirely from input changes — exactly what you want.

This isn't a speedup per se, but it eliminates the temptation to crank up steps to "smooth out" flicker that's actually caused by random seeds.

## Stacked impact (rough)

Starting from a naive `pipe(...)` call in the draw loop on M-series:

| Technique | Approx. effect |
|---|---|
| Baseline (steps=4, strength=0.9, std VAE) | ~1.5 fps display, locked to diffusion |
| + TAESD | ~2.5 fps |
| + tuned params (steps=2, strength=0.5) | ~5 fps |
| + warm-up | same fps, smooth start |
| + async diffusion | ~5 fps diffusion, **30+ fps display** |
| + interpolation | same numbers, motion looks smooth |
| + similarity filter | diffusion runs on demand, idles when input is static |

The async + interpolation combo is the largest perceptual win. The user feels like they're driving a 30 fps system even though under the hood diffusion may be running at a fifth of that.
