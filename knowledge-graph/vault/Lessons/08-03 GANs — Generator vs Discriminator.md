---
id: "lesson:08/03"
type: lesson
ref: 08/03
phase: 8
num: 3
title: "GANs — Generator vs Discriminator"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 37
aliases:
  - 08/03
  - 08-03
tags:
  - phase/08
  - type/build
  - community/37
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/03-gans-generator-discriminator/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/03-gans-generator-discriminator"
---

# 08/03 GANs — Generator vs Discriminator

> Goodfellow's trick in 2014 was to skip density entirely. Two networks. One makes fakes. One catches them. They fight until the fakes are indistinguishable from real. It shouldn't work. It often doesn't. When it does, the samples are still the sharpest in the literature for narrow domains.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/03-gans-generator-discriminator/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/03-gans-generator-discriminator) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/03-gans-generator-discriminator) · code: main.py  
**Community:** [[Communities/37 Discriminator · Generator · Minimax|37 Discriminator · Generator · Minimax]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 02 (Backprop), Phase 3 · 08 (Optimizers), Phase 8 · 02 (VAE)`

- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]] — Backprop
- [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]] — Optimizers
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]] — VAE

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]
- depth 3: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Builds on this

- [[Lessons/08-04 Conditional GANs & Pix2Pix|08/04 Conditional GANs & Pix2Pix]]
- [[Lessons/08-05 StyleGAN|08/05 StyleGAN]]

## Concepts taught

- [[Concepts/Generator|Generator]] `lesson term` — Noise-to-sample network, G: z → x̂.
- [[Concepts/Discriminator|Discriminator]] `lesson term` — Classifier D: x → [0, 1], real vs fake.
- [[Concepts/Minimax|Minimax]] `lesson term` — min_G max_D of a joint objective.
- [[Concepts/Non-saturating loss|Non-saturating loss]] `lesson term` — Use -log D(G(z)) for G instead of log(1 - D(G(z))).
- [[Concepts/Mode collapse|Mode collapse]] `lesson term` — Generator produces few distinct outputs despite diverse data.
- WGAN `lesson term` — Replace BCE with Earth-Mover distance + gradient penalty; smoother gradient.
- [[Concepts/Spectral norm|Spectral norm]] `lesson term` — Constrain D's weight norms to bound its slope; stabilizes training.
- StyleGAN `lesson term` — Mapping network + AdaIN; best-in-class for faces, still in 2026.

## Ships

- [[Artifacts/08-03 gan-debugger|gan-debugger]] `skill` — Diagnose failing GAN training from loss curves and sample grids; prescribe one-line fixes.

## Further reading

- [[Resources/Generative Adversarial Networks (Goodfellow et al., 2014)|Generative Adversarial Networks (Goodfellow et al., 2014)]] ([link](https://arxiv.org/abs/1406.2661)) — the original GAN paper. ·  also cited by 2 other lessons
- [[Resources/DCGAN (Radford, Metz, Chintala, 2015)|DCGAN (Radford, Metz, Chintala, 2015)]] ([link](https://arxiv.org/abs/1511.06434)) — the first stable architecture. ·  also cited by 1 other lesson
- [[Resources/Wasserstein GAN (Arjovsky et al., 2017)|Wasserstein GAN (Arjovsky et al., 2017)]] ([link](https://arxiv.org/abs/1701.07875)) — WGAN. ·  also cited by 1 other lesson
- [[Resources/Spectral Normalization for GANs (Miyato et al., 2018)|Spectral Normalization for GANs (Miyato et al., 2018)]] ([link](https://arxiv.org/abs/1802.05957)) — SN. ·  also cited by 1 other lesson
- [[Resources/Karras et al. (2020). Analyzing and Improving the Image Quality of StyleGAN|Karras et al. (2020). Analyzing and Improving the Image Quality of StyleGAN]] ([link](https://arxiv.org/abs/1912.04958)) — StyleGAN2. ·  also cited by 1 other lesson
- [[Resources/StyleGAN3 (Karras et al., 2021)|StyleGAN3 (Karras et al., 2021)]] ([link](https://arxiv.org/abs/2106.12423)) — StyleGAN3. ·  also cited by 2 other lessons
- [[Resources/Sauer et al. (2023). Adversarial Diffusion Distillation|Sauer et al. (2023). Adversarial Diffusion Distillation]] ([link](https://arxiv.org/abs/2311.17042)) — SDXL-Turbo. ·  also cited by 1 other lesson


%% ── my notes ── %%
