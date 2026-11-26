---
id: "lesson:04/23"
type: lesson
ref: 04/23
phase: 4
num: 23
title: "Diffusion Transformers & Rectified Flow"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
community: 12
libraries:
  - numpy
  - torch
aliases:
  - 04/23
  - 04-23
tags:
  - phase/04
  - type/learn+build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/23-diffusion-transformers-rectified-flow/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/23-diffusion-transformers-rectified-flow"
---

# 04/23 Diffusion Transformers & Rectified Flow

> The U-Net is not the secret of diffusion. Replace it with a transformer, swap the noise schedule for a straight-line flow, and suddenly you have SD3, FLUX, and every 2026 text-to-image model.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/23-diffusion-transformers-rectified-flow/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/23-diffusion-transformers-rectified-flow) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/23-diffusion-transformers-rectified-flow) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 10 (Diffusion DDPM), Phase 4 Lesson 14 (ViT), Phase 7 Lesson 02 (Self-Attention)`

- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]] — Diffusion DDPM
- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — ViT
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/04-28 World Models & Video Diffusion|04/28 World Models & Video Diffusion]]

## Concepts taught

- [[Concepts/DiT|DiT]] `lesson term` — Transformer that replaces the U-Net as the diffusion denoiser; operates on patchified latents
- AdaLN `lesson term` — Timestep/text conditioning via learned scale, shift, gate applied after LayerNorm; standard in every modern DiT
- [[Concepts/MMDiT|MMDiT]] `lesson term` — Separate weight streams for text and image tokens that share a joint self-attention
- Single-stream / double-stream `lesson term` — First N blocks double-stream (separate weights per modality), later blocks single-stream (concat + shared weights) for efficiency
- [[Concepts/Rectified flow|Rectified flow]] `lesson term` — Linear interpolation between data and noise; network predicts velocity; fewer ODE steps needed at inference
- Velocity target `lesson term` — The regression target in rectified flow; points from clean data to noise
- CFG guidance `lesson term` — Mix conditional and unconditional predictions; still used in rectified-flow models
- Schnell / turbo / LCM `lesson term` — Small-step variants distilled from full-quality models; production real-time

## Ships

- [[Artifacts/04-23 prompt-dit-model-picker|prompt-dit-model-picker]] `prompt` — Pick between SD3, SD3.5, FLUX.1-dev, FLUX.1-schnell, Z-Image, SD4 Turbo given quality, latency, and license
- [[Artifacts/04-23 skill-rectified-flow-trainer|skill-rectified-flow-trainer]] `skill` — Write a complete rectified-flow training loop with AdaLN DiT and Euler sampling

## Further reading

- [[Resources/Elucidating the Design Space of Diffusion (Karras et al., 2022)|Elucidating the Design Space of Diffusion (Karras et al., 2022)]] ([link](https://arxiv.org/abs/2206.00364)) — the reference for every diffusion design trade-off ·  also cited by 2 other lessons
- [[Resources/Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)|Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)]] ([link](https://arxiv.org/abs/2212.09748)) — the DiT paper ·  also cited by 3 other lessons
- Latent Consistency Models (Luo et al., 2023) ([link](https://arxiv.org/abs/2310.04378)) — how LCM-LoRA gives you 4-step inference
- [[Resources/Scaling Rectified Flow Transformers (Esser et al., SD3 paper)|Scaling Rectified Flow Transformers (Esser et al., SD3 paper)]] ([link](https://arxiv.org/abs/2403.03206)) — MMDiT and rectified-flow at scale ·  also cited by 4 other lessons
- Z-Image: Efficient Image Generation Foundation Model (2025) ([link](https://arxiv.org/html/2511.22699v1)) — single-stream DiT at 6B
- FLUX.1 model card and technical report (Black Forest Labs) ([link](https://huggingface.co/black-forest-labs/FLUX.1-dev)) — double + single-stream details


%% ── my notes ── %%
