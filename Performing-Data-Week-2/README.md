# Performing Data, Week 2: Generative Text in Performance

← [All teaching samples](../README.md) · [Teaching approach](../TEACHING-APPROACH.md)

> **In one sentence:** from Strachey’s 1953 love letters and Fluxus event scores to GPT-written films, students explore generated text as script, score and collaborator. They then run a language model on their own laptop and perform what it writes.

| | |
|---|---|
| **Unit** | Performing Data · MSc Applied Machine Learning for Creatives · Term 3 · 20 credits |
| **Session length** | 4 hours: lecture, screening, lab, “table read” |
| **Prior knowledge** | Python, and the Dorothy draw loop |
| **Tools** | A local LLM (Qwen2.5) through [MLX](https://github.com/ml-explore/mlx) on Apple Silicon or [Ollama](https://ollama.com) elsewhere; [Dorothy](https://github.com/Louismac/dorothy) |
| **Student output** | A short performance using generated text, read or performed to the group |
| **Full plan** | [delivery-context.md](delivery-context.md) |

**Contents:** [Learning outcomes](#learning-outcomes) · [Session plan](#session-plan) · [Materials](#materials-in-this-folder) · [Lecture](#lecture) · [Screening](#screening-ai-scripted-films) · [Lab](#lab) · [Critical framing](#critical-and-ethical-framing) · [Why it works](#why-this-session-works)

---

## Learning outcomes

By the end of the session, students will be able to:

| # | Class learning outcome | Unit outcome | Practised in |
|---|---|---|---|
| 1 | Trace a history of generative text in art and performance, from template systems and Fluxus event scores to neural language models, and tell “human as curator” apart from “human as collaborator” approaches | LO3 | [Lecture](performing-data-week-2-slides.pdf) |
| 2 | Run a small language model locally and shape its output through prompts, system messages, temperature, token limits and model size | LO1 | [Lab scripts](performing-data-week-2-lab/README.md) |
| 3 | Design and perform a short piece in which generated text works as script, score or live material | LO1 | [Performance briefs](performing-data-week-2-lab/brief.md), table read |
| 4 | Critically reflect on authorship, curation and harmful outputs in AI-generated text for performance | LO3 | Screening discussion, table read |

The unit learning outcomes (LO1–LO3) are listed in full in [delivery-context.md](delivery-context.md#learning-outcomes-of-unit).

---

## Session plan

| Block | Activity | Materials |
|---|---|---|
| Lecture | Generative text from templates to transformers, and text as instruction | [Slides (PDF, 60 slides)](performing-data-week-2-slides.pdf) |
| Break | | |
| Screening and discussion | *Sunspring* (2016) and *Date Night* (2021), two films scripted by AI | [Links](#screening-ai-scripted-films) |
| Lab | Run a local LLM; generate a script, score or live text under a constraint | [Lab guide](performing-data-week-2-lab/README.md) · [Briefs](performing-data-week-2-lab/brief.md) |
| Table read | Groups perform or read their outputs, and reflect | |

Exact timings are in [delivery-context.md](delivery-context.md#lesson-schedule-4-hours).

---

## Materials in this folder

| File | What it is |
|---|---|
| [`performing-data-week-2-slides.pdf`](performing-data-week-2-slides.pdf) | The lecture: 60 slides |
| [`performing-data-week-2-lab/`](performing-data-week-2-lab/) | Briefs, setup guide and four scripts. See the [lab guide](performing-data-week-2-lab/README.md) |
| [`delivery-context.md`](delivery-context.md) | Unit description, learning outcomes, schedule, screening links |

---

## Lecture

The [slides](performing-data-week-2-slides.pdf) are built around two ideas. One is the human’s role (**curator or collaborator?**, after Chung, 2021). The other is generated text not as an end product but as **instruction**: a script, a score or a prompt for something else.

| Section | Examples |
|---|---|
| Generative text and human collaboration | Kate Compton’s *Opulent AI*; human in the loop (Chung, 2021); Eric Drass, *Viq & I* |
| Template-based text art | Christopher Strachey’s love-letter generator (1953) and its place in queer computing history; Kate Compton’s *Tracery*; David Lublin’s *TV Comments Bot* |
| Beyond “what comes next?” | Allison Parrish’s computational poetry; Ross Goodwin’s *1 the Road* (2018) |
| Words and music | The Seals (NIME 2021); the AI Song Contest |
| Performing AI | Janelle Shane’s *A.I.nktober*; *Sunspring*; Shardcore’s *Algonory*; Calamity AI’s *Date Night*; Annie Dorsen’s *A Piece of Work* (2013) |
| Into the GPT era | Janelle Shane on clichés; neologisms; K Allado-McDowell’s *Pharmako-AI*; *AI Dungeon*; *Nothing, Forever* |
| Text as instruction | Fluxus event scores and Yoko Ono’s *Grapefruit*; Alison Knowles and James Tenney’s *The House of Dust* (1967); Sol LeWitt’s wall drawings and Amy Goodchild’s ChatGPT versions; Jennifer Walshe’s *Text Score Dataset*; Eryk Salvaggio’s *Fluxus Ex Machina* |
| Text to everything | Generated text as the control interface for image, music, video and 3D |

---

## Screening: AI-scripted films

- [*Sunspring* (2016)](https://www.youtube.com/watch?v=LY7x2Ihqjmc): a script generated by a character-level RNN trained on science-fiction screenplays
- [*Date Night* (2021)](https://www.youtube.com/watch?v=xY1VWZPJ5FE&t=2s): a script generated by GPT-3 from a short prompt. The makers discarded two earlier versions, one because of misogynistic violence.

Watching both side by side shows students how the technology changed, and how much human interpretation (actors, directors, editors) a generated text needs before it becomes a performance.

---

## Lab

Students choose a brief and a way of working. They can pre-generate a script and perform it, or generate text live during the performance.

**Briefs** ([`brief.md`](performing-data-week-2-lab/brief.md)):

- **Constrained vocabulary:** a two-minute monologue using only words from one category
- **One sentence, infinite variations:** expand one sentence under a rule, such as only questions, only stage directions, or every line rhyming
- **The repetition piece:** one phrase repeated seven times, its meaning shifting each time

**Parameters to experiment with:**

- token limits, as an economy of language
- temperature, from predictable to chaotic, and mixing temperatures within one piece
- different models

**Code:** two chat-loop scripts, for Apple Silicon or Windows and Intel, and two that display a generated screenplay line by line in a Dorothy window, like a teleprompter for performers. The [lab guide](performing-data-week-2-lab/README.md) explains which to use.

---

## Critical and ethical framing

The session keeps returning to four questions:

- **Who is the author?** The model, the prompter, the curator who throws away bad outputs, or the actors who make it work?
- **What gets curated out?** *Date Night*’s discarded scripts and Eryk Salvaggio’s note on GPT-2’s “weird propensity toward violence” show that curation is also content moderation.
- **Is “better” better for art?** Janelle Shane argues large models are good at cliché, so artists have to work harder to be weird. Salvaggio found GPT-3 *too* good at removing the ambiguity that made his scores generative.
- **What does running a model locally change?** Privacy, cost and control, compared with cloud services.

---

## Why this session works

- **Deep context before tools.** Students meet 70 years of generative text practice, so they see LLMs as one more step in a tradition of rules, chance and instruction, not as magic.
- **A conceptual bridge from scores to prompts.** Fluxus event scores and LeWitt’s instructions give students a way to think about prompting as composition.
- **Accessible and private.** The model runs offline on students’ own laptops, with no API keys, costs or data leaving the room. Students with more RAM can step up to bigger models.
- **Constraints that spark creativity.** Each brief has a tight, playful constraint, which makes the exercise about creative decisions rather than prompt luck.
- **Feedback through performance.** The table read gives every group an audience and immediate peer response.
