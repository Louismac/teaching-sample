# Coding for Digital Media, Week 4: Cut and Paste Audio

← [All teaching samples](../README.md) · [Teaching approach](../TEACHING-APPROACH.md)

> **In one sentence:** students discover that an audio file is just a list of numbers, then use list slicing and array arithmetic to cut, paste, mix and transform sound. They do this in the tradition of tape composers and hip-hop producers, and finish by making their own sound collage.

| | |
|---|---|
| **Unit** | Coding for Digital Media |
| **Session length** | 4 hours: lecture, live-code lecture, seminar and lab |
| **Prior knowledge** | Python variables and lists, including indexing from Week 3 |
| **Tools** | Python, [librosa](https://librosa.org/), NumPy, [Dorothy](https://github.com/Louismac/dorothy) |
| **Student output** | A sound collage made in code |
| **Full plan** | [delivery-context.md](delivery-context.md) |

**Contents:** [Learning outcomes](#learning-outcomes) · [Session plan](#session-plan) · [Materials](#materials-in-this-folder) · [Lecture](#lecture) · [Animations](#animations) · [Seminar](#seminar) · [Lab and collage brief](#lab-and-collage-brief) · [Why it works](#why-this-session-works) · [Running the code](#running-the-code)

---

## Learning outcomes

By the end of the session, students will be able to:

| # | Class learning outcome | Unit outcome | Practised in |
|---|---|---|---|
| 1 | Load, manipulate and rearrange audio files in Python using list range indexing (slicing) | LO1, LO3 | [Exercises 02–04, 09–10](coding-for-digital-media-week-4-lab/week4/exercises/), [week4-cut.py](coding-for-digital-media-week-4-lab/week4/week4-cut.py), [week4-paste.py](coding-for-digital-media-week-4-lab/week4/week4-paste.py) |
| 2 | Use array arithmetic to change perceptual characteristics (volume, fades, speed, pitch) and to recombine audio | LO2, LO3 | [Exercises 05–08](coding-for-digital-media-week-4-lab/week4/exercises/), [week4-fadein.py](coding-for-digital-media-week-4-lab/week4/week4-fadein.py), [week4-mix.py](coding-for-digital-media-week-4-lab/week4/week4-mix.py) |
| 3 | Reflect on analog and digital sampling as both a cultural and an aesthetic choice | LO1 | [Seminar prompts](Seminar-prompts.md), lecture Part 3 (history of cut and paste) |

The unit learning outcomes (LO1–LO3) are listed in full in [delivery-context.md](delivery-context.md#learning-outcomes-of-unit).

---

## Session plan

| Block | Activity | Materials |
|---|---|---|
| Lecture | Sound → digital audio → a history of cut and paste → cutting and pasting in code | [Combined lecture (PDF)](coding4dm-week4-combined-lecture.pdf) |
| Live-code lecture | Run the example sketches one by one, predicting what each will sound like | [Example sketches](coding-for-digital-media-week-4-lab/README.md#example-sketches) |
| Break | | |
| Seminar | Small groups pick one of five prompts on the ethics, law and culture of sampling | [Seminar prompts](Seminar-prompts.md) |
| Lab | Ten scaffolded exercises, then an open sound collage | [Exercises](coding-for-digital-media-week-4-lab/README.md#exercises) · [Collage brief](#lab-and-collage-brief) |

Exact timings are in [delivery-context.md](delivery-context.md#lesson-schedule-4-hours).

---

## Materials in this folder

| File | What it is |
|---|---|
| [`coding4dm-week4-combined-lecture.pdf`](coding4dm-week4-combined-lecture.pdf) | **The main lecture.** 63 slides with speaker notes, combining the slide lecture and the code lecture into one narrative, with redrawn diagrams |
| [`coding4dm-week4-slides.pdf`](coding4dm-week4-slides.pdf) | The original 27-slide deck: physics of sound, digital audio, history of sampling |
| [`animations/`](animations/) | Six short MP4 animations used in the lecture, three of them with sound |
| [`Seminar-prompts.md`](Seminar-prompts.md) | Five discussion prompts on sampling, copyright and culture |
| [`delivery-context.md`](delivery-context.md) | Unit description, learning outcomes, schedule, further reading |
| [`coding-for-digital-media-week-4-lab/`](coding-for-digital-media-week-4-lab/) | Example sketches, audio loops, exercises and answers. See the [lab guide](coding-for-digital-media-week-4-lab/README.md) |

---

## Lecture

The [combined lecture](coding4dm-week4-combined-lecture.pdf) answers four questions in five parts. A tracker at the top of each slide shows where students are in the story.

| Part | Content | Question it answers |
|---|---|---|
| 1 · Sound | Vibrations, air pressure, microphones as transducers, from air to file | What is sound, and how is it recorded? |
| 2 · Digital audio | Sampling, sample rate, bit depth, audio as a list, `librosa.load`, format strings, drawing a waveform | What is inside an audio file? |
| 3 · A history of cut and paste | Schaeffer, Stockhausen, Cage, Daphne Oram, Delia Derbyshire, the Mellotron, hip-hop DJs, the Fairlight, the SP-1200 and MPC, Plunderphonics, mashups | Who cut and pasted sound before computers? |
| 4 · Cutting | Slicing `[start:end]`, cutting by seconds and by beats, musical timing, integer division | How do we cut audio in Python? |
| 5 · Pasting and editing | Overwriting, mixing, “lists join but arrays add”, clipping, volume, fades, reverse, speed and pitch | How do we paste and edit it? |

The lecture closes with Daphne Oram’s idea of the **“third tape recorder”**: pasting into a blank canvas. That idea leads straight into the collage brief.

---

## Animations

Short animations make abstract ideas visible. Each is under 10 seconds long and loops. The PDF export shows only a still, so the MP4 files are included here for presenting or dropping into PowerPoint.

| Animation | Shows | Sound |
|---|---|---|
| [air-pressure.mp4](animations/air-pressure.mp4) | Molecules compressing and rarefying, with the pressure wave they make | – |
| [sampling.mp4](animations/sampling.mp4) | A continuous wave measured at regular intervals and becoming a Python list | – |
| [waveform-playhead-sound.mp4](animations/waveform-playhead-sound.mp4) | What `week4-waveform.py` draws: the waveform with a moving playhead | ✓ |
| [speed-and-pitch-sound.mp4](animations/speed-and-pitch-sound.mp4) | The same samples played at `sr`, `sr*2` and `sr/2` | ✓ |
| [hear-the-edits-sound.mp4](animations/hear-the-edits-sound.mp4) | One bar played as is, at `* 0.2`, faded in with a ramp, and reversed | ✓ |
| [collage.mp4](animations/collage.mp4) | Clips pasted one by one into a blank timeline, then played through | – |

---

## Seminar

The [seminar prompts](Seminar-prompts.md) ask groups to pick one of five themes:

1. **Artistic intent vs. legal reality:** parody, experimentation and commercial use
2. **Technology and accessibility:** who gets to make sound collage when tools become cheap
3. **Cultural context and musical borrowing:** African American, Jamaican and Brazilian traditions against Western ideas of originality
4. **High art vs. popular music:** why sampling is policed more than visual appropriation
5. **Recognition and transformation:** Oswald’s plunderphonics compared with dub “versioning”

These connect learning outcome 3 to the history in Part 3 of the lecture. They also prepare students to make deliberate choices about source material in their own collages. Readings are listed under [Additional materials](delivery-context.md#additional-materials).

---

## Lab and collage brief

**1. Scaffolded exercises.** Ten short exercises, each targeting one concept. They are labelled **FIX**, where students debug broken code, or **MODIFY**, where they change working code. Every file opens with *Predict → Run → Task → Hint → Check*, and there are [worked answers](coding-for-digital-media-week-4-lab/week4/exercises/ANSWERS.md) for after students have tried. A full list is in the [lab guide](coding-for-digital-media-week-4-lab/README.md#exercises).

**2. Sound collage.** Students source their own audio (music, field recordings, spoken word, found sound) and assemble a new composition in code. They use at least these techniques:

| Technique | Code idea | Example |
|---|---|---|
| Volume | `clip * 0.5` | [week4-quieter.py](coding-for-digital-media-week-4-lab/week4/week4-quieter.py) |
| Cut, rearrange and repeat | `audio[start:end]`, `np.concatenate` | [week4-cut.py](coding-for-digital-media-week-4-lab/week4/week4-cut.py) |
| Fades | `clip * np.linspace(0, 1, len(clip))` | [week4-fadein.py](coding-for-digital-media-week-4-lab/week4/week4-fadein.py), [exercise 07](coding-for-digital-media-week-4-lab/week4/exercises/ex07_fade_out.py) |
| Reverse | `np.flip(clip)` | [week4-reverse.py](coding-for-digital-media-week-4-lab/week4/week4-reverse.py) |
| Speed and pitch | change `sr`, or resample | [week4-faster.py](coding-for-digital-media-week-4-lab/week4/week4-faster.py), [week4-slower.py](coding-for-digital-media-week-4-lab/week4/week4-slower.py) |
| Paste into a blank timeline | `timeline = np.zeros(sr * 60)` | [week4-paste-into-blank.py](coding-for-digital-media-week-4-lab/week4/week4-paste-into-blank.py) |

Students are asked whether their piece is **abstract**, built on juxtaposition and texture, or **musically sequenced**, and when to **overwrite** rather than **mix**. Audacity is suggested for finding good cut points.

---

## Why this session works

- **A familiar medium for an abstract idea.** Indexing and slicing are easy to describe and hard to *feel*. Applied to sound, an off-by-one slice is something you can hear.
- **It builds directly on Week 3.** List indexing from last week becomes slicing this week. Overwriting one item (`colour[1] = 34`) becomes overwriting a range (`audio[a:b] = cut`).
- **Mistakes are expected and explained.** Exercise 09 crashes on purpose with a real `ValueError` so students learn to read it. The lecture explains the error message too.
- **Maths with a musical reason.** Students work out samples per beat (`len(audio) // 2 // 4`) because cutting by seconds sounds wrong. Integer division arrives because they need it.
- **Culture as content.** The history section shows that every operation students code, from looping to reversing to changing speed, was first an artistic decision made with tape and vinyl. The seminar then asks who gets to sample whom.
- **An open creative ending.** The collage is open-ended, so confident students can stretch, for example with the rhythmic and beat-matching extension sketches, while everyone still meets the core outcomes.

---

## Running the code

```bash
pip install dorothy-cci librosa numpy
cd coding-for-digital-media-week-4-lab
python week4/week4-waveform.py
```

Run the sketches from inside `coding-for-digital-media-week-4-lab/`, because the audio paths are relative (`week4/audio/...`). The [lab guide](coding-for-digital-media-week-4-lab/README.md) has the full file list.
