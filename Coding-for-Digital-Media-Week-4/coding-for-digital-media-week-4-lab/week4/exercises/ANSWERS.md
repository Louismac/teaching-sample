# Week 4 Exercise Answers: Audio Cut and Paste

← [Lab guide](../../README.md#exercises) · [Week 4 overview](../../../README.md)

Try each exercise properly before you look. There's often more than one right answer; these are just one way of doing it.

## 01 · ex01_format_strings.py

Change

```python
print("{num_samples} samples at {sr}Hz lasts for {num_samples / sr} seconds")
```

to

```python
print(f"{num_samples} samples at {sr}Hz lasts for {num_samples / sr:.2f} seconds")
```

Without the `f`, Python prints the text exactly as written. With it, each `{...}` is replaced by its value, and `:.2f` rounds that value to 2 decimal places.

## 02 · ex02_the_last_two_seconds.py

Change

```python
clip = audio[:sr]
```

to

```python
clip = audio[-sr * 2:]
```

`audio[-sr * 2:]` means "from 2 seconds before the end, to the end".

## 03 · ex03_samples_not_seconds.py

Change

```python
clip = audio[1:3]
```

to

```python
clip = audio[sr * 1:sr * 3]
```

`audio[1:3]` is just 2 samples, which is less than a thousandth of a second. To work in seconds, multiply by `sr`.

## 04 · ex04_third_beat.py

Change

```python
beat = audio[0:samples_in_beat]
```

to

```python
beat = audio[samples_in_beat * 2:samples_in_beat * 3]
```

The third beat has index 2, so it starts at `samples_in_beat * 2` and ends at `samples_in_beat * 3`. It's the same count-from-zero idea as list indexes in Week 3.

## 05 · ex05_playback_speed.py

Change

```python
speed = 2
```

to

```python
speed = 0.5
```

Change

```python
print(f"this will play for {len(audio) / sr:.2f} seconds")
```

to

```python
print(f"this will play for {len(audio) / (sr * speed):.2f} seconds")
```

These are the same samples, interpreted as more or less time. At half the rate they take twice as long (6.4s becomes 12.8s) and the pitch drops an octave, like slowing down a record.

## 06 · ex06_quieter_second_bar.py

Change

```python
audio = audio * 0.2
```

to

```python
audio[half:] = audio[half:] * 0.2
```

`audio[half:]` picks out the second bar. Multiplying it by 0.2 and writing it back changes only that part.

## 07 · ex07_fade_out.py

Change

```python
ramp = np.linspace(0, 1, len(audio), dtype=np.float32)
```

to

```python
ramp = np.linspace(1, 0, len(audio), dtype=np.float32)
```

Sample 0 gets multiplied by `ramp[0]`, sample 1 by `ramp[1]`, and so on. A ramp from 1 to 0 turns the volume down over time.

## 08 · ex08_reverse_one_beat.py

Change

```python
audio = np.flip(audio)
```

to

```python
audio[-samples_in_beat:] = np.flip(audio[-samples_in_beat:])
```

This is the same pattern as Exercise 06: pick a slice, change it, and put it back in the same place.

## 09 · ex09_paste_must_fit.py

Change

```python
audio[samples_in_beat:samples_in_beat * 4] = cut
```

to

```python
audio[samples_in_beat:samples_in_beat * 3] = cut
```

"could not broadcast input array from shape (A,) into shape (B,)" means the two sizes don't match. Getting that error is normal, and now you know what it means.

## 10 · ex10_third_tape_recorder.py

Change

```python
start = sr * 0
```

to

```python
start = sr * 4
```

Change

```python
timeline[start:end] = harp
```

to

```python
timeline[start:end] = timeline[start:end] + harp
```

`end = start + len(harp)` makes the slice the right size automatically (see Exercise 09). `=` replaces what's on the timeline, and `+` layers on top of it.
