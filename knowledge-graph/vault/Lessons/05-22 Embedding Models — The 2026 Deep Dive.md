---
id: "lesson:05/22"
type: lesson
ref: 05/22
phase: 5
num: 22
title: "Embedding Models — The 2026 Deep Dive"
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
  - 05/22
  - 05-22
tags:
  - phase/05
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive"
---

# 05/22 Embedding Models — The 2026 Deep Dive

> Word2Vec gave you a vector per word. Modern embedding models give you a vector per passage, cross-lingual, with sparse, dense, and multi-vector views, sized to fit your index. Pick wrong and your RAG retrieves the wrong thing.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 03 (Word2Vec), Phase 5 · 14 (Information Retrieval)`

- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]] — Word2Vec
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Information Retrieval

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]

## Builds on this

- [[Lessons/05-23 Chunking Strategies for RAG|05/23 Chunking Strategies for RAG]]
- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]]

## Concepts taught

- Dense embedding `lesson term` — One fixed-size vector per text. Cosine similarity for ranking.
- Sparse embedding `lesson term` — One weight per vocab token; mostly zeros; trained end-to-end.
- [[Concepts/Multi-vector|Multi-vector]] `lesson term` — One vector per token; MaxSim scoring; bigger index, better recall.
- Matryoshka `lesson term` — First N dims are a valid smaller embedding on their own.
- [[Concepts/MTEB|MTEB]] `lesson term` — Massive Text Embedding Benchmark — 56 tasks at launch, 100+ in v2.
- BEIR `lesson term` — 18 zero-shot retrieval tasks; often cited for cross-domain robustness.
- Asymmetric encoding `lesson term` — Model uses different projections for queries and documents.

## Ships

- [[Artifacts/05-22 embedding-picker|embedding-picker]] `skill` — Pick embedding model, dimension, and retrieval mode for a given corpus and deployment.

## Further reading

- Reimers, Gurevych (2019). Sentence-BERT ([link](https://arxiv.org/abs/1908.10084)) — the bi-encoder paper.
- Santhanam et al. (2022). ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction ([link](https://arxiv.org/abs/2112.01488)) — late interaction in production.
- Kusupati et al. (2022). Matryoshka Representation Learning ([link](https://arxiv.org/abs/2205.13147)) — the dimension-ladder training objective.
- [[Resources/Muennighoff et al. (2022). MTEB- Massive Text Embedding Benchmark|Muennighoff et al. (2022). MTEB: Massive Text Embedding Benchmark]] ([link](https://arxiv.org/abs/2210.07316)) — the leaderboard paper. ·  also cited by 1 other lesson
- Chen et al. (2024). BGE-M3: Multi-lingual, Multi-functionality, Multi-granularity ([link](https://arxiv.org/abs/2402.03216)) — the unified three-mode model.
- MTEB leaderboard on Hugging Face ([link](https://huggingface.co/spaces/mteb/leaderboard)) — live rankings.


%% ── my notes ── %%
