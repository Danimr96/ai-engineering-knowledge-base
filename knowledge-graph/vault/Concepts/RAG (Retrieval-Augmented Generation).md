---
id: "concept:rag-retrieval-augmented-generation"
type: concept
name: RAG (Retrieval-Augmented Generation)
canonical: true
category: "Retrieval & generation"
taught_in: 3
community: 55
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# RAG (Retrieval-Augmented Generation)

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

> *What people say:* A model answering with retrieved knowledge.

**What it actually means:** A system pattern that retrieves evidence relevant to a request and supplies selected content to a generative model before it answers or acts. Retrieval can use lexical, vector, structured, or hybrid methods.

**Why it matters:** RAG can make current or private evidence available without encoding it into model weights, but retrieval and grounding must be evaluated separately.

**Why it's called that:** Retrieval finds evidence, augmentation adds selected evidence to context, and generation produces the response.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/BM25|BM25]]
- [[Concepts/Chunking|Chunking]]
- [[Concepts/Fine-tuning|Fine-tuning]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Hallucination|Hallucination]]
- [[Concepts/Hybrid Retrieval|Hybrid Retrieval]]
- [[Concepts/Maximum Marginal Relevance (MMR)|Maximum Marginal Relevance (MMR)]]
- [[Concepts/Reranker|Reranker]]

## Taught in

- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] `alias` — Retrieval-augmented generation. Retriever + reader pipeline.
- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]] `alias` — Retrieve relevant docs, then ground the LLM's response.
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — Retrieve relevant documents, paste them into the prompt, and generate an answer grounded in those documents

## Sources

- Retrieval-Augmented Generation paper ([link](https://arxiv.org/abs/2005.11401))


%% ── my notes ── %%
