---
id: "lesson:05/16"
type: lesson
ref: 05/16
phase: 5
num: 16
title: "Text Generation Before Transformers — N-gram Language Models"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
aliases:
  - 05/16
  - 05-16
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer"
---

# 05/16 Text Generation Before Transformers — N-gram Language Models

> If a word is surprising, the model is bad. Perplexity makes surprise a number. Smoothing keeps it finite.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 01 (Text Processing), Phase 2 · 14 (Naive Bayes)`

- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]] — Naive Bayes
- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]] — Text Processing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Concepts taught

- N-gram `lesson term` — Sequence of n consecutive tokens.
- Smoothing `lesson term` — Reallocating probability mass so unseen events get non-zero probability.
- [[Concepts/Perplexity|Perplexity]] `glossary` — exp(-average log-prob) on held-out data. Lower is better.
- Backoff `lesson term` — If trigram count is zero, use bigram. Katz backoff formalizes this.
- Kneser-Ney `lesson term` — Absolute discounting + continuation probability for the lower-order model.
- Continuation probability `lesson term` — P(w) weighted by number of contexts w appears in, not by raw count.
- Entropy of text `lesson term` — Average bits needed to encode the next symbol given the context. Shannon's 1951 estimate for printed English with up to 100 letters of context: 0.6-1.3 bits/letter, measured before any model existed.

## Ships

- [[Artifacts/05-16 lm-baseline|lm-baseline]] `prompt` — Build a reproducible n-gram language model baseline before training a neural LM.

## Further reading

- Chen and Goodman (1998). An Empirical Study of Smoothing Techniques for Language Modeling ([link](https://dash.harvard.edu/handle/1/25104739)) — the paper that settled Kneser-Ney as the best n-gram smoother.
- Kneser and Ney (1995). Improved Backing-off for M-gram Language Modeling ([link](https://ieeexplore.ieee.org/document/479394)) — the original KN paper.
- KenLM ([link](https://kheafield.com/code/kenlm/)) — fast production n-gram LM, still used in 2026 for latency-sensitive applications.
- Shannon (1951). Prediction and Entropy of Printed English ([link](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf)) — the guessing-game experiment that defined the target every language model still optimizes.
- Jurafsky and Martin — Speech and Language Processing, Chapter 3 (2026 draft) ([link](https://web.stanford.edu/~jurafsky/slp3/3.pdf)) — the canonical treatment of n-gram LMs and smoothing.


%% ── my notes ── %%
