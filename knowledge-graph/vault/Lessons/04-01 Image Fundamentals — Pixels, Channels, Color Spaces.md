---
id: "lesson:04/01"
type: lesson
ref: 04/01
phase: 4
num: 1
title: "Image Fundamentals — Pixels, Channels, Color Spaces"
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
aliases:
  - 04/01
  - 04-01
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/01-image-fundamentals/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/01-image-fundamentals"
---

# 04/01 Image Fundamentals — Pixels, Channels, Color Spaces

> An image is a tensor of light samples. Every vision model you will ever use starts from this one fact.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/01-image-fundamentals/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/01-image-fundamentals) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/01-image-fundamentals) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 1 Lesson 12 (Tensor Operations), Phase 3 Lesson 11 (Intro to PyTorch)`

- [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]] — Tensor Operations
- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — Intro to PyTorch

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]

## Concepts taught

- Pixel `lesson term` — One sample of light intensity at one grid location — three numbers for colour, one for grayscale
- Channel `lesson term` — One of the parallel spatial grids stacked into an image tensor; last axis in HWC, first in CHW
- HWC / CHW `lesson term` — Axis orderings for an image tensor; disk and PIL use HWC, PyTorch and cuDNN use CHW
- [[Concepts/Normalize|Normalize]] `lesson term` — Divide by 255 so pixels live in [0, 1] — necessary but not sufficient
- Standardize `lesson term` — Subtract mean and divide by std per channel so the input distribution matches what the model was trained on
- Grayscale conversion `lesson term` — A weighted sum with coefficients 0.299/0.587/0.114 that matches human luminance perception
- Interpolation `lesson term` — The rule that decides output values when the new grid does not align with the old one — nearest for labels, bilinear for training, bicubic for display
- Aspect ratio `lesson term` — The ratio that distinguishes "resize and pad" from "resize and stretch"

## Ships

- [[Artifacts/04-01 prompt-vision-preprocessing-audit|prompt-vision-preprocessing-audit]] `prompt` — Turn any model card or dataset card into a checklist of the preprocessing invariants a vision pipeline must honour
- [[Artifacts/04-01 skill-image-tensor-inspector|skill-image-tensor-inspector]] `skill` — Inspect any image-shaped tensor or array and report dtype, layout, range, and whether it looks raw, normalized, or standardized

## Further reading

- Charles Poynton — A Guided Tour of Color Space ([link](https://poynton.ca/PDFs/Guided_tour.pdf)) — the clearest technical treatment of why there are so many color spaces and when each one matters
- ImageNet Preprocessing Conventions (torchvision models) ([link](https://pytorch.org/vision/stable/models.html)) — the source of truth for `mean=[0.485, 0.456, 0.406]` and why every model in the zoo expects it
- PyTorch Vision Transforms Docs ([link](https://pytorch.org/vision/stable/transforms.html)) — the full pipeline of transforms you will actually compose in production
- How JPEG Works (Colt McAnlis) ([link](https://www.youtube.com/watch?v=F1kYBnY6mwg)) — a sharp visual tour of chroma subsampling, DCT, and why JPEG encodes YCbCr rather than RGB


%% ── my notes ── %%
