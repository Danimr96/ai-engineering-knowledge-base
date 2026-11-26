---
id: "lesson:19/33"
type: lesson
ref: 19/33
phase: 19
num: 33
title: Multi-Head Self-Attention
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 3
community: 2
libraries:
  - torch
aliases:
  - 19/33
  - 19-33
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/33-multihead-self-attention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/33-multihead-self-attention"
---

# 19/33 Multi-Head Self-Attention

> One linear projection, three views, H parallel heads, one mask. The attention block as the model actually uses it.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/33-multihead-self-attention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/33-multihead-self-attention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/33-multihead-self-attention) · code: main.py, tests/test_attention.py · quiz: 6 questions  
**Track:** [[Tracks/19-B GPT from scratch in PyTorch|Phase 19 Track B: GPT from scratch in PyTorch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 04 lessons, Phase 07 transformer lessons, Lessons 30 through 32 of this phase`

- **19/30-32**:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
- Whole phase: [[Phases/04 Computer Vision|Phase 4: Computer Vision]] ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] ·  medium confidence

## Builds on this

- [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
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


%% ── my notes ── %%
