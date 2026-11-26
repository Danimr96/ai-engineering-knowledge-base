---
id: "lesson:19/78"
type: lesson
ref: 19/78
phase: 19
num: 78
title: ZeRO Optimizer State Sharding
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
  - 19/78
  - 19-78
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/78-zero-parameter-sharding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/78-zero-parameter-sharding"
---

# 19/78 ZeRO Optimizer State Sharding

> Adam stores two moment estimates per parameter, both in float32. A 7B-parameter model carries 56 GB of optimiser state. ZeRO stage 1 shards that across N ranks; each rank owns 1/N of the optimiser. After the local step the updated parameter shards broadcast back, every rank reconstructs the full model, and the next step begins. The win is a linear memory drop on the largest single allocation in the training stack.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/78-zero-parameter-sharding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/78-zero-parameter-sharding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/78-zero-parameter-sharding) · code: main.py · quiz: 6 questions  
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

- ZeRO-1 `lesson term` — Each rank holds 1/N of fp32 master + Adam moments
- ZeRO-2 `lesson term` — Each rank also drops the non-shard gradients after reduce_scatter
- ZeRO-3 `lesson term` — Each rank holds 1/N of fp16 params; allgather per layer in forward
- Master copy `lesson term` — The high-precision parameter copy the optimiser updates
- [[Concepts/Reduce-scatter|Reduce-scatter]] (as *Reduce_scatter*) `lesson term` — Deliver each rank only its shard's summed gradient

## Further reading

- [[Resources/Rajbhandari et al., 2020 - -ZeRO- Memory Optimizations Toward Training Trillion Parameter Models|Rajbhandari et al., 2020 -- "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models]] ([link](https://arxiv.org/abs/1910.02054)) ·  also cited by 1 other lesson
- DeepSpeed ZeRO documentation ([link](https://www.deepspeed.ai/tutorials/zero/))
- [[Resources/PyTorch FSDP2 documentation|PyTorch FSDP2 documentation]] ([link](https://pytorch.org/docs/stable/fsdp.html)) ·  also cited by 1 other lesson


%% ── my notes ── %%
