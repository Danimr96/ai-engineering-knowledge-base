---
id: "lesson:05/23"
type: lesson
ref: 05/23
phase: 5
num: 23
title: Chunking Strategies for RAG
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 8
code_files: 2
concepts: 7
prereqs: 2
aliases:
  - 05/23
  - 05-23
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag"
---

# 05/23 Chunking Strategies for RAG

> Chunking configuration influences retrieval quality as much as the choice of embedding model (Vectara NAACL 2025). Get chunking wrong and no amount of reranking saves you.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag) · code: main.py, main.ts · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 14 (Information Retrieval), Phase 5 · 22 (Embedding Models)`

- [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]] — Information Retrieval
- [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]] — Embedding Models

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]

## Builds on this

- [[Lessons/05-28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR|05/28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR]]

## Concepts taught

- [[Concepts/Chunk|Chunk]] `lesson term` — Sub-document unit that gets embedded, indexed, and retrieved.
- [[Concepts/Overlap|Overlap]] `lesson term` — N tokens shared between adjacent chunks; often useless in 2026 benchmarks.
- Semantic chunking `lesson term` — Split where adjacent-sentence embedding similarity drops.
- Parent-document `lesson term` — Retrieve small children, return larger parents.
- Late chunking `lesson term` — Embed full doc at token level, pool into chunk vectors.
- Contextual retrieval `lesson term` — LLM-generated summary prepended to each chunk before indexing.
- Context cliff `lesson term` — Quality drop observed around 2.5k context tokens in RAG (Jan 2026).

## Ships

- [[Artifacts/05-23 chunker|chunker]] `skill` — Pick a chunking strategy, size, and overlap for a given corpus and query distribution.

## Further reading

- [[Resources/Anthropic — Contextual Retrieval|Anthropic — Contextual Retrieval]] ([link](https://www.anthropic.com/news/contextual-retrieval)) — 35-50% retrieval improvement with LLM-generated context prefixes. ·  also cited by 3 other lessons
- Vectara (2024, NAACL 2025). Chunking configurations analysis ([link](https://arxiv.org/abs/2410.13070)) — chunking matters as much as embedding choice.
- NVIDIA 2026 chunk-size benchmark — Premai summary ([link](https://blog.premai.io/rag-chunking-strategies-the-2026-benchmark-guide/)) — chunk size by query type.
- Jina AI — Late Chunking in Long-Context Embedding Models (2024) ([link](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)) — the late chunking paper.
- Yepes et al. / LangChain — Recursive Character Splitting docs ([link](https://python.langchain.com/docs/how_to/recursive_text_splitter/)) — the default in production.


%% ── my notes ── %%
