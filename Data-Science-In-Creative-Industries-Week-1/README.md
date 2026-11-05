# Data Science in Creative Industries, Week 1: Creative Industry Data × Raw Data is an Oxymoron

← [All teaching samples](../README.md) · [Teaching approach](../TEACHING-APPROACH.md)

> **In one sentence:** the opening session of the unit asks what data actually is, where it comes from and who it leaves out. Students first explore a real historical dataset with pandas, then imagine the datasets that don’t exist, and finally make their own data by hand.

| | |
|---|---|
| **Unit** | Data Science in Creative Industries |
| **Session length** | 4 hours: lecture, notebook lecture, two group tasks |
| **Prior knowledge** | Basic Python. pandas is introduced here |
| **Tools** | Python, pandas, Jupyter; paper, pens and found materials |
| **Student output** | A dataset proposal, and a hand-made or performed data artefact |
| **Full plan** | [delivery-context.md](delivery-context.md) |

**Contents:** [Learning outcomes](#learning-outcomes) · [Session plan](#session-plan) · [Materials](#materials-in-this-folder) · [Lecture slides](#lecture-slides) · [Notebook](#notebook-the-legacies-of-british-slavery-dataset) · [Group tasks](#group-tasks) · [Assessment link](#assessment-link) · [Why it works](#why-this-session-works) · [Running the notebook](#running-the-notebook)

> ⚠️ **Content note:** the notebook deals with colonial history, the transatlantic slave trade and racial inequality. It opens with a content warning.

---

## Learning outcomes

By the end of the session, students will be able to:

| # | Class learning outcome | Unit outcome | Practised in |
|---|---|---|---|
| 1 | Distinguish quantitative (discrete, continuous) from qualitative (nominal, ordinal) data, and structured from unstructured data, using creative industries examples | LO1 | Lecture; notebook “Data Types” section |
| 2 | Load and explore a real tabular dataset with pandas: inspect types, summarise, select, count, sort, filter and find missing values | LO2 | [Notebook](legacies-of-british-slavery-notebook.ipynb) and its tasks |
| 3 | Critically discuss how datasets are made, whose experiences they record or erase, and why some datasets are missing altogether | LO3 | Notebook introduction; [Missing Datasets task](ds-for-ci-week-1-lab/lab-brief.md#missing-datasets-task) |
| 4 | Represent self-collected data through a hand-made or performed artefact, making deliberate choices about what to highlight | LO1 | [Dear Data task](ds-for-ci-week-1-lab/lab-brief.md#dear-data-task) |

The unit learning outcomes (LO1–LO3) are listed in full in [delivery-context.md](delivery-context.md#learning-outcomes-of-unit).

---

## Session plan

| Block | Activity | Materials |
|---|---|---|
| Lecture | What is data science? What are the creative industries, and why do they use data? What’s in a dataset? | [Slides (Keynote)](dsforci_week1.key), outlined [below](#lecture-slides) |
| Notebook lecture | Exploring the *Legacies of British Slavery* dataset with pandas | [Notebook](legacies-of-british-slavery-notebook.ipynb) |
| Break | | |
| Group task 1 | **Missing Datasets:** propose a dataset that should exist but doesn’t, then discuss | [Brief](ds-for-ci-week-1-lab/lab-brief.md#missing-datasets-task) |
| Group task 2 | **Dear Data:** collect a small dataset and turn it into a drawing, object or performance | [Brief](ds-for-ci-week-1-lab/lab-brief.md#dear-data-task) |

Exact timings are in [delivery-context.md](delivery-context.md#lesson-schedule-4-hours).

---

## Materials in this folder

| File | What it is |
|---|---|
| [`dsforci_week1.key`](dsforci_week1.key) | Lecture slides (Apple Keynote, 41 slides). Outlined [below](#lecture-slides) for readers without Keynote |
| [`legacies-of-british-slavery-notebook.ipynb`](legacies-of-british-slavery-notebook.ipynb) | Notebook lecture with saved outputs, so it reads in full on GitHub |
| [`ds-for-ci-week-1-lab/lab-brief.md`](ds-for-ci-week-1-lab/lab-brief.md) | Briefs for the Missing Datasets and Dear Data tasks |
| [`delivery-context.md`](delivery-context.md) | Unit description, learning outcomes, schedule |

---

## Lecture slides

The [Keynote deck](dsforci_week1.key) moves from the purpose of data science to a critical view of where data comes from:

1. **Welcome and the unit:** times, the teaching team, and the assessment (a portfolio of three small projects)
2. **What is data science?** “Improving decision making through the analysis of data”, with a commitment that runs through the whole unit: *all data is of people*. Exploitation of minorities, undervaluing of creatives and erasure of personal experience are real outcomes.
3. **A repeatable method used every week:**
   - What is the question I can answer?
   - What data will I need?
   - What stats or modelling do I do?
   - How do I interpret the results?
   - Can I express a confidence?
4. **What are the creative industries?** Definitions from Terras et al. (2024) and the United Nations (2008)
5. **Why do they use data?** Real industry questions:
   - campaign performance
   - audience
   - release timing
   - genre tagging
   - recommendation
   - “Is what we’re doing legal?” and “Is it ethical?”
6. **Industry research:** recommendation and search papers from Spotify, Netflix and video platforms in the ACM RecSys 2024 industry track
7. **Who is affected:** creators, platforms and audiences, and what data means for each
8. **What’s in a dataset?** “Data” is plural. Loukissas: *all data are local*. Drucker: *capta* rather than *data*.
9. **Data types:** discrete, continuous, nominal and ordinal, each illustrated with a creative industries example
10. **Structured and unstructured data**, and the kinds of creative industry data (behaviour, metadata, media, performance metrics)
11. **“Raw data is an oxymoron”** (Gitelman and Bowker): all data is cooked, collected for a reason and carrying both prejudice and intent

---

## Notebook: the Legacies of British Slavery dataset

[`legacies-of-british-slavery-notebook.ipynb`](legacies-of-british-slavery-notebook.ipynb) uses the *Physical* section of UCL’s [Legacies of British Slavery](https://www.ucl.ac.uk/lbs/) database. This section records buildings and places funded by the profits of slavery.

The notebook teaches core pandas through real questions about this history:

| Section | pandas skill | Question asked of the data |
|---|---|---|
| Loading | `pd.read_csv(..., delimiter="\t")` | What is in this dataset (626 rows, 16 columns)? |
| Data types | `df.dtypes` | Which columns are nominal and which continuous? What can we do with each? |
| Summary data | `df.describe(include="all")` | What does a quick overview reveal? |
| Selecting columns | `df["Sex"]` | What is the gender balance of recorded owners? |
| Counting | `value_counts()` | Which families, counties and titles appear most? |
| Sorting | `sort_values(...)` | When was the last property built, long after abolition in 1833? |
| Filtering | `df[df["Ownership"] == ...]` | What do the Church of England and the National Trust own today? |
| Missing values | `count()`, `isna()`, `notna()` | What is missing, and *why*? |

The technical work is framed throughout by its purpose: supporting decolonial edits to Wikipedia pages about these places. The framing also names what the dataset misses, the lives of enslaved people, and points to resources that centre them, such as the [Switching the Lens](https://www.cityoflondon.gov.uk/things-to-do/history-and-heritage/london-metropolitan-archives/about-lma/switching-the-lens-project) project.

---

## Group tasks

Both tasks are in [`lab-brief.md`](ds-for-ci-week-1-lab/lab-brief.md).

**Missing Datasets** (groups of 4–5). Inspired by Mimi Onuoha’s [Library of Missing Datasets](https://github.com/MimiOnuoha/missing-datasets). Groups propose a dataset that *should* exist and ask why it doesn’t: whether it is hard to collect, held across fragmented platforms, shaped by historical bias, legally risky, or underreported. This turns the notebook’s critique into students’ own enquiry.

**Dear Data** (groups of 2–3). After Giorgia Lupi and Stefanie Posavec’s *Dear Data*, groups choose a theme, collect a small dataset in the room, and represent it by hand as a drawing, collage, sculpture, piece of music or movement sequence. The brief is time-boxed (brainstorm → collect → conceptualise → make) and includes ten example prompts for groups who get stuck. It ends with a gallery of everyone’s results.

---

## Assessment link

The unit is assessed by a portfolio of three small projects, submitted in Week 10. Each one is an independent investigation using a technique from the term. This session lays the foundations for all three: the repeatable question-to-confidence method, pandas exploration, and the habit of asking where data came from.

---

## Why this session works

- **It starts with values, not tools.** Students meet the ethics of data in the first hour of the unit, so it frames everything after it rather than being bolted on in a final week.
- **A real dataset with real stakes.** pandas skills are learnt on data that matters, and every technical step (missing values, inconsistent formats) is also a historical and ethical question.
- **Theory made tangible.** “Raw data is an oxymoron” is an abstract claim. Collecting and drawing their own data shows students how many choices go into a dataset.
- **Industry-relevant.** Real questions from streaming and media companies, and current industry research, show where these skills are used.
- **Varied modes of participation.** Lecture, code, discussion and making all happen in one session, so different learners have a way in.

---

## Running the notebook

```bash
pip install pandas jupyter
jupyter notebook legacies-of-british-slavery-notebook.ipynb
```

The notebook expects the data file `lbs.tsv` in the same folder. The dataset was shared for teaching by the UCL Centre for the Study of the Legacies of British Slavery, so it is **not redistributed** here. All outputs are saved in the notebook, so it can be read in full on GitHub without running it.
