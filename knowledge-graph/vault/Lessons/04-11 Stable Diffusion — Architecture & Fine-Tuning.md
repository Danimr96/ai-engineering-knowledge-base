---
id: "lesson:04/11"
type: lesson
ref: 04/11
phase: 4
num: 11
title: "Stable Diffusion — Architecture & Fine-Tuning"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 12
libraries:
  - diffusers
  - torch
aliases:
  - 04/11
  - 04-11
tags:
  - phase/04
  - type/learn
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/11-stable-diffusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/11-stable-diffusion"
---

# 04/11 Stable Diffusion — Architecture & Fine-Tuning

> Stable Diffusion is a DDPM that runs in the latent space of a pretrained VAE, conditioned on text via cross-attention, sampled with a fast deterministic ODE solver, and steered by classifier-free guidance.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Use · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/11-stable-diffusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/11-stable-diffusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/11-stable-diffusion) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/diffusers (python)|diffusers]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 10 (Diffusion), Phase 7 Lesson 02 (Self-Attention)`

- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]] — Diffusion
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]

## Concepts taught

- Latent diffusion `lesson term` — Run the entire DDPM in the VAE latent space (4x64x64) instead of pixel space (3x512x512); 48x compute saving
- VAE scale factor `lesson term` — Constant that rescales the VAE's raw latent to roughly unit variance; hardcoded in every SD pipeline
- [[Concepts/Classifier-free guidance|Classifier-free guidance]] `lesson term` — Mix conditional and unconditional noise predictions; the single most impactful inference knob
- Scheduler `lesson term` — The algorithm that turns noise + model predictions into a denoised latent trajectory
- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]] (as *LoRA*) `glossary` — Small rank-decomposition matrices that fine-tune attention layers without touching base weights
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — Attention from latent tokens to text tokens; injects prompt information at every U-Net level
- [[Concepts/ControlNet|ControlNet]] `lesson term` — A separately-trained adapter that steers SD with an extra input (canny, depth, pose, segmentation)
- DPM-Solver++ `lesson term` — Second-order deterministic ODE solver; best quality at low step counts (20-30) in 2026

## Ships

- [[Artifacts/04-11 prompt-sd-pipeline-planner|prompt-sd-pipeline-planner]] `prompt` — Pick SD 1.5 / SDXL / SD3 / FLUX plus scheduler and precision given a latency budget, fidelity target, and licensing constraint
- [[Artifacts/04-11 skill-lora-training-setup|skill-lora-training-setup]] `skill` — Write a full LoRA training config for a custom dataset, including captions, rank, batch size, and learning rate

## Further reading

- [[Resources/LoRA paper|LoRA paper]] ([link](https://arxiv.org/abs/2106.09685)) — LoRA was NLP-first; it transferred to SD with almost no changes ·  also cited by 1 other lesson
- [[Resources/High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)|High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)]] ([link](https://arxiv.org/abs/2112.10752)) — the Stable Diffusion paper; includes every ablation that justifies the design ·  also cited by 2 other lessons
- [[Resources/Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)|Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)]] ([link](https://arxiv.org/abs/2207.12598)) — the CFG paper ·  also cited by 2 other lessons
- diffusers documentation ([link](https://huggingface.co/docs/diffusers)) — the reference for every SD / SDXL / SD3 / FLUX pipeline


%% ── my notes ── %%
