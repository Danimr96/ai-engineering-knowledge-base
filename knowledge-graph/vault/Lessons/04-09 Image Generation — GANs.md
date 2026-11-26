---
id: "lesson:04/09"
type: lesson
ref: 04/09
phase: 4
num: 9
title: "Image Generation — GANs"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
community: 37
libraries:
  - numpy
  - torch
aliases:
  - 04/09
  - 04-09
tags:
  - phase/04
  - type/build
  - community/37
source: ai-engineering-from-scratch/phases/04-computer-vision/09-image-generation-gans/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/09-image-generation-gans"
---

# 04/09 Image Generation — GANs

> A GAN is two neural networks in a fixed game. One draws, one critiques. They get better together until the drawings fool the critic.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/09-image-generation-gans/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/09-image-generation-gans) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/09-image-generation-gans) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/37 Discriminator · Generator · Minimax|37 Discriminator · Generator · Minimax]] · **Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 3 Lesson 06 (Optimizers), Phase 3 Lesson 07 (Regularization)`

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Optimizers
- [[Lessons/03-07 Regularization|03/07 Regularization]] — Regularization
- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]

## Concepts taught

- [[Concepts/Generator|Generator]] (as *Generator (G)*) `lesson term` — Maps noise to images; trained to fool the discriminator
- [[Concepts/Discriminator|Discriminator]] (as *Discriminator (D)*) `lesson term` — Binary classifier; trained to distinguish real from generated images
- [[Concepts/Minimax|Minimax]] `lesson term` — min over G, max over D of an adversarial loss; equilibrium is p_G = p_data
- [[Concepts/Non-saturating loss|Non-saturating loss]] `lesson term` — G's loss is -log(D(G(z))) instead of log(1 - D(G(z))) to avoid vanishing gradients early in training
- [[Concepts/Mode collapse|Mode collapse]] `lesson term` — G produces only a small subset of the data distribution; fix with SN, minibatch discrimination, or larger batch
- TTUR `lesson term` — D learns faster than G, typically by a factor of 2-4; stabilises training
- [[Concepts/Spectral norm|Spectral norm]] `lesson term` — A weight-normalisation that bounds each layer's Lipschitz constant; stops D from becoming arbitrarily steep
- [[Concepts/FID|FID]] `lesson term` — Distance between Inception-v3 feature distributions of real and generated sets; the standard evaluation metric

## Ships

- [[Artifacts/04-09 prompt-gan-training-triage|prompt-gan-training-triage]] `prompt` — Read a description of GAN training curves and pick the failure mode plus the single recommended fix
- [[Artifacts/04-09 skill-dcgan-scaffold|skill-dcgan-scaffold]] `skill` — Write a complete DCGAN scaffold from z_dim, image_size, and num_channels, including training loop and sample saver

## Further reading

- [[Resources/Generative Adversarial Networks (Goodfellow et al., 2014)|Generative Adversarial Networks (Goodfellow et al., 2014)]] ([link](https://arxiv.org/abs/1406.2661)) — the paper that started it all ·  also cited by 2 other lessons
- [[Resources/DCGAN (Radford, Metz, Chintala, 2015)|DCGAN (Radford, Metz, Chintala, 2015)]] ([link](https://arxiv.org/abs/1511.06434)) — the architecture rules that made GANs trainable ·  also cited by 1 other lesson
- [[Resources/Spectral Normalization for GANs (Miyato et al., 2018)|Spectral Normalization for GANs (Miyato et al., 2018)]] ([link](https://arxiv.org/abs/1802.05957)) — the single most useful stabilisation trick ·  also cited by 1 other lesson
- [[Resources/StyleGAN3 (Karras et al., 2021)|StyleGAN3 (Karras et al., 2021)]] ([link](https://arxiv.org/abs/2106.12423)) — the SOTA GAN; reads like a greatest-hits album of every trick from the last decade ·  also cited by 2 other lessons


%% ── my notes ── %%
