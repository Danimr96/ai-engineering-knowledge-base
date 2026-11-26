---
id: "lesson:05/15"
type: lesson
ref: 05/15
phase: 5
num: 15
title: "Topic Modeling — LDA and BERTopic"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 8
code_files: 1
concepts: 5
prereqs: 2
community: 63
aliases:
  - 05/15
  - 05-15
tags:
  - phase/05
  - type/learn
  - community/63
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/15-topic-modeling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/15-topic-modeling"
---

# 05/15 Topic Modeling — LDA and BERTopic

> LDA: documents are mixtures of topics, topics are distributions over words. BERTopic: documents cluster in embedding space, clusters are topics. Same goal, different decompositions.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/15-topic-modeling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/15-topic-modeling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/15-topic-modeling) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/63 Topic · UMAP|63 Topic · UMAP]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 5 · 03 (Word2Vec)`

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF
- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]] — Word2Vec

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]

## Concepts taught

- [[Concepts/Topic|Topic]] `lesson term` — A probability distribution over words (LDA) or a cluster of similar documents (BERTopic).
- Mixed membership `lesson term` — LDA assigns each document a distribution over all topics.
- [[Concepts/UMAP|UMAP]] `lesson term` — Manifold learning that preserves local structure; used in BERTopic.
- HDBSCAN `lesson term` — Finds variable-size clusters; produces "noise" label (-1) for outliers.
- c_v coherence `lesson term` — Average pointwise mutual information of top topic words within sliding windows.

## Ships

- [[Artifacts/05-15 topic-picker|topic-picker]] `skill` — Pick LDA or BERTopic for a corpus. Specify library, knobs, evaluation.

## Further reading

- Grootendorst (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure ([link](https://arxiv.org/abs/2203.05794)) — the BERTopic paper.
- Blei, Ng, Jordan (2003). Latent Dirichlet Allocation ([link](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)) — the LDA paper.
- BERTopic documentation ([link](https://maartengr.github.io/BERTopic/)) — the production reference. Excellent examples.
- Röder, Both, Hinneburg (2015). Exploring the Space of Topic Coherence Measures ([link](https://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf)) — the paper that introduced c_v and friends.


%% ── my notes ── %%
