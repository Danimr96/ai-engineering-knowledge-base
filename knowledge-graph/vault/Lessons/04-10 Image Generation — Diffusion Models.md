---
id: "lesson:04/10"
type: lesson
ref: 04/10
phase: 4
num: 10
title: "Image Generation — Diffusion Models"
lesson_type: build
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
  - 04/10
  - 04-10
tags:
  - phase/04
  - type/build
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/10-image-generation-diffusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/10-image-generation-diffusion"
---

# 04/10 Image Generation — Diffusion Models

> A diffusion model learns to denoise. Train it to remove a tiny bit of noise from a noisy image, repeat that backwards a thousand times, and you have an image generator.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/10-image-generation-diffusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/10-image-generation-diffusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/10-image-generation-diffusion) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 07 (U-Net), Phase 1 Lesson 06 (Probability), Phase 3 Lesson 06 (Optimizers)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Probability
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Optimizers
- [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]] — U-Net

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]

## Builds on this

- [[Lessons/04-11 Stable Diffusion — Architecture & Fine-Tuning|04/11 Stable Diffusion — Architecture & Fine-Tuning]]
- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-22 3D Gaussian Splatting from Scratch|04/22 3D Gaussian Splatting from Scratch]]
- [[Lessons/04-23 Diffusion Transformers & Rectified Flow|04/23 Diffusion Transformers & Rectified Flow]]
- [[Lessons/04-28 World Models & Video Diffusion|04/28 World Models & Video Diffusion]]
- [[Lessons/06-09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake|06/09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake]]

## Concepts taught

- [[Concepts/Forward process|Forward process]] `lesson term` — Fixed Markov chain that corrupts an image into Gaussian noise over T steps
- [[Concepts/Reverse process|Reverse process]] `lesson term` — Learned distribution that walks back from noise to image
- Epsilon prediction `lesson term` — The training target: epsilon_theta(x_t, t) predicts the noise added at step t
- Beta schedule `lesson term` — Sequence of T small variances that define how much noise enters per step
- alpha_bar_t `lesson term` — Product of (1 - beta_s) up to time t; bigger t means less signal left
- DDPM sampler `lesson term` — Samples each x{t-1} from its conditional Gaussian; 1000 steps
- DDIM sampler `lesson term` — Rewrites sampling as a deterministic ODE; 20-100 steps with similar quality
- Time conditioning `lesson term` — Sinusoidal embedding of t injected into the U-Net so it knows the noise level

## Ships

- [[Artifacts/04-10 prompt-diffusion-sampler-picker|prompt-diffusion-sampler-picker]] `prompt` — Pick DDPM, DDIM, DPM-Solver++, or Euler ancestral based on quality target, latency budget, and conditioning type
- [[Artifacts/04-10 skill-noise-schedule-designer|skill-noise-schedule-designer]] `skill` — Produce a linear, cosine, or sigmoid beta schedule given T and target corruption level, plus SNR plot

## Further reading

- [[Resources/Ho, Jain, Abbeel (2020)- Denoising Diffusion Probabilistic Models|Ho, Jain, Abbeel (2020): Denoising Diffusion Probabilistic Models]] ([link](https://arxiv.org/abs/2006.11239)) — the paper that made diffusion practical and beat GANs on FID ·  also cited by 3 other lessons
- [[Resources/DDIM (Song, Meng, Ermon, 2020)|DDIM (Song, Meng, Ermon, 2020)]] ([link](https://arxiv.org/abs/2010.02502)) — the deterministic sampler that made real-time inference possible ·  also cited by 1 other lesson
- [[Resources/Improved DDPM (Nichol & Dhariwal, 2021)|Improved DDPM (Nichol & Dhariwal, 2021)]] ([link](https://arxiv.org/abs/2102.09672)) — cosine schedule and v-parameterisation ·  also cited by 1 other lesson
- [[Resources/Elucidating the Design Space of Diffusion (Karras et al., 2022)|Elucidating the Design Space of Diffusion (Karras et al., 2022)]] ([link](https://arxiv.org/abs/2206.00364)) — a unified view of every diffusion design choice; current best reference ·  also cited by 2 other lessons


%% ── my notes ── %%
