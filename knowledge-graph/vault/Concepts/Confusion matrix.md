---
id: "concept:confusion-matrix"
type: concept
name: Confusion matrix
canonical: false
taught_in: 3
community: 4
tags:
  - concept/lesson-term
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/03-logistic-regression/docs/en.md
---

# Confusion matrix

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

> *What people say:* "The error breakdown"

**What it actually means:** A table showing TP, TN, FP, FN counts for each class pair

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — C x C table where entry (i, j) counts images of true class i predicted as j; diagonal is right, off-diagonal tells you what to fix
- [[Lessons/19-83 Capstone 83 — Prompt Injection Detector|19/83 Capstone 83 — Prompt Injection Detector]] — the per-category breakdown of TP, FP, TN, FN used to compute precision and recall


%% ── my notes ── %%
