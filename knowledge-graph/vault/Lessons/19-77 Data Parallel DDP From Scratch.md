---
id: "lesson:19/77"
type: lesson
ref: 19/77
phase: 19
num: 77
title: Data Parallel DDP From Scratch
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
  - 19/77
  - 19-77
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/77-data-parallel-ddp/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/77-data-parallel-ddp"
---

# 19/77 Data Parallel DDP From Scratch

> DistributedDataParallel is a hook on top of allreduce. Wrap a model, broadcast the initial parameters from rank 0 so every rank starts identical, install a backward hook on every parameter that issues an allreduce of the gradient, and the rest is gradient descent. The whole pattern is 200 lines.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/77-data-parallel-ddp/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/77-data-parallel-ddp) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/77-data-parallel-ddp) · code: main.py · quiz: 6 questions  
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

- DDP `lesson term` — Wrapper that broadcasts params and allreduces grads each step
- [[Concepts/Bucket|Bucket]] `lesson term` — Group N small allreduces into one large one
- [[Concepts/Overlap|Overlap]] `lesson term` — Issue allreduce while later layers still computing backward
- no_sync `lesson term` — Skip the post-backward allreduce for gradient accumulation
- find_unused `lesson term` — Detect parameters with no grad before reducing

## Further reading

- Li et al, PyTorch Distributed: Experiences on Accelerating Data Parallel Training ([link](https://arxiv.org/abs/2006.15704))
- PyTorch DistributedDataParallel docs ([link](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html))
- PyTorch DDP internals tutorial ([link](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html))


%% ── my notes ── %%
