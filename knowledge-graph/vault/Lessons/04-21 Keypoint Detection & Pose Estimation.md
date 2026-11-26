---
id: "lesson:04/21"
type: lesson
ref: 04/21
phase: 4
num: 21
title: "Keypoint Detection & Pose Estimation"
lesson_type: build
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
aliases:
  - 04/21
  - 04-21
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/21-keypoint-pose/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/21-keypoint-pose"
---

# 04/21 Keypoint Detection & Pose Estimation

> A pose is a set of ordered keypoints. A keypoint detector is a heatmap regressor. Everything else is bookkeeping.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/21-keypoint-pose/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/21-keypoint-pose) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/21-keypoint-pose) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 06 (Detection), Phase 4 Lesson 07 (U-Net)`

- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]] — Detection
- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]] — U-Net

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]

## Concepts taught

- Keypoint `lesson term` — A specific ordered point on an object (joint, corner, feature)
- Pose `lesson term` — An ordered set of keypoints belonging to one instance
- Top-down `lesson term` — Two-stage pipeline: person detector + per-crop keypoint model; highest accuracy
- Bottom-up `lesson term` — Single-pass all-keypoint prediction + grouping; constant time in crowd size
- Heatmap `lesson term` — H x W tensor per keypoint with peak at the true location; the preferred regression target
- PAF `lesson term` — 2-channel unit vector field encoding limb directions; used to group keypoints into instances
- OKS `lesson term` — Object Keypoint Similarity; the COCO metric for pose
- HRNet `lesson term` — The dominant top-down keypoint architecture; preserves high-res features throughout

## Ships

- [[Artifacts/04-21 prompt-pose-stack-picker|prompt-pose-stack-picker]] `prompt` — Pick MediaPipe / YOLOv8-pose / HRNet / ViTPose given latency, crowd size, and 2D vs 3D need
- [[Artifacts/04-21 skill-heatmap-to-coords|skill-heatmap-to-coords]] `skill` — Write the sub-pixel heatmap-to-coordinate routine used by every production pose model

## Further reading

- OpenPose (Cao et al., 2017) ([link](https://arxiv.org/abs/1812.08008)) — bottom-up with PAFs; still the best writeup of the approach
- HRNet (Sun et al., 2019) ([link](https://arxiv.org/abs/1902.09212)) — the top-down reference architecture
- ViTPose (Xu et al., 2022) ([link](https://arxiv.org/abs/2204.12484)) — plain ViT as a pose backbone; current SOTA on many benchmarks
- MediaPipe Pose ([link](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker)) — production real-time pose; the fastest deployed stack in 2026


%% ── my notes ── %%
