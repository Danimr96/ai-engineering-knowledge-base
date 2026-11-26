---
id: "lesson:07/09"
type: lesson
ref: 07/09
phase: 7
num: 9
title: Vision Transformers (ViT)
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 5
aliases:
  - 07/09
  - 07-09
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/09-vision-transformers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/09-vision-transformers"
---

# 07/09 Vision Transformers (ViT)

> An image is a grid of patches. A sentence is a grid of tokens. The same transformer eats both.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/09-vision-transformers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/09-vision-transformers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/09-vision-transformers) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 05 (Full Transformer), Phase 4 · 03 (CNNs), Phase 4 · 14 (Vision Transformers intro)`

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — Vision Transformers intro
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]]
- [[Lessons/08-10 Video Generation|08/10 Video Generation]]

## Concepts taught

- [[Concepts/Patch|Patch]] `glossary` — Flat vector of pixel values for a P × P × C region of the image.
- Patchify `lesson term` — Slice image into non-overlapping patches, flatten each to a vector.
- [[Concepts/CLS- token|[CLS] token]] `lesson term` — Prepended learnable token; its final embedding is the image representation.
- [[Concepts/Inductive Bias|Inductive Bias]] `glossary` — ViT has fewer priors than CNNs; needs more data to make up the gap.
- [[Concepts/DINOv2|DINOv2]] `lesson term` — Trained without labels using image augmentation + momentum teacher. Best general image features in 2026.
- [[Concepts/SigLIP|SigLIP]] `lesson term` — ViT + text encoder trained with sigmoid contrastive loss; better than CLIP on matched compute.
- Swin `lesson term` — Hierarchical ViT with local attention + shifted windows; sub-quadratic.
- Register tokens `lesson term` — A few extra learnable tokens that soak up attention sinks; improves DINOv2 features.

## Ships

- [[Artifacts/07-09 vit-configurator|vit-configurator]] `skill` — Pick a ViT variant, patch size, and pretraining source for a new vision task.

## Further reading

- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929)) — the ViT paper. ·  also cited by 2 other lessons
- [[Resources/DeiT- Data-efficient Image Transformers (Touvron et al., 2020)|DeiT: Data-efficient Image Transformers (Touvron et al., 2020)]] ([link](https://arxiv.org/abs/2012.12877)) — DeiT. ·  also cited by 1 other lesson
- Liu et al. (2021). Swin Transformer: Hierarchical Vision Transformer using Shifted Windows ([link](https://arxiv.org/abs/2103.14030)) — Swin.
- [[Resources/DINOv2 (Oquab et al., 2023)|DINOv2 (Oquab et al., 2023)]] ([link](https://arxiv.org/abs/2304.07193)) — DINOv2. ·  also cited by 2 other lessons
- [[Resources/Darcet et al. (2023). Vision Transformers Need Registers|Darcet et al. (2023). Vision Transformers Need Registers]] ([link](https://arxiv.org/abs/2309.16588)) — the register-token fix for DINOv2. ·  also cited by 1 other lesson


%% ── my notes ── %%
