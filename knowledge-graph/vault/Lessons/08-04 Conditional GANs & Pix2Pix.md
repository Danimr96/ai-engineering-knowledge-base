---
id: "lesson:08/04"
type: lesson
ref: 08/04
phase: 8
num: 4
title: "Conditional GANs & Pix2Pix"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 3
community: 72
aliases:
  - 08/04
  - 08-04
tags:
  - phase/08
  - type/build
  - community/72
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/04-conditional-gans-pix2pix/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/04-conditional-gans-pix2pix"
---

# 08/04 Conditional GANs & Pix2Pix

> The first big unlock of 2014-2017 was controlling what a GAN makes. Attach a label, or an image, or a sentence. Pix2Pix did the image version and it still beats every generic text-to-image model on narrow image-to-image tasks.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/04-conditional-gans-pix2pix/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/04-conditional-gans-pix2pix) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/04-conditional-gans-pix2pix) · code: main.py  
**Community:** [[Communities/72 Early stopping · Layer normalization · RMSNorm|72 Early stopping · Layer normalization · RMSNorm]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 03 (GANs), Phase 4 · 06 (U-Net), Phase 3 · 07 (CNNs)`

- [[Lessons/03-07 Regularization|03/07 Regularization]] — CNNs
- [[Lessons/04-06 Object Detection — YOLO from Scratch|04/06 Object Detection — YOLO from Scratch]] — U-Net
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]] — GANs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- Conditional GAN `lesson term` — G(z, c), D(x, c). Both networks see the condition.
- Pix2Pix `lesson term` — Paired cGAN with U-Net G and PatchGAN D + L1 loss.
- U-Net `lesson term` — Symmetric conv network; skips preserve high-freq.
- PatchGAN `lesson term` — D outputs per-patch score instead of global score.
- CycleGAN `lesson term` — Two G's + cycle-consistency loss; no paired data.
- SPADE `lesson term` — Normalizes intermediate activations with the semantic map; segmentation-to-image.
- FiLM `lesson term` — Per-feature affine transform from the condition; cheap conditioning.

## Ships

- [[Artifacts/08-04 img2img-chooser|img2img-chooser]] `skill` — Pick an image-to-image approach given paired vs unpaired data, domain specificity, and latency budget.

## Further reading

- Mirza & Osindero (2014). Conditional Generative Adversarial Nets ([link](https://arxiv.org/abs/1411.1784)) — the cGAN paper.
- Isola et al. (2017). Image-to-Image Translation with Conditional Adversarial Networks ([link](https://arxiv.org/abs/1611.07004)) — Pix2Pix.
- Zhu et al. (2017). Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks ([link](https://arxiv.org/abs/1703.10593)) — CycleGAN.
- Wang et al. (2018). High-Resolution Image Synthesis with Conditional GANs ([link](https://arxiv.org/abs/1711.11585)) — Pix2PixHD.
- Miyato & Koyama (2018). cGANs with Projection Discriminator ([link](https://arxiv.org/abs/1802.05637)) — the projection D.
- Park et al. (2019). Semantic Image Synthesis with Spatially-Adaptive Normalization ([link](https://arxiv.org/abs/1903.07291)) — SPADE / GauGAN.


%% ── my notes ── %%
