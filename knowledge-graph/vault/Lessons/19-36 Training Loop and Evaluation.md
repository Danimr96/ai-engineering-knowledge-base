---
id: "lesson:19/36"
type: lesson
ref: 19/36
phase: 19
num: 36
title: Training Loop and Evaluation
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 6
community: 2
libraries:
  - torch
aliases:
  - 19/36
  - 19-36
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/36-training-loop-eval/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/36-training-loop-eval"
---

# 19/36 Training Loop and Evaluation

> A loop that does not measure is a loop that lies. This lesson builds the training loop that drives the GPT model: AdamW with weight decay split, a warmup plus cosine learning rate schedule, a `calc_loss_batch` helper, an `evaluate_model` pass on held out data, a `generate_and_print_sample` qualitative probe every K steps, and a JSONL log of losses you can plot after. The same skeleton trains every decoder LLM you will ever build.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/36-training-loop-eval/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/36-training-loop-eval) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/36-training-loop-eval) · code: main.py, tests/test_training.py · quiz: 6 questions  
**Track:** [[Tracks/19-B GPT from scratch in PyTorch|Phase 19 Track B: GPT from scratch in PyTorch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30 to 35`

- **19/30-35**:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]

## Builds on this

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

- Loss alignment `lesson term` — Input tokens at positions 0..T-1, target tokens at positions 1..T; cross entropy is computed on flattened shapes
- Decay split `lesson term` — AdamW receives matrix shaped tensors with weight decay and scale or bias tensors with none
- [[Concepts/Warmup|Warmup]] `glossary` — The learning rate climbs from zero to its target over a fixed number of steps so the optimizer state can populate
- Eval batches `lesson term` — A fixed slice of the validation token tensor, sliced once at script start, used identically every probe
- Qualitative probe `lesson term` — A short generation from a fixed prompt printed every K steps to catch failure modes loss alone hides


%% ── my notes ── %%
