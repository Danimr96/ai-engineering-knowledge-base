---
id: "lesson:04/02"
type: lesson
ref: 04/02
phase: 4
num: 2
title: Convolutions from Scratch
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 1
community: 13
libraries:
  - numpy
aliases:
  - 04/02
  - 04-02
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/02-convolutions-from-scratch/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/02-convolutions-from-scratch"
---

# 04/02 Convolutions from Scratch

> A convolution is a tiny dense layer you slide across an image, sharing the same weights at every location.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/02-convolutions-from-scratch/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/02-convolutions-from-scratch) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/02-convolutions-from-scratch) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 3 (Deep Learning Core), Phase 4 Lesson 01 (Image Fundamentals)`

- [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]] — Image Fundamentals
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — Deep Learning Core ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]

## Builds on this

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]]

## Concepts taught

- Convolution `lesson term` — A learnable dot product applied at every spatial location with shared weights; mathematically a cross-correlation, but everyone calls it convolution
- Kernel / filter `lesson term` — A small weight tensor of shape (C_in, K, K) whose dot product with a window of input produces one output pixel
- [[Concepts/Stride|Stride]] `lesson term` — The step size between consecutive kernel placements; stride 2 halves each spatial dimension
- Padding `lesson term` — Extra values added around the input so the kernel can centre on border pixels; same padding keeps output size equal to input size
- Receptive field `lesson term` — The patch of original input that a given output activation depends on, growing with depth and stride
- im2col `lesson term` — Rearranging every receptive window into columns so convolution becomes one big matrix multiply — the core of every fast conv kernel
- Depthwise conv `lesson term` — A conv with groups == C_in, computing each output channel from only its matching input channel; the backbone of MobileNet and ConvNeXt
- Translation equivariance `lesson term` — Property that shifting the input by k pixels shifts the output by k pixels; comes for free with shared weights

## Ships

- [[Artifacts/04-02 prompt-cnn-architect|prompt-cnn-architect]] `prompt` — Design a stack of Conv2d layers from input size, parameter budget, and target receptive field
- [[Artifacts/04-02 skill-conv-shape-calculator|skill-conv-shape-calculator]] `skill` — Walk a CNN spec layer by layer and report output shape, receptive field, and parameter count for every block

## Further reading

- A guide to convolution arithmetic for deep learning (Dumoulin & Visin, 2016) ([link](https://arxiv.org/abs/1603.07285)) — the definitive diagrams of padding/stride/dilation that every course quietly copies
- CS231n: Convolutional Neural Networks for Visual Recognition ([link](https://cs231n.github.io/convolutional-networks/)) — the canonical lecture notes, including the original im2col explanation
- Receptive Field Arithmetic for CNNs (Dang Ha The Hien) ([link](https://distill.pub/2019/computing-receptive-fields/)) — the paper-quality interactive explainer of receptive field calculations
- The Annotated ConvNet (fast.ai) ([link](https://nbviewer.org/github/fastai/fastbook/blob/master/13_convolutions.ipynb)) — a notebook that walks from manual convolution to a trained digit classifier


%% ── my notes ── %%
