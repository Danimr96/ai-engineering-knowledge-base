---
id: "lesson:19/45"
type: lesson
ref: 19/45
phase: 19
num: 45
title: Gradient Clipping and Mixed Precision
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
  - 19/45
  - 19-45
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/45-gradient-clipping-amp/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/45-gradient-clipping-amp"
---

# 19/45 Gradient Clipping and Mixed Precision

> The optimizer and schedule from the previous lesson assume gradients are sane. They usually are not. A single bad batch can spike the gradient norm by three orders of magnitude. Mixed-precision training amplifies this by introducing FP16 overflow on the loss side. This lesson builds the two safety belts that production training cannot ship without: gradient clipping to a configured global L2 norm, and a mixed-precision loop with autocast and GradScaler that detects NaN and Inf, skips the step cleanly, and logs the scaling factor for forensics.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/45-gradient-clipping-amp/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/45-gradient-clipping-amp) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/45-gradient-clipping-amp) · code: main.py, tests/__init__.py, tests/test_amp.py · quiz: 6 questions  
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

- Global L2 norm `lesson term` — Euclidean norm of the concatenated gradient vector across all trainable parameters
- autocast `lesson term` — Selective FP16 (or BF16) execution of eligible operations inside a with block
- GradScaler `lesson term` — Helper that multiplies the loss before backward and inverse-scales gradients before the optimizer step
- Skip `lesson term` — An optimizer step refused because the gradient or loss was non-finite; the scaler halves the factor
- Scaling factor `lesson term` — The GradScaler's current multiplier; doubles after clean stretches and halves on every skip

## Further reading

- On the difficulty of training recurrent neural networks ([link](https://arxiv.org/abs/1211.5063)) — the gradient-clipping reference paper
- [[Resources/Mixed Precision Training (Micikevicius et al., 2018)|Mixed Precision Training (Micikevicius et al., 2018)]] ([link](https://arxiv.org/abs/1710.03740)) — the original loss-scaling proposal ·  also cited by 1 other lesson
- PyTorch torch.amp.GradScaler ([link](https://docs.pytorch.org/docs/stable/amp.html)) — the scaler API this lesson wraps
- PyTorch torch.nn.utils.clip_grad_norm_ ([link](https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html)) — the clipping primitive this lesson uses


%% ── my notes ── %%
