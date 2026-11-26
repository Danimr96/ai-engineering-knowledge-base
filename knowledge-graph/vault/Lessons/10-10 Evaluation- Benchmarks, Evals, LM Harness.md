---
id: "lesson:10/10"
type: lesson
ref: 10/10
phase: 10
num: 10
title: "Evaluation: Benchmarks, Evals, LM Harness"
lesson_type: build
languages:
  - Python
time_min: 90
status: planned
status_auto: planned
on_route: true
route_order: 10
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 5
community: 1
libraries:
  - numpy
aliases:
  - 10/10
  - 10-10
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/10-evaluation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/10-evaluation"
---

# 10/10 Evaluation: Benchmarks, Evals, LM Harness

> Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. Every frontier lab games benchmarks. MMLU scores go up while models still can't reliably count the number of R's in "strawberry." The only eval that matters is YOUR eval -- on YOUR task, with YOUR data.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/10-evaluation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/10-evaluation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/10-evaluation) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

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

- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]

## Concepts taught

- MMLU `lesson term` — Massive Multitask Language Understanding -- 15,908 multiple choice questions across 57 subjects, saturated above 88% by 2025
- HumanEval `lesson term` — 164 Python function-completion problems from OpenAI, tests only isolated function generation
- [[Concepts/SWE-bench|SWE-bench]] `lesson term` — 2,294 GitHub issues from 12 Python repos, measures end-to-end bug fixing including test generation
- [[Concepts/Perplexity|Perplexity]] `glossary` — exp(-avg(log P(token_i given context))) -- lower means the model assigns higher probability to the actual tokens
- ELO rating `lesson term` — A relative skill rating computed from pairwise win/loss records, used by Chatbot Arena to rank 100+ models
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]] (as *LLM-as-judge*) `glossary` — A strong model scores a weaker model's outputs against a rubric, ~80% agreement with human judges at ~$0.01/judgment
- [[Concepts/Benchmark Contamination|Benchmark Contamination]] (as *Data contamination*) `glossary` — Training data includes benchmark questions, inflating scores without improving real capability
- Eval suite `lesson term` — A versioned collection of (input, expected_output, scorer) triples that measure a specific capability
- Pass rate `lesson term` — Fraction of eval cases scoring above a threshold -- more actionable than mean score because it measures reliability
- Chatbot Arena `lesson term` — LMSYS platform with 2M+ human preference votes, producing the most trusted LLM leaderboard via ELO ratings

## Ships

- [[Artifacts/10-10 prompt-eval-designer|prompt-eval-designer]] `prompt` — Design a custom evaluation suite for any LLM task, including test cases, scoring functions, and pass/fail thresholds
- [[Artifacts/10-10 skill-llm-evaluation|skill-llm-evaluation]] `skill` — Decision framework for choosing the right LLM evaluation strategy based on task type, budget, and requirements

## Further reading

- Hendrycks et al., 2021 -- "Measuring Massive Multitask Language Understanding ([link](https://arxiv.org/abs/2009.03300)) — the MMLU paper, still the most cited LLM benchmark despite its saturation
- Evaluating Large Language Models Trained on Code ([link](https://arxiv.org/abs/2107.03374)) — the HumanEval paper from OpenAI, established code generation evaluation methodology
- [[Resources/Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena|Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]] ([link](https://arxiv.org/abs/2306.05685)) — systematic analysis of using LLMs to evaluate LLMs, including position bias and verbosity bias findings ·  also cited by 2 other lessons
- [[Resources/LMSYS Chatbot Arena|LMSYS Chatbot Arena]] ([link](https://chat.lmsys.org/)) — crowdsourced model comparison platform with 2M+ votes, the most trusted real-world LLM ranking ·  also cited by 2 other lessons

## My route

- Step 10 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Evaluation: benchmarks, LM harness
- Previous: [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
- Next: [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]


%% ── my notes ── %%
