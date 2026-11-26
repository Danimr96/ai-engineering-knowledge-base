---
id: "lesson:10/02"
type: lesson
ref: 10/02
phase: 10
num: 2
title: Building a Tokenizer from Scratch
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 2
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 1
libraries:
  - regex
  - tiktoken
aliases:
  - 10/02
  - 10-02
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/02-building-a-tokenizer"
---

# 10/02 Building a Tokenizer from Scratch

> Lesson 01 gave you a toy. This lesson gives you a weapon.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/02-building-a-tokenizer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/02-building-a-tokenizer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/02-building-a-tokenizer) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/regex (python)|regex]], [[Libraries/tiktoken (python)|tiktoken]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 01 (Tokenizers: BPE, WordPiece, SentencePiece)`

- [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] — Tokenizers: BPE, WordPiece, SentencePiece

## Builds on this

- [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]

## Concepts taught

- [[Concepts/Byte-level BPE|Byte-level BPE]] `lesson term` — BPE with a base vocabulary of 256 byte values -- handles any input without unknown tokens
- [[Concepts/Pre-tokenization|Pre-tokenization]] `lesson term` — Regex or rule-based splitting that prevents BPE from merging across word boundaries
- NFKC normalization `lesson term` — Canonical decomposition followed by compatibility composition -- "fi" ligature becomes "fi", fullwidth "A" becomes "A"
- [[Concepts/Chat template|Chat template]] `lesson term` — The exact format for converting a list of role/content messages into a flat token sequence -- model-specific and must match training format
- Special tokens `lesson term` — Reserved token IDs that bypass BPE -- [BOS], [EOS], [PAD], chat markers -- matched exactly before merge
- [[Concepts/Fertility|Fertility]] `lesson term` — Ratio of output tokens to input words -- 1.3 for English in GPT-4, 2-3 for Korean, higher means wasted context
- [[Concepts/tiktoken|tiktoken]] `lesson term` — Rust BPE implementation with Python bindings -- 10-100x faster than pure Python
- [[Concepts/Merge table|Merge table]] `lesson term` — Ordered list of byte-pair merges learned during training -- this IS the tokenizer's learned knowledge

## Ships

- [[Artifacts/10-02 prompt-tokenizer-builder|prompt-tokenizer-builder]] `prompt` — Build and debug production-quality tokenizers for LLM projects

## Further reading

- [[Resources/Kudo, Richardson (2018). SentencePiece- A simple and language independent subword tokenizer|Kudo, Richardson (2018). SentencePiece: A simple and language independent subword tokenizer]] ([link](https://arxiv.org/abs/1808.06226)) — language-agnostic tokenization ·  also cited by 2 other lessons
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — details on 128K vocabulary and tokenizer training ·  also cited by 7 other lessons
- HuggingFace tokenizers ([link](https://github.com/huggingface/tokenizers)) — Rust tokenizer library supporting BPE, WordPiece, Unigram
- GPT-2 tokenizer source ([link](https://github.com/openai/gpt-2/blob/master/src/encoder.py)) — the original byte-to-Unicode mapping
- [[Resources/OpenAI tiktoken repo|OpenAI tiktoken repo]] ([link](https://github.com/openai/tiktoken)) — Rust BPE implementation used by GPT-3.5/4 ·  also cited by 2 other lessons

## My route

- Step 2 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Building a tokenizer from scratch
- Previous: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
- Next: [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]


%% ── my notes ── %%
