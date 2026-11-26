---
id: "lesson:19/62"
type: lesson
ref: 19/62
phase: 19
num: 62
title: Vision-Language Pretraining
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
  - 19/62
  - 19-62
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/62-vision-language-pretraining/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/62-vision-language-pretraining"
---

# 19/62 Vision-Language Pretraining

> The encoder, projection, and decoder are wired. Now train them together. Two objectives drive learning: a contrastive image-text loss (InfoNCE) that pulls matching pairs together in the joint embedding space, and a language modeling loss that asks the decoder to caption each image. Combined, they teach the network both to find the right image for a caption and to write a caption for the image.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/62-vision-language-pretraining/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/62-vision-language-pretraining) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/62-vision-language-pretraining) · code: main.py, test_main.py · quiz: 6 questions  
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

- [[Concepts/InfoNCE|InfoNCE]] `lesson term` — Noise contrastive estimation: cross-entropy on a similarity matrix
- [[Concepts/Temperature|Temperature]] `glossary` — Scalar that controls how peaked the contrastive softmax is
- [[Concepts/Hard negative|Hard negative]] `lesson term` — An off-diagonal pair the model finds confusing, useful for sampling
- LM loss `lesson term` — Standard next-token cross-entropy on the captioning side
- Joint embedding space `lesson term` — The shared space where image and text vectors live after projection


%% ── my notes ── %%
