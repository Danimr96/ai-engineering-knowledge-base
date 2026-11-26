---
id: "lesson:11/04"
type: lesson
ref: 11/04
phase: 11
num: 4
title: "Embeddings & Vector Representations"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 13
prereqs: 1
community: 18
libraries:
  - numpy
aliases:
  - 11/04
  - 11-04
tags:
  - phase/11
  - type/build
  - community/18
source: ai-engineering-from-scratch/phases/11-llm-engineering/04-embeddings/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/04-embeddings"
---

# 11/04 Embeddings & Vector Representations

> Text is discrete. Math is continuous. Every time you ask an LLM to find "similar" documents, compare meanings, or search beyond keywords, you're relying on a bridge between these two worlds. That bridge is an embedding. If you don't understand embeddings, you don't understand modern AI. You just use it.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/04-embeddings/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/04-embeddings) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/04-embeddings) · code: embeddings.py, main.ts  
**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 11, Lesson 01 (Prompt Engineering)`

- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — Prompt Engineering

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]]
- [[Lessons/19-65 Hybrid Retrieval with BM25 and Dense Embeddings|19/65 Hybrid Retrieval with BM25 and Dense Embeddings]]
- [[Lessons/19-67 Query Rewriting- HyDE, Multi-Query, and Decomposition|19/67 Query Rewriting: HyDE, Multi-Query, and Decomposition]]

## Concepts taught

- [[Concepts/Embedding|Embedding]] `glossary` — A dense vector where geometric proximity encodes semantic similarity
- Word2Vec `lesson term` — 2013 model that learned word vectors by predicting context words; proved vector arithmetic encodes meaning
- [[Concepts/Cosine Similarity|Cosine Similarity]] `glossary` — Cosine of the angle between vectors; 1 = identical direction, 0 = orthogonal, -1 = opposite
- [[Concepts/HNSW|HNSW]] `glossary` — Hierarchical Navigable Small World graph -- multi-layer structure enabling O(log n) approximate nearest neighbor search
- [[Concepts/Bi-encoder|Bi-encoder]] `lesson term` — Encodes query and document independently into vectors; enables pre-computation and fast retrieval
- [[Concepts/Cross-encoder|Cross-encoder]] `lesson term` — Processes query-document pair jointly through the full model; higher accuracy, no pre-computation
- Matryoshka embeddings `lesson term` — Embeddings trained so the first N dimensions capture the most important information, enabling variable-size storage
- Binary quantization `lesson term` — Converting float vectors to binary (sign bit only) for 32x storage reduction with Hamming distance search
- [[Concepts/Chunking|Chunking]] `glossary` — Breaking documents into 256-512 token segments so each can be independently embedded and retrieved
- [[Concepts/Vector Database|Vector Database]] `glossary` — Data store optimized for storing vectors and performing approximate nearest neighbor search at scale
- [[Concepts/Contrastive Learning|Contrastive Learning]] `glossary` — Training approach that pushes similar pair embeddings together and dissimilar pair embeddings apart
- [[Concepts/MTEB|MTEB]] `lesson term` — Massive Text Embedding Benchmark -- 56 datasets across 8 tasks; standard for comparing embedding models

## Ships

- [[Artifacts/11-04 prompt-embedding-advisor|prompt-embedding-advisor]] `prompt` — Choose embedding models, dimensions, and strategies for specific use cases
- [[Artifacts/11-04 skill-embedding-patterns|skill-embedding-patterns]] `skill` — Production patterns for embeddings, vector search, and similarity

## Further reading

- [[Resources/Muennighoff et al. (2022). MTEB- Massive Text Embedding Benchmark|Muennighoff et al. (2022). MTEB: Massive Text Embedding Benchmark]] ([link](https://arxiv.org/abs/2210.07316)) — the benchmark defining 8 task categories (classification, clustering, pair classification, reranking, retrieval, STS, summarization, bitext mining) that the leaderboard reports; read before trusting any single MTEB score. ·  also cited by 1 other lesson
- Sentence Transformers documentation ([link](https://www.sbert.net/)) — canonical reference for bi-encoder vs cross-encoder, pooling strategies, and the ingest-split-embed-store RAG pipeline this lesson implements.

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 5, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 3, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 3, required


%% ── my notes ── %%
