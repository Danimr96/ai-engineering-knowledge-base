---
id: "lesson:11/07"
type: lesson
ref: 11/07
phase: 11
num: 7
title: "Advanced RAG (Chunking, Reranking, Hybrid Search)"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 1
community: 26
aliases:
  - 11/07
  - 11-07
tags:
  - phase/11
  - type/build
  - community/26
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/07-advanced-rag/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/07-advanced-rag"
---

# 11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)

> Basic RAG retrieves the top-k most similar chunks. That works for simple questions. It falls apart for multi-hop reasoning, ambiguous queries, and large corpora. Advanced RAG is the difference between a demo that works on 10 documents and a system that works on 10 million.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/07-advanced-rag/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/07-advanced-rag) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/07-advanced-rag) · code: main.py  
**Community:** [[Communities/26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder|26 BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11, Lesson 06 (RAG)`

- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — RAG

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]], [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]], [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]], [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]]
- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]]

## Concepts taught

- [[Concepts/BM25|BM25]] `glossary` — A probabilistic ranking algorithm that scores documents by term frequency, inverse document frequency, and document length normalization
- [[Concepts/Hybrid search|Hybrid search]] `lesson term` — Running semantic (vector) and keyword (BM25) search in parallel, then merging results with rank fusion
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]] (as *Reciprocal Rank Fusion*) `glossary` — Combining multiple ranked lists by summing 1/(k + rank) for each document across all lists
- Reranking `lesson term` — Using a more expensive cross-encoder model to re-score a candidate set from initial retrieval
- [[Concepts/Cross-encoder|Cross-encoder]] `lesson term` — A model that takes a query and document as a single input, producing a relevance score; more accurate than bi-encoders but too slow for full corpus search
- [[Concepts/Bi-encoder|Bi-encoder]] `lesson term` — A model that embeds queries and documents independently; fast because embeddings are precomputed, but less accurate than cross-encoders
- [[Concepts/HyDE|HyDE]] `lesson term` — Generate a hypothetical answer to the query, embed it, and search for real documents similar to it
- Parent-child chunking `lesson term` — Index small chunks for precise retrieval but return the larger parent chunk to provide sufficient context
- Metadata filtering `lesson term` — Filtering documents by attributes (date, source, category) before running vector search to reduce the search space
- [[Concepts/Faithfulness|Faithfulness]] `lesson term` — Whether the generated answer is supported by the retrieved documents, as opposed to hallucinated from the model's training data
- [[Concepts/Hybrid Retrieval|Hybrid Retrieval]] `glossary` — Retrieval that combines signals from different methods, commonly lexical matching and dense-vector similarity, before merging or reranking results.

## Ships

- [[Artifacts/11-07 prompt-advanced-rag-debugger|prompt-advanced-rag-debugger]] `prompt` — Diagnose and fix RAG quality issues across retrieval, generation, and evaluation
- [[Artifacts/11-07 skill-advanced-rag|skill-advanced-rag]] `skill` — Build production-grade RAG with hybrid search, reranking, and evaluation

## Further reading

- [[Resources/DSPy- Compiling Declarative Language Model Calls into Self-Improving Pipelines|DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines]] ([link](https://arxiv.org/abs/2310.03714)) — treats prompt construction and weight selection as an optimization problem over retrieval pipelines; read this for "program LLMs" instead of "prompt LLMs." ·  also cited by 1 other lesson
- Asai et al., "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection" (ICLR 2024) ([link](https://arxiv.org/abs/2310.11511)) — self-evaluating RAG with reflection tokens; the agentic frontier past static retrieve-then-generate.
- Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" (Microsoft Research 2024) ([link](https://arxiv.org/abs/2404.16130)) — GraphRAG paper: entity-relation extraction + Leiden community detection for query-focused summarization; the global vs local retrieval distinction.
- LangChain Query Construction blog ([link](https://blog.langchain.dev/query-construction/)) — how to translate natural-language queries into structured database queries (Text-to-SQL, Cypher) as a pre-retrieval step.

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 8, required


%% ── my notes ── %%
