---
id: "lesson:12/04"
type: lesson
ref: 12/04
phase: 12
num: 4
title: Flamingo and Gated Cross-Attention for Few-Shot VLMs
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 93
aliases:
  - 12/04
  - 12-04
tags:
  - phase/12
  - type/learn
  - community/93
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/04-flamingo-gated-cross-attention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/04-flamingo-gated-cross-attention"
---

# 12/04 Flamingo and Gated Cross-Attention for Few-Shot VLMs

> DeepMind's Flamingo (2022) did two things before anyone else. It showed a single model could process arbitrarily interleaved sequences of images, videos, and text. And it showed VLMs could learn in-context — give a few-shot prompt with three example (image, caption) pairs and the model captions a new image without any gradient step. The mechanism: gated cross-attention layers, inserted between the frozen LLM's existing layers, with a learned tanh gate that starts at zero so the LLM's text capability is preserved at initialization. This lesson walks Flamingo's Perceiver resampler and gated cross-attention architecture — the ancestor of Gemini's interleaved inputs and Idefics2's visual tokens.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/04-flamingo-gated-cross-attention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/04-flamingo-gated-cross-attention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/04-flamingo-gated-cross-attention) · code: main.py  
**Community:** [[Communities/93 Perceiver resampler · Projection head|93 Perceiver resampler · Projection head]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 03 (BLIP-2 Q-Former)`

- [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]] — BLIP-2 Q-Former

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Concepts taught

- [[Concepts/Perceiver resampler|Perceiver resampler]] `lesson term` — Module that produces K fixed tokens from a variable number of input patches
- Gated cross-attention `lesson term` — Residual layer y = tanh(alpha)cross + x, learnable alpha, init 0
- Interleaved input `lesson term` — Prompt format with images and text mixed freely in reading order
- Frozen LLM `lesson term` — The text LLM's weights do not update; only resampler + cross-attn layers train
- [[Concepts/Few-Shot|Few-Shot]] `glossary` — Give a few (image, answer) pairs in the prompt; model generalizes without finetuning
- OBELICS `lesson term` — Open dataset of 141M web pages with images and text in reading order
- Chinchilla `lesson term` — Flamingo's frozen text LLM, from DeepMind's Chinchilla paper
- Gate schedule `lesson term` — The rate at which the cross-attention gate opens during training
- Cross-attn frequency `lesson term` — How often a gated cross-attention block is inserted; Flamingo uses M=4
- OpenFlamingo `lesson term` — MosaicML/LAION open checkpoint at 3-9B; architecture-identical to Flamingo

## Ships

- [[Artifacts/12-04 gated-bridge-diagnostic|gated-bridge-diagnostic]] `skill` — Identify Flamingo-lineage design elements in an open VLM config and diagnose freezing / gating issues.

## Further reading

- [[Resources/Jaegle et al. — Perceiver IO (arXiv-2107.14795)|Jaegle et al. — Perceiver IO (arXiv:2107.14795)]] ([link](https://arxiv.org/abs/2107.14795)) — the general Perceiver architecture. ·  also cited by 1 other lesson
- Flamingo: a Visual Language Model for Few-Shot Learning ([link](https://arxiv.org/abs/2204.14198)) — the original paper.
- Li et al. — Otter (arXiv:2305.03726) ([link](https://arxiv.org/abs/2305.03726)) — instruction-tuned Flamingo descendant.
- Laurençon et al. — OBELICS (arXiv:2306.16527) ([link](https://arxiv.org/abs/2306.16527)) — interleaved web corpus.
- Awadalla et al. — OpenFlamingo (arXiv:2308.01390) ([link](https://arxiv.org/abs/2308.01390)) — open reproduction.
- [[Resources/Laurençon et al. — Idefics2 (arXiv-2405.02246)|Laurençon et al. — Idefics2 (arXiv:2405.02246)]] ([link](https://arxiv.org/abs/2405.02246)) — modern simplification of the Flamingo approach. ·  also cited by 2 other lessons


%% ── my notes ── %%
