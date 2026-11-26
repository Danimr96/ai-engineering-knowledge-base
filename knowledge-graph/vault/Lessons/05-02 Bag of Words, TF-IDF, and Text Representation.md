---
id: "lesson:05/02"
type: lesson
ref: 05/02
phase: 5
num: 2
title: "Bag of Words, TF-IDF, and Text Representation"
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
aliases:
  - 05/02
  - 05-02
tags:
  - phase/05
  - type/build
  - community/63
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf"
---

# 05/02 Bag of Words, TF-IDF, and Text Representation

> Count first, think later. TF-IDF still beats embeddings on well-defined tasks in 2026.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/63 Topic · UMAP|63 Topic · UMAP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 01 (Text Processing), Phase 2 · 02 (Linear Regression from Scratch)`

- [[Lessons/02-02 Linear Regression|02/02 Linear Regression]] — Linear Regression from Scratch
- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]] — Text Processing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]]
- depth 3: [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]

## Builds on this

- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- [[Lessons/05-05 Sentiment Analysis|05/05 Sentiment Analysis]]
- [[Lessons/05-06 Named Entity Recognition|05/06 Named Entity Recognition]]
- [[Lessons/05-12 Text Summarization|05/12 Text Summarization]]
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]]
- [[Lessons/05-15 Topic Modeling — LDA and BERTopic|05/15 Topic Modeling — LDA and BERTopic]]
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]

## Concepts taught

- BoW `lesson term` — Counts of vocabulary words in one document. Throws away order.
- TF `lesson term` — Count of a word in a document, optionally normalized by document length.
- DF `lesson term` — Count of documents containing the word at least once.
- IDF `lesson term` — log(N / df) smoothed. Downweights words that appear everywhere.
- Sparse vector `lesson term` — Vocabulary is typically 10k-100k words; most are absent from any given document.
- [[Concepts/Cosine Similarity|Cosine Similarity]] `glossary` — Dot product of L2-normalized vectors. 1 is identical, 0 is orthogonal.

## Ships

- [[Artifacts/05-02 vectorization-picker|vectorization-picker]] `prompt` — Given a text-classification task, recommend BoW, TF-IDF, embeddings, or a hybrid.

## Further reading

- Why TF-IDF Still Beats Embeddings" — Ashfaque Thonikkadavan (Medium) ([link](https://medium.com/@cmtwskb/why-tf-idf-still-beats-embeddings-ad85c123e1b2)) — 2026 take on when the old method wins and why.
- Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval ([link](https://www.sciencedirect.com/science/article/pii/0306457388900210)) — the paper that made TF-IDF the default for a decade.
- [[Resources/scikit-learn — feature extraction from text|scikit-learn — feature extraction from text]] ([link](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)) — the canonical API reference, plus notes on every knob. ·  also cited by 1 other lesson


%% ── my notes ── %%
