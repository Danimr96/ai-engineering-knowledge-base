---
id: "concept:bi-encoder"
type: concept
name: Bi-encoder
canonical: false
taught_in: 5
community: 26
tags:
  - concept/lesson-term
  - community/26
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en.md
---

# Bi-encoder

**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]]

> *What people say:* Embedding model

**What it actually means:** Encodes query and doc independently. Fast at query time.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]]
- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — Encodes query and document independently into vectors; enables pre-computation and fast retrieval
- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]] — A model that embeds queries and documents independently; fast because embeddings are precomputed, but less accurate than cross-encoders
- [[Lessons/12-23 ColPali and Vision-Native Document RAG|12/23 ColPali and Vision-Native Document RAG]] — One vector per document; faster but loses granularity
- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]] — Encodes query and doc independently; cosine ranks them


%% ── my notes ── %%
