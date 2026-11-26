---
id: "lesson:05/07"
type: lesson
ref: 05/07
phase: 5
num: 7
title: POS Tagging and Syntactic Parsing
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 2
aliases:
  - 05/07
  - 05-07
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing"
---

# 05/07 POS Tagging and Syntactic Parsing

> Grammar was unfashionable for a while. Then every LLM pipeline needed to validate structured extraction, and it came back.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/07-pos-tagging-parsing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 01 (Text Processing), Phase 2 · 14 (Naive Bayes)`

- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]] — Naive Bayes
- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]] — Text Processing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Builds on this

- [[Lessons/05-24 Coreference Resolution|05/24 Coreference Resolution]]

## Concepts taught

- [[Concepts/POS tag|POS tag]] `lesson term` — Grammatical category. PTB has 36; UD has 17.
- Penn Treebank `lesson term` — English-specific. Fine-grained verb tenses and noun number.
- Universal Dependencies `lesson term` — Coarser than PTB; language-neutral; defaults for cross-lingual work.
- Dependency parse `lesson term` — Each word has one head, each edge has a grammatical relation.
- Viterbi `lesson term` — Finds the highest-probability tag sequence given emissions and transitions.

## Ships

- [[Artifacts/05-07 grammar-pipeline|grammar-pipeline]] `skill` — Design a classical POS + dependency pipeline for a downstream NLP task.

## Further reading

- Chen and Manning (2014). A Fast and Accurate Dependency Parser using Neural Networks ([link](https://nlp.stanford.edu/pubs/emnlp2014-depparser.pdf)) — the paper that brought neural parsers into the mainstream.
- [[Resources/spaCy 101 — linguistic features|spaCy 101 — linguistic features]] ([link](https://spacy.io/usage/linguistic-features)) — practical reference for every attribute exposed on `Token`. ·  also cited by 2 other lessons
- Universal Dependencies project ([link](https://universaldependencies.org/)) — the cross-lingual tagset and treebank collection used by every multilingual parser.
- Jurafsky and Martin — Speech and Language Processing, chapters 8 and 18 ([link](https://web.stanford.edu/~jurafsky/slp3/)) — the canonical textbook treatment of POS and parsing.


%% ── my notes ── %%
