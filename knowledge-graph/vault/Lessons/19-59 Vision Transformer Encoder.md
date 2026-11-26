---
id: "lesson:19/59"
type: lesson
ref: 19/59
phase: 19
num: 59
title: Vision Transformer Encoder
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 8
community: 2
libraries:
  - numpy
  - torch
aliases:
  - 19/59
  - 19-59
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/59-vit-transformer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/59-vit-transformer"
---

# 19/59 Vision Transformer Encoder

> Patches alone do not see. A 12-layer pre-LN transformer with 12 attention heads turns the sequence of patch tokens into a sequence of contextual tokens, with the CLS token pooling whole-image features in its final hidden state. This lesson is the engine room of every modern vision-language model.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/59-vit-transformer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/59-vit-transformer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/59-vit-transformer) · code: main.py, test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-E Vision-language model from scratch|Phase 19 Track E: Vision-language model from scratch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30-37 (Track B foundations)`

- **19/30-37** — Track B foundations:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-63 Multimodal Evaluation|19/63 Multimodal Evaluation]]

## Concepts taught

- [[Concepts/Pre-LN|Pre-LN]] `lesson term` — LayerNorm applied before each sub-layer instead of after
- [[Concepts/Self-Attention|Self-Attention]] `glossary` — Each token attends to every other token in the same sequence
- Multi-head `lesson term` — The hidden dim is split across H independent attention heads
- [[Concepts/FFN expansion|FFN expansion]] `lesson term` — The feed-forward layer widens to 4 hidden before contracting
- CLS pooling `lesson term` — Use the first token's final hidden state as the image summary


%% ── my notes ── %%
