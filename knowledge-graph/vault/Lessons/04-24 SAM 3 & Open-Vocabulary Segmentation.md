---
id: "lesson:04/24"
type: lesson
ref: 04/24
phase: 4
num: 24
title: "SAM 3 & Open-Vocabulary Segmentation"
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
aliases:
  - 04/24
  - 04-24
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/24-sam3-open-vocab-segmentation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/24-sam3-open-vocab-segmentation"
---

# 04/24 SAM 3 & Open-Vocabulary Segmentation

> Give a model a text prompt and an image and get masks for every matching object. SAM 3 made that a single forward pass.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Use + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/24-sam3-open-vocab-segmentation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/24-sam3-open-vocab-segmentation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/24-sam3-open-vocab-segmentation) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 07 (U-Net), Phase 4 Lesson 08 (Mask R-CNN), Phase 4 Lesson 18 (CLIP)`

- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]] — U-Net
- [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]] — Mask R-CNN
- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]] — CLIP

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]

## Builds on this

- [[Lessons/04-27 Multi-Object Tracking & Video Memory|04/27 Multi-Object Tracking & Video Memory]]

## Concepts taught

- Open-vocabulary segmentation `lesson term` — Produce masks for objects described in natural language, not a fixed label set
- PCS `lesson term` — SAM 3's core task — given a noun-phrase or image exemplar, segment all matching instances
- Concept prompt `lesson term` — Short noun phrase or image exemplar; not a full sentence
- Presence head `lesson term` — SAM 3 module that decides whether the concept exists in the image before localisation
- SA-CO `lesson term` — 270K-concept open-vocabulary segmentation benchmark; 50x larger than prior open-vocab benchmarks
- [[Concepts/Object Multiplex|Object Multiplex]] `lesson term` — Shared-memory multi-object tracking; fast joint tracking of many instances
- Grounded SAM 2 `lesson term` — Detector + SAM 2 cascade; still relevant when detector swap matters
- SAM-MI `lesson term` — Mask Injection for 1.6x speedup over Grounded-SAM

## Ships

- [[Artifacts/04-24 prompt-open-vocab-stack-picker|prompt-open-vocab-stack-picker]] `prompt` — Pick SAM 3 / Grounded SAM 2 / YOLO-World / SAM-MI based on latency, concept complexity, and licensing
- [[Artifacts/04-24 skill-concept-prompt-designer|skill-concept-prompt-designer]] `skill` — Turn user utterances into well-formed SAM 3 concept prompts with splitting, disambiguation, and fallbacks

## Further reading

- [[Resources/SAM 3.1 Object Multiplex (Meta AI, March 2026)|SAM 3.1 Object Multiplex (Meta AI, March 2026)]] ([link](https://ai.meta.com/blog/segment-anything-model-3/)) ·  also cited by 1 other lesson
- SAM 3: Segment Anything with Concepts (arXiv 2511.16719) ([link](https://arxiv.org/abs/2511.16719))
- SAM3-I: Instruction-aware SAM (arXiv 2512.04585) ([link](https://arxiv.org/abs/2512.04585))
- Ultralytics SAM 3 docs ([link](https://docs.ultralytics.com/models/sam-3/))
- SAM 3 model page on Hugging Face ([link](https://huggingface.co/facebook/sam3))
- Grounded SAM 2 tutorial (PyImageSearch) ([link](https://pyimagesearch.com/2026/01/19/grounded-sam-2-from-open-set-detection-to-segmentation-and-tracking/))


%% ── my notes ── %%
