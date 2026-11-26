---
id: "lesson:08/07"
type: lesson
ref: 08/07
phase: 8
num: 7
title: "Latent Diffusion & Stable Diffusion"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 68
aliases:
  - 08/07
  - 08-07
tags:
  - phase/08
  - type/build
  - community/68
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/07-latent-diffusion-stable-diffusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/07-latent-diffusion-stable-diffusion"
---

# 08/07 Latent Diffusion & Stable Diffusion

> Pixel-space diffusion on 512×512 images is a computational war crime. Rombach et al. (2022) noticed that you do not need all 786k dimensions to generate an image — you need enough to capture semantic structure, and a separate decoder for the rest. Run diffusion inside a VAE's latent space. That one idea is Stable Diffusion.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/07-latent-diffusion-stable-diffusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/07-latent-diffusion-stable-diffusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/07-latent-diffusion-stable-diffusion) · code: main.py  
**Community:** [[Communities/68 CFG · ControlNet|68 CFG · ControlNet]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 02 (VAE), Phase 8 · 06 (DDPM), Phase 7 · 09 (ViT)`

- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]] — ViT
- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]] — VAE
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]] — DDPM

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Builds on this

- [[Lessons/08-08 ControlNet, LoRA & Conditioning|08/08 ControlNet, LoRA & Conditioning]]
- [[Lessons/08-09 Inpainting, Outpainting & Image Editing|08/09 Inpainting, Outpainting & Image Editing]]
- [[Lessons/08-10 Video Generation|08/10 Video Generation]]
- [[Lessons/08-12 3D Generation|08/12 3D Generation]]

## Concepts taught

- First stage `lesson term` — Trained encoder/decoder pair; compresses 512² to 64².
- Second stage `lesson term` — Diffusion model over the latent space.
- [[Concepts/CFG|CFG]] `lesson term` — (1+w)·εcond - w·εuncond; tunes conditioning strength.
- Null token `lesson term` — Unconditional embed used for εuncond.
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — Each U-Net block attends to text tokens as K and V.
- [[Concepts/DiT|DiT]] `lesson term` — Replace U-Net with a transformer over latent patches; scales better.
- [[Concepts/MMDiT|MMDiT]] `lesson term` — SD3's architecture: text and image streams with joint attention.
- VAE scaling factor `lesson term` — Divides latents by ~5.4 so diffusion operates in unit-variance space.

## Ships

- [[Artifacts/08-07 sd-prompter|sd-prompter]] `skill` — Configure Stable Diffusion / Flux inference for a given prompt, style, and quality bar.

## Further reading

- [[Resources/High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)|High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)]] ([link](https://arxiv.org/abs/2112.10752)) — Stable Diffusion. ·  also cited by 2 other lessons
- [[Resources/Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)|Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)]] ([link](https://arxiv.org/abs/2207.12598)) — CFG. ·  also cited by 2 other lessons
- [[Resources/Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)|Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)]] ([link](https://arxiv.org/abs/2212.09748)) — DiT. ·  also cited by 3 other lessons
- Podell et al. (2023). SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis ([link](https://arxiv.org/abs/2307.01952)) — SDXL.
- [[Resources/Scaling Rectified Flow Transformers (Esser et al., SD3 paper)|Scaling Rectified Flow Transformers (Esser et al., SD3 paper)]] ([link](https://arxiv.org/abs/2403.03206)) — SD3, MMDiT. ·  also cited by 4 other lessons
- [[Resources/Labs (2024). Flux.1 — Black Forest Labs announcement|Labs (2024). Flux.1 — Black Forest Labs announcement]] ([link](https://blackforestlabs.ai/announcing-black-forest-labs/)) — Flux.1 family. ·  also cited by 1 other lesson
- Hugging Face Diffusers docs ([link](https://huggingface.co/docs/diffusers/index)) — reference implementation for every checkpoint above.


%% ── my notes ── %%
