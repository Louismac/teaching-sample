# Week 2 lab: Generative Text in Performance

← [Week 2 overview](../README.md) · [All teaching samples](../../README.md)

Generate text with a language model running on your own laptop, then perform it.

## Start here

1. **Set up a local model:** follow [Running a local LLM](running-local-llm.md). It covers Apple Silicon (MLX), Windows and Intel Mac (Ollama), and how to step up to larger models.
2. **Choose a brief:** [Performance briefs](brief.md)
3. **Pick a script** from the table below, and change the prompt to suit your brief.

## Files

| File | Platform | What it does |
|---|---|---|
| [`running-local-llm.md`](running-local-llm.md) | All | Setup guide: which script to use, installation, choosing a model size |
| [`brief.md`](brief.md) | All | Three constrained-writing briefs, plus parameters to experiment with (tokens, temperature, models) |
| [`week-2-silicon.py`](week-2-silicon.py) | Apple Silicon | Chat loop in the terminal using MLX (Qwen2.5 3B, 4-bit). Type a prompt, get a response, keep the conversation history |
| [`week-2-ollama.py`](week-2-ollama.py) | Windows, Intel Mac | The same chat loop using Ollama (Qwen2.5 0.5B by default) |
| [`week-2-display-font.py`](week-2-display-font.py) | Apple Silicon | Generates a noir screenplay from a system and user prompt, then shows it line by line in a Dorothy window, like a teleprompter for live performance |
| [`week-2-display-font-ollama.py`](week-2-display-font-ollama.py) | Windows, Intel Mac | The same teleprompter using Ollama |

## Two ways to perform

- **Pre-generate:** use a chat loop to iterate on a script, choose what to keep, rehearse and perform it. Here you are the *curator*.
- **Generate live:** adapt a display script so the text is generated during the performance and the performers respond to what appears. Here you are a *collaborator*, and so is the model.

## Things to try

- Change the temperature: `temp` in `make_sampler()` for MLX, or `"temperature"` in `options` for Ollama. Run the same prompt at 0.2 and at 1.2.
- Limit the length to force an economy of language: `max_tokens` for MLX, or add `"num_predict"` to `options` for Ollama.
- Change the system prompt (“You write terse, cinematic screenplays…”) to change voice and form.
- Change how often the teleprompter advances (`dot.frames % 200`) to set the pace of the performance.

At the end of the session, each group shares its piece in a **table read**.
