# Teaching approach

← [Back to the overview](README.md)

---

## 1. Constructive alignment

Every session starts from the unit’s learning outcomes and narrows them to three or four class outcomes. Each class outcome is then practised in the lab and revisited in the critical activity, so that what is taught, what students do and what is discussed all point at the same goals.

Where to see it: the outcome tables in each overview.

| Session | Outcomes |
|---|---|
| Coding for Digital Media, Week 4 | [Learning outcomes](Coding-for-Digital-Media-Week-4/README.md#learning-outcomes) |
| Data Science in Creative Industries, Week 1 | [Learning outcomes](Data-Science-In-Creative-Industries-Week-1/README.md#learning-outcomes) |
| Performing Data, Week 2 | [Learning outcomes](Performing-Data-Week-2/README.md#learning-outcomes) |
| Performing Data, Week 5 | [Learning outcomes](Performing-Data-Week-5/README.md#learning-outcomes) |

## 2. Technique and critique

No technique is taught on its own. Each session pairs a technical skill with a critical question about power, culture or ethics. The unit outcomes explicitly ask students to “think critically about the use of technology and AI in creative work”, so this question is part of the core content rather than an add-on.

| Technical skill | Critical question | Where |
|---|---|---|
| Slicing and mixing audio arrays | Who owns a sample? When is borrowing creative, and when is it theft? | [Seminar prompts](Coding-for-Digital-Media-Week-4/Seminar-prompts.md) |
| Loading, filtering and summarising a dataset with pandas | Whose lives does a dataset record, and whose does it erase? | [Legacies of British Slavery notebook](Data-Science-In-Creative-Industries-Week-1/legacies-of-british-slavery-notebook.ipynb) |
| Finding and opening datasets | Which datasets don’t exist, and why? | [Missing Datasets task](Data-Science-In-Creative-Industries-Week-1/ds-for-ci-week-1-lab/lab-brief.md#missing-datasets-task) |
| Prompting and sampling a local LLM | Who is the author of a generated script? | [Week 2 discussion](Performing-Data-Week-2/README.md#critical-and-ethical-framing) |
| Real-time img2img diffusion | Are you performing the model, or is it performing you? | [Week 5 wrap-up](Performing-Data-Week-5/performing-data-week-5-lab/README.md#wrap-up-discussion) |

The notebook opens with a content warning and frames the analysis around decolonial practice. Students are directed to resources centred on the lives of enslaved people, not only on the property of slave-owners.

## 3. Grounding code in diverse histories of practice

Technical ideas are introduced through the artists and communities who pioneered them, so students see code as part of a creative lineage they can join. These figures are deliberately chosen to go beyond the usual canon:

- **Week 4 (audio):** Pierre Schaeffer, John Cage, Daphne Oram and Delia Derbyshire of the BBC Radiophonic Workshop, hip-hop DJs and producers (Kool Herc, Grandmaster Flash, Afrika Bambaataa, The Bomb Squad), John Oswald, and Kate Bush’s use of the Fairlight.
- **Week 1 (data):** Mimi Onuoha’s *Library of Missing Datasets*, Giorgia Lupi and Stefanie Posavec’s *Dear Data*, Johanna Drucker on *capta*, and Lisa Gitelman and Geoffrey Bowker on “raw data”.
- **Week 2 (text):** Christopher Strachey’s 1953 love-letter generator and its place in queer computing history, Kate Compton’s *Tracery*, Allison Parrish, Ross Goodwin, and the feminist noise band The Seals.

## 4. A consistent session shape

Each four-hour session follows a recognisable arc. Students know what to expect, and each activity builds on the one before:

```
Lecture (context + concepts) → Live code / notebook → Break → Critical activity → Lab (making) → Share / perform
```

Timed plans are in each `delivery-context.md`.

## 5. Scaffolded, low-barrier code

Example code is short, with one idea per file, named after the concept it shows (`week4-cut.py`, `week4-fadein.py`, `week5-2-singleshot.py`). Activities are ordered so each one adds a single new idea to the last.

## 6. Equitable access to tools

Students use their own laptops, so no session assumes expensive hardware or paid accounts:

- **Performing Data, Week 2** runs a 0.5B-parameter language model locally, with separate paths for Apple Silicon (MLX) and Windows or Intel machines (Ollama). A table helps students with more RAM step up to larger models. See [running a local LLM](Performing-Data-Week-2/performing-data-week-2-lab/running-local-llm.md).
- **Performing Data, Week 5** uses SD Turbo, which needs only 1–4 steps. Install instructions cover Apple Silicon, CPU and NVIDIA. An [offline rendering extension](Performing-Data-Week-5/performing-data-week-5-lab/README.md#extension--offline-rendering-to-video) lets students on slower machines still produce high-quality work.
- **Troubleshooting sections** anticipate the common failures, such as the wrong webcam index, display scaling and window focus. See the [Week 5 troubleshooting notes](Performing-Data-Week-5/performing-data-week-5-lab/README.md#troubleshooting).

## 7. Learning by making, sharing and performing

Every session ends with students making something and sharing it, which gives immediate peer and tutor feedback:

| Session | Output | How it’s shared |
|---|---|---|
| Coding for Digital Media, Week 4 | A sound collage | [Brief](Coding-for-Digital-Media-Week-4/README.md#lab-and-collage-brief) |
| Data Science in Creative Industries, Week 1 | A hand-made data drawing or performance | Gallery walk (“check out your colleagues’ results”) |
| Performing Data, Week 2 | A script or live-generated performance | A “table read” of student outputs |
| Performing Data, Week 5 | A live AI-visual performance | Group performances at the end of class |
