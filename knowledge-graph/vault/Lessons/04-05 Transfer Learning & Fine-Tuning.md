---
id: "lesson:04/05"
type: lesson
ref: 04/05
phase: 4
num: 5
title: "Transfer Learning & Fine-Tuning"
lesson_type: build
languages:
  - Python
time_min: 75
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
  - 04/05
  - 04-05
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/05-transfer-learning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/05-transfer-learning"
---

# 04/05 Transfer Learning & Fine-Tuning

> Somebody else spent a million GPU hours teaching a network what edges, textures, and object parts look like. You should borrow those features before training your own.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/05-transfer-learning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/05-transfer-learning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/05-transfer-learning) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]], [[Libraries/torchvision (python)|torchvision]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification)`

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]

## Concepts taught

- Feature extraction `lesson term` — Backbone parameters frozen, only the new classifier head receives gradient
- [[Concepts/Fine-tuning|Fine-tuning]] `glossary` — All parameters trainable, usually with much smaller LR than scratch training
- Discriminative LR `lesson term` — Optimizer parameter groups where early-stage LR is a fraction of late-stage LR
- Layer-wise LR decay `lesson term` — Per-layer LR multiplied by decay^(L - k); common in transformer fine-tunes
- [[Concepts/Catastrophic forgetting|Catastrophic forgetting]] `lesson term` — A too-high LR overwrites pretrained features before the new task signal is learnt
- BN statistics drift `lesson term` — BatchNorm running_mean/var computed on a different distribution than the current task, silently hurting accuracy
- [[Concepts/Linear probe|Linear probe]] `lesson term` — Evaluation of pretrained features — accuracy of the best linear classifier on top of the frozen representation
- Catastrophic collapse `lesson term` — Happens when fine-tuning with an LR high enough to destroy features before gradients from the head can stabilise

## Ships

- [[Artifacts/04-05 prompt-fine-tune-planner|prompt-fine-tune-planner]] `prompt` — Pick feature extraction vs progressive vs end-to-end fine-tuning given dataset size, domain distance, and compute budget
- [[Artifacts/04-05 skill-freeze-inspector|skill-freeze-inspector]] `skill` — Report which parameters are trainable, which BatchNorm layers are in eval mode, and whether the optimizer is actually consuming the trainable parameters

## Further reading

- How transferable are features in deep neural networks? (Yosinski et al., 2014) ([link](https://arxiv.org/abs/1411.1792)) — the paper that quantified feature transferability across layers
- Universal Language Model Fine-tuning (ULMFiT, Howard & Ruder, 2018) ([link](https://arxiv.org/abs/1801.06146)) — the original discriminative LR / progressive unfreezing recipe; the ideas transfer directly to vision
- A Simple Framework for Linear-Probe Evaluation (Kornblith et al., 2019) ([link](https://arxiv.org/abs/1805.08974)) — why linear-probe accuracy matters and how to report it correctly
- [[Resources/timm documentation|timm documentation]] ([link](https://huggingface.co/docs/timm)) — the reference for modern vision backbones and the exact fine-tune defaults they were trained with ·  also cited by 1 other lesson


%% ── my notes ── %%
