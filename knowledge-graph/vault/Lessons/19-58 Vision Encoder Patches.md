---
id: "lesson:19/58"
type: lesson
ref: 19/58
phase: 19
num: 58
title: Vision Encoder Patches
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
  - 19/58
  - 19-58
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/58-vision-encoder-patches/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/58-vision-encoder-patches"
---

# 19/58 Vision Encoder Patches

> A vision model that reads pixels needs a tokenizer for pixels. Patch embedding is that tokenizer. Cut the image into a grid of squares, flatten each square, project it through one linear layer, then add a 2D position signal so the transformer knows where each square sat in the original image.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/58-vision-encoder-patches/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/58-vision-encoder-patches) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/58-vision-encoder-patches) · code: main.py, test_main.py · quiz: 6 questions  
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

- [[Concepts/Patch|Patch]] `glossary` — A square sub-region of the image, typically 14x14 or 16x16
- [[Concepts/Patch Embedding|Patch Embedding]] `glossary` — Linear projection of one flattened patch to the hidden dim
- Sequence length `lesson term` — Number of tokens after patch tokenization, usually plus CLS
- Sinusoidal position `lesson term` — Fixed sin/cos signal that encodes 2D grid coordinates
- [[Concepts/CLS- token|[CLS] token]] (as *CLS token*) `lesson term` — Learned vector prepended to the sequence as the pooling head


%% ── my notes ── %%
