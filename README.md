# Kenya Clinical Reasoning Challenge

This repository contains a basic solution for the [Kenya Clinical Reasoning Challenge](https://zindi.africa/competitions/kenya-clinical-reasoning-challenge) hosted on Zindi.

## About the Challenge

Can a machine think like a real clinician in rural Kenya?

In this challenge, you're given 400 real-life clinical cases written as short prompts. These come from Kenyan nurses working in different health facilities and cover situations like childbirth, emergencies, and more. Your job is to predict how a trained clinician would respond to each case.

Each prompt includes details like the patient's condition, the nurse's background, and the facility type. The goal is to match expert-level reasoning, even in low-resource environments where decisions have to be fast and accurate.

The dataset is small—400 training and 100 test samples—because it's based on real, expert-reviewed medical data. The cases were even evaluated by top AI models like GPT-4, LLAMA, and GEMINI. So yeah, it’s a tough but very meaningful problem.

## My Progress So Far

This code is a basic version using sentence embeddings and FAISS search. It currently reaches a **ROUGE score of 0.35**, up from the sample baseline of **0.25**. The top participant is sitting at **0.44**, and yes, I’m hoping to catch up (or pass) soon.

## What's Inside

- Code to load and process the data
- SentenceTransformer for prompt embeddings
- FAISS index to find the best-matching clinician
- CSV submission file generator

## How to Use

1. Download the dataset from the competition page.
2. Update the script with your local file paths.
3. Run the script to generate `submission.csv`.
4. Submit to Zindi and check your score.

## Setup

To run the code, make sure you have the following Python packages installed:

```bash
pip install -U sentence-transformers faiss-cpu pandas numpy
```

## Note

This isn't my best code — that version is staying private for now.  
What you're seeing here is a basic, working version to help others get started.

---

## Dataset Files

| File Name                            | Description                                                                                      | Size     |
|-------------------------------------|--------------------------------------------------------------------------------------------------|----------|
| `train_raw.csv`                     | Raw training data with full details.                                                             | 5 MB     |
| `test_raw.csv`                      | Raw test data, similar format as `train_raw.csv` but without target labels.                      | 64.4 KB  |
| `train.csv`                         | Processed training set used to train your model. Contains the target (`Clinician`) column.       | 4.7 MB   |
| `test.csv`                          | Processed test set where the model will make predictions. No target column.                      | 62.8 KB  |
| `SampleSubmission.csv`             | Sample of what the final submission format should look like. IDs must match test file.           | 1.5 KB   |
| `Kenya medical vignettes data dictionary.docx` | Description of all variables used in the data files.                                      | 15.5 KB  |

---

## What’s Inside the Files (So You Don’t Have to Open Them One by One)

I’m saving you the trouble of clicking through every CSV — here’s what each file actually contains.

| File Name           | Columns (aka the stuff inside)                                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `test_raw.csv`      | `['Master_Index', 'County', 'Health level', 'Years of Experience', 'Prompt', 'Nursing Competency', 'Clinical Panel']`                                           |
| `train_raw.csv`     | `['Master_Index', 'County', 'Health level', 'Years of Experience', 'Prompt', 'Nursing Competency', 'Clinical Panel', 'Clinician', 'GPT4.0', 'LLAMA', 'GEMINI', 'DDX SNOMED']` |
| `test.csv`          | `['Master_Index', 'County', 'Health level', 'Years of Experience', 'Prompt', 'Nursing Competency', 'Clinical Panel']`                                           |
| `train.csv`         | `Same as train_raw.csv but slightly cleaned. Still has all the cool stuff like GPT4 and Clinician labels.`                                                     |
| `SampleSubmission.csv` | `['Master_Index', 'Clinician']` — this is what your output should look like when you submit. Keep the IDs right, or the leaderboard will ignore you.         |

So yeah — you’re welcome. I already peeked inside the files so you don’t have to scroll through 400 rows just to figure out what’s what.


---

Good luck to everyone competing. And to the top scorer — you're doing great, but don’t get too comfortable.

---

## Final Note

If this repo looks a bit quiet or under-polished, it’s because I’ve got a lot going on right now — not just in code, but in life.

I'm currently trying to win this hackathon so I can earn some money — enough to pay for my **SAT**, **IELTS**, and application forms for different universities.  
This isn't just a side project; it's part of the bigger plan.

At the same time, I’m also:
- Studying for **Improvement Exams**
- Keeping **JEE** as a backup (because Plan B needs love too)
- Building projects and trying to stay consistent in between it all

So if I’m not super active on GitHub or this code looks a bit raw — just know the grind is real behind the scenes.

And hey, this is India —  
**big dreams are just myths unless you’re ready to grind for them yourself.**

### Certificate

Here’s my official Zindi participation certificate:  
[View Certificate](https://zindi.africa/users/mrfanyntom/competitions/certificate)

---
