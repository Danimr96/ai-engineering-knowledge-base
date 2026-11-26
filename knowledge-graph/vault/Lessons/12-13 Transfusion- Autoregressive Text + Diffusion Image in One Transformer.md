---
id: "lesson:12/13"
type: lesson
ref: 12/13
phase: 12
num: 13
title: "Transfusion: Autoregressive Text + Diffusion Image in One Transformer"
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
community: 73
aliases:
  - 12/13
  - 12-13
tags:
  - phase/12
  - type/build
  - community/73
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion"
---

# 12/13 Transfusion: Autoregressive Text + Diffusion Image in One Transformer

> Chameleon and Emu3 bet everything on discrete tokens. They work, but the quantization bottleneck is visible — the image quality plateaus below continuous-space diffusion models. Transfusion (Meta, Zhou et al., August 2024) takes the opposite bet: keep images continuous, drop the VQ-VAE entirely, and train one transformer with two losses. Text tokens get next-token-prediction. Image patches get a flow-matching / diffusion loss. Both objectives optimize the same weights. The architecture underlying Stable Diffusion 3 (MMDiT) is a close cousin. This lesson reads the Transfusion thesis, builds a toy two-loss trainer, and traces the attention mask that lets one transformer do both jobs.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/13-transfusion-autoregressive-diffusion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion) · code: main.py  
**Community:** [[Communities/73 Flow matching · MMDiT · VQ-VAE|73 Flow matching · MMDiT · VQ-VAE]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 11 (Chameleon), Phase 8 (Generative AI)`

- [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]] — Chameleon
- Whole phase: [[Phases/08 Generative AI|Phase 8: Generative AI]] — Generative AI ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-14 Show-o and Discrete-Diffusion Unified Models|12/14 Show-o and Discrete-Diffusion Unified Models]]
- [[Lessons/12-15 Janus-Pro- Decoupled Encoders for Unified Multimodal Models|12/15 Janus-Pro: Decoupled Encoders for Unified Multimodal Models]]

## Concepts taught

- Two-loss training `lesson term` — A single transformer optimizes both cross-entropy on text tokens and MSE on continuous image patches in the same gradient step
- [[Concepts/Flow matching|Flow matching]] `lesson term` — Diffusion variant that predicts a velocity field from noise to clean data; simpler math than DDPM
- [[Concepts/MMDiT|MMDiT]] `lesson term` — Stable Diffusion 3's architecture: joint attention, modality-specific MLPs and norms
- Block-triangular mask `lesson term` — Attention mask that is causal across text but bidirectional within image regions
- Continuous image representation `lesson term` — Image patches as real-valued vectors, not integer codebook indices
- Velocity prediction `lesson term` — Network output is the velocity field between noise and data, not the noise itself

## Ships

- [[Artifacts/12-13 two-loss-trainer-designer|two-loss-trainer-designer]] `skill` — Design a Transfusion / MMDiT-style two-loss training setup (NTP on one modality, diffusion on another) with loss weights, mask design, and schedule.

## Further reading

- [[Resources/Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)|Scalable Diffusion Models with Transformers (Peebles & Xie, 2023)]] ([link](https://arxiv.org/abs/2212.09748)) ·  also cited by 3 other lessons
- [[Resources/Scaling Rectified Flow Transformers (Esser et al., SD3 paper)|Scaling Rectified Flow Transformers (Esser et al., SD3 paper)]] ([link](https://arxiv.org/abs/2403.03206)) ·  also cited by 4 other lessons
- Zhou et al. — Transfusion (arXiv:2408.11039) ([link](https://arxiv.org/abs/2408.11039))
- [[Resources/Xie et al. — Show-o (arXiv-2408.12528)|Xie et al. — Show-o (arXiv:2408.12528)]] ([link](https://arxiv.org/abs/2408.12528)) ·  also cited by 1 other lesson
- Zhao et al. — MonoFormer (arXiv:2409.16280) ([link](https://arxiv.org/abs/2409.16280))


%% ── my notes ── %%
