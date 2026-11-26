---
id: "lesson:10/03"
type: lesson
ref: 10/03
phase: 10
num: 3
title: Data Pipelines for Pre-Training
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 3
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 1
aliases:
  - 10/03
  - 10-03
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/03-data-pipelines/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/03-data-pipelines"
---

# 10/03 Data Pipelines for Pre-Training

> The model is a mirror. It reflects whatever data you feed it. Feed it garbage, it reflects garbage with perfect fluency.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/03-data-pipelines/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/03-data-pipelines) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/03-data-pipelines) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10, Lessons 01-02 (Tokenizers, Building a Tokenizer)`

- **10/01-02** — Tokenizers, Building a Tokenizer:
    - [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
    - [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]

## Builds on this

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]

## Concepts taught

- Common Crawl `lesson term` — A non-profit that crawls the web monthly -- ~250TB raw, the starting point for most LLM training data
- MinHash `lesson term` — A technique to estimate Jaccard similarity between sets using fixed-size signatures -- enables near-duplicate detection at scale
- LSH `lesson term` — A method to group similar items into the same bucket -- reduces pairwise comparisons from O(n^2) to near-linear
- Sequence packing `lesson term` — Fitting multiple documents into fixed-length sequences with proper attention masks -- eliminates padding waste
- Chinchilla scaling `lesson term` — For a fixed compute budget, optimal performance requires scaling model size and training tokens roughly equally
- [[Concepts/Fertility|Fertility]] `lesson term` — Average number of tokens per word -- 1.3 for English in GPT-4, higher for non-Latin scripts
- Data mixing `lesson term` — The ratio of code vs text vs math vs multilingual data -- no formula, requires experimentation
- [[Concepts/Perplexity filter|Perplexity filter]] `lesson term` — Use a small language model to score documents -- high perplexity means the text is unlike clean reference data
- Deduplication `lesson term` — Eliminating exact and near-duplicate documents -- typically removes 30-40% of raw web data
- Attention mask `lesson term` — A binary mask that prevents attention across document boundaries in packed sequences

## Ships

- [[Artifacts/10-03 prompt-data-quality-checker|prompt-data-quality-checker]] `prompt` — Validate and debug data quality in LLM pre-training pipelines

## Further reading

- Deduplicating Training Data Makes Language Models Better ([link](https://arxiv.org/abs/2107.06499)) — why deduplication matters more than you think
- [[Resources/Hoffmann et al. (2022). Training Compute-Optimal Large Language Models|Hoffmann et al. (2022). Training Compute-Optimal Large Language Models]] ([link](https://arxiv.org/abs/2203.15556)) — the paper that changed how we think about data scale ·  also cited by 2 other lessons
- Penedo et al., 2023 -- The RefinedWeb Dataset for Falcon LLM ([link](https://arxiv.org/abs/2306.01116)) — how to filter Common Crawl to high quality
- [[Resources/Touvron et al., 2023 - Llama 2- Open Foundation and Fine-Tuned Chat Models|Touvron et al., 2023 -- Llama 2: Open Foundation and Fine-Tuned Chat Models]] ([link](https://arxiv.org/abs/2307.09288)) — data pipeline details for Llama 2 ·  also cited by 1 other lesson
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — 15.6T tokens, data mixing ratios, filtering pipeline ·  also cited by 7 other lessons
- Broder, 1997 -- On the Resemblance and Containment of Documents ([link](https://ieeexplore.ieee.org/document/666900)) — the original MinHash paper

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 4, required

## My route

- Step 3 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Data pipelines for pre-training
- Previous: [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
- Next: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]


%% ── my notes ── %%
