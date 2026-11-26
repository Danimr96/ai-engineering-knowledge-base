---
id: "concept:approximate-nearest-neighbor-ann"
type: concept
name: Approximate Nearest Neighbor (ANN)
canonical: true
category: "Retrieval & generation"
taught_in: 2
community: 18
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Approximate Nearest Neighbor (ANN)

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** A search method that returns vectors likely to be among the nearest to a query without exhaustively comparing the query with every stored vector.

**Why it matters:** Approximation makes large vector indexes practical, but it introduces a measurable tradeoff between search speed, memory, and retrieval recall.

**In practice:** Tune index and search parameters against a held-out query set, then report latency together with Recall@K instead of assuming every true neighbor is found.

**Common confusion:** ANN describes a search objective and tradeoff, while HNSW is one particular index algorithm that can implement it.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Cosine Similarity|Cosine Similarity]]
- [[Concepts/HNSW|HNSW]]
- [[Concepts/Recall@K|Recall@K]]
- [[Concepts/Vector Database|Vector Database]]

## Taught in

- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] `alias` — Algorithms (HNSW, LSH, IVF) that find approximately closest points much faster than exact search
- [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]] `alias` — Algorithms (HNSW, LSH, IVF) that find approximately nearest points much faster than exact search

## Sources

- Efficient and Robust Approximate Nearest Neighbor Search Using HNSW ([link](https://dl.acm.org/doi/10.1109/TPAMI.2018.2889473))


%% ── my notes ── %%
