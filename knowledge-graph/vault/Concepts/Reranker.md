---
id: "concept:reranker"
type: concept
name: Reranker
canonical: true
category: "Retrieval & generation"
taught_in: 0
community: 55
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# Reranker

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

**What it actually means:** A second-stage model or scoring function that reorders a small candidate set using a richer comparison between the query and each candidate.

**Why it matters:** Fast first-stage retrieval maximizes candidate coverage, while reranking can improve which evidence reaches the limited context window.

**In practice:** Retrieve 50 candidates with hybrid search, score each query-document pair with a cross-encoder, and pass the top 5 supported chunks to generation.

**Common confusion:** A reranker does not search the entire corpus. It only reorders candidates that retrieval already found.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/BM25|BM25]]
- [[Concepts/Chunking|Chunking]]
- [[Concepts/Cosine Similarity|Cosine Similarity]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Hybrid Retrieval|Hybrid Retrieval]]
- [[Concepts/Maximum Marginal Relevance (MMR)|Maximum Marginal Relevance (MMR)]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/Recall@K|Recall@K]]
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]]
- [[Concepts/Semantic Search|Semantic Search]]


%% ── my notes ── %%
