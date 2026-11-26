---
id: "lesson:08/10"
type: lesson
ref: 08/10
phase: 8
num: 10
title: Video Generation
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 27
aliases:
  - 08/10
  - 08-10
tags:
  - phase/08
  - type/build
  - community/27
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/10-video-generation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/10-video-generation"
---

# 08/10 Video Generation

> An image is a 2-D tensor. A video is a 3-D one. The theory is the same; the compute is 10-100x harder. OpenAI's Sora (Feb 2024) proved it was possible. By 2026 Veo 2, Kling 1.5, Runway Gen-3, Pika 2.0, and WAN 2.2 ship production video from text at 1080p — and the open-weights stack (CogVideoX, HunyuanVideo, Mochi-1, WAN 2.2) is 12 months behind.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/10-video-generation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/10-video-generation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/10-video-generation) · code: main.py  
**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 07 (Latent Diffusion), Phase 7 · 09 (ViT), Phase 8 · 06 (DDPM)`

- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]] — ViT
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]] — DDPM
- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]] — Latent Diffusion

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- Video VAE `lesson term` — Encoder that compresses (T, H, W, C) → spatiotemporal latent.
- [[Concepts/Patch|Patch]] (as *Patches*) `glossary` — Fixed-size 3-D blocks of the latent; input to the DiT.
- Factorized attention `lesson term` — Run attention over space, then over time; skip full 3-D attention.
- Image-to-video (as *Image-to-video (I2V)*) `lesson term` — Model takes an image + text, outputs a video that starts from it.
- Keyframe conditioning `lesson term` — Pin specific frames to control the video's arc.
- Motion brush `lesson term` — UI input where the user paints motion vectors onto the image.
- Re-captioning `lesson term` — Using an LLM to re-label training clips with detailed prompts.
- Flicker `lesson term` — Frame-to-frame inconsistency; fixed with coupled denoising.

## Ships

- [[Artifacts/08-10 video-brief|video-brief]] `skill` — Translate a video brief into a model + prompt + shot plan for a 2026 video generator.

## Further reading

- Ho, Salimans, Gritsenko et al. (2022). Video Diffusion Models ([link](https://arxiv.org/abs/2204.03458)) — the seminal video diffusion paper.
- Blattmann et al. (2023). Align your Latents (Video LDM) ([link](https://arxiv.org/abs/2304.08818)) — Stable Video Diffusion's ancestor.
- Yang et al. (2024). CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer ([link](https://arxiv.org/abs/2408.06072)) — CogVideoX.
- Kong et al. (2024). HunyuanVideo: A Systematic Framework for Large Video Generative Models ([link](https://arxiv.org/abs/2412.03603)) — HunyuanVideo.
- Genmo (2024). Mochi-1 Technical Report ([link](https://www.genmo.ai/blog/mochi)) — Mochi-1.
- [[Resources/Sora technical report (OpenAI)|Sora technical report (OpenAI)]] ([link](https://openai.com/index/video-generation-models-as-world-simulators/)) — Sora technical report. ·  also cited by 1 other lesson
- Alibaba (2025). WAN 2.2 ([link](https://wanvideo.io/)) — open SOTA mid-2025.


%% ── my notes ── %%
