---
id: "lesson:19/34"
type: lesson
ref: 19/34
phase: 19
num: 34
title: Transformer Block from Scratch
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 4
community: 2
libraries:
  - torch
aliases:
  - 19/34
  - 19-34
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/34-transformer-block/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/34-transformer-block"
---

# 19/34 Transformer Block from Scratch

> One block is the unit of every modern decoder LLM. Layer norm, multi head attention, residual, MLP, residual. The pre-LN variant trains stably without warmup. The post-LN variant is what the original paper shipped. This lesson builds both, side by side, and shows which one survives a 12 layer stack at common learning rates.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/34-transformer-block/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/34-transformer-block) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/34-transformer-block) · code: main.py, tests/test_block.py · quiz: 6 questions  
**Track:** [[Tracks/19-B GPT from scratch in PyTorch|Phase 19 Track B: GPT from scratch in PyTorch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30 to 33 (tokenizer, embeddings, attention math, batched data loader)`

- **19/30-33** — tokenizer, embeddings, attention math, batched data loader:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]

## Builds on this

- [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
- [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
- [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]
- [[Lessons/19-38 Capstone Lesson 38- Classifier Fine-Tuning by Head Swap|19/38 Capstone Lesson 38: Classifier Fine-Tuning by Head Swap]]
- [[Lessons/19-39 Capstone Lesson 39- Instruction Tuning by Supervised Fine-Tuning|19/39 Capstone Lesson 39: Instruction Tuning by Supervised Fine-Tuning]]
- [[Lessons/19-40 Capstone Lesson 40- Direct Preference Optimization from Scratch|19/40 Capstone Lesson 40: Direct Preference Optimization from Scratch]]
- [[Lessons/19-41 Capstone Lesson 41- Full Evaluation Pipeline|19/41 Capstone Lesson 41: Full Evaluation Pipeline]]
- [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]]
- [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]]
- [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]]
- [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]]
- [[Lessons/19-58 Vision Encoder Patches|19/58 Vision Encoder Patches]]
- [[Lessons/19-59 Vision Transformer Encoder|19/59 Vision Transformer Encoder]]
- [[Lessons/19-60 Projection Layer for Modality Alignment|19/60 Projection Layer for Modality Alignment]]
- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]]
- [[Lessons/19-62 Vision-Language Pretraining|19/62 Vision-Language Pretraining]]
- [[Lessons/19-70 Task Spec Format|19/70 Task Spec Format]]
- [[Lessons/19-71 Classical Metrics|19/71 Classical Metrics]]
- [[Lessons/19-72 Code Exec Metric|19/72 Code Exec Metric]]
- [[Lessons/19-73 Perplexity and Calibration|19/73 Perplexity and Calibration]]
- [[Lessons/19-74 Leaderboard Aggregation|19/74 Leaderboard Aggregation]]
- [[Lessons/19-75 End-to-End Eval Runner|19/75 End-to-End Eval Runner]]

## Concepts taught

- [[Concepts/Pre-LN|Pre-LN]] `lesson term` — LayerNorm inside the residual branch, before each sublayer; the residual carries the unnormalized signal
- Post-LN `lesson term` — LayerNorm after the residual add; what the 2017 paper shipped and what needs warmup
- [[Concepts/Causal mask|Causal mask]] `lesson term` — The upper triangle of the attention logits set to negative infinity so token i cannot read token j when j is greater than i
- Fused QKV `lesson term` — One linear of width 3D instead of three linears of width D; one kernel, one matmul
- Residual stream `lesson term` — The unnormalized tensor that flows top to bottom through every block; what each block adds to


%% ── my notes ── %%
