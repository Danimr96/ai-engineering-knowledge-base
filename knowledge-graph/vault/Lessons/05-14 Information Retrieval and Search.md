---
id: "lesson:05/14"
type: lesson
ref: 05/14
phase: 5
num: 14
title: Information Retrieval and Search
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 26
aliases:
  - 05/14
  - 05-14
tags:
  - phase/05
  - type/build
  - community/26
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search"
---

# 05/14 Information Retrieval and Search

> BM25 is precise but brittle. Dense casts a wide net but misses keywords. Hybrid is the 2026 default. Everything else is tuning.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 02 (BoW + TF-IDF), Phase 5 · 04 (GloVe, FastText, Subword)`

- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — BoW + TF-IDF
- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]] — GloVe, FastText, Subword

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]

## Builds on this

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]]
- [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]]
- [[Lessons/05-23 Chunking Strategies for RAG|05/23 Chunking Strategies for RAG]]
- [[Lessons/05-27 LLM Evaluation — RAGAS, DeepEval, G-Eval|05/27 LLM Evaluation — RAGAS, DeepEval, G-Eval]]

## Concepts taught

- [[Concepts/BM25|BM25]] `glossary` — Okapi BM25. Scores documents by term frequency, IDF, and length.
- [[Concepts/Dense Retrieval|Dense Retrieval]] `glossary` — Encode query + doc into vectors, find nearest neighbors.
- [[Concepts/Bi-encoder|Bi-encoder]] `lesson term` — Encodes query and doc independently. Fast at query time.
- [[Concepts/Cross-encoder|Cross-encoder]] `lesson term` — Encodes query + doc together. Slow but accurate.
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]] (as *RRF*) `glossary` — Combine two rankings by summing 1/(k + rank).
- [[Concepts/Recall@K|Recall@K]] `glossary` — Fraction of queries where a relevant doc is in the top-k.

## Ships

- [[Artifacts/05-14 retrieval-picker|retrieval-picker]] `skill` — Pick a retrieval stack for a given corpus and query pattern.

## Further reading

- [[Resources/Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA|Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA]] ([link](https://arxiv.org/abs/2004.04906)) — DPR, the canonical bi-encoder. ·  also cited by 2 other lessons
- [[Resources/Khattab and Zaharia (2020). ColBERT- Efficient and Effective Passage Search|Khattab and Zaharia (2020). ColBERT: Efficient and Effective Passage Search]] ([link](https://arxiv.org/abs/2004.12832)) — late-interaction retrieval. ·  also cited by 1 other lesson
- Formal et al. (2021). SPLADE: Sparse Lexical and Expansion Model ([link](https://arxiv.org/abs/2107.05720)) — the learned-sparse retriever that closes the gap with dense.
- Cormack, Clarke, Büttcher (2009). Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods ([link](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)) — RRF paper.
- Robertson and Zaragoza (2009). The Probabilistic Relevance Framework: BM25 and Beyond ([link](https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf)) — the definitive BM25 treatment.


%% ── my notes ── %%
