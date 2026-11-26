---
id: "lesson:19/60"
type: lesson
ref: 19/60
phase: 19
num: 60
title: Projection Layer for Modality Alignment
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 6
prereqs: 8
community: 2
libraries:
  - numpy
  - torch
aliases:
  - 19/60
  - 19-60
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/60-projection-layer-modality-align/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/60-projection-layer-modality-align"
---

# 19/60 Projection Layer for Modality Alignment

> A vision encoder produces image tokens. A text decoder consumes text tokens. The two live in different vector spaces. A small two-layer MLP projects image tokens into the text embedding space, and a cosine alignment loss against a paired caption pulls the two spaces into agreement. That projection is the smallest piece of a vision-language model and the one that matters most for transfer.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/60-projection-layer-modality-align/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/60-projection-layer-modality-align) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/60-projection-layer-modality-align) · code: main.py, test_main.py · quiz: 6 questions  
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

- [[Concepts/Modality Alignment|Modality Alignment]] `glossary` — The act of making image and text embeddings comparable in one shared space
- [[Concepts/Projection head|Projection head]] `lesson term` — The small module that maps one space to another, usually a 2-layer MLP
- [[Concepts/Cosine Similarity|Cosine Similarity]] `glossary` — Dot product divided by the product of L2 norms
- Frozen encoder `lesson term` — The vision (or text) model has all parameters with requires_grad=False
- Mock corpus `lesson term` — Synthetic pairs used so training has no dataset download dependency


%% ── my notes ── %%
