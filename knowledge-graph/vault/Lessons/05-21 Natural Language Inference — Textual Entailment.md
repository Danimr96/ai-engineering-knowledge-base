---
id: "lesson:05/21"
type: lesson
ref: 05/21
phase: 5
num: 21
title: "Natural Language Inference — Textual Entailment"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
aliases:
  - 05/21
  - 05-21
tags:
  - phase/05
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment"
---

# 05/21 Natural Language Inference — Textual Entailment

> "t entails h" means a human reading t would conclude h is true. NLI is the task of predicting entailment / contradiction / neutral. Boring on the surface, load-bearing in production.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/21-nli-textual-entailment/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 05 (Sentiment Analysis), Phase 5 · 13 (Question Answering)`

- [[Lessons/05-05 Sentiment Analysis|05/05 Sentiment Analysis]] — Sentiment Analysis
- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] — Question Answering

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Concepts taught

- NLI `lesson term` — 3-way classification of premise-hypothesis relationship.
- RTE `lesson term` — Older name for NLI; same task.
- Entailment `lesson term` — A typical reader would conclude h is true given t.
- Contradiction `lesson term` — A typical reader would conclude h is false given t.
- Neutral `lesson term` — No inference from t to h either way.
- Zero-shot classification `lesson term` — Verbalize labels as hypotheses, pick max entailment.
- [[Concepts/Faithfulness|Faithfulness]] `lesson term` — NLI over (retrieved context, generated answer).

## Ships

- [[Artifacts/05-21 nli-picker|nli-picker]] `skill` — Pick an NLI model, label template, and evaluation setup for a classification / faithfulness / zero-shot task.

## Further reading

- Bowman et al. (2015). A large annotated corpus for learning natural language inference ([link](https://arxiv.org/abs/1508.05326)) — SNLI.
- Williams, Nangia, Bowman (2017). A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference ([link](https://arxiv.org/abs/1704.05426)) — MultiNLI.
- Yin, Hay, Roth (2019). Benchmarking Zero-shot Text Classification ([link](https://arxiv.org/abs/1909.00161)) — NLI-as-classifier.
- Nie et al. (2019). Adversarial NLI ([link](https://arxiv.org/abs/1910.14599)) — the ANLI benchmark.
- He et al. (2021). DeBERTa: Decoding-enhanced BERT with Disentangled Attention ([link](https://arxiv.org/abs/2006.03654)) — the 2026 NLI workhorse.


%% ── my notes ── %%
