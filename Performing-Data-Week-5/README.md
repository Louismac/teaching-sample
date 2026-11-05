# Performing Data, Week 5: Generative Visuals in Performance

← [All teaching samples](../README.md) · [Teaching approach](../TEACHING-APPROACH.md)

> **In one sentence:** students turn Stable Diffusion into a playable visual instrument. They build up, step by step, a real-time img2img system driven by webcam, mouse, keyboard and audio, then perform with it in groups.

| | |
|---|---|
| **Unit** | Performing Data · MSc Applied Machine Learning for Creatives · Term 3 · 20 credits |
| **Session length** | 4 hours: lecture, group performance lab, performances |
| **Prior knowledge** | Python and Dorothy; earlier weeks of the unit |
| **Tools** | [Dorothy](https://github.com/Louismac/dorothy), Hugging Face [Diffusers](https://huggingface.co/docs/diffusers) with SD Turbo, PyTorch, OpenCV |
| **Hardware** | Runs on Apple Silicon, NVIDIA GPUs, or CPU (more slowly). There is an offline rendering route for slower machines |
| **Student output** | A short live audiovisual performance, made in groups |
| **Full plan** | [delivery-context.md](delivery-context.md) |

**Contents:** [Learning outcomes](#learning-outcomes) · [Session plan](#session-plan) · [Materials](#materials-in-this-folder) · [Lab progression](#lab-progression) · [Key concepts](#key-concepts) · [Why it works](#why-this-session-works)

---

## Learning outcomes

By the end of the session, students will be able to:

| # | Class learning outcome | Unit outcome | Practised in |
|---|---|---|---|
| 1 | Understand and use the parameters of Stable Diffusion (strength, steps, guidance, resolution, seed, prompt) for real-time performance | LO1 | Activities 2–4; [tuning notes](performing-data-week-5-lab/sd_turbo_tuning_notes.md) |
| 2 | Build an interactive img2img system that maps live inputs (webcam, mouse, keyboard, audio) to generation parameters | LO1 | Activities 4–7 |
| 3 | Evaluate the trade-offs between latency, frame rate and image quality, and choose settings to suit a performance context | LO1, LO3 | Activity 3; offline extension; [tuning notes](performing-data-week-5-lab/sd_turbo_tuning_notes.md) |
| 4 | Critically reflect on agency and authorship when performing with a generative model | LO3 | Discussion prompts in each activity; [wrap-up](performing-data-week-5-lab/README.md#wrap-up-discussion); group performances |

The unit learning outcomes (LO1–LO3) are listed in full in [delivery-context.md](delivery-context.md#learning-outcomes-of-unit).

---

## Session plan

| Block | Activity | Materials |
|---|---|---|
| Before class | Download the SD Turbo model (about 2 GB) | [`week5-0-download-model.py`](performing-data-week-5-lab/week5-0-download-model.py) |
| Lecture | Diffusion for performance: denoise strength (“the AI whispers / the AI screams”), prompt manipulation, structural control, feedback loops, and the frame-rate spectrum | |
| Break | | |
| Group performance lab | Work through the activities, then build a group piece | [Lab guide](performing-data-week-5-lab/README.md) |
| Performances | Each group performs live and the class discusses | [Wrap-up questions](performing-data-week-5-lab/README.md#wrap-up-discussion) |

Exact timings are in [delivery-context.md](delivery-context.md#lesson-schedule-4-hours).

---

## Materials in this folder

| File | What it is |
|---|---|
| [`performing-data-week-5-lab/README.md`](performing-data-week-5-lab/README.md) | **The lab.** Setup, troubleshooting, seven activities with “try” and “discuss” prompts, an offline extension, and a reference card |
| [`performing-data-week-5-lab/sd_turbo_tuning_notes.md`](performing-data-week-5-lab/sd_turbo_tuning_notes.md) | Reference notes on how strength, steps and resolution interact, with rules of thumb for live work |
| [`performing-data-week-5-lab/diffusion_utils.py`](performing-data-week-5-lab/diffusion_utils.py) | Shared helpers: device detection, model loading, webcam capture, a threaded `LivePipe` that skips near-identical frames, and prompt-embedding interpolation |
| `performing-data-week-5-lab/week5-*.py` | One sketch per activity (see below) |
| [`performing-data-week-5-lab/audio/disco.wav`](performing-data-week-5-lab/audio/disco.wav) | A music file for the audio-reactive activity |
| [`delivery-context.md`](delivery-context.md) | Unit description, learning outcomes, schedule |

---

## Lab progression

Each activity adds one idea to the last. Students always know whether a problem comes from Dorothy or from the model.

| Step | Sketch | New idea |
|---|---|---|
| 0 | [`week5-0-download-model.py`](performing-data-week-5-lab/week5-0-download-model.py) | Cache the model before class |
| 1 | [`week5-1-webcam.py`](performing-data-week-5-lab/week5-1-webcam.py) | A webcam baseline in the Dorothy draw loop, with no AI yet |
| 2 | [`week5-2-singleshot.py`](performing-data-week-5-lab/week5-2-singleshot.py) | One img2img generation on a key press; meet `strength`, `steps` and `guidance` |
| 3 | [`week5-3-continuous.py`](performing-data-week-5-lab/week5-3-continuous.py) | Generating continuously, and the frame-rate cost |
| 3b | [`week5-3-continuous-canvas.py`](performing-data-week-5-lab/week5-3-continuous-canvas.py) | Generated graphics instead of a camera as the input. Who is performing now? |
| 4 | *(edit to step 3)* | Map strength to the mouse and play a 30-second arc from grounded to chaotic |
| 5 | [`week5-5-prompt-blend.py`](performing-data-week-5-lab/week5-5-prompt-blend.py) | Prompts as scenes: switch with keys and crossfade in embedding space |
| 6 | [`week5-6-audio-reactive.py`](performing-data-week-5-lab/week5-6-audio-reactive.py) | Amplitude drives strength; onsets switch prompts |
| ext | [`week5-6-audio-reactive-offline.py`](performing-data-week-5-lab/week5-6-audio-reactive-offline.py) | Offline render to video at higher quality, with sound added back |
| 7 | [`week5-7-feedback.py`](performing-data-week-5-lab/week5-7-feedback.py) | A feedback loop (“I am sitting in a model”), with output fed back as input |
| + | [`week5-8-interpolation.py`](performing-data-week-5-lab/week5-8-interpolation.py) | A 30-second automated journey through four prompts, using spherical interpolation of embeddings |

The lab ends with a **reference card** listing the six “dials” of an img2img instrument: strength, prompt, blend rate, feedback, seed and steps. Students are invited to map any of them to anything.

---

## Key concepts

The [tuning notes](performing-data-week-5-lab/sd_turbo_tuning_notes.md) reduce a confusing set of parameters to one idea students can reason with:

```
effective_steps = int(num_inference_steps * strength)
```

They also give practical rules: lower resolution before lowering steps; keep guidance at 0 for Turbo; lower strength means less flicker. Together these let students make informed trade-offs rather than guess.

---

## Why this session works

- **Small steps with a stable base.** Starting from a plain webcam sketch, before any AI, means failures are easy to locate. Each later step adds exactly one capability.
- **Parameters become gestures.** Putting `strength` on the mouse turns an abstract number into something students *play*. The 30-second arc exercise is a first performance.
- **Discussion is part of the lab.** Every activity ends with a question, such as “What changes when the input is purely generative?”, “Performance or automation?” or “Are you performing the model, or is it performing you?”. Critique happens while students make, not afterwards.
- **Real constraints, taught honestly.** Students meet real-time limits (about 3 fps on a laptop) and learn to design around them with threading, frame skipping, lower resolution, or slower deliberate crossfades. They also have an offline route when quality matters more than liveness.
- **Inclusive of hardware.** Install paths cover Apple Silicon, CPU and NVIDIA, the model is small, and the [troubleshooting section](performing-data-week-5-lab/README.md#troubleshooting) covers the problems students actually hit.
- **It ends in performance.** Groups perform to the class, which gives immediate audience feedback and connects to the unit’s focus on live creative practice.
