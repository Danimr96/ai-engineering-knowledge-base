---
id: "lesson:04/03"
type: lesson
ref: 04/03
phase: 4
num: 3
title: "CNNs — LeNet to ResNet"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
community: 13
libraries:
  - torch
aliases:
  - 04/03
  - 04-03
tags:
  - phase/04
  - type/learn+build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/03-cnns-lenet-to-resnet"
---

# 04/03 CNNs — LeNet to ResNet

> Every major CNN of the last thirty years is the same conv–nonlinearity–downsample recipe with one new idea bolted on. Learn the ideas in order.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/03-cnns-lenet-to-resnet/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/03-cnns-lenet-to-resnet) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/03-cnns-lenet-to-resnet) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 3 Lesson 11 (PyTorch), Phase 4 Lesson 01 (Image Fundamentals), Phase 4 Lesson 02 (Convolutions from Scratch)`

- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — PyTorch
- [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]] — Image Fundamentals
- [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]] — Convolutions from Scratch

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-04 Image Classification|04/04 Image Classification]]
- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]]
- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]]
- [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
- [[Lessons/04-12 Video Understanding — Temporal Modeling|04/12 Video Understanding — Temporal Modeling]]
- [[Lessons/04-13 3D Vision — Point Clouds & NeRFs|04/13 3D Vision — Point Clouds & NeRFs]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]]

## Concepts taught

- [[Concepts/Backbone|Backbone]] `lesson term` — The stack of convolutional blocks that produces the feature map fed to the task head
- [[Concepts/Residual connection|Residual connection]] `lesson term` — y = F(x) + x; lets the optimiser learn identity by setting F to zero, which makes arbitrary depth trainable
- BasicBlock `lesson term` — The ResNet-18/34 building block: conv-BN-ReLU-conv-BN-add-ReLU
- Bottleneck `lesson term` — The ResNet-50/101/152 block; cheap at high channel counts because the 3x3 runs on a reduced width
- Degradation problem `lesson term` — Past ~20 plain conv layers, both training and test error increase; solved by residual connections, not by more data
- [[Concepts/Stem|Stem]] `lesson term` — The initial conv that converts 3-channel input into the base feature width; usually 7x7 stride 2 for ImageNet, 3x3 stride 1 for CIFAR
- [[Concepts/Head|Head]] `lesson term` — The layers after the final backbone block: adaptive pool, flatten, linear(s)
- [[Concepts/Transfer Learning|Transfer Learning]] `glossary` — Loading a backbone trained on ImageNet and fine-tuning only the head on your task

## Ships

- [[Artifacts/04-03 prompt-backbone-selector|prompt-backbone-selector]] `prompt` — Pick the right vision backbone (LeNet, VGG, ResNet, MobileNet, EfficientNet-Lite, ConvNeXt, ViT) for a given task, dataset size, and compute budget
- [[Artifacts/04-03 skill-residual-block-reviewer|skill-residual-block-reviewer]] `skill` — Review a PyTorch residual block for skip-connection correctness, BN placement, activation order, and shape alignment

## Further reading

- Very Deep Convolutional Networks (Simonyan & Zisserman, 2014) ([link](https://arxiv.org/abs/1409.1556)) — the VGG paper; still the best reference for "why 3x3"
- Going Deeper with Convolutions (Szegedy et al., 2014) ([link](https://arxiv.org/abs/1409.4842)) — Inception v1; the parallel-filter idea that still shows up in vision transformers
- Deep Residual Learning for Image Recognition (He et al., 2015) ([link](https://arxiv.org/abs/1512.03385)) — the ResNet paper; every figure is worth studying
- ImageNet Classification with Deep CNNs (Krizhevsky et al., 2012) ([link](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)) — AlexNet; the paper that ended the hand-crafted-feature era


%% ── my notes ── %%
