---
id: "lesson:12/03"
type: lesson
ref: 12/03
phase: 12
num: 3
title: "From CLIP to BLIP-2 — Q-Former as Modality Bridge"
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 93
aliases:
  - 12/03
  - 12-03
tags:
  - phase/12
  - type/build
  - community/93
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/03-blip2-qformer-bridge/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/03-blip2-qformer-bridge"
---

# 12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge

> CLIP aligns image and text but cannot generate captions, answer questions, or hold a conversation. BLIP-2 (Salesforce, 2023) solved that with a small trainable bridge: 32 learnable query vectors attend over a frozen ViT's features via cross-attention, then slot directly into a frozen LLM's input stream. 188M parameters of bridge connected an 11B LLM to a ViT-g/14. Every adapter-based VLM through 2026 — MiniGPT-4, InstructBLIP, LLaVA's cousins — is a descendant. This lesson reads the Q-Former's architecture, explains its two-stage training, and builds a toy version that feeds visual tokens into a frozen text decoder.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/03-blip2-qformer-bridge/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/03-blip2-qformer-bridge) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/03-blip2-qformer-bridge) · code: main.py  
**Community:** [[Communities/93 Perceiver resampler · Projection head|93 Perceiver resampler · Projection head]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 02 (CLIP), Phase 7 (Transformers)`

- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]] — CLIP
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — Transformers ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Builds on this

- [[Lessons/06-10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio|06/10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio]]
- [[Lessons/12-04 Flamingo and Gated Cross-Attention for Few-Shot VLMs|12/04 Flamingo and Gated Cross-Attention for Few-Shot VLMs]]
- [[Lessons/12-19 Audio-Language Models- the Whisper to Audio Flamingo 3 Arc|12/19 Audio-Language Models: the Whisper to Audio Flamingo 3 Arc]]

## Concepts taught

- [[Concepts/Q-former|Q-former]] `lesson term` — Small transformer with 32 learnable query vectors that cross-attend to frozen ViT features
- Learnable queries `lesson term` — A fixed set of parameters that serve as the query side of cross-attention; learned per model, shared across all inputs
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — Attention where query, key, and value come from different sources; how the queries pull from ViT patches
- ITC `lesson term` — CLIP-style loss applied to Q-Former pooled queries vs text CLS
- ITM `lesson term` — Binary classifier on hard-negative-mined pairs; forces the queries to discriminate fine-grained mismatches
- ITG `lesson term` — Causal LM loss where text is generated conditioned on queries; forces queries to encode text-decodable content
- Two-stage pretraining `lesson term` — Stage 1 trains Q-Former alone (ITC/ITM/ITG); Stage 2 attaches frozen LLM and trains only the projection + Q-Former
- Frozen backbone `lesson term` — The vision encoder and LLM weights are fixed; only the bridge trains
- [[Concepts/Projection head|Projection head]] `lesson term` — Final linear layer mapping Q-Former output to the LLM's embedding dimension
- [[Concepts/Perceiver resampler|Perceiver resampler]] `lesson term` — Similar learnable-query cross-attention, used by Flamingo at every layer rather than as a single bridge

## Ships

- [[Artifacts/12-03 modality-bridge-picker|modality-bridge-picker]] `skill` — Recommend Q-Former vs MLP projector vs Perceiver resampler for a VLM configuration given token budget, quality target, and training compute.

## Further reading

- Li et al. — ALBEF (arXiv:2107.07651) ([link](https://arxiv.org/abs/2107.07651)) — "align before fuse" — the conceptual ancestor of stage 1 training.
- [[Resources/Jaegle et al. — Perceiver IO (arXiv-2107.14795)|Jaegle et al. — Perceiver IO (arXiv:2107.14795)]] ([link](https://arxiv.org/abs/2107.14795)) — general architecture for learnable-query cross-attention. ·  also cited by 1 other lesson
- Li et al. — BLIP (arXiv:2201.12086) ([link](https://arxiv.org/abs/2201.12086)) — the predecessor with the ITC/ITM/ITG trio.
- Li et al. — BLIP-2 (arXiv:2301.12597) ([link](https://arxiv.org/abs/2301.12597)) — the core paper.
- Zhu et al. — MiniGPT-4 (arXiv:2304.10592) ([link](https://arxiv.org/abs/2304.10592)) — projector-only approach.
- Dai et al. — InstructBLIP (arXiv:2305.06500) ([link](https://arxiv.org/abs/2305.06500)) — instruction-aware Q-Former.


%% ── my notes ── %%
