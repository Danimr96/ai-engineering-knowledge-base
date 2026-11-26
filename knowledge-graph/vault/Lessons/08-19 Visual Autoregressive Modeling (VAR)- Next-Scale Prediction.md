---
id: "lesson:08/19"
type: lesson
ref: 08/19
phase: 8
num: 19
title: "Visual Autoregressive Modeling (VAR): Next-Scale Prediction"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
libraries:
  - numpy
aliases:
  - 08/19
  - 08-19
tags:
  - phase/08
  - type/build
source: ai-engineering-from-scratch/phases/08-generative-ai/19-visual-autoregressive-var/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/19-visual-autoregressive-var"
---

# 08/19 Visual Autoregressive Modeling (VAR): Next-Scale Prediction

> Diffusion models sample iteratively in time (denoising steps). VAR samples iteratively in scale — it predicts a 1x1 token, then 2x2, then 4x4, up to the final resolution, each scale conditioning on the previous. The 2024 paper showed VAR matches GPT-style scaling laws for image generation and beats DiT at the same compute budget. This lesson builds the core mechanism.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/19-visual-autoregressive-var/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/19-visual-autoregressive-var) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/19-visual-autoregressive-var) · code: main.py  
**Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 7 Lesson 03 (Multi-Head Attention), Phase 8 Lesson 06 (DDPM)`

- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]] — Multi-Head Attention
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]] — DDPM

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- VAR `lesson term` — Image generation by next-scale prediction over a pyramid of VQ token grids
- Next-scale prediction `lesson term` — The model predicts tokens at increasing resolution scales, conditioning on all previous scales
- Multi-scale VQ tokenizer `lesson term` — VQ-VAE that produces K token grids of increasing resolution, with decoder summing all scales
- Scale k `lesson term` — One of K resolution levels, from 1x1 at k=1 up to (H/p)x(W/p) at k=K
- Parallel-within-scale `lesson term` — All tokens at scale k are predicted in one transformer pass, not autoregressively
- Causal-across-scales `lesson term` — Token at scale k can attend to all of scales 1..k but not scales k+1..K
- [[Concepts/Residual VQ|Residual VQ]] `lesson term` — Each scale's tokens encode the residual left by lower scales; decoder sums all scale embeddings
- VAR scaling law `lesson term` — FID follows a predictable power law in compute, like language models' perplexity
- HART `lesson term` — Text-conditional VAR variant combining MaskGIT-style iterative decoding with VAR's scale structure
- Scale position embedding `lesson term` — Positional encoding carries both the scale index and spatial coordinates within the scale

## Ships

- [[Artifacts/08-19 var-tokenizer-designer|var-tokenizer-designer]] `skill` — Design a multi-scale residual VQ tokenizer for next-scale visual autoregressive image generation.

## Further reading

- [[Resources/VQ-VAE|VQ-VAE]] ([link](https://arxiv.org/abs/1711.00937)) — VQ-VAE, the foundation of discrete image tokenization ·  also cited by 1 other lesson
- Esser et al., 2021 — "Taming Transformers for High-Resolution Image Synthesis ([link](https://arxiv.org/abs/2012.09841)) — VQGAN, the tokenizer family VAR's multi-scale tokenizer extends
- [[Resources/Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)|Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)]] ([link](https://arxiv.org/abs/2212.09748)) — DiT, the diffusion comparison baseline ·  also cited by 3 other lessons
- [[Resources/Tian et al., 2024 — -Visual Autoregressive Modeling- Scalable Image Generation via Next-Scale Prediction|Tian et al., 2024 — "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction]] ([link](https://arxiv.org/abs/2404.02905)) — the VAR paper, canonical reference ·  also cited by 1 other lesson
- Tang et al., 2024 — "HART: Efficient Visual Generation with Hybrid Autoregressive Transformer ([link](https://arxiv.org/abs/2410.10812)) — text-conditional VAR


%% ── my notes ── %%
