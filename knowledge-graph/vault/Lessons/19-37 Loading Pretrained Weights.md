---
id: "lesson:19/37"
type: lesson
ref: 19/37
phase: 19
num: 37
title: Loading Pretrained Weights
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 7
community: 2
libraries:
  - safetensors
  - torch
aliases:
  - 19/37
  - 19-37
tags:
  - phase/19
  - type/build
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/37-loading-pretrained-weights/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/37-loading-pretrained-weights"
---

# 19/37 Loading Pretrained Weights

> Training a 124 million parameter model from scratch is a budget decision; loading a published checkpoint is a Tuesday. This lesson loads pretrained GPT-2 style weights from a safetensors file into the exact architecture from lesson 35, walks the parameter name mapping piece by piece, and sanity generates a continuation to prove the load worked. No network, no third party loaders, no opaque magic.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/37-loading-pretrained-weights/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/37-loading-pretrained-weights) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/37-loading-pretrained-weights) · code: main.py, tests/test_load.py · quiz: 6 questions  
**Track:** [[Tracks/19-B GPT from scratch in PyTorch|Phase 19 Track B: GPT from scratch in PyTorch]]  
**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]] · **Libraries:** [[Libraries/safetensors (python)|safetensors]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 19 lessons 30 to 36`

- **19/30-36**:
    - [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]]
    - [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]]
    - [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]]
    - [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]]
    - [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]]
    - [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]]
    - [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]]

## Builds on this

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

- Name map `lesson term` — The function from pretrained tensor names to local parameter names; usually a literal dict with one entry per layer index expanded over a loop
- Shape mismatch `lesson term` — The pretrained tensor exists under the mapped name but its dimensions disagree with the local parameter; the loader refuses to assign and logs the pair
- Transpose-on-load `lesson term` — Published GPT-2 stores attention and MLP projections in the transpose of what nn.Linear expects; the loader transposes during assignment
- Weight tying alias `lesson term` — Setting model.lm_head.weight = model.tok_embed.weight so the head and embedding share storage; the head is not in the file because of this
- Load report `lesson term` — A small dataclass that tracks loaded, missing, unexpected, and shape_mismatch lists; printing it is how you tell whether the load succeeded


%% ── my notes ── %%
