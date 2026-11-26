---
id: "lesson:08/02"
type: lesson
ref: 08/02
phase: 8
num: 2
title: "Autoencoders & Variational Autoencoders (VAE)"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 27
aliases:
  - 08/02
  - 08-02
tags:
  - phase/08
  - type/build
  - community/27
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/02-autoencoders-vae/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/02-autoencoders-vae"
---

# 08/02 Autoencoders & Variational Autoencoders (VAE)

> A plain autoencoder compresses then reconstructs. It memorizes. It does not generate. Add one trick — force the code to look Gaussian — and you get a sampler. That single trick, the reparameterization of `z = μ + σ·ε`, is why every latent-diffusion and flow-matching image model you use in 2026 has a VAE at the input.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/02-autoencoders-vae/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/02-autoencoders-vae) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/02-autoencoders-vae) · code: main.py  
**Community:** [[Communities/27 Decision boundary · Bias · ELBO|27 Decision boundary · Bias · ELBO]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 02 (Backprop), Phase 3 · 07 (CNNs), Phase 8 · 01 (Taxonomy)`

- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]] — Backprop
- [[Lessons/03-07 Regularization|03/07 Regularization]] — CNNs
- [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]] — Taxonomy

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- depth 3: [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]], [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]], [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]

## Builds on this

- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]]
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]]
- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]]

## Concepts taught

- Autoencoder `lesson term` — x → z → x̂, learn MSE. Not generative.
- [[Concepts/VAE (Variational Autoencoder)|VAE (Variational Autoencoder)]] (as *VAE*) `glossary` — Encoder outputs a distribution, KL penalty shapes code space.
- [[Concepts/ELBO|ELBO]] `lesson term` — log p(x) ≥ recon - KL[q(z|x) || p(z)]; tight when q = p(z|x).
- Reparameterization `lesson term` — Rewrites stochastic node as deterministic + pure noise. Enables backprop through sampling.
- [[Concepts/Prior|Prior]] `lesson term` — Target distribution for the latent, typically N(0, I).
- Posterior collapse `lesson term` — Encoder ignores x, outputs the prior; decoder must hallucinate.
- [[Concepts/VQ-VAE|VQ-VAE]] `lesson term` — Replace continuous z with nearest codebook vector; enables transformer modelling.

## Ships

- [[Artifacts/08-02 vae-trainer|vae-trainer]] `skill` — Specify VAE architecture, latent size, beta schedule, and eval plan for a given dataset and downstream use.

## Further reading

- [[Resources/Auto-Encoding Variational Bayes|Auto-Encoding Variational Bayes]] ([link](https://arxiv.org/abs/1312.6114)) — the VAE paper. ·  also cited by 2 other lessons
- [[Resources/VQ-VAE|VQ-VAE]] ([link](https://arxiv.org/abs/1711.00937)) — VQ-VAE. ·  also cited by 1 other lesson
- Vahdat & Kautz (2021). NVAE: A Deep Hierarchical Variational Autoencoder ([link](https://arxiv.org/abs/2007.03898)) — state-of-the-art image VAE.
- [[Resources/High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)|High-Resolution Image Synthesis with Latent Diffusion (Rombach et al., 2022)]] ([link](https://arxiv.org/abs/2112.10752)) — Stable Diffusion; VAE as encoder. ·  also cited by 2 other lessons
- [[Resources/Défossez et al. (2023). EnCodec|Défossez et al. (2023). EnCodec]] ([link](https://arxiv.org/abs/2210.13438)) — Encodec, the audio VAE standard. ·  also cited by 2 other lessons
- Higgins et al. (2017). β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework ([link](https://openreview.net/forum?id=Sy2fzU9gl)) — disentangled β-VAE.


%% ── my notes ── %%
