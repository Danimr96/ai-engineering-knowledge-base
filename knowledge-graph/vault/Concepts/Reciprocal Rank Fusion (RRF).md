---
id: "concept:reciprocal-rank-fusion-rrf"
type: concept
name: Reciprocal Rank Fusion (RRF)
canonical: true
category: "Retrieval & generation"
taught_in: 3
community: 26
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/26
source: ai-engineering-from-scratch/glossary/terms.md
---

# Reciprocal Rank Fusion (RRF)

**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]]

**What it actually means:** A rank-fusion method that combines several result lists by summing contributions that decrease with each item's rank in each list.

**Why it matters:** It can merge lexical, dense, or multi-query rankings without assuming their raw scores share the same scale.

**In practice:** Retrieve independent candidate lists, deduplicate by stable document identity, apply one versioned fusion constant, and evaluate against each individual retriever.

**Common confusion:** RRF combines ranks, not embeddings or relevance scores, and it cannot recover an item absent from every input list.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/BM25|BM25]]
- [[Concepts/Dense Retrieval|Dense Retrieval]]
- [[Concepts/Hybrid Retrieval|Hybrid Retrieval]]
- [[Concepts/Reranker|Reranker]]

## Taught in

- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] `alias` — Combine two rankings by summing 1/(k + rank).
- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]] `alias` — Combining multiple ranked lists by summing 1/(k + rank) for each document across all lists
- [[Lessons/19-65 Hybrid Retrieval with BM25 and Dense Embeddings|19/65 Hybrid Retrieval with BM25 and Dense Embeddings]] `alias` — Sum of 1 / (k + rank) across ranked lists; k = 60 default

## Sources

- Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods ([link](https://dl.acm.org/doi/10.1145/1571941.1572114))


%% ── my notes ── %%
