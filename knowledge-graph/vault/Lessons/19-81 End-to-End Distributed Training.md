---
id: "lesson:19/81"
type: lesson
ref: 19/81
phase: 19
num: 81
title: End-to-End Distributed Training
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 1
concepts: 4
prereqs: 8
community: 2
libraries:
  - torch
aliases:
  - 19/81
  - 19-81
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/81-end-to-end-distributed-train/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/81-end-to-end-distributed-train"
---

# 19/81 End-to-End Distributed Training

> Lessons 76 through 80 each built one piece. This is the assembly: a tiny GPT trained across 4 simulated ranks with DDP for gradient sync, ZeRO-1 for optimiser-state sharding, and a sharded checkpoint at the halfway mark. The demo runs 20 steps, self-terminates, prints a loss curve plus a memory profile, and writes a resumable checkpoint.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/81-end-to-end-distributed-train/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/81-end-to-end-distributed-train) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/81-end-to-end-distributed-train) · code: main.py · quiz: 6 questions  
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

- [[Concepts/End-to-end|End-to-end]] `lesson term` — One run composes every piece, not a unit test per piece
- Memory profile `lesson term` — Bytes held on each rank for params, grads, optimiser state
- Resume contract `lesson term` — Per-rank state byte-equal after a checkpoint round-trip
- Self-terminating `lesson term` — Fixed step count, exit 0 on completion, no human in the loop

## Further reading

- DeepSpeed end-to-end training tutorial ([link](https://www.deepspeed.ai/getting-started/))
- [[Resources/Megatron-LM pipeline parallel docs|Megatron-LM pipeline parallel docs]] ([link](https://github.com/NVIDIA/Megatron-LM)) ·  also cited by 1 other lesson
- PyTorch FSDP advanced tutorial ([link](https://pytorch.org/tutorials/intermediate/FSDP_advanced_tutorial.html))


%% ── my notes ── %%
