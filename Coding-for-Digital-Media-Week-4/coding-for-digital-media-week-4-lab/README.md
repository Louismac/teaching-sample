# Week 4 lab: Audio Cut and Paste

← [Week 4 overview](../README.md) · [All teaching samples](../../README.md)

Example sketches, audio loops and scaffolded exercises for [Coding for Digital Media, Week 4](../README.md).

## Setup

```bash
pip install dorothy-cci librosa numpy
cd coding-for-digital-media-week-4-lab      # run everything from this folder
python week4/week4-waveform.py
```

All audio paths are relative (`week4/audio/drums.wav`), so run the scripts from this folder. Each sketch plays its audio and draws the waveform with a moving playhead, so students can see what they hear.

## Audio

| File | Length | Contents |
|---|---|---|
| [`drums.wav`](week4/audio/drums.wav) | 4.53 s | 2 bars of 4 beats at 106 bpm (99,849 samples at librosa’s default 22,050 Hz) |
| [`drums75.wav`](week4/audio/drums75.wav) | 6.4 s | 2-bar drum loop at 75 bpm |
| [`keys4.wav`](week4/audio/keys4.wav) | 6.4 s | 2-bar keyboard loop, same length as `drums75.wav` |
| [`harp1.wav`](week4/audio/harp1.wav) | 6.4 s | 2-bar harp loop, same length as `drums75.wav` |

The loops share lengths so they can be overwritten and mixed without any extra maths. The `drums.wav` and `drums75.wav` pair, at different tempos, is used for the beat-matching extension.

## Example sketches

These are run live during the code lecture, roughly in this order. Each file shows one idea.

| # | Sketch | Concept | Key line |
|---|---|---|---|
| 1 | [`week4-waveform.py`](week4/week4-waveform.py) | Load, play and draw audio; length in seconds | `audio, sr = librosa.load(...)` |
| 2 | [`week4-cut.py`](week4/week4-cut.py) | Slicing by seconds and rejoining the pieces | `audio[sr:sr*3]`, `np.concatenate(...)` |
| 3 | [`week4-bars.py`](week4/week4-bars.py) | Slicing by beats instead of seconds; bar and beat lines drawn on the waveform | `samples_in_beat = samples_in_bar // 4` |
| 4 | [`week4-paste.py`](week4/week4-paste.py) | Overwriting part of one sound with part of another | `audio[a:b] = cut` |
| 5 | [`week4-mix.py`](week4/week4-mix.py) | Mixing by adding arrays item by item | `audio + drums` |
| 6 | [`week4-quieter.py`](week4/week4-quieter.py) | Volume | `audio * 0.1` |
| 7 | [`week4-fadein.py`](week4/week4-fadein.py) | Fading with a ramp. The file currently ramps from 1 to 0, a fade *out*; swap the numbers for a fade in | `audio * np.linspace(1, 0, len(audio))` |
| 8 | [`week4-reverse.py`](week4/week4-reverse.py) | Reverse | `np.flip(audio)` |
| 9 | [`week4-faster.py`](week4/week4-faster.py) / [`week4-slower.py`](week4/week4-slower.py) | Speed and pitch through the sample rate: faster resamples to half the samples; slower plays at half the rate | `librosa.resample(...)` / `sr=sr/2` |
| 10 | [`week4-paste-into-blank.py`](week4/week4-paste-into-blank.py) | The “third tape recorder”: overwrite *and* mix into a silent timeline | `timeline = np.zeros(sr*60)` |

**Extensions** for confident students:

| Sketch | What it adds |
|---|---|
| [`week4-paste-into-blank-rhythmic.py`](week4/week4-paste-into-blank-rhythmic.py) | Uses loops to paste a kick drum at ever-faster divisions of the beat, building a drum-roll “drop” |
| [`week4-beat-match.py`](week4/week4-beat-match.py) | Resamples a 75 bpm loop to match a 106 bpm loop, then mixes them |
| [`fft.py`](week4/fft.py) | A live frequency spectrum, previewing next week’s topic of perception and analysis |
| [`util.py`](week4/util.py) | Helper that draws bar and beat lines over the waveform |

## Exercises

Ten short exercises in [`week4/exercises/`](week4/exercises/). Each targets one concept and opens with the same header:

```
PREDICT  What do you think will happen?
RUN      python week4/exercises/exNN_....py
TASK     what to change
HINT     a nudge, not the answer
CHECK    what success looks and sounds like
```

**FIX** exercises start broken and ask students to repair them. **MODIFY** exercises start working and ask students to change what they do.

| # | Exercise | Type | Concept |
|---|---|---|---|
| 01 | [`ex01_format_strings.py`](week4/exercises/ex01_format_strings.py) | FIX | f-strings and `:.2f` |
| 02 | [`ex02_the_last_two_seconds.py`](week4/exercises/ex02_the_last_two_seconds.py) | MODIFY | Slicing with `[start:end]` and negative indexes |
| 03 | [`ex03_samples_not_seconds.py`](week4/exercises/ex03_samples_not_seconds.py) | FIX | Indexes are samples, not seconds |
| 04 | [`ex04_third_beat.py`](week4/exercises/ex04_third_beat.py) | MODIFY | Slicing by musical time |
| 05 | [`ex05_playback_speed.py`](week4/exercises/ex05_playback_speed.py) | FIX | Sample rate controls speed and pitch |
| 06 | [`ex06_quieter_second_bar.py`](week4/exercises/ex06_quieter_second_bar.py) | MODIFY | Maths on part of a list |
| 07 | [`ex07_fade_out.py`](week4/exercises/ex07_fade_out.py) | MODIFY | Item-wise multiplication with a ramp |
| 08 | [`ex08_reverse_one_beat.py`](week4/exercises/ex08_reverse_one_beat.py) | MODIFY | `np.flip()` on a slice |
| 09 | [`ex09_paste_must_fit.py`](week4/exercises/ex09_paste_must_fit.py) | FIX | Pasting: the slice and the cut must be the same size (reading a `ValueError`) |
| 10 | [`ex10_third_tape_recorder.py`](week4/exercises/ex10_third_tape_recorder.py) | FIX | Pasting into a blank timeline, then mixing instead of replacing |

**Answers:** [`ANSWERS.md`](week4/exercises/ANSWERS.md) gives the change for each exercise and a short explanation of *why* it works. Students are encouraged to try each exercise properly first.

## Then: the sound collage

Once the exercises are done, students apply the same techniques to their own audio. See the [collage brief](../README.md#lab-and-collage-brief).
