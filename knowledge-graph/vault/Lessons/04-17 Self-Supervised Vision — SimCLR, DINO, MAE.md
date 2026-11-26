---
id: "lesson:04/17"
type: lesson
ref: 04/17
phase: 4
num: 17
title: "Self-Supervised Vision — SimCLR, DINO, MAE"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
libraries:
  - torch
aliases:
  - 04/17
  - 04-17
tags:
  - phase/04
  - type/learn+build
source: ai-engineering-from-scratch/phases/04-computer-vision/17-self-supervised-vision/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/17-self-supervised-vision"
---

# 04/17 Self-Supervised Vision — SimCLR, DINO, MAE

> Labels are the bottleneck of supervised vision. Self-supervised pretraining removes them: learn visual features from 100M unlabelled images, fine-tune on 10k labelled ones.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/17-self-supervised-vision/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/17-self-supervised-vision) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/17-self-supervised-vision) · code: main.py · quiz: 5 questions  
**Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 04 (Image Classification), Phase 4 Lesson 14 (ViT)`

- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]]
- [[Lessons/04-26 Monocular Depth & Geometry Estimation|04/26 Monocular Depth & Geometry Estimation]]

## Concepts taught

- Self-supervised `lesson term` — A pretext task that produces useful representations from unlabelled data
- Pretext task `lesson term` — The objective used during SSL (reconstruct patches, match views); discarded after pretraining
- [[Concepts/Linear probe|Linear probe]] `lesson term` — Standard SSL evaluation: train only a linear classifier on top of frozen features
- [[Concepts/InfoNCE|InfoNCE]] `lesson term` — softmax over cosine similarities; positive pair is the target class, all others are negatives
- EMA teacher `lesson term` — Teacher whose weights are an exponential moving average of the student's; used by BYOL, MoCo, DINO
- Mask ratio `lesson term` — Fraction of patches masked during MAE; 75% for vision, 15% for text
- Representation collapse `lesson term` — SSL failure where the encoder outputs a constant vector for all inputs; prevented by centring, sharpening, or negatives
- [[Concepts/DINOv2|DINOv2]] `lesson term` — Meta's 2023 self-supervised ViT; strongest general-purpose image features in 2026

## Ships

- [[Artifacts/04-17 prompt-ssl-pretraining-picker|prompt-ssl-pretraining-picker]] `prompt` — Pick SimCLR / MAE / DINOv2 given dataset size, compute, and downstream task
- [[Artifacts/04-17 skill-linear-probe-runner|skill-linear-probe-runner]] `skill` — Write the complete linear-probe evaluation for any frozen encoder and labelled dataset

## Further reading

- SimCLR (Chen et al., 2020) ([link](https://arxiv.org/abs/2002.05709)) — contrastive learning reference
- DINO (Caron et al., 2021) ([link](https://arxiv.org/abs/2104.14294)) — teacher-student with momentum, centring, sharpening
- [[Resources/Masked Autoencoders are Scalable Vision Learners (He et al., 2022)|Masked Autoencoders are Scalable Vision Learners (He et al., 2022)]] ([link](https://arxiv.org/abs/2111.06377)) — masked autoencoder pretraining for ViT ·  also cited by 2 other lessons
- [[Resources/DINOv2 (Oquab et al., 2023)|DINOv2 (Oquab et al., 2023)]] ([link](https://arxiv.org/abs/2304.07193)) — scaling self-supervised ViT to production features ·  also cited by 2 other lessons


%% ── my notes ── %%
