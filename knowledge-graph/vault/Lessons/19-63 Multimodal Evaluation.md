---
id: "lesson:19/63"
type: lesson
ref: 19/63
phase: 19
num: 63
title: Multimodal Evaluation
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 5
community: 2
libraries:
  - numpy
  - torch
aliases:
  - 19/63
  - 19-63
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/63-multimodal-eval/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/63-multimodal-eval"
---

# 19/63 Multimodal Evaluation

> Training is half the loop. The other half is measurement. This lesson builds three evaluation surfaces from primitives: image-caption retrieval reported as R@1, R@5, R@10; visual question answering reported as exact match accuracy; and image captioning reported as BLEU-4. Each metric is a function over the model's outputs and a synthetic eval suite that runs in seconds.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/63-multimodal-eval/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/63-multimodal-eval) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/63-multimodal-eval) · code: main.py, test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-E Vision-language model from scratch|Phase 19 Track E: Vision-language model from scratch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 58-62 (Track E foundations: encoder, transformer, projection, cross-attention fusion, pretraining)`

- **19/58-62** — Track E foundations: encoder, transformer, projection, cross-attention fusion, pretraining:
    - [[Lessons/19-58 Vision Encoder Patches|19/58 Vision Encoder Patches]]
    - [[Lessons/19-59 Vision Transformer Encoder|19/59 Vision Transformer Encoder]]
    - [[Lessons/19-60 Projection Layer for Modality Alignment|19/60 Projection Layer for Modality Alignment]]
    - [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]]
    - [[Lessons/19-62 Vision-Language Pretraining|19/62 Vision-Language Pretraining]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]], [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]], [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]], [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]], [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]], [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]], [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]], [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Concepts taught

- R@K `lesson term` — Fraction of queries where the correct match lands in the top K results
- [[Concepts/Exact Match (EM)|Exact Match (EM)]] (as *Exact match*) `glossary` — The simplest VQA scoring: predicted answer equals reference
- BLEU-4 `lesson term` — Geometric mean of 1- to 4-gram precisions, with brevity penalty
- Multi-reference `lesson term` — A captioning metric accepts several reference captions per image
- Held-out `lesson term` — The eval set is sampled from a seed disjoint from the training corpus


%% ── my notes ── %%
