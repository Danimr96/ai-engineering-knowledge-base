---
id: "concept:hybrid-retrieval"
type: concept
name: Hybrid Retrieval
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

# Hybrid Retrieval

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** Retrieval that combines signals from different methods, commonly lexical matching and dense-vector similarity, before merging or reranking results.

**Why it matters:** Exact identifiers, rare terms, and semantic paraphrases behave differently, so one retrieval signal can miss useful evidence.

**In practice:** Retrieve candidates with both BM25-style keyword search and embeddings, merge their ranks, then rerank the combined set for the user query.

**Common confusion:** Hybrid retrieval combines candidate signals. A reranker applies a second relevance model to candidates already retrieved.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/BM25|BM25]]
- [[Concepts/Dense Retrieval|Dense Retrieval]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]]
- [[Concepts/Reranker|Reranker]]
- [[Concepts/Semantic Search|Semantic Search]]
- [[Concepts/Vector Database|Vector Database]]

## Taught in

- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]]


%% ── my notes ── %%
