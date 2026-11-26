---
id: "lesson:04/12"
type: lesson
ref: 04/12
phase: 4
num: 12
title: "Video Understanding — Temporal Modeling"
lesson_type: learn+build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 13
libraries:
  - numpy
  - torch
  - torchvision
aliases:
  - 04/12
  - 04-12
tags:
  - phase/04
  - type/learn+build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/12-video-understanding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/12-video-understanding"
---

# 04/12 Video Understanding — Temporal Modeling

> A video is a sequence of images plus the physics that connects them. Every video model either treats time as an extra axis (3D conv), a sequence to attend over (transformer), or a feature to extract once and pool (2D+pool).

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/12-video-understanding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/12-video-understanding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/12-video-understanding) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]], [[Libraries/torchvision (python)|torchvision]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification)`

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-28 World Models & Video Diffusion|04/28 World Models & Video Diffusion]]

## Concepts taught

- 2D + pool `lesson term` — Run a 2D CNN on every sampled frame, average-pool features across time, classify
- 3D convolution `lesson term` — Kernel that convolves over (T, H, W); can model motion natively
- Inflation `lesson term` — Initialise 3D conv weights by repeating a 2D conv's weights along the new time axis, then divide by kernel_T to preserve activation scale
- (2+1)D `lesson term` — Split 3D into 2D spatial + 1D temporal; fewer parameters, extra non-linearity between
- [[Concepts/Divided attention|Divided attention]] `lesson term` — Transformer block with two attentions per layer: one over tokens at the same frame, one over tokens at the same position
- [[Concepts/Clip|Clip]] `lesson term` — A sampled subsequence of T frames; the unit a video model consumes
- Clip vs video accuracy `lesson term` — Clip = one sample per video, video = average across multiple sampled clips
- Kinetics `lesson term` — 400-700 action classes, 300k+ YouTube clips, the standard video pretraining corpus

## Ships

- [[Artifacts/04-12 prompt-video-architecture-picker|prompt-video-architecture-picker]] `prompt` — Pick 2D+pool / I3D / (2+1)D / spatio-temporal transformer based on appearance-vs-motion, dataset size, and compute budget
- [[Artifacts/04-12 skill-frame-sampler-auditor|skill-frame-sampler-auditor]] `skill` — Audit a video pipeline's frame sampler for off-by-one, short-clip handling, and crop consistency

## Further reading

- I3D: Quo Vadis, Action Recognition (Carreira & Zisserman, 2017) ([link](https://arxiv.org/abs/1705.07750)) — introduces inflation and the Kinetics dataset
- R(2+1)D: A Closer Look at Spatiotemporal Convolutions (Tran et al., 2018) ([link](https://arxiv.org/abs/1711.11248)) — factorised conv, still a strong baseline
- [[Resources/TimeSformer- Is Space-Time Attention All You Need- (Bertasius et al., 2021)|TimeSformer: Is Space-Time Attention All You Need? (Bertasius et al., 2021)]] ([link](https://arxiv.org/abs/2102.05095)) — the first strong video transformer ·  also cited by 1 other lesson
- VideoMAE (Tong et al., 2022) ([link](https://arxiv.org/abs/2203.12602)) — masked autoencoder pretraining for video; current dominant pretraining recipe


%% ── my notes ── %%
