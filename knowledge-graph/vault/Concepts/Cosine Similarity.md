---
id: "concept:cosine-similarity"
type: concept
name: Cosine Similarity
canonical: true
category: "Data & representations"
taught_in: 5
community: 18
tags:
  - concept/glossary
  - category/data-and-representations
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Cosine Similarity

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

> *What people say:* How similar two vectors are.

**What it actually means:** The normalized dot product of two vectors. It compares their direction rather than their magnitude and ranges from -1 to 1 for real-valued vectors.

**Common confusion:** High cosine similarity only has meaning relative to the embedding model and the data distribution. It does not prove factual or semantic equivalence.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Approximate Nearest Neighbor (ANN)|Approximate Nearest Neighbor (ANN)]]
- [[Concepts/Contrastive Learning|Contrastive Learning]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Reranker|Reranker]]
- [[Concepts/Semantic Search|Semantic Search]]
- [[Concepts/Shared Embedding Space|Shared Embedding Space]]

## Taught in

- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Dot product normalized by both magnitudes. Ranges from -1 to +1. Ignores vector length
- [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]] — Dot product of L2-normalized vectors. 1 is identical, 0 is orthogonal.
- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — Cosine of the angle between vectors; 1 = identical direction, 0 = orthogonal, -1 = opposite
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — The cosine of the angle between two vectors; 1 = identical direction, 0 = orthogonal, -1 = opposite
- [[Lessons/19-60 Projection Layer for Modality Alignment|19/60 Projection Layer for Modality Alignment]] — Dot product divided by the product of L2 norms


%% ── my notes ── %%
