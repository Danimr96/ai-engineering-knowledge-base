---
id: "lesson:04/06"
type: lesson
ref: 04/06
phase: 4
num: 6
title: "Object Detection — YOLO from Scratch"
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
  - 04/06
  - 04-06
tags:
  - phase/04
  - type/build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/06-object-detection-yolo/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/06-object-detection-yolo"
---

# 04/06 Object Detection — YOLO from Scratch

> Detection is classification plus regression, run at every position in a feature map, then cleaned up with non-maximum suppression.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/06-object-detection-yolo/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/06-object-detection-yolo) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/06-object-detection-yolo) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification), Phase 4 Lesson 05 (Transfer Learning)`

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification
- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]] — Transfer Learning

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]]

## Builds on this

- [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-19 OCR & Document Understanding|04/19 OCR & Document Understanding]]
- [[Lessons/04-21 Keypoint Detection & Pose Estimation|04/21 Keypoint Detection & Pose Estimation]]
- [[Lessons/04-27 Multi-Object Tracking & Video Memory|04/27 Multi-Object Tracking & Video Memory]]
- [[Lessons/08-04 Conditional GANs & Pix2Pix|08/04 Conditional GANs & Pix2Pix]]

## Concepts taught

- Anchor `lesson term` — A pre-defined box shape at each grid cell from which the network predicts deltas instead of absolute coordinates
- IoU `lesson term` — Intersection-over-union of two boxes; the universal similarity measure in detection
- NMS `lesson term` — Greedy algorithm that keeps highest-score predictions and removes overlapping ones above a threshold
- Objectness `lesson term` — Per-anchor, per-cell scalar predicting whether an object is centred in that cell
- Grid stride `lesson term` — Pixels per grid cell; a 416-px input with a 13-grid head has stride 32
- [[Concepts/MAP|MAP]] `lesson term` — Average of the area under the precision-recall curve, averaged over classes and (for COCO) IoU thresholds
- AP@0.5 `lesson term` — Average precision with IoU threshold 0.5; the lenient version of the metric
- mAP@0.5:0.95 `lesson term` — Average over IoU thresholds 0.5..0.95 step 0.05; the strict version and current community standard

## Ships

- [[Artifacts/04-06 prompt-detection-metric-reader|prompt-detection-metric-reader]] `prompt` — Turn a precision/recall/AP/mAP row into a one-line diagnosis and the single most useful next experiment
- [[Artifacts/04-06 skill-anchor-designer|skill-anchor-designer]] `skill` — Given a dataset of ground-truth boxes, run k-means on (w, h) and return anchor sets per FPN level plus coverage statistics

## Further reading

- YOLOv1: You Only Look Once (Redmon et al., 2016) ([link](https://arxiv.org/abs/1506.02640)) — the founding paper; every YOLO since is a refinement of this structure
- YOLOv3 (Redmon & Farhadi, 2018) ([link](https://arxiv.org/abs/1804.02767)) — the paper that introduced multi-scale FPN-style heads; still the clearest diagram
- Ultralytics YOLOv8 docs ([link](https://docs.ultralytics.com)) — the current production reference; covers dataset formats, augmentations, training recipes
- The Illustrated Guide to Object Detection (Jonathan Hui) ([link](https://jonathan-hui.medium.com/object-detection-series-24d03a12f904)) — best plain-English tour of the full detector zoo; priceless for understanding how DETR, RetinaNet, FCOS, and YOLO relate


%% ── my notes ── %%
