---
id: "concept:chunking"
type: concept
name: Chunking
canonical: true
category: "Retrieval & generation"
taught_in: 2
community: 55
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# Chunking

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

> *What people say:* Splitting documents into pieces.

**What it actually means:** Dividing source material into retrievable units before indexing. Chunk boundaries, overlap, metadata, and document structure determine whether retrieval returns enough context without flooding the prompt.

**Why it matters:** The right chunking strategy depends on document shape, query type, embedding model, and evaluation results. There is no universal token size or overlap percentage.

**In practice:** Keep headings and code blocks intact, attach source metadata, then measure retrieval quality on real questions before tuning size.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Grounding|Grounding]]
- [[Concepts/Maximum Marginal Relevance (MMR)|Maximum Marginal Relevance (MMR)]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/Reranker|Reranker]]

## Taught in

- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — Breaking documents into 256-512 token segments so each can be independently embedded and retrieved
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — Breaking documents into smaller segments (typically 256-512 tokens) so each can be embedded and retrieved independently


%% ── my notes ── %%
