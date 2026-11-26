---
id: "lesson:04/08"
type: lesson
ref: 04/08
phase: 4
num: 8
title: "Instance Segmentation — Mask R-CNN"
lesson_type: learn+build
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
  - torch
  - torchvision
aliases:
  - 04/08
  - 04-08
tags:
  - phase/04
  - type/learn+build
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/08-instance-segmentation-mask-rcnn"
---

# 04/08 Instance Segmentation — Mask R-CNN

> Add a tiny mask branch to a Faster R-CNN detector and you have instance segmentation. The hard part is RoIAlign, and it is harder than it looks.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build + Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/08-instance-segmentation-mask-rcnn) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/08-instance-segmentation-mask-rcnn) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]] · **Libraries:** [[Libraries/torch (python)|torch]], [[Libraries/torchvision (python)|torchvision]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 06 (YOLO), Phase 4 Lesson 07 (U-Net)`

- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]] — YOLO
- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]] — U-Net

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-24 SAM 3 & Open-Vocabulary Segmentation|04/24 SAM 3 & Open-Vocabulary Segmentation]]
- [[Lessons/04-27 Multi-Object Tracking & Video Memory|04/27 Multi-Object Tracking & Video Memory]]
- [[Lessons/08-05 StyleGAN|08/05 StyleGAN]]

## Concepts taught

- Mask R-CNN `lesson term` — Faster R-CNN + a small FCN head that predicts a 28x28 mask per proposal per class
- FPN `lesson term` — Top-down + lateral connections that give every stride level C channels of semantic-rich features
- RPN `lesson term` — A small conv head that produces ~1000 object/no-object proposals per image
- RoIAlign `lesson term` — Bilinearly samples a fixed-size feature grid from any float-coordinate box
- RoIPool `lesson term` — Same purpose as RoIAlign but rounds box coordinates; obsolete
- Mask AP `lesson term` — Average precision computed with mask IoU instead of box IoU; the COCO instance segmentation metric
- Binary mask head `lesson term` — Predicts one binary mask per class for each proposal; only the predicted class's channel is kept
- Background class `lesson term` — The catch-all "no object" class; indices for real classes start at 1

## Ships

- [[Artifacts/04-08 prompt-instance-vs-semantic-router|prompt-instance-vs-semantic-router]] `prompt` — Ask three questions and pick instance vs semantic vs panoptic segmentation plus the first model
- [[Artifacts/04-08 skill-mask-rcnn-head-swapper|skill-mask-rcnn-head-swapper]] `skill` — Generate the exact code for swapping box and mask heads on a torchvision Mask R-CNN for a custom num_classes

## Further reading

- FPN: Feature Pyramid Networks (Lin et al., 2017) ([link](https://arxiv.org/abs/1612.03144)) — the FPN paper; every modern detector uses it
- Mask R-CNN (He et al., 2017) ([link](https://arxiv.org/abs/1703.06870)) — the paper; section 3 on RoIAlign is the critical read
- Detectron2 model zoo ([link](https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md)) — production implementations with trained weights for nearly every detection and segmentation variant
- torchvision Mask R-CNN tutorial ([link](https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html)) — the reference for the fine-tuning loop


%% ── my notes ── %%
