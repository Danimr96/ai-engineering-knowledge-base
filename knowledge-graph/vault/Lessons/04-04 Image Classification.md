---
id: "lesson:04/04"
type: lesson
ref: 04/04
phase: 4
num: 4
title: Image Classification
lesson_type: build
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
  - numpy
  - torch
aliases:
  - 04/04
  - 04-04
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/04-image-classification/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/04-image-classification"
---

# 04/04 Image Classification

> A classifier is a function from pixels to a probability distribution over classes. Everything else is plumbing.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/04-image-classification/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/04-image-classification) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/04-image-classification) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 2 Lesson 09 (Model Evaluation), Phase 3 Lesson 10 (Mini Framework), Phase 4 Lesson 03 (CNNs)`

- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]] — Model Evaluation
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]] — Mini Framework
- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]

## Builds on this

- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]]
- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]]
- [[Lessons/04-12 Video Understanding — Temporal Modeling|04/12 Video Understanding — Temporal Modeling]]
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]
- [[Lessons/04-15 Real-Time Vision — Edge Deployment|04/15 Real-Time Vision — Edge Deployment]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]]

## Concepts taught

- [[Concepts/Logits|Logits]] `glossary` — The pre-softmax vector of C numbers per image; cross-entropy expects these, not softmaxed values
- [[Concepts/Cross-Entropy|Cross-Entropy]] `glossary` — Negative log-probability of the correct class; combines log-softmax and NLL in one stable op
- [[Concepts/DataLoader|DataLoader]] `lesson term` — Wraps a dataset with shuffling, batching, and (optional) multi-worker loading; gets blamed for half of training bugs
- Augmentation `lesson term` — Any pixel-level transform at training time that preserves the label; teaches invariances the CNN does not have natively
- Mixup / Cutmix `lesson term` — Blend both inputs and labels so the classifier learns smooth interpolations instead of hard boundaries
- [[Concepts/Label smoothing|Label smoothing]] `lesson term` — Replace one-hot with (1-eps, eps/(C-1), ...); improves calibration and slightly boosts accuracy
- Top-k accuracy `lesson term` — The correct class is in the k highest-probability predictions; used on datasets with genuinely ambiguous classes
- [[Concepts/Confusion matrix|Confusion matrix]] `lesson term` — C x C table where entry (i, j) counts images of true class i predicted as j; diagonal is right, off-diagonal tells you what to fix

## Ships

- [[Artifacts/04-04 prompt-classifier-pipeline-auditor|prompt-classifier-pipeline-auditor]] `prompt` — Audit a PyTorch image classification training script for the five invariants that cover most silent bugs
- [[Artifacts/04-04 skill-classification-diagnostics|skill-classification-diagnostics]] `skill` — Given a confusion matrix and class names, surface per-class failures and propose the single most impactful fix

## Further reading

- Why temperature scaling matters (Guo et al., 2017) ([link](https://arxiv.org/abs/1706.04599)) — the paper that proved modern networks are miscalibrated and fixed it with one scalar parameter
- mixup: Beyond Empirical Risk Minimization (Zhang et al., 2017) ([link](https://arxiv.org/abs/1710.09412)) — the original mixup paper; three pages of theory plus convincing experiments
- Bag of Tricks for Image Classification (He et al., 2019) ([link](https://arxiv.org/abs/1812.01187)) — every small trick that together adds 3-4% to ResNet accuracy on ImageNet
- CS231n: Training Neural Networks ([link](https://cs231n.github.io/neural-networks-3/)) — still the clearest tour of the training pipeline at a single page


%% ── my notes ── %%
