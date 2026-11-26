---
id: "lesson:04/14"
type: lesson
ref: 04/14
phase: 4
num: 14
title: Vision Transformers (ViT)
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 9
prereqs: 2
community: 12
libraries:
  - torch
aliases:
  - 04/14
  - 04-14
tags:
  - phase/04
  - type/build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/14-vision-transformers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/14-vision-transformers"
---

# 04/14 Vision Transformers (ViT)

> Cut the image into patches, treat each patch as a word, run a standard transformer. Don't look back.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/14-vision-transformers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/14-vision-transformers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/14-vision-transformers) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 7 Lesson 02 (Self-Attention), Phase 4 Lesson 04 (Image Classification)`

- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Image Classification
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]]
- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]]
- [[Lessons/04-20 Image Retrieval & Metric Learning|04/20 Image Retrieval & Metric Learning]]
- [[Lessons/04-23 Diffusion Transformers & Rectified Flow|04/23 Diffusion Transformers & Rectified Flow]]
- [[Lessons/04-25 Vision-Language Models — The ViT-MLP-LLM Pattern|04/25 Vision-Language Models — The ViT-MLP-LLM Pattern]]
- [[Lessons/04-26 Monocular Depth & Geometry Estimation|04/26 Monocular Depth & Geometry Estimation]]
- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]]

## Concepts taught

- [[Concepts/Patch Embedding|Patch Embedding]] `glossary` — A conv with kernel size = stride = patch size; turns the image into a grid of token embeddings
- Class token `lesson term` — A learned vector prepended to the token sequence; its final output is the global image representation
- Positional embedding `lesson term` — A learned vector added to every token so the transformer knows where each patch came from
- [[Concepts/Pre-LN|Pre-LN]] `lesson term` — The stable transformer variant: x + sublayer(LN(x)) instead of LN(x + sublayer(x))
- [[Concepts/Multi-head attention|Multi-head attention]] `lesson term` — Standard transformer attention split into num_heads independent subspaces, concatenated afterwards
- ViT-B/16 `lesson term` — The canonical size: dim=768, depth=12, heads=12, patch_size=16, image=224; ~86M params
- DeiT `lesson term` — ViT trained on ImageNet-1k alone with strong augmentation; proved large pretraining datasets are not strictly required
- MAE `lesson term` — Self-supervised pretraining: mask 75% of patches, reconstruct; the dominant ViT pretraining recipe
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]] `glossary` — A vision architecture that represents an image as a sequence of patch embeddings with position information and processes that sequence with transformer encoder blocks.

## Ships

- [[Artifacts/04-14 prompt-vit-vs-cnn-picker|prompt-vit-vs-cnn-picker]] `prompt` — Pick between ViT, ConvNeXt, or Swin based on dataset size, compute, and inference stack
- [[Artifacts/04-14 skill-vit-patch-and-pos-embed-inspector|skill-vit-patch-and-pos-embed-inspector]] `skill` — Verify a ViT's patch embedding and positional embedding shapes match the model's expected sequence length

## Further reading

- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929)) — the ViT paper ·  also cited by 2 other lessons
- [[Resources/DeiT- Data-efficient Image Transformers (Touvron et al., 2020)|DeiT: Data-efficient Image Transformers (Touvron et al., 2020)]] ([link](https://arxiv.org/abs/2012.12877)) — how to train ViT on ImageNet-1k alone ·  also cited by 1 other lesson
- [[Resources/Masked Autoencoders are Scalable Vision Learners (He et al., 2022)|Masked Autoencoders are Scalable Vision Learners (He et al., 2022)]] ([link](https://arxiv.org/abs/2111.06377)) — MAE pretraining ·  also cited by 2 other lessons
- [[Resources/timm documentation|timm documentation]] ([link](https://huggingface.co/docs/timm)) — the reference for every vision transformer you will use in production ·  also cited by 1 other lesson


%% ── my notes ── %%
