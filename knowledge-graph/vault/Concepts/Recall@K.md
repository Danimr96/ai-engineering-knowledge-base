---
id: "concept:recall-k"
type: concept
name: "Recall@K"
canonical: true
category: "Retrieval & generation"
taught_in: 4
community: 18
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Recall@K

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** For one query, Recall@K is `|relevant items intersecting the top k| / |relevant items|`. A dataset score aggregates those per-query values under a stated rule.

**Why it matters:** It tells you whether a retrieval stage supplies downstream generation or reranking with enough relevant candidates.

**In practice:** Define relevance judgments, k, the aggregation method, and a policy for queries with no judged relevant items, then inspect queries with zero recalled evidence.

**Common confusion:** High Recall@K does not mean the top result is good, the ranking is well ordered, or the final answer is grounded. Queries with no relevant items require an explicit exclusion or assigned-value policy because the denominator is zero.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Approximate Nearest Neighbor (ANN)|Approximate Nearest Neighbor (ANN)]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/HNSW|HNSW]]
- [[Concepts/Precision & Recall|Precision & Recall]]
- [[Concepts/Reranker|Reranker]]

## Taught in

- [[Lessons/04-20 Image Retrieval & Metric Learning|04/20 Image Retrieval & Metric Learning]] — Fraction of queries with at least one correct result in the top K
- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Fraction of queries where a relevant doc is in the top-k.
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]] — Fraction of queries where any of the top-k chunks overlaps the gold answer span
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]] — Fraction of gold in top-k

## Sources

- BEIR ([link](https://openreview.net/forum?id=wCu6T5xFjeJ))


%% ── my notes ── %%
