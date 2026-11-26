---
id: "lesson:10/01"
type: lesson
ref: 10/01
phase: 10
num: 1
title: "Tokenizers: BPE, WordPiece, SentencePiece"
lesson_type: build
languages:
  - Python
time_min: 90
status: done
status_auto: done
on_route: true
route_order: 1
quiz_count: 0
code_files: 3
concepts: 11
prereqs: 0
community: 1
libraries:
  - tiktoken
aliases:
  - 10/01
  - 10-01
tags:
  - phase/10
  - type/build
  - status/done
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/01-tokenizers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/01-tokenizers"
---

# 10/01 Tokenizers: BPE, WordPiece, SentencePiece

> Your LLM does not read English. It reads integers. The tokenizer decides whether those integers carry meaning or waste it.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** done  
**Open:** [[Upstream/10-llms-from-scratch/01-tokenizers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/01-tokenizers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/01-tokenizers) · code: bpe.py, bpe.rs, main.py  
**My work:** [visual lesson](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/lessons/10-01-tokenizers.html) · [artifact](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/learning-artifacts/10-01-tokenizers)  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/tiktoken (python)|tiktoken]]  

## Prerequisites

Stated upstream: `Phase 05 (NLP Foundations)`

- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP Foundations ·  medium confidence

## Builds on this

- [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
- [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]]

## Concepts taught

- [[Concepts/Token|Token]] `glossary` — A unit in the model's vocabulary -- could be a character, subword, word, or multi-word chunk
- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]] (as *BPE*) `glossary` — Byte Pair Encoding -- iteratively merge the most frequent adjacent pair of tokens until the target vocabulary size is reached
- WordPiece `lesson term` — Like BPE but merges maximize the likelihood ratio count(AB)/(count(A)count(B)) instead of raw frequency
- [[Concepts/SentencePiece|SentencePiece]] `lesson term` — A language-agnostic tokenizer that operates on raw Unicode without pre-tokenization, supporting BPE and Unigram algorithms
- Vocabulary size `lesson term` — The total number of unique tokens: GPT-2 has 50,257, BERT has 30,522, Llama 3 has 128,256
- [[Concepts/Fertility|Fertility]] `lesson term` — Average number of tokens per word -- measures tokenizer efficiency across languages (1.0 is perfect, 3.0 means the model works three times harder)
- [[Concepts/Byte-level BPE|Byte-level BPE]] `lesson term` — BPE operating on raw bytes (0-255) instead of Unicode characters, guaranteeing no unknown tokens for any input
- [[Concepts/Merge table|Merge table]] `lesson term` — Ordered list of pair merges learned during training -- this IS the tokenizer, and order matters
- [[Concepts/Pre-tokenization|Pre-tokenization]] `lesson term` — Rules applied before subword tokenization: whitespace splitting, digit separation, punctuation handling
- Compression ratio `lesson term` — Tokens produced divided by input bytes -- lower means better compression and faster inference

## Ships

- [[Artifacts/10-01 prompt-tokenizer-analyzer|prompt-tokenizer-analyzer]] `prompt` — Analyze tokenization efficiency for a given text across different models and tokenizer types
- [[Artifacts/10-01 skill-tokenizer|skill-tokenizer]] `skill` — Choosing and building tokenizers for LLM projects

## Further reading

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909)) — the paper that introduced BPE for NLP, turning a 1994 compression algorithm into the foundation of modern tokenization ·  also cited by 2 other lessons
- [[Resources/Kudo, Richardson (2018). SentencePiece- A simple and language independent subword tokenizer|Kudo, Richardson (2018). SentencePiece: A simple and language independent subword tokenizer]] ([link](https://arxiv.org/abs/1808.06226)) — language-agnostic tokenization that made multilingual models practical ·  also cited by 2 other lessons
- [[Resources/OpenAI tiktoken repo|OpenAI tiktoken repo]] ([link](https://github.com/openai/tiktoken)) — production BPE implementation in Rust with Python bindings, used by GPT-3.5/4/4o ·  also cited by 2 other lessons
- Hugging Face Tokenizers documentation ([link](https://huggingface.co/docs/tokenizers)) — production-grade tokenizer training with Rust performance

## My route

- Step 1 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Tokenizers: BPE, WordPiece, SentencePiece
- Next: [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]


%% ── my notes ── %%
