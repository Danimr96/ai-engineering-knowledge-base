---
id: "concept:hnsw"
type: concept
name: HNSW
canonical: true
category: "Retrieval & generation"
aliases:
  - Hierarchical Navigable Small World
taught_in: 3
community: 18
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# HNSW

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** An approximate-nearest-neighbor index that organizes vectors in layered proximity graphs and searches from coarse upper layers toward detailed lower layers.

**Why it matters:** It is a common way to make high-recall vector search practical at scales where exhaustive comparison is too slow.

**In practice:** Tune construction and query parameters against latency, memory, and Recall@K targets, then rebuild the index when embedding versions change.

**Common confusion:** HNSW is an index algorithm, not a similarity metric, embedding model, or complete vector database.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Approximate Nearest Neighbor (ANN)|Approximate Nearest Neighbor (ANN)]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Recall@K|Recall@K]]
- [[Concepts/Vector Database|Vector Database]]

## Taught in

- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Hierarchical Navigable Small World graph. Multi-layer graph for fast approximate nearest neighbor search
- [[Lessons/04-20 Image Retrieval & Metric Learning|04/20 Image Retrieval & Metric Learning]] — Hierarchical navigable small world; fast approximate NN with small memory overhead
- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — Hierarchical Navigable Small World graph -- multi-layer structure enabling O(log n) approximate nearest neighbor search

## Sources

- Efficient and Robust Approximate Nearest Neighbor Search Using HNSW ([link](https://dl.acm.org/doi/10.1109/TPAMI.2018.2889473))


%% ── my notes ── %%
