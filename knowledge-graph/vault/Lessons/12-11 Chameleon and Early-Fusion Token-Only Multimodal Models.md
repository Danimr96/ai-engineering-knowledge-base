---
id: "lesson:12/11"
type: lesson
ref: 12/11
phase: 12
num: 11
title: Chameleon and Early-Fusion Token-Only Multimodal Models
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 73
aliases:
  - 12/11
  - 12-11
tags:
  - phase/12
  - type/build
  - community/73
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/11-chameleon-early-fusion-tokens/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/11-chameleon-early-fusion-tokens"
---

# 12/11 Chameleon and Early-Fusion Token-Only Multimodal Models

> Every VLM we have seen so far keeps images and text separate. Visual tokens come from a vision encoder, flow into a projector, then meet text inside the LLM. The vision and text vocabularies never overlap. Chameleon (Meta, May 2024) asked: what if they did? Train a VQ-VAE that turns an image into a sequence of discrete tokens from a shared vocabulary. Every multimodal document is now one sequence — text tokens and image tokens interleaved, a single autoregressive loss. Side effect: the model can generate mixed-modality outputs — alternating text and image tokens in a single inference call. This lesson reads the early-fusion thesis and builds a toy version end to end.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/11-chameleon-early-fusion-tokens/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/11-chameleon-early-fusion-tokens) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/11-chameleon-early-fusion-tokens) · code: main.py  
**Community:** [[Communities/73 Flow matching · MMDiT · VQ-VAE|73 Flow matching · MMDiT · VQ-VAE]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05, Phase 8 (Generative AI)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- Whole phase: [[Phases/08 Generative AI|Phase 8: Generative AI]] — Generative AI ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Builds on this

- [[Lessons/12-12 Emu3- Next-Token Prediction for Image and Video Generation|12/12 Emu3: Next-Token Prediction for Image and Video Generation]]
- [[Lessons/12-13 Transfusion- Autoregressive Text + Diffusion Image in One Transformer|12/13 Transfusion: Autoregressive Text + Diffusion Image in One Transformer]]
- [[Lessons/12-16 MIO and Any-to-Any Streaming Multimodal Models|12/16 MIO and Any-to-Any Streaming Multimodal Models]]

## Concepts taught

- [[Concepts/Early Fusion|Early Fusion]] `glossary` — Images converted to discrete tokens sharing the transformer's vocabulary from step one
- [[Concepts/VQ-VAE|VQ-VAE]] `lesson term` — CNN + ViT + codebook that maps images to integer indices the transformer can predict
- Shared vocabulary `lesson term` — A single token ID space covering text + image + modality separators
- QK-Norm `lesson term` — LayerNorm applied to query and key before their dot product, prevents norm blowup
- Mixed-modality generation `lesson term` — Inference that autonomously produces interleaved text and image tokens in one pass
- Codebook size `lesson term` — Number of discrete vectors the VQ-VAE can quantize to; trades compression for fidelity
- Tokenizer ceiling `lesson term` — Best PSNR achievable by decoding VQ tokens; bounds the model's image quality

## Ships

- [[Artifacts/12-11 tokenizer-vs-adapter-picker|tokenizer-vs-adapter-picker]] `skill` — Pick between Chameleon-style early fusion (shared-vocab tokenizer) and LLaVA-style late fusion (adapter on frozen LLM) for a VLM project.

## Further reading

- Adept — Fuyu-8B blog (adept.ai) ([link](https://www.adept.ai/blog/fuyu-8b))
- Aghajanyan et al. — CM3 (arXiv:2201.07520) ([link](https://arxiv.org/abs/2201.07520))
- Yu et al. — CM3Leon (arXiv:2309.02591) ([link](https://arxiv.org/abs/2309.02591))
- [[Resources/Zhan et al. — AnyGPT (arXiv-2402.12226)|Zhan et al. — AnyGPT (arXiv:2402.12226)]] ([link](https://arxiv.org/abs/2402.12226)) ·  also cited by 1 other lesson
- Chameleon: Mixed-Modal Early-Fusion Foundation Models ([link](https://arxiv.org/abs/2405.09818))


%% ── my notes ── %%
