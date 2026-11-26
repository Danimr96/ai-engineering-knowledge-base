---
id: "lesson:08/01"
type: lesson
ref: 08/01
phase: 8
num: 1
title: "Generative Models — Taxonomy & History"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 88
aliases:
  - 08/01
  - 08-01
tags:
  - phase/08
  - type/learn
  - community/88
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/01-generative-models-taxonomy-history/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/01-generative-models-taxonomy-history"
---

# 08/01 Generative Models — Taxonomy & History

> Every image model, text model, video model, and 3D model fits in one of five buckets. Pick the wrong bucket and you will fight the math for weeks. Pick the right one and the field's last twelve years of progress stacks cleanly in your head.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/01-generative-models-taxonomy-history/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/01-generative-models-taxonomy-history) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/01-generative-models-taxonomy-history) · code: main.py  
**Community:** [[Communities/88 FID · Generative model|88 FID · Generative model]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 2 (ML Fundamentals), Phase 3 (Deep Learning Core), Phase 7 · 14 (Transformers)`

- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]] — Transformers
- Whole phase: [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] — ML Fundamentals ·  medium confidence
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — Deep Learning Core ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]], [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]], [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]
- depth 3: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- [[Lessons/08-14 Evaluation — FID, CLIP Score, Human Preference|08/14 Evaluation — FID, CLIP Score, Human Preference]]

## Concepts taught

- [[Concepts/Generative model|Generative model]] `lesson term` — Learns a sampler for p_data(x), optionally exposes log p(x).
- Explicit density `lesson term` — Model provides a closed-form or tractable log p(x).
- Implicit density `lesson term` — Only a sampler — no way to evaluate p(x) of a given point.
- [[Concepts/ELBO|ELBO]] `lesson term` — A tractable lower bound on log p(x); VAEs and diffusion optimize it.
- Score `lesson term` — ∇x log p(x); diffusion and SDE models learn this field.
- Manifold hypothesis `lesson term` — High-dim data concentrates on a low-dim manifold; why dimensionality reduction works.
- [[Concepts/Autoregressive|Autoregressive]] `glossary` — Factorize joint as product of conditionals.
- Latent `lesson term` — Low-dim representation from which a decoder can reconstruct the input.

## Ships

- [[Artifacts/08-01 generative-model-chooser|generative-model-chooser]] `skill` — Pick a generative-model family, backbone, and hosted alternative for a given task and budget.

## Further reading

- [[Resources/Auto-Encoding Variational Bayes|Auto-Encoding Variational Bayes]] ([link](https://arxiv.org/abs/1312.6114)) — the VAE paper. ·  also cited by 2 other lessons
- [[Resources/Generative Adversarial Networks (Goodfellow et al., 2014)|Generative Adversarial Networks (Goodfellow et al., 2014)]] ([link](https://arxiv.org/abs/1406.2661)) — the GAN paper. ·  also cited by 2 other lessons
- [[Resources/Ho, Jain, Abbeel (2020)- Denoising Diffusion Probabilistic Models|Ho, Jain, Abbeel (2020): Denoising Diffusion Probabilistic Models]] ([link](https://arxiv.org/abs/2006.11239)) — the DDPM paper. ·  also cited by 3 other lessons
- Song et al. (2021). Score-Based Generative Modeling through SDEs ([link](https://arxiv.org/abs/2011.13456)) — diffusion as an SDE.
- [[Resources/Lipman et al. (2023). Flow Matching for Generative Modeling|Lipman et al. (2023). Flow Matching for Generative Modeling]] ([link](https://arxiv.org/abs/2210.02747)) — the flow matching paper. ·  also cited by 1 other lesson
- [[Resources/Scaling Rectified Flow Transformers (Esser et al., SD3 paper)|Scaling Rectified Flow Transformers (Esser et al., SD3 paper)]] ([link](https://arxiv.org/abs/2403.03206)) — Stable Diffusion 3. ·  also cited by 4 other lessons


%% ── my notes ── %%
