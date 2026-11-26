---
id: "lesson:04/07"
type: lesson
ref: 04/07
phase: 4
num: 7
title: "Semantic Segmentation — U-Net"
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
aliases:
  - 04/07
  - 04-07
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/07-semantic-segmentation-unet/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/07-semantic-segmentation-unet"
---

# 04/07 Semantic Segmentation — U-Net

> Segmentation is classification at every pixel. U-Net makes it work by pairing a downsampling encoder with an upsampling decoder and wiring skip connections between them.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/07-semantic-segmentation-unet/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/07-semantic-segmentation-unet) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/07-semantic-segmentation-unet) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification)`

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]]
- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-21 Keypoint Detection & Pose Estimation|04/21 Keypoint Detection & Pose Estimation]]
- [[Lessons/04-24 SAM 3 & Open-Vocabulary Segmentation|04/24 SAM 3 & Open-Vocabulary Segmentation]]
- [[Lessons/04-26 Monocular Depth & Geometry Estimation|04/26 Monocular Depth & Geometry Estimation]]

## Concepts taught

- Semantic segmentation `lesson term` — Per-pixel classification into C classes; instances of the same class merge
- Instance segmentation `lesson term` — Separates distinct instances of the same class; foreground-only
- Panoptic segmentation `lesson term` — Every pixel gets a class; every thing instance also gets a unique id
- Skip connection `lesson term` — Concatenation of encoder features into matching-resolution decoder features; preserves high-frequency detail
- Transposed conv `lesson term` — Learnable upsampling; can produce checkerboard artifacts
- Dice loss `lesson term` — ); optimises mask overlap directly and is robust to class imbalance
- mIoU `lesson term` — Average IoU across classes; the community-standard metric for segmentation
- Boundary F1 `lesson term` — F1 score computed on boundary pixels only; matters for precision-critical tasks

## Ships

- [[Artifacts/04-07 prompt-segmentation-task-picker|prompt-segmentation-task-picker]] `prompt` — Pick semantic vs instance vs panoptic segmentation and name the architecture for a given task
- [[Artifacts/04-07 skill-segmentation-mask-inspector|skill-segmentation-mask-inspector]] `skill` — Report class distribution, predicted-mask statistics, and the classes most likely to be under-predicted or boundary-blurred

## Further reading

- Fully Convolutional Networks (Long et al., 2015) ([link](https://arxiv.org/abs/1411.4038)) — the paper that first made segmentation an end-to-end conv problem
- U-Net: Convolutional Networks for Biomedical Image Segmentation (Ronneberger et al., 2015) ([link](https://arxiv.org/abs/1505.04597)) — the original paper; the figure everyone copies is on page 2
- segmentation_models_pytorch ([link](https://github.com/qubvel/segmentation_models.pytorch)) — the reference for production segmentation; every standard architecture plus every standard loss
- Lessons learned from training SOTA segmentation (kaggle.com competitions) ([link](https://www.kaggle.com/code/iafoss/carvana-unet-pytorch)) — a walkthrough of why TTA, pseudo-labeling, and class weights matter on real data


%% ── my notes ── %%
