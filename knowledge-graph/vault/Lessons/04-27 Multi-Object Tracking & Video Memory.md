---
id: "lesson:04/27"
type: lesson
ref: 04/27
phase: 4
num: 27
title: "Multi-Object Tracking & Video Memory"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
community: 13
libraries:
  - numpy
  - scipy
aliases:
  - 04/27
  - 04-27
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/27-multi-object-tracking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/27-multi-object-tracking"
---

# 04/27 Multi-Object Tracking & Video Memory

> Tracking is detection plus association. Detect every frame. Match this frame's detections to last frame's tracks by ID.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/27-multi-object-tracking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/27-multi-object-tracking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/27-multi-object-tracking) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/scipy (python)|scipy]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 06 (YOLO Detection), Phase 4 Lesson 08 (Mask R-CNN), Phase 4 Lesson 24 (SAM 3)`

- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]] — YOLO Detection
- [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]] — Mask R-CNN
- [[Lessons/04-24 SAM 3 & Open-Vocabulary Segmentation|04/24 SAM 3 & Open-Vocabulary Segmentation]] — SAM 3

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]]

## Concepts taught

- Tracking-by-detection `lesson term` — Per-frame detector + Hungarian assignment on IoU / appearance
- Kalman filter `lesson term` — Linear dynamics + covariance for smooth track predictions and occlusion handling
- Hungarian algorithm `lesson term` — Solves the minimum-cost bipartite matching problem; scipy.optimize.linear_sum_assignment
- ByteTrack `lesson term` — Re-match unmatched tracks to low-confidence detections to recover short occlusions
- DeepSORT `lesson term` — Adds a ReID feature for cross-frame matching; better for ID preservation
- Memory bank `lesson term` — Per-instance spatio-temporal features stored across frames; cross-attention replaces explicit association
- [[Concepts/Object Multiplex|Object Multiplex]] `lesson term` — Single shared memory with per-instance queries for fast many-object tracking
- HOTA `lesson term` — Decomposes into detection and association accuracy; community standard

## Ships

- [[Artifacts/04-27 prompt-tracker-picker|prompt-tracker-picker]] `prompt` — Pick SORT / ByteTrack / BoT-SORT / SAM 2 / SAM 3.1 given scene type, occlusion patterns, and latency budget
- [[Artifacts/04-27 skill-mot-evaluator|skill-mot-evaluator]] `skill` — Write a complete evaluation harness for MOTA / IDF1 / HOTA against ground-truth tracks

## Further reading

- [[Resources/SAM 3.1 Object Multiplex (Meta AI, March 2026)|SAM 3.1 Object Multiplex (Meta AI, March 2026)]] ([link](https://ai.meta.com/blog/segment-anything-model-3/)) ·  also cited by 1 other lesson
- SAM 2 video segmentation (Meta, 2024) ([link](https://ai.meta.com/sam2/)) — memory-based tracker
- SORT (Bewley et al., 2016) ([link](https://arxiv.org/abs/1602.00763)) — the minimal tracking-by-detection paper
- DeepSORT (Wojke et al., 2017) ([link](https://arxiv.org/abs/1703.07402)) — adds appearance feature
- HOTA (Luiten et al., 2020) ([link](https://arxiv.org/abs/2009.07736)) — decomposed tracking metric
- ByteTrack (Zhang et al., 2022) ([link](https://arxiv.org/abs/2110.06864)) — low-confidence second pass
- BoT-SORT (Aharon et al., 2022) ([link](https://arxiv.org/abs/2206.14651)) — camera motion compensation


%% ── my notes ── %%
