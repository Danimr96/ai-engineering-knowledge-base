---
id: "lesson:04/26"
type: lesson
ref: 04/26
phase: 4
num: 26
title: "Monocular Depth & Geometry Estimation"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
libraries:
  - numpy
  - torch
aliases:
  - 04/26
  - 04-26
tags:
  - phase/04
  - type/build
source: ai-engineering-from-scratch/phases/04-computer-vision/26-monocular-depth/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/26-monocular-depth"
---

# 04/26 Monocular Depth & Geometry Estimation

> A depth map is a single-channel image where each pixel is a distance from the camera. Predicting it from one RGB frame used to be impossible without stereo or LiDAR. In 2026 a frozen ViT encoder plus a lightweight head gets within a few percent of ground truth.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build + Use · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/26-monocular-depth/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/26-monocular-depth) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/26-monocular-depth) · code: main.py · quiz: 5 questions  
**Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 14 (ViT), Phase 4 Lesson 17 (Self-Supervised Vision), Phase 4 Lesson 07 (U-Net)`

- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]] — U-Net
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]] — Self-Supervised Vision

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Concepts taught

- Monocular depth `lesson term` — Depth estimation from one RGB frame, no stereo or LiDAR
- Relative depth `lesson term` — Ordered z-values without real-world units
- Metric depth `lesson term` — Depth in metres; requires calibration or a model trained with metric supervision
- AbsRel `lesson term` — / d_gt; standard depth metric
- Delta accuracy `lesson term` — Fraction of pixels with prediction within 25% of ground truth
- Pinhole camera `lesson term` — The camera model used to lift (u, v, d) to (X, Y, Z)
- DPT `lesson term` — The conv-based decoder used on top of frozen ViT encoders for depth
- DINOv2 backbone `lesson term` — Self-supervised features that generalise across domains without depth labels

## Ships

- [[Artifacts/04-26 prompt-depth-model-picker|prompt-depth-model-picker]] `prompt` — Pick Depth Anything V3 / Marigold / UniDepth / MiDaS given latency, metric-vs-relative need, and scene type
- [[Artifacts/04-26 skill-depth-to-pointcloud|skill-depth-to-pointcloud]] `skill` — Build point clouds from depth maps with correct intrinsics handling and export to .ply

## Further reading

- DINOv3 blog post (Meta) ([link](https://ai.meta.com/blog/dinov3-self-supervised-vision-model/)) — the encoder family that lifts depth accuracy
- UniDepth (Piccinelli et al., 2024) ([link](https://arxiv.org/abs/2403.18913)) — metric depth with intrinsics
- Depth Anything V3 paper page ([link](https://depth-anything.github.io/)) — SOTA monocular depth with DINOv2 encoder
- MiDaS v3.1 (Intel ISL) ([link](https://github.com/isl-org/MiDaS)) — the canonical relative-depth baseline
- Marigold (Ke et al., CVPR 2024) ([link](https://marigoldmonodepth.github.io/)) — diffusion-based depth estimation


%% ── my notes ── %%
