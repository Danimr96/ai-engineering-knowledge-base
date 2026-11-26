---
id: "lesson:05/03"
type: lesson
ref: 05/03
phase: 5
num: 3
title: "Word Embeddings — Word2Vec from Scratch"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 63
libraries:
  - numpy
aliases:
  - 05/03
  - 05-03
tags:
  - phase/05
  - type/build
  - community/63
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec"
---

# 05/03 Word Embeddings — Word2Vec from Scratch

> A word is the company it keeps. Train a shallow net on that idea and geometry falls out.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/63 Topic · UMAP|63 Topic · UMAP]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 3 · 03 (Backpropagation from Scratch)`

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — Backpropagation from Scratch
- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]]

## Builds on this

- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]]
- [[Lessons/05-06 Named Entity Recognition|05/06 Named Entity Recognition]]
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]
- [[Lessons/05-15 Topic Modeling — LDA and BERTopic|05/15 Topic Modeling — LDA and BERTopic]]
- [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]]

## Concepts taught

- Word embedding `lesson term` — A dense, low-dim (typically 100-300) representation learned from context.
- Skip-gram `lesson term` — Predict context words from center word. Slower than CBOW, better for rare words.
- Negative sampling `lesson term` — Replace softmax over full vocab with binary classification against k random words.
- Static embedding `lesson term` — Same vector regardless of context. Fails on polysemy.
- Contextual embedding `lesson term` — Different vector for each occurrence based on surrounding words. What transformers produce.
- [[Concepts/OOV|OOV]] `lesson term` — Word not seen in training. Word2Vec cannot produce a vector for these.

## Ships

- [[Artifacts/05-03 embedding-probe|embedding-probe]] `skill` — Inspect a word2vec model. Run analogies, find neighbors, diagnose quality.

## Further reading

- Mikolov et al. (2013). Distributed Representations of Words and Phrases and their Compositionality ([link](https://arxiv.org/abs/1310.4546)) — the negative-sampling paper. Short and readable.
- Rong, X. (2014). word2vec Parameter Learning Explained ([link](https://arxiv.org/abs/1411.2738)) — the clearest derivation of the gradients, if the original paper's math feels dense.
- gensim Word2Vec tutorial ([link](https://radimrehurek.com/gensim/models/word2vec.html)) — production training settings that actually work.


%% ── my notes ── %%
