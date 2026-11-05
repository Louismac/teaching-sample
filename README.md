# Teaching Samples: Louis McCallum

Four complete teaching sessions from creative computing units taught at the **UAL Creative Computing Institute**. They range from introductory programming for digital media to MSc-level machine learning for live performance.

Each session is a full four-hour class, and for each one the repo has everything needed to teach it:

- the delivery plan, with learning outcomes and a schedule
- the lecture slides
- runnable code
- a hands-on lab
- a discussion or critical activity
- further reading

> **Short on time?** Start with the [Coding for Digital Media Week 4 overview](Coding-for-Digital-Media-Week-4/README.md). It is the most complete example of the approach, from slides and animations through scaffolded exercises with answers to a seminar and a creative brief. Then read [Teaching approach](TEACHING-APPROACH.md) for how the samples map to the Advance HE Professional Standards Framework.

---

## The samples at a glance

| Session | Unit and level | Topic | Highlights | Start here |
|---|---|---|---|---|
| **Coding for Digital Media, Week 4: Cut and Paste Audio** | Coding for Digital Media (introductory programming) | Audio as data: sampling, slicing arrays, editing and collage | 63-slide lecture with animated diagrams · 10 scaffolded exercises with answers · seminar on the ethics and law of sampling · sound collage brief | [Overview](Coding-for-Digital-Media-Week-4/README.md) |
| **Data Science in Creative Industries, Week 1: Raw Data is an Oxymoron** | Data Science in Creative Industries | What data is, where it comes from and who it leaves out | Notebook analysing the *Legacies of British Slavery* dataset · Missing Datasets task · *Dear Data* physical data-art task | [Overview](Data-Science-In-Creative-Industries-Week-1/README.md) |
| **Performing Data, Week 2: Generative Text in Performance** | Performing Data · MSc Applied Machine Learning for Creatives (Term 3, 20 credits) | From Strachey’s love letters to local LLMs as performance scores | History of generative text · local language models on student laptops · constrained-writing briefs · live “table read” of student work | [Overview](Performing-Data-Week-2/README.md) |
| **Performing Data, Week 5: Generative Visuals in Performance** | Performing Data · MSc Applied Machine Learning for Creatives (Term 3, 20 credits) | Real-time Stable Diffusion as a playable instrument | Seven-step lab building an audio- and webcam-reactive img2img instrument · tuning notes on the speed and quality trade-off · group performances | [Overview](Performing-Data-Week-5/README.md) |

---

## What every sample contains

Each folder follows the same structure, so a reviewer can find the same thing in the same place every time:

| Element | Where to find it | What it shows |
|---|---|---|
| **Overview** | `README.md` in each folder | The session at a glance: learning outcomes, schedule, a guide to the materials, and why it is designed the way it is |
| **Delivery context** | `delivery-context.md` | The unit description, unit learning outcomes, class learning outcomes, timed lesson plan and further reading |
| **Lecture** | Slides (`.pdf` or `.key`) and, where used, a notebook | The taught content |
| **Lab** | The `*-lab/` folder | Runnable code, briefs and troubleshooting notes for hands-on work |
| **Critical activity** | Seminar prompts, discussion tasks, screenings | Space to question the technology as well as use it |

---

## Why this is strong teaching material

The samples share a set of design principles. These are explained in full, with evidence, in [Teaching approach](TEACHING-APPROACH.md).

