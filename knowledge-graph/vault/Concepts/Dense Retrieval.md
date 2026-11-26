---
id: "concept:dense-retrieval"
type: concept
name: Dense Retrieval
canonical: true
category: "Retrieval & generation"
taught_in: 1
community: 18
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Dense Retrieval

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** First-stage retrieval that embeds queries and candidates into vector representations and ranks candidates by a similarity function.

**Why it matters:** It can retrieve paraphrases and semantic matches that share few exact words, complementing lexical methods such as BM25.

**In practice:** Train or select an embedding model for the domain, index candidate vectors, and evaluate retrieval recall before connecting the results to generation.

**Common confusion:** Dense retrieval is not a reranker. It searches the collection, while a reranker rescores a smaller candidate set.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/BM25|BM25]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Hybrid Retrieval|Hybrid Retrieval]]
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]]
- [[Concepts/Semantic Search|Semantic Search]]

## Taught in

- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Encode query + doc into vectors, find nearest neighbors.

## Sources

- Dense Passage Retrieval ([link](https://aclanthology.org/2020.emnlp-main.550/))


%% ── my notes ── %%
