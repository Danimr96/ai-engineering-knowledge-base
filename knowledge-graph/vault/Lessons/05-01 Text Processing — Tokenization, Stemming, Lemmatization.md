---
id: "lesson:05/01"
type: lesson
ref: 05/01
phase: 5
num: 1
title: "Text Processing — Tokenization, Stemming, Lemmatization"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 1
aliases:
  - 05/01
  - 05-01
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/01-text-processing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/01-text-processing"
---

# 05/01 Text Processing — Tokenization, Stemming, Lemmatization

> Language is continuous. Models are discrete. Preprocessing is the bridge.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/01-text-processing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/01-text-processing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/01-text-processing) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 2 · 14 (Naive Bayes)`

- [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]] — Naive Bayes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Builds on this

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]
- [[Lessons/05-07 POS Tagging and Syntactic Parsing|05/07 POS Tagging and Syntactic Parsing]]
- [[Lessons/05-16 Text Generation Before Transformers — N-gram Language Models|05/16 Text Generation Before Transformers — N-gram Language Models]]
- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]]

## Concepts taught

- [[Concepts/Token|Token]] `glossary` — Whatever unit the model consumes. Can be word, subword, character, or byte.
- [[Concepts/Stem|Stem]] `lesson term` — Result of rule-based suffix stripping. Not always a real word.
- Lemma `lesson term` — The form you'd look up. Requires grammatical context to compute correctly.
- [[Concepts/POS tag|POS tag]] `lesson term` — Category like NOUN, VERB, ADJ. Needed to lemmatize accurately.
- Morphology `lesson term` — How a word changes form based on tense, number, case. Lemmatization depends on it.

## Ships

- [[Artifacts/05-01 preprocessing-advisor|preprocessing-advisor]] `prompt` — Recommends a tokenization, stemming, and lemmatization setup for an NLP task.

## Further reading

- NLTK book, chapter 3 ([link](https://www.nltk.org/book/ch03.html)) — tokenization edge cases you haven't thought of yet.
- [[Resources/spaCy 101 — linguistic features|spaCy 101 — linguistic features]] ([link](https://spacy.io/usage/linguistic-features)) — how a real pipeline is wired. ·  also cited by 2 other lessons
- Porter, M. F. (1980). An algorithm for suffix stripping ([link](https://tartarus.org/martin/PorterStemmer/def.txt)) — the original paper, five pages, still the clearest explanation.


%% ── my notes ── %%
