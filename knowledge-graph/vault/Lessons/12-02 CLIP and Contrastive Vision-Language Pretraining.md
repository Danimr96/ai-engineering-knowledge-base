---
id: "lesson:12/02"
type: lesson
ref: 12/02
phase: 12
num: 2
title: CLIP and Contrastive Vision-Language Pretraining
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 1
community: 40
aliases:
  - 12/02
  - 12-02
tags:
  - phase/12
  - type/build
  - community/40
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/02-clip-contrastive-pretraining/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/02-clip-contrastive-pretraining"
---

# 12/02 CLIP and Contrastive Vision-Language Pretraining

> OpenAI's CLIP (2021) proved a single idea big enough to power the next five years: align an image encoder and a text encoder in the same vector space using only noisy web image-caption pairs and a contrastive loss. Zero supervised labels. 400M pairs. The resulting embedding space does zero-shot classification, image-text retrieval, and plugs into every 2026 VLM as its vision tower. SigLIP 2 (2025) replaced softmax with sigmoid and scaled past CLIP at lower cost. This lesson walks the math from InfoNCE to sigmoid pairwise loss and builds the training step in stdlib Python.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/02-clip-contrastive-pretraining/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/02-clip-contrastive-pretraining) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/02-clip-contrastive-pretraining) · code: main.py  
**Community:** [[Communities/40 NaFlex · Backbone · Hard negative|40 NaFlex · Backbone · Hard negative]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 01 (ViT patches), Phase 7 (Transformers)`

- [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]] — ViT patches
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — Transformers ·  medium confidence

## Builds on this

- [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]]
- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]

## Concepts taught

- [[Concepts/InfoNCE|InfoNCE]] `lesson term` — Cross-entropy over a batch's similarity matrix; each item's positive is its paired item, negatives are everything else
- Sigmoid loss `lesson term` — Per-pair binary cross-entropy; no softmax, no all-gather, scales cheaply in distributed training
- [[Concepts/Temperature|Temperature]] `glossary` — Scalar that scales logits before softmax/sigmoid; controls sharpness of the distribution
- [[Concepts/Zero-Shot|Zero-Shot]] `glossary` — Use text prompts to construct class embeddings and classify by cosine similarity; no training on target classes
- [[Concepts/Prompt template|Prompt template]] `lesson term` — Text scaffold around a class name; affects zero-shot accuracy by 1-5 points
- Dual encoder `lesson term` — One image encoder + one text encoder, outputs in shared D-dim space
- [[Concepts/Hard negative|Hard negative]] `lesson term` — A negative similar enough to the positive that the model has to work to separate them
- [[Concepts/Linear probe|Linear probe]] `lesson term` — Train only a linear classifier on top of frozen features; measures feature quality
- [[Concepts/NaFlex|NaFlex]] `lesson term` — SigLIP 2 capability to ingest images at any aspect ratio and resolution without resizing
- Temperature scaling `lesson term` — CLIP parametrizes log(1/tau) so gradients behave; clips to prevent collapse to near-zero tau
- [[Concepts/Shared Embedding Space|Shared Embedding Space]] `glossary` — A common vector space in which representations from different modalities can be compared with the same similarity function.

## Ships

- [[Artifacts/12-02 clip-zero-shot|clip-zero-shot]] `skill` — Run zero-shot image classification with a CLIP / SigLIP checkpoint, producing ranked predictions with similarity scores.

## Further reading

- Jia et al. — ALIGN (arXiv:2102.05918) ([link](https://arxiv.org/abs/2102.05918)) — scale with noisy web data.
- [[Resources/CLIP|CLIP]] ([link](https://arxiv.org/abs/2103.00020)) — the CLIP paper. ·  also cited by 2 other lessons
- Cherti et al. — Reproducible scaling laws for contrastive language-image learning (arXiv:2212.07143) ([link](https://arxiv.org/abs/2212.07143)) — OpenCLIP scaling laws.
- [[Resources/SigLIP- Sigmoid Loss for Language-Image Pre-Training (Zhai et al., 2023)|SigLIP: Sigmoid Loss for Language-Image Pre-Training (Zhai et al., 2023)]] ([link](https://arxiv.org/abs/2303.15343)) — SigLIP. ·  also cited by 1 other lesson
- [[Resources/Tschannen et al. — SigLIP 2 (arXiv-2502.14786)|Tschannen et al. — SigLIP 2 (arXiv:2502.14786)]] ([link](https://arxiv.org/abs/2502.14786)) — multilingual + NaFlex. ·  also cited by 2 other lessons


%% ── my notes ── %%
