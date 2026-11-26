---
id: "lesson:11/06"
type: lesson
ref: 11/06
phase: 11
num: 6
title: RAG (Retrieval-Augmented Generation)
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 12
prereqs: 5
community: 3
aliases:
  - 11/06
  - 11-06
tags:
  - phase/11
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/06-rag/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/06-rag"
---

# 11/06 RAG (Retrieval-Augmented Generation)

> Your LLM knows everything up to its training cutoff. It knows nothing about your company's docs, your codebase, or last week's meeting notes. RAG solves this by retrieving relevant documents and stuffing them into the prompt. It's the most deployed pattern in production AI. If you build one thing from this course, build a RAG pipeline.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/06-rag/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/06-rag) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/06-rag) · code: main.py, main.ts  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 (LLMs from Scratch), Phase 11 Lessons 01-05`

- **11/01-05**:
    - [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
    - [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]]
    - [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
    - [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]]
    - [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]]
- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from Scratch ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]]
- [[Lessons/19-65 Hybrid Retrieval with BM25 and Dense Embeddings|19/65 Hybrid Retrieval with BM25 and Dense Embeddings]]
- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]]
- [[Lessons/19-67 Query Rewriting- HyDE, Multi-Query, and Decomposition|19/67 Query Rewriting: HyDE, Multi-Query, and Decomposition]]
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]]
- [[Lessons/19-69 End-to-End RAG System|19/69 End-to-End RAG System]]

## Concepts taught

- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]] (as *RAG*) `glossary` — Retrieve relevant documents, paste them into the prompt, and generate an answer grounded in those documents
- [[Concepts/Embedding|Embedding]] `glossary` — A dense vector representation of text where similar meanings produce similar vectors
- [[Concepts/Vector Database|Vector Database]] `glossary` — A data store optimized for storing vectors and finding the nearest neighbors by similarity
- [[Concepts/Chunking|Chunking]] `glossary` — Breaking documents into smaller segments (typically 256-512 tokens) so each can be embedded and retrieved independently
- [[Concepts/Cosine Similarity|Cosine Similarity]] `glossary` — The cosine of the angle between two vectors; 1 = identical direction, 0 = orthogonal, -1 = opposite
- Top-k retrieval `lesson term` — Return the k most similar chunks to the query from the vector store
- [[Concepts/Context Window|Context Window]] `glossary` — The maximum number of tokens the LLM can process in a single request; retrieved chunks must fit within this
- Augmented generation `lesson term` — Generating a response using retrieved documents as context rather than relying solely on trained knowledge
- [[Concepts/TF-IDF|TF-IDF]] `lesson term` — Term Frequency times Inverse Document Frequency; weights words by how distinctive they are within a corpus
- Indexing `lesson term` — The offline process of chunking, embedding, and storing documents so they can be searched at query time
- [[Concepts/Grounding|Grounding]] `glossary` — Connecting a generated answer or action to evidence, state, or observations that the system can identify and check.

## Ships

- [[Artifacts/11-06 prompt-rag-architect|prompt-rag-architect]] `prompt` — Design RAG systems for specific use cases with concrete architecture decisions
- [[Artifacts/11-06 skill-rag-pipeline|skill-rag-pipeline]] `skill` — Build and debug RAG pipelines from first principles

## Further reading

- [[Resources/Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA|Karpukhin et al. (2020). Dense Passage Retrieval for Open-Domain QA]] ([link](https://arxiv.org/abs/2004.04906)) — the DPR paper that proved dense bi-encoder retrieval beats BM25 on open-domain QA and set the pattern for modern RAG retrievers. ·  also cited by 2 other lessons
- LlamaIndex High-Level Concepts ([link](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)) — the main concepts to know when building RAG pipelines: data loaders, node parsers, indices, retrievers, response synthesizers.
- [[Resources/LangChain documentation on RAG|LangChain documentation on RAG]] ([link](https://python.langchain.com/docs/tutorials/rag/)) — the opposite-flavor orchestrator; chain-of-runnables view of the same retrieve-then-generate pattern. ·  also cited by 1 other lesson

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 7, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 5, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 5, required
- [[Paths/Customer AI Deployment|Customer AI Deployment]] — step 6, required


%% ── my notes ── %%
