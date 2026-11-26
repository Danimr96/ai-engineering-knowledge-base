---
id: "lesson:19/79"
type: lesson
ref: 19/79
phase: 19
num: 79
title: Pipeline Parallel and Bubble Analysis
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 1
concepts: 5
prereqs: 8
community: 2
libraries:
  - torch
aliases:
  - 19/79
  - 19-79
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/79-pipeline-parallel/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/79-pipeline-parallel"
---

# 19/79 Pipeline Parallel and Bubble Analysis

> Tensor parallelism splits the matrix multiply across ranks. Pipeline parallelism splits the model across ranks, one stage per rank. Microbatches flow through the pipeline. The empty time at the start and end is the bubble; minimising it is the whole craft.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/79-pipeline-parallel/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/79-pipeline-parallel) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/79-pipeline-parallel) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 Track C lessons 42-49`

- **19/42-49**:
    - [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]]
    - [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]]
    - [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]]
    - [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]]
    - [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]]
    - [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]
    - [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]]
    - [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]], [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]], [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]], [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]], [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]], [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]], [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]], [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Concepts taught

- [[Concepts/Pipeline|Pipeline]] `lesson term` — One stage per rank, activations flow stage to stage
- Bubble `lesson term` — (N-1) steps at start + end where some stages have no work
- Microbatch `lesson term` — One forward/backward unit; bubble shrinks as M grows
- GPipe `lesson term` — All M forwards before any backward; high activation memory
- [[Concepts/1F1B|1F1B]] `lesson term` — One forward one backward per stage; bounded activation memory

## Further reading

- [[Resources/Narayanan et al. — PipeDream - 1F1B (arXiv-1806.03377, 2018-2021)|Narayanan et al. — PipeDream / 1F1B (arXiv:1806.03377, 2018-2021)]] ([link](https://arxiv.org/abs/1806.03377)) ·  also cited by 1 other lesson
- [[Resources/GPipe|GPipe]] ([link](https://arxiv.org/abs/1811.06965)) ·  also cited by 1 other lesson
- [[Resources/Megatron-LM pipeline parallel docs|Megatron-LM pipeline parallel docs]] ([link](https://github.com/NVIDIA/Megatron-LM)) ·  also cited by 1 other lesson


%% ── my notes ── %%
