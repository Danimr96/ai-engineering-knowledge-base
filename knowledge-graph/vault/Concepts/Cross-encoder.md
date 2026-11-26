---
id: "concept:cross-encoder"
type: concept
name: Cross-encoder
canonical: false
taught_in: 5
community: 26
tags:
  - concept/lesson-term
  - community/26
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/en.md
---

# Cross-encoder

**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]]

> *What people say:* Reranker model

**What it actually means:** Encodes query + doc together. Slow but accurate.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]]
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]] — A BERT that takes both query and doc as input, outputs a relevance score.
- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — Processes query-document pair jointly through the full model; higher accuracy, no pre-computation
- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]] — A model that takes a query and document as a single input, producing a relevance score; more accurate than bi-encoders but too slow for full corpus search
- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]] — Encodes (query, doc) jointly; outputs one relevance scalar


%% ── my notes ── %%
