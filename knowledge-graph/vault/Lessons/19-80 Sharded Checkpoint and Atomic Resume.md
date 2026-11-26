---
id: "lesson:19/80"
type: lesson
ref: 19/80
phase: 19
num: 80
title: Sharded Checkpoint and Atomic Resume
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
  - 19/80
  - 19-80
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/80-checkpoint-sharded-resume/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/80-checkpoint-sharded-resume"
---

# 19/80 Sharded Checkpoint and Atomic Resume

> A 70B-parameter training job is paused by a node failure every few hours. The checkpoint format decides whether you lose 30 minutes or 30 hours. A sharded checkpoint writes every rank's shard in parallel and records ownership in a manifest. Resume loads each rank's shard from its own file, reconstructs the state on the same world size, and the optimiser steps as if nothing happened. Atomic write keeps a half-finished checkpoint from poisoning the next resume.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/80-checkpoint-sharded-resume/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/80-checkpoint-sharded-resume) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/80-checkpoint-sharded-resume) · code: main.py · quiz: 6 questions  
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

- [[Concepts/Sharded checkpoint|Sharded checkpoint]] `lesson term` — Each rank writes its own shard file in parallel
- [[Concepts/Manifest|Manifest]] `lesson term` — JSON file recording shard paths, offsets, and sha256
- [[Concepts/Atomic write|Atomic write]] `lesson term` — Write to .tmp then POSIX rename so a crash leaves the previous file live
- Partial write `lesson term` — A crash during write produces a corrupt shard; sha256 catches it
- Rotation `lesson term` — Delete oldest checkpoint before writing new one to bound disk usage

## Further reading

- DeepSpeed checkpointing ([link](https://deepspeed.readthedocs.io/en/latest/model-checkpointing.html))
- POSIX rename atomicity ([link](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html))
- PyTorch torch.distributed.checkpoint ([link](https://pytorch.org/docs/stable/distributed.checkpoint.html))


%% ── my notes ── %%
