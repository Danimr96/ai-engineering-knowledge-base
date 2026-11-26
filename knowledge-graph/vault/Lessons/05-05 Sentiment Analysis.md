---
id: "lesson:05/05"
type: lesson
ref: 05/05
phase: 5
num: 5
title: Sentiment Analysis
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 2
community: 75
aliases:
  - 05/05
  - 05-05
tags:
  - phase/05
  - type/build
  - community/75
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/05-sentiment-analysis/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/05-sentiment-analysis"
---

# 05/05 Sentiment Analysis

> The canonical NLP task. Most of what you need to know about classical text classification shows up here.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/05-sentiment-analysis/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/05-sentiment-analysis) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/05-sentiment-analysis) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/75 L2 regularization · PRM · Reward Model|75 L2 regularization · PRM · Reward Model]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 2 · 14 (Naive Bayes)`

- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]] — Naive Bayes
- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Builds on this

- [[Lessons/05-21 Natural Language Inference — Textual Entailment|05/21 Natural Language Inference — Textual Entailment]]
- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]]

## Concepts taught

- Polarity `lesson term` — Binary label; sometimes extended to neutral or fine-grained (5-star).
- Aspect-based sentiment `lesson term` — Attribute sentiment to specific entities or attributes mentioned in text.
- Negation scoping `lesson term` — Prefix tokens after "not" with NOT until punctuation.
- [[Concepts/Laplace smoothing|Laplace smoothing]] `lesson term` — Prevents zero-probability features in Naive Bayes.
- [[Concepts/L2 regularization|L2 regularization]] `lesson term` — Adds lambda sum(w^2) to loss. Essential for sparse text features.

## Ships

- [[Artifacts/05-05 sentiment-baseline|sentiment-baseline]] `prompt` — Design a sentiment analysis baseline for a new dataset.

## Further reading

- Wang and Manning (2012). Baselines and Bigrams: Simple, Good Sentiment and Topic Classification ([link](https://aclanthology.org/P12-2018/)) — the paper that showed bigrams + Naive Bayes is hard to beat on short text.
- Pang and Lee (2008). Opinion Mining and Sentiment Analysis ([link](https://www.cs.cornell.edu/home/llee/opinion-mining-sentiment-analysis-survey.html)) — the foundational survey. Long, but the first four sections cover everything classical.
- [[Resources/scikit-learn — feature extraction from text|scikit-learn — feature extraction from text]] ([link](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)) — reference for `CountVectorizer`, `TfidfVectorizer`, and every knob you'll tune. ·  also cited by 1 other lesson


%% ── my notes ── %%
