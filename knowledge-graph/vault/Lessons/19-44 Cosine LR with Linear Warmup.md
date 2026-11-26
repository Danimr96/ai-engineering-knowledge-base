---
id: "lesson:19/44"
type: lesson
ref: 19/44
phase: 19
num: 44
title: Cosine LR with Linear Warmup
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 3
concepts: 5
prereqs: 8
community: 2
libraries:
  - torch
aliases:
  - 19/44
  - 19-44
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/44-cosine-lr-warmup/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/44-cosine-lr-warmup"
---

# 19/44 Cosine LR with Linear Warmup

> The learning-rate schedule is the second most important decision after the loss function. AdamW with a cosine decay and a linear warmup is the modern default for language-model training because it lets the model see a small effective step size during the brittle first thousand updates, ramps up to a configured peak, and decays smoothly back toward zero. This lesson builds that schedule, plots the curve over training steps, logs gradient norms next to the schedule, and proves the schedule honors warmup, peak, and decay boundaries.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/44-cosine-lr-warmup/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/44-cosine-lr-warmup) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/44-cosine-lr-warmup) · code: main.py, tests/__init__.py, tests/test_schedule.py · quiz: 6 questions  
**Track:** [[Tracks/19-C Large-scale pre-training infrastructure|Phase 19 Track C: Large-scale pre-training infrastructure]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30-37`

- **19/30-37**:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]]
- [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]
- [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]]
- [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]
- [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- [[Lessons/19-77 Data Parallel DDP From Scratch|19/77 Data Parallel DDP From Scratch]]
- [[Lessons/19-78 ZeRO Optimizer State Sharding|19/78 ZeRO Optimizer State Sharding]]
- [[Lessons/19-79 Pipeline Parallel and Bubble Analysis|19/79 Pipeline Parallel and Bubble Analysis]]
- [[Lessons/19-80 Sharded Checkpoint and Atomic Resume|19/80 Sharded Checkpoint and Atomic Resume]]
- [[Lessons/19-81 End-to-End Distributed Training|19/81 End-to-End Distributed Training]]

## Concepts taught

- [[Concepts/Warmup|Warmup]] `glossary` — Linear ramp from zero to lr_max over the first warmup_steps updates
- Cosine decay `lesson term` — Upper-half cosine curve from lr_max to lr_min over the remaining steps
- Floor `lesson term` — The fixed lr_min value the schedule pins at past total_steps
- Gradient norm `lesson term` — The Euclidean norm of the concatenated gradient vector, logged each step
- Global step `lesson term` — A monotonic step counter that survives restarts and drives the schedule

## Further reading

- SGDR ([link](https://arxiv.org/abs/1608.03983)) — the cosine schedule's reference paper
- Decoupled Weight Decay Regularization ([link](https://arxiv.org/abs/1711.05101)) — AdamW's reference paper
- PyTorch torch.optim.lr_scheduler ([link](https://docs.pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate)) — how step functions compose with framework schedulers


%% ── my notes ── %%
