---
id: "lesson:08/05"
type: lesson
ref: 08/05
phase: 8
num: 5
title: StyleGAN
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 37
aliases:
  - 08/05
  - 08-05
tags:
  - phase/08
  - type/build
  - community/37
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/05-stylegan/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/05-stylegan"
---

# 08/05 StyleGAN

> Most generators stir `z` into every layer at the same time. StyleGAN split it apart: first map `z` to an intermediate `w`, then *inject* `w` at every resolution level through AdaIN. That single change untangled the latent space and made photorealistic faces a solved problem for seven years running.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/05-stylegan/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/05-stylegan) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/05-stylegan) · code: main.py  
**Community:** [[Communities/37 Discriminator · Generator · Minimax|37 Discriminator · Generator · Minimax]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 03 (GANs), Phase 4 · 08 (Normalization), Phase 3 · 07 (CNNs)`

- [[Lessons/03-07 Regularization|03/07 Regularization]] — CNNs
- [[Lessons/04-08 Instance Segmentation — Mask R-CNN|04/08 Instance Segmentation — Mask R-CNN]] — Normalization
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]] — GANs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- Mapping network `lesson term` — f: Z → W, 8 layers, decouples latent geometry from data statistics.
- W space `lesson term` — Output of the mapping network; roughly disentangled.
- AdaIN `lesson term` — Normalize feature map, then scale + shift by w-projection.
- Truncation trick `lesson term` — w = mean + ψ·(w - mean), ψ<1 trades diversity for quality.
- Path-length regularization `lesson term` — Penalizes large changes in image per unit change in w; makes W smoother.
- Weight demodulation `lesson term` — Normalize conv weights instead of activations; kills droplet artifacts.
- Alias-free `lesson term` — Windowed sinc filters; eliminates texture sticking to the pixel grid.
- Inversion `lesson term` — Optimize or encode x → w so G(w) ≈ x.

## Ships

- [[Artifacts/08-05 stylegan-inversion|stylegan-inversion]] `skill` — Choose an inversion and editing pipeline for a pretrained StyleGAN over a real photo.

## Further reading

- Karras et al. (2019). A Style-Based Generator Architecture for GANs ([link](https://arxiv.org/abs/1812.04948)) — StyleGAN.
- [[Resources/Karras et al. (2020). Analyzing and Improving the Image Quality of StyleGAN|Karras et al. (2020). Analyzing and Improving the Image Quality of StyleGAN]] ([link](https://arxiv.org/abs/1912.04958)) — StyleGAN2. ·  also cited by 1 other lesson
- Tov et al. (2021). Designing an Encoder for StyleGAN Image Manipulation ([link](https://arxiv.org/abs/2102.02766)) — e4e inversion.
- [[Resources/StyleGAN3 (Karras et al., 2021)|StyleGAN3 (Karras et al., 2021)]] ([link](https://arxiv.org/abs/2106.12423)) — StyleGAN3. ·  also cited by 2 other lessons
- Sauer et al. (2022). StyleGAN-XL: Scaling StyleGAN to Large Diverse Datasets ([link](https://arxiv.org/abs/2202.00273)) — StyleGAN-XL.
- Huang et al. (2024). R3GAN: The GAN is dead; long live the GAN! ([link](https://arxiv.org/abs/2501.05441)) — modern minimal GAN recipe.


%% ── my notes ── %%
