---
id: "lesson:12/01"
type: lesson
ref: 12/01
phase: 12
num: 1
title: Vision Transformers and the Patch-Token Primitive
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 0
community: 40
aliases:
  - 12/01
  - 12-01
tags:
  - phase/12
  - type/learn
  - community/40
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/01-vision-transformer-patch-tokens/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/01-vision-transformer-patch-tokens"
---

# 12/01 Vision Transformers and the Patch-Token Primitive

> Before anything multimodal, an image has to become a sequence of tokens a transformer can eat. The 2020 ViT paper answered this with 16x16 pixel patches, a linear projection, and a position embedding. Five years later every 2026 frontier model (Claude Opus 4.7 at 2576px native, Gemini 3.1 Pro, Qwen3.5-Omni) still begins this way — the encoder changed from ViT to DINOv2 to SigLIP 2, register tokens were added, the positional scheme became 2D-RoPE, but the primitive held. This lesson reads the patch-token pipeline end to end and builds it in stdlib Python so the rest of Phase 12 has a concrete mental model for "visual tokens."

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/01-vision-transformer-patch-tokens/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/01-vision-transformer-patch-tokens) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/01-vision-transformer-patch-tokens) · code: main.py  
**Community:** [[Communities/40 NaFlex · Backbone · Hard negative|40 NaFlex · Backbone · Hard negative]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 (Transformers), Phase 4 (Computer Vision)`

- Whole phase: [[Phases/04 Computer Vision|Phase 4: Computer Vision]] — Computer Vision ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — Transformers ·  medium confidence

## Builds on this

- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]]

## Concepts taught

- [[Concepts/Patch|Patch]] `glossary` — A fixed-size non-overlapping region of the input image; becomes one token
- [[Concepts/Patch Embedding|Patch Embedding]] `glossary` — A shared learned matrix (or Conv2d with stride=P) mapping flattened patch pixels to D-dim vectors
- [[Concepts/CLS- token|[CLS] token]] (as *CLS token*) `lesson term` — Prepended learnable vector whose final hidden state represents the whole image; optional in 2026
- Register token `lesson term` — Extra learnable tokens that absorb the high-norm attention artifacts ViTs develop during pretraining
- [[Concepts/Position embedding|Position embedding]] `lesson term` — Per-position vector or rotation making the sequence-order-aware; 2D-RoPE is the modern default
- Grid `lesson term` — The (H/P) x (W/P) 2D array of patches for a given resolution and patch size
- [[Concepts/NaFlex|NaFlex]] `lesson term` — SigLIP 2 feature: single model serves multiple aspect ratios and resolutions without retraining
- [[Concepts/Backbone|Backbone]] `lesson term` — The pretrained image encoder whose patch-token outputs feed the LLM in a VLM
- Pooling `lesson term` — Strategy to turn patch tokens into one vector: CLS, mean, attention pool, or register-based
- Patch 14 vs 16 `lesson term` — Patch 14 produces more tokens per image, better fidelity for OCR, slower; patch 16 is the classic default

## Ships

- [[Artifacts/12-01 patch-geometry-reader|patch-geometry-reader]] `skill` — Read a ViT config and produce a patch-token, parameter, and VRAM analysis for downstream VLM planning.

## Further reading

- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929)) — original ViT. ·  also cited by 2 other lessons
- Zhai et al. — Scaling Vision Transformers (arXiv:2106.04560) ([link](https://arxiv.org/abs/2106.04560)) — empirical scaling laws.
- [[Resources/Masked Autoencoders are Scalable Vision Learners (He et al., 2022)|Masked Autoencoders are Scalable Vision Learners (He et al., 2022)]] ([link](https://arxiv.org/abs/2111.06377)) — MAE, self-supervised pretraining. ·  also cited by 2 other lessons
- [[Resources/DINOv2 (Oquab et al., 2023)|DINOv2 (Oquab et al., 2023)]] ([link](https://arxiv.org/abs/2304.07193)) — self-distillation at scale, no labels. ·  also cited by 2 other lessons
- [[Resources/Darcet et al. (2023). Vision Transformers Need Registers|Darcet et al. (2023). Vision Transformers Need Registers]] ([link](https://arxiv.org/abs/2309.16588)) — register tokens and artifact analysis. ·  also cited by 1 other lesson
- [[Resources/Tschannen et al. — SigLIP 2 (arXiv-2502.14786)|Tschannen et al. — SigLIP 2 (arXiv:2502.14786)]] ([link](https://arxiv.org/abs/2502.14786)) — the 2026 default vision tower. ·  also cited by 2 other lessons


%% ── my notes ── %%