1. **Constructive alignment.** Every class learning outcome is mapped to the unit learning outcomes, and each one is practised in the lab and discussed in the critical activity. See the outcome tables in each overview.
2. **Technique and critique together.** Every session pairs a technical skill with a question about power, ethics or culture:
   - [the ethics and law of sampling](Coding-for-Digital-Media-Week-4/Seminar-prompts.md)
   - [datasets that don’t exist](Data-Science-In-Creative-Industries-Week-1/ds-for-ci-week-1-lab/lab-brief.md)
   - [colonial legacies in data](Data-Science-In-Creative-Industries-Week-1/legacies-of-british-slavery-notebook.ipynb)
   - [authorship with AI](Performing-Data-Week-2/README.md#critical-and-ethical-framing)
3. **Diverse histories of practice.** Technical ideas are grounded in the artists who pioneered them, including Daphne Oram, Delia Derbyshire, hip-hop producers, Christopher Strachey, Kate Compton, Allison Parrish, Mimi Onuoha and Giorgia Lupi with Stefanie Posavec.
4. **Learning by making.** Each session ends in something students make, perform or share: a sound collage, a data drawing, a performed script or a live visual performance.
5. **Scaffolded, low-barrier code.** Examples are short and build one idea at a time. The [Week 4 exercises](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/week4/exercises/) use a *Predict → Run → Task → Hint → Check* format with [worked answers](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/week4/exercises/ANSWERS.md).
6. **Equitable access to tools.** Labs run on students’ own laptops. There are separate paths for Apple Silicon, Windows and NVIDIA machines, and small local models, so nobody needs a paid account or a powerful GPU. See [running a local LLM](Performing-Data-Week-2/performing-data-week-2-lab/running-local-llm.md) and the [Week 5 setup](Performing-Data-Week-5/performing-data-week-5-lab/README.md#before-you-start).
7. **Clear visual explanation.** Diagrams and short animations make abstract ideas visible: sampling, sample rate, slicing and mixing. See the [Week 4 animations](Coding-for-Digital-Media-Week-4/README.md#animations).

---

## Repository structure

```
teaching-samples/
├── README.md                          ← you are here
├── TEACHING-APPROACH.md               ← design principles and PSF 2023 mapping
│
├── Coding-for-Digital-Media-Week-4/   Audio as data: cut, paste and collage
│   ├── README.md                      overview and guide
│   ├── delivery-context.md            unit, outcomes, schedule, reading
│   ├── coding4dm-week4-combined-lecture.pdf   63-slide lecture (slides + code lecture)
│   ├── coding4dm-week4-slides.pdf     original 27-slide deck
│   ├── animations/                    6 MP4 animations used in the lecture
│   ├── Seminar-prompts.md             reading discussion on sampling
│   └── coding-for-digital-media-week-4-lab/
│       ├── README.md                  how to run, file guide
│       └── week4/                     example sketches, audio, exercises and answers
│
├── Data-Science-In-Creative-Industries-Week-1/   Raw data is an oxymoron
│   ├── README.md
│   ├── delivery-context.md
│   ├── dsforci_week1.key              lecture slides (Keynote)
│   ├── legacies-of-british-slavery-notebook.ipynb   notebook lecture
│   └── ds-for-ci-week-1-lab/lab-brief.md   Missing Datasets and Dear Data tasks
│
├── Performing-Data-Week-2/            Generative text in performance
│   ├── README.md
│   ├── delivery-context.md
│   ├── performing-data-week-2-slides.pdf
│   └── performing-data-week-2-lab/
│       ├── README.md                  file guide
│       ├── brief.md                   performance briefs
│       ├── running-local-llm.md       setup for Mac, Windows and Intel
│       └── *.py                       local LLM scripts
│
└── Performing-Data-Week-5/            Generative visuals in performance
    ├── README.md
    ├── delivery-context.md
    └── performing-data-week-5-lab/
        ├── README.md                  the full step-by-step lab
        ├── sd_turbo_tuning_notes.md   speed and quality reference
        ├── diffusion_utils.py
        └── week5-*.py                 one sketch per activity
```

---

## Running the code

All code is Python 3. Most sketches use [Dorothy](https://github.com/Louismac/dorothy) (`pip install dorothy-cci`), an open-source creative-coding library for interactive audio and audio-reactive drawing, written by the author for teaching. Each sample lists its own dependencies:

| Sample | Install | Instructions |
|---|---|---|
| Coding for Digital Media, Week 4 | `pip install dorothy-cci librosa numpy` | [Lab README](Coding-for-Digital-Media-Week-4/coding-for-digital-media-week-4-lab/README.md) |
| Data Science in Creative Industries, Week 1 | `pip install pandas jupyter` | [Overview](Data-Science-In-Creative-Industries-Week-1/README.md#running-the-notebook) |
| Performing Data, Week 2 | `pip install mlx-lm` (Apple Silicon) or `pip install ollama` | [Running a local LLM](Performing-Data-Week-2/performing-data-week-2-lab/running-local-llm.md) |
| Performing Data, Week 5 | `pip install dorothy-cci diffusers transformers accelerate torch opencv-python` | [Lab README](Performing-Data-Week-5/performing-data-week-5-lab/README.md#before-you-start) |

---

## Credits and third-party material

- **Legacies of British Slavery dataset:** UCL Centre for the Study of the Legacies of British Slavery, shared for teaching by Keith McClelland. The dataset itself is not redistributed here. The notebook keeps its outputs so it can be read on GitHub.
- **Images, artworks and video stills** in the slides belong to their creators and are used for teaching, with sources given on the slides.
- **Audio loops** in the Week 4 and Week 5 labs are teaching examples.
