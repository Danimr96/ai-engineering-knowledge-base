---
id: "lesson:04/28"
type: lesson
ref: 04/28
phase: 4
num: 28
title: "World Models & Video Diffusion"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
community: 12
libraries:
  - torch
aliases:
  - 04/28
  - 04-28
tags:
  - phase/04
  - type/learn+build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/28-world-models-video-diffusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/28-world-models-video-diffusion"
---

# 04/28 World Models & Video Diffusion

> A video model that predicts the next seconds of a scene is a world simulator. Condition that prediction on actions and you have a learned game engine.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/28-world-models-video-diffusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/28-world-models-video-diffusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/28-world-models-video-diffusion) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 10 (Diffusion), Phase 4 Lesson 12 (Video Understanding), Phase 4 Lesson 23 (DiT + Rectified Flow)`

- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]] — Diffusion
- [[Lessons/04-12 Video Understanding — Temporal Modeling|04/12 Video Understanding — Temporal Modeling]] — Video Understanding
- [[Lessons/04-23 Diffusion Transformers & Rectified Flow|04/23 Diffusion Transformers & Rectified Flow]] — DiT + Rectified Flow

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Concepts taught

- World model `lesson term` — A model that predicts future observations given state and action
- Video DiT `lesson term` — Diffusion transformer with 3D patchification and divided attention
- Latent action `lesson term` — Discrete or continuous action latent inferred from frame pairs; used to condition next-frame generation
- [[Concepts/Divided attention|Divided attention]] `lesson term` — Two attention operations per block — across time then across space — to keep O(N^2) manageable
- Object permanence `lesson term` — Scene property that video models must learn; classic failure mode on food, glassware
- FVD `lesson term` — Video equivalent of FID; primary visual quality metric
- Inverse dynamics model `lesson term` — Given (state, next state), output the action that connects them; closes robotics loop
- Cosmos-Drive `lesson term` — Open-weights autonomous-driving world model for RL and evaluation

## Ships

- [[Artifacts/04-28 prompt-video-model-picker|prompt-video-model-picker]] `prompt` — Pick Sora 2 / Runway Gen-5 / Wan-Video / HunyuanVideo / Cosmos for a given task, license, and latency target
- [[Artifacts/04-28 skill-physical-plausibility-checks|skill-physical-plausibility-checks]] `skill` — Automated checks for object permanence, gravity, and continuity on any generated video before shipping

## Further reading

- [[Resources/TimeSformer- Is Space-Time Attention All You Need- (Bertasius et al., 2021)|TimeSformer: Is Space-Time Attention All You Need? (Bertasius et al., 2021)]] ([link](https://arxiv.org/abs/2102.05095)) — divided attention for video transformers ·  also cited by 1 other lesson
- DreamerV3 (Hafner et al., 2023) ([link](https://arxiv.org/abs/2301.04104)) — world models for RL
- Genie: Generative Interactive Environments (Bruce et al., 2024) ([link](https://arxiv.org/abs/2402.15391)) — latent action world models
- Top 10 Video Generation Models 2026 (DataCamp) ([link](https://www.datacamp.com/blog/top-video-generation-models))
- From Video Generation to World Model — survey repo ([link](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model/))
- [[Resources/Sora technical report (OpenAI)|Sora technical report (OpenAI)]] ([link](https://openai.com/index/video-generation-models-as-world-simulators/)) ·  also cited by 1 other lesson
- Cosmos-Drive-Dreams (NVIDIA, 2025) ([link](https://research.nvidia.com/labs/toronto-ai/cosmos-drive-dreams/)) — driving world model


%% ── my notes ── %%
