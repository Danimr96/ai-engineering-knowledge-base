---
id: "lesson:05/24"
type: lesson
ref: 05/24
phase: 5
num: 24
title: Coreference Resolution
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 1
concepts: 7
prereqs: 2
community: 76
aliases:
  - 05/24
  - 05-24
tags:
  - phase/05
  - type/learn
  - community/76
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/24-coreference-resolution/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/24-coreference-resolution"
---

# 05/24 Coreference Resolution

> "She called him. He did not answer. The doctor was at lunch." Three references to two people and nobody is named. Coreference resolution figures out who is who.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/24-coreference-resolution/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/24-coreference-resolution) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/24-coreference-resolution) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/76 Provenance|76 Provenance]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 06 (NER), Phase 5 · 07 (POS & Parsing)`

- [[Lessons/05-06 Named Entity Recognition|05/06 Named Entity Recognition]] — NER
- [[Lessons/05-07 POS Tagging and Syntactic Parsing|05/07 POS Tagging and Syntactic Parsing]] — POS & Parsing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]

## Builds on this

- [[Lessons/05-25 Entity Linking & Disambiguation|05/25 Entity Linking & Disambiguation]]

## Concepts taught

- Mention `lesson term` — A span of text that refers to an entity (name, pronoun, noun phrase).
- Antecedent `lesson term` — The earlier mention a later one corefers with.
- Cluster `lesson term` — Set of mentions that all refer to the same real-world entity.
- Anaphora `lesson term` — Later mention refers to earlier ("he" → "John").
- Cataphora `lesson term` — Earlier mention refers to later ("When he arrived, John...").
- Bridging `lesson term` — "I bought a car. The wheels were bad." (wheels of THAT car.)
- CoNLL F1 `lesson term` — Average of MUC, B³, CEAF-φ4 F1 scores.

## Ships

- [[Artifacts/05-24 coref-picker|coref-picker]] `skill` — Pick a coreference approach, evaluation plan, and integration strategy.

## Further reading

- Pradhan et al. (2012). CoNLL-2012 Shared Task ([link](https://aclanthology.org/W12-4501/)) — the benchmark.
- Lee et al. (2017). End-to-end Neural Coreference Resolution ([link](https://arxiv.org/abs/1707.07045)) — span-based end-to-end.
- Joshi et al. (2020). SpanBERT ([link](https://arxiv.org/abs/1907.10529)) — pretraining that improves coref.
- Hobbs (1978). Resolving Pronoun References ([link](https://www.sciencedirect.com/science/article/pii/0024384178900064)) — the rule-based classic.
- Jurafsky & Martin, SLP3 Ch. 26 — Coreference Resolution and Entity Linking ([link](https://web.stanford.edu/~jurafsky/slp3/26.pdf)) — canonical textbook chapter.


%% ── my notes ── %%
