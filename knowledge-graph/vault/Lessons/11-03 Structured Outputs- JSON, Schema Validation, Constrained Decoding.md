---
id: "lesson:11/03"
type: lesson
ref: 11/03
phase: 11
num: 3
title: "Structured Outputs: JSON, Schema Validation, Constrained Decoding"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 11
prereqs: 5
community: 1
aliases:
  - 11/03
  - 11-03
tags:
  - phase/11
  - type/build
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/03-structured-outputs/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/03-structured-outputs"
---

# 11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding

> Your LLM returns a string. Your application needs JSON. That gap has crashed more production systems than any model hallucination. Structured output is the bridge between natural language and typed data. Get it right and your LLM becomes a reliable API. Get it wrong and you're parsing free-text with regex at 3am.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/03-structured-outputs/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/03-structured-outputs) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/03-structured-outputs) · code: main.py, main.ts  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10, Lessons 01-05 (LLMs from Scratch)`

- **10/01-05** — LLMs from Scratch:
    - [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
    - [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
    - [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
    - [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
    - [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]]

## Concepts taught

- [[Concepts/JSON mode|JSON mode]] `lesson term` — API flag that guarantees syntactically valid JSON output, but does not enforce any particular schema
- [[Concepts/Structured Output|Structured Output]] `glossary` — Output that matches a specific JSON Schema with correct keys, types, and constraints
- [[Concepts/Constrained decoding|Constrained decoding]] `lesson term` — At each token position, mask out tokens that would produce invalid output -- guarantees 100% schema compliance
- JSON Schema `lesson term` — A declarative language for describing the structure, types, and constraints of JSON data (used by OpenAPI, JSON Forms, etc.)
- Pydantic `lesson term` — Python library that defines data models with type validation, used by FastAPI and Instructor to generate JSON Schemas
- [[Concepts/Function Calling|Function Calling]] `glossary` — LLM outputs a structured function invocation (name + typed arguments) instead of free text -- OpenAI and Anthropic both support this
- Instructor `lesson term` — Python library that wraps LLM clients to return validated Pydantic instances, with automatic retry on validation failure
- Token masking `lesson term` — Setting specific token probabilities to zero during generation so the model cannot produce them
- Schema compliance `lesson term` — The output has every required field, correct types, values within constraints, and no extra disallowed fields
- Retry loop `lesson term` — Send validation errors back to the model and ask it to fix the output -- Instructor does this automatically, up to a configurable max

## Ships

- [[Artifacts/11-03 prompt-structured-extractor|prompt-structured-extractor]] `prompt` — Extract structured data from unstructured text given a JSON Schema definition
- [[Artifacts/11-03 skill-structured-outputs|skill-structured-outputs]] `skill` — Decision framework for choosing the right structured output strategy based on provider, reliability, and complexity

## Further reading

- Beurer-Kellner et al., "Prompting Is Programming: A Query Language for Large Language Models" (LMQL) ([link](https://arxiv.org/abs/2212.06094)) — the LMQL paper framing constrained decoding as a query language with type and value constraints.
- [[Resources/Willard, Louf (2023). Efficient Guided Generation for LLMs|Willard, Louf (2023). Efficient Guided Generation for LLMs]] ([link](https://arxiv.org/abs/2307.09702)) — the Outlines paper, describing how to compile JSON Schemas into finite state machines for token-level constraints ·  also cited by 1 other lesson
- [[Resources/XGrammar paper (2024)|XGrammar paper (2024)]] ([link](https://arxiv.org/abs/2411.15100)) — the current state-of-the-art grammar engine; pushdown-automaton compilation that masks tokens at ~100 ns / token. ·  also cited by 1 other lesson
- [[Resources/Anthropic Tool Use Guide|Anthropic Tool Use Guide]] ([link](https://docs.anthropic.com/en/docs/tool-use)) — how Claude implements structured output via tool use with JSON Schema input_schema ·  also cited by 1 other lesson
- Microsoft Guidance (framework docs) ([link](https://github.com/guidance-ai/guidance)) — template-driven constrained generation; vendor-agnostic complement to Outlines and XGrammar.
- Outlines library ([link](https://github.com/outlines-dev/outlines)) — open-source constrained generation using regex and JSON Schema compiled to finite state machines
- JSON Schema specification ([link](https://json-schema.org/)) — the full spec for the schema language used by every major structured output system
- [[Resources/OpenAI — Structured Outputs guide|OpenAI — Structured Outputs guide]] ([link](https://platform.openai.com/docs/guides/structured-outputs)) — official documentation for JSON Schema-based constrained decoding in the OpenAI API ·  also cited by 3 other lessons
- [[Resources/Instructor library|Instructor library]] ([link](https://python.useinstructor.com/)) — the standard library for getting structured outputs from any LLM with Pydantic validation and retries ·  also cited by 1 other lesson

## In learning paths

- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 2, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 2, required


%% ── my notes ── %%
