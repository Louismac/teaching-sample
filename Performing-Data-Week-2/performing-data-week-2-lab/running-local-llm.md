# Week 2 — Running a Local LLM

← [Lab guide](README.md) · [Week 2 overview](../README.md)

Both scripts run a local text generation model (Qwen2.5 0.5B) in a simple input loop: type a prompt, get a response.

---

## Which should I use?

| | `week-2-silicon.py` | `week-2-ollama.py` |
|---|---|---|
| **Best for** | Mac with Apple Silicon (M1/M2/M3) | Everyone else (Windows, Intel Mac) |
| **Install size** | ~400 MB | ~400 MB + Ollama app |
| **Speed** | Fast (uses Metal GPU) | Good (optimised CPU/GPU) |
| **Requires** | Apple Silicon Mac | Ollama installed |

---

## Option 1: `week-2-silicon.py` — Apple Silicon Mac only

### Install

```bash
pip install mlx-lm
```

### Run

```bash
python week-2-silicon.py
```

The model (~400 MB) downloads automatically on first run and is cached for future sessions.

---

## Option 2: `week-2-ollama.py` — Windows or Intel Mac

### Install

1. Download and install Ollama from [ollama.com](https://ollama.com)
2. Install the Python package:

```bash
pip install ollama
```

### Run

Download model first e.g.

```bash
ollama pull qwen2.5:0.5b
```

```bash
python week-2-ollama.py
```

---

## Using the scripts

Both scripts run an input loop — type your prompt and press Enter to get a response. Press `Ctrl+C` to quit.

---

## Want to try a larger model?

If you have more disk space and RAM, try swapping the model for a larger version. The code is identical — just change the model name.

| Model | Size | RAM needed | Quality |
|---|---|---|---|
| 0.5B (default) | ~400 MB | 2 GB | Baseline |
| **1.5B** | ~900 MB | 4 GB | Noticeably better |
| **3B** | ~2 GB | 8 GB | Strong, recommended if you can |

### Apple Silicon — change this line in `week-2-silicon.py`:

```python
# 1.5B
model, tokenizer = load("mlx-community/Qwen2.5-1.5B-Instruct-4bit")

# 3B
model, tokenizer = load("mlx-community/Qwen2.5-3B-Instruct-4bit")
```

### Ollama — change this line in `week-2-ollama.py`:

```python
# 1.5B
model="qwen2.5:1.5b"

# 3B
model="qwen2.5:3b"
```

Or pre-download before class:

```bash
ollama pull qwen2.5:1.5b
ollama pull qwen2.5:3b
```
