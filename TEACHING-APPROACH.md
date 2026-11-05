# Teaching approach

← [Back to the overview](README.md)

This page explains the design principles behind the four sessions and points to where each one can be seen in the materials. It ends with a mapping to the [Advance HE Professional Standards Framework (PSF 2023)](https://www.advance-he.ac.uk/teaching-learning/professional-standards-framework).

**Contents**
- [1. Constructive alignment](#1-constructive-alignment)
- [2. Technique and critique, together](#2-technique-and-critique-together)
- [3. Grounding code in diverse histories of practice](#3-grounding-code-in-diverse-histories-of-practice)
- [4. A consistent session shape](#4-a-consistent-session-shape)
- [5. Scaffolded, low-barrier code](#5-scaffolded-low-barrier-code)
- [6. Equitable access to tools](#6-equitable-access-to-tools)
- [7. Making the abstract visible](#7-making-the-abstract-visible)
- [8. Learning by making, sharing and performing](#8-learning-by-making-sharing-and-performing)
- [Mapping to the PSF 2023](#mapping-to-the-professional-standards-framework-psf-2023)

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

## 2. Technique and critique, together

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

The [Week 4 exercises](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/week4/exercises/) use a structured format inspired by PRIMM (Predict–Run–Investigate–Modify–Make). Each file opens with:

```
PREDICT  What do you think will happen?
RUN      the exact command
TASK     what to change
HINT     a nudge, not the answer
CHECK    what success looks and sounds like
```

They mix **FIX** tasks, where students debug deliberately broken code including a real `ValueError`, with **MODIFY** tasks, where they extend working code. Each one comes with [worked answers](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/week4/exercises/ANSWERS.md) that explain *why*, not just *what*. Error messages are treated as normal and readable, never as failure.

## 6. Equitable access to tools

Students use their own laptops, so no session assumes expensive hardware or paid accounts:

- **Performing Data, Week 2** runs a 0.5B-parameter language model locally, with separate paths for Apple Silicon (MLX) and Windows or Intel machines (Ollama). A table helps students with more RAM step up to larger models. See [running a local LLM](Performing-Data-Week-2/performing-data-week-2-lab/running-local-llm.md).
- **Performing Data, Week 5** uses SD Turbo, which needs only 1–4 steps. Install instructions cover Apple Silicon, CPU and NVIDIA. An [offline rendering extension](Performing-Data-Week-5/performing-data-week-5-lab/README.md#extension--offline-rendering-to-video) lets students on slower machines still produce high-quality work.
- **Troubleshooting sections** anticipate the common failures, such as the wrong webcam index, display scaling and window focus. See the [Week 5 troubleshooting notes](Performing-Data-Week-5/performing-data-week-5-lab/README.md#troubleshooting).

## 7. Making the abstract visible

Abstract ideas are drawn, animated or made audible:

- The Week 4 lecture uses computed diagrams and [six short animations](Coding-for-Digital-Media-Week-4/README.md#animations): air pressure, sampling, playback rate, a waveform playhead, edits you can hear, and a collage being built.
- Every code example draws its waveform on screen with a playhead, so students *see* the slice they cut while they hear it.
- The [SD Turbo tuning notes](Performing-Data-Week-5/performing-data-week-5-lab/sd_turbo_tuning_notes.md) turn a confusing set of parameters into a single formula and a rules-of-thumb table.

## 8. Learning by making, sharing and performing

Every session ends with students making something and sharing it, which gives immediate peer and tutor feedback:

| Session | Output | How it’s shared |
|---|---|---|
| Coding for Digital Media, Week 4 | A sound collage | [Brief](Coding-for-Digital-Media-Week-4/README.md#lab-and-collage-brief) |
| Data Science in Creative Industries, Week 1 | A hand-made data drawing or performance | Gallery walk (“check out your colleagues’ results”) |
| Performing Data, Week 2 | A script or live-generated performance | A “table read” of student outputs |
| Performing Data, Week 5 | A live AI-visual performance | Group performances at the end of class |

---

## Mapping to the Professional Standards Framework (PSF 2023)

The table shows where each dimension of the [PSF 2023](https://www.advance-he.ac.uk/teaching-learning/professional-standards-framework) is evidenced in this repository.

### Areas of Activity

| Dimension | Evidence |
|---|---|
| **A1** Design and plan learning activities and/or programmes | Timed lesson plans and aligned outcomes in every `delivery-context.md`. The sequenced lab in [Week 5](Performing-Data-Week-5/performing-data-week-5-lab/README.md). The [Week 4 lecture](Coding-for-Digital-Media-Week-4/coding4dm-week4-combined-lecture.pdf), restructured into one narrative from slides and a code lecture. |
| **A2** Teach and/or support learning through appropriate approaches and environments | Lecture → live code → lab → critique. Group tasks such as [Missing Datasets](Data-Science-In-Creative-Industries-Week-1/ds-for-ci-week-1-lab/lab-brief.md). Performance-based learning in Performing Data. |
| **A3** Assess and give feedback for learning | Self-checking exercises with [worked answers](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/week4/exercises/ANSWERS.md). End-of-session performances and table reads as formative feedback. Unit portfolio assessment described in the [Week 1 overview](Data-Science-In-Creative-Industries-Week-1/README.md#assessment-link). |
| **A4** Support and guide learners | Setup guides for each platform, [troubleshooting notes](Performing-Data-Week-5/performing-data-week-5-lab/README.md#troubleshooting), hints in every exercise, and a content warning on sensitive material. |
| **A5** Enhance practice through own continuing professional development | Materials revised over several years: the Week 4 deck was restructured and given new diagrams, and Week 1 uses 2024 industry research (RecSys industry track). Teaching is informed by creative-technology research and by developing the open-source [Dorothy](https://github.com/Louismac/dorothy) library. |

### Core Knowledge

| Dimension | Evidence |
|---|---|
| **K1** How learners learn | Predict-before-run exercises. One concept per file. Errors treated as learning. Abstract ideas made concrete through sound and image. |
| **K2** Approaches appropriate for subject and level | Students new to programming learn it through a familiar creative medium (audio). MSc students get open, research-style briefs. |
| **K3** Critical evaluation as a basis for effective practice | Seminar and discussion prompts in every session. Corrections and caveats noted in the speaker notes of the Week 4 deck. |
| **K4** Appropriate use of digital technologies | Local, free models. Jupyter notebooks with saved outputs. Live-coding with Dorothy. Animated diagrams. |
| **K5** Quality assurance and enhancement | Class outcomes mapped to validated unit outcomes. Consistent documentation for each session. |

### Professional Values

| Dimension | Evidence |
|---|---|
| **V1** Respect individual learners and diverse groups | Diverse histories of practice, a content warning, and attention to whose data is missing or misrepresented. |
| **V2** Promote engagement and equity of opportunity | Laptop-friendly tools, no paid accounts, step-up options for stronger hardware, and an offline route for slower machines. |
| **V3** Use scholarship and evidence-informed approaches | Readings in the [delivery contexts](Coding-for-Digital-Media-Week-4/delivery-context.md#additional-materials). Lectures cite current research: NIME papers in Week 2, and ACM RecSys 2024 industry papers in Week 1. |
| **V4** Respond to the wider context of higher education | Engagement with generative AI in creative work, copyright and sampling law, decolonising the curriculum, and employability (industry case studies in Week 1). |
| **V5** Collaborate with others to enhance practice | Working with external partners and colleagues: UCL’s *Legacies of British Slavery* team, who opened their dataset for teaching, and Lucy Panesar’s decolonising lecture, which the notebook builds on. |
