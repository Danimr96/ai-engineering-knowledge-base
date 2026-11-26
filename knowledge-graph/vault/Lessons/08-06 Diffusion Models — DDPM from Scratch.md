---
id: "lesson:08/06"
type: lesson
ref: 08/06
phase: 8
num: 6
title: "Diffusion Models — DDPM from Scratch"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 2
community: 27
aliases:
  - 08/06
  - 08-06
tags:
  - phase/08
  - type/build
  - community/27
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/06-diffusion-ddpm-from-scratch/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/06-diffusion-ddpm-from-scratch"
---

# 08/06 Diffusion Models — DDPM from Scratch

> Ho, Jain, Abbeel (2020) gave the field a recipe it could not quit. Destroy the data with noise over a thousand small steps. Train one neural net to predict the noise. Reverse the process at inference. Today every mainstream image, video, 3D, and music model runs on this loop, possibly with flow matching or consistency tricks on top.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/06-diffusion-ddpm-from-scratch/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/06-diffusion-ddpm-from-scratch) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/06-diffusion-ddpm-from-scratch) · code: main.py  
**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 02 (Backprop), Phase 8 · 02 (VAE)`

- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]] — Backprop
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]] — VAE

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]
- depth 3: [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Builds on this

- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]]
- [[Lessons/08-10 Video Generation|08/10 Video Generation]]
- [[Lessons/08-11 Audio Generation|08/11 Audio Generation]]
- [[Lessons/08-13 Flow Matching & Rectified Flows|08/13 Flow Matching & Rectified Flows]]
- [[Lessons/08-19 Visual Autoregressive Modeling (VAR)- Next-Scale Prediction|08/19 Visual Autoregressive Modeling (VAR): Next-Scale Prediction]]

## Concepts taught

- [[Concepts/Forward process|Forward process]] `lesson term` — Fixed Markov chain q(x_t | x{t-1}) that destroys the data.
- [[Concepts/Reverse process|Reverse process]] `lesson term` — Learned chain pθ(x{t-1} | x_t) that reconstructs the data.
- [[Concepts/Schedule|Schedule]] (as *β schedule*) `lesson term` — Per-step variance; linear, cosine, or sigmoid.
- Simple loss `lesson term` — ||ε - εθ(x_t, t)||²; all variational derivations collapse to this.
- ε-prediction `lesson term` — Output is the noise added; standard DDPM.
- V-prediction `lesson term` — Output is α·ε - σ·x; better conditioning across t.
- DDPM `lesson term` — Ho et al. 2020; linear β, 1000 steps, U-Net.
- DDIM `lesson term` — Non-Markov sampler, 20-50 steps, same training objective.
- [[Concepts/Classifier-free guidance|Classifier-free guidance]] `lesson term` — Mix conditional and unconditional noise predictions to amplify conditioning.

## Ships

- [[Artifacts/08-06 diffusion-trainer|diffusion-trainer]] `skill` — Configure a diffusion training run: schedule, prediction target, sampler, and eval plan.

## Further reading

- Sohl-Dickstein et al. (2015). Deep Unsupervised Learning using Nonequilibrium Thermodynamics ([link](https://arxiv.org/abs/1503.03585)) — the diffusion paper, ahead of its time.
- [[Resources/Ho, Jain, Abbeel (2020)- Denoising Diffusion Probabilistic Models|Ho, Jain, Abbeel (2020): Denoising Diffusion Probabilistic Models]] ([link](https://arxiv.org/abs/2006.11239)) — DDPM. ·  also cited by 3 other lessons
- [[Resources/DDIM (Song, Meng, Ermon, 2020)|DDIM (Song, Meng, Ermon, 2020)]] ([link](https://arxiv.org/abs/2010.02502)) — DDIM, fewer steps. ·  also cited by 1 other lesson
- [[Resources/Improved DDPM (Nichol & Dhariwal, 2021)|Improved DDPM (Nichol & Dhariwal, 2021)]] ([link](https://arxiv.org/abs/2102.09672)) — cosine schedule, learned variance. ·  also cited by 1 other lesson
- Dhariwal & Nichol (2021). Diffusion Models Beat GANs on Image Synthesis ([link](https://arxiv.org/abs/2105.05233)) — classifier guidance.
- [[Resources/Elucidating the Design Space of Diffusion (Karras et al., 2022)|Elucidating the Design Space of Diffusion (Karras et al., 2022)]] ([link](https://arxiv.org/abs/2206.00364)) — unified notation, cleanest recipe. ·  also cited by 2 other lessons
- [[Resources/Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)|Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)]] ([link](https://arxiv.org/abs/2207.12598)) — CFG. ·  also cited by 2 other lessons


%% ── my notes ── %%
