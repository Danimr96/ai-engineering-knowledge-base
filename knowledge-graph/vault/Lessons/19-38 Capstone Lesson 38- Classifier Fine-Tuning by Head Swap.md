---
id: "lesson:19/38"
type: lesson
ref: 19/38
phase: 19
num: 38
title: "Capstone Lesson 38: Classifier Fine-Tuning by Head Swap"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 8
community: 2
libraries:
  - numpy
  - torch
aliases:
  - 19/38
  - 19-38
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/38-classifier-finetuning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/38-classifier-finetuning"
---

# 19/38 Capstone Lesson 38: Classifier Fine-Tuning by Head Swap

> Track B's first capstone. A pretrained language model is a stack of self-attention blocks ending in a token-prediction head. When you want spam vs ham, the head is wrong but the body is mostly right. This lesson rips the head off, glues a two-class linear layer onto the pooled representation, and trains the classifier two different ways: final-layer only, and full fine-tuning. The eval is precision, recall, and F1 on a held-out split. You learn what each strategy buys you and what it costs.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/38-classifier-finetuning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/38-classifier-finetuning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/38-classifier-finetuning) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-B GPT from scratch in PyTorch|Phase 19 Track B: GPT from scratch in PyTorch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30-37 (NLP LLM track: tokenizer, embedding table, attention block, transformer body, pre-training loop, checkpointing, generation, perplexity)`

- **19/30-37** — NLP LLM track: tokenizer, embedding table, attention block, transformer body, pre-training loop, checkpointing, generation, perplexity:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]
    - [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/19-70 Task Spec Format|19/70 Task Spec Format]]
- [[Lessons/19-71 Classical Metrics|19/71 Classical Metrics]]
- [[Lessons/19-72 Code Exec Metric|19/72 Code Exec Metric]]
- [[Lessons/19-73 Perplexity and Calibration|19/73 Perplexity and Calibration]]
- [[Lessons/19-74 Leaderboard Aggregation|19/74 Leaderboard Aggregation]]
- [[Lessons/19-75 End-to-End Eval Runner|19/75 End-to-End Eval Runner]]


%% ── my notes ── %%
