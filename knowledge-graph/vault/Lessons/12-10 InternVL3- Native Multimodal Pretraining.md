---
id: "lesson:12/10"
type: lesson
ref: 12/10
phase: 12
num: 10
title: "InternVL3: Native Multimodal Pretraining"
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
aliases:
  - 12/10
  - 12-10
tags:
  - phase/12
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/10-internvl3-native-multimodal/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/10-internvl3-native-multimodal"
---

# 12/10 InternVL3: Native Multimodal Pretraining

> Every open VLM before InternVL3 followed the same three-step recipe: take a text LLM trained on trillions of text tokens, bolt on a vision encoder, then fine-tune the seams. This works but has alignment debt — the text LLM has spent its full pretraining budget on pure text and does not natively understand visual tokens. When you add vision post-hoc, the LLM has to re-learn how to relate visual input to its text reasoning without forgetting the text. InternVL3 (Zhu et al., April 2025) rejects the post-hoc approach: one pretraining run, text and multimodal interleaved from step one. The result matches Gemini 2.5 Pro on MMMU-Pro at 78B params open. This lesson reads the case for native pretraining and what changes when you make it.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/10-internvl3-native-multimodal/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/10-internvl3-native-multimodal) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/10-internvl3-native-multimodal) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05, Phase 12 · 07 (recipes)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- [[Lessons/12-07 Open-Weight VLM Recipes- What Actually Matters|12/07 Open-Weight VLM Recipes: What Actually Matters]] — recipes

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Concepts taught

- Native multimodal pretraining `lesson term` — Text + image + video tokens participate in the loss from step 1, not bolted on later
- Alignment debt `lesson term` — Measurable regression in text skills and answer consistency that comes from bolting vision onto a frozen LLM
- V2PE `lesson term` — Per-modality learnable position encoding allocation; InternVL3's M-RoPE successor
- ViR `lesson term` — Small classifier that picks minimum resolution needed per query before encoding, saving inference tokens
- DvD `lesson term` — Vision encoder on one GPU, LLM on another, with stream handoff; doubles throughput for large VLMs
- InternVL-U `lesson term` — 2026 follow-up that adds image-generation heads to the native-pretrain backbone
- Interleaved corpus `lesson term` — Documents with text and images in natural reading order; the raw material for native pretraining

## Ships

- [[Artifacts/12-10 native-vs-posthoc-auditor|native-vs-posthoc-auditor]] `skill` — Audit a proposed VLM training plan and recommend native multimodal pretraining or post-hoc adapter-on-LLM, with corpus-mix and alignment-debt analysis.

## Further reading

- Chen et al. — InternVL 1 (arXiv:2312.14238) ([link](https://arxiv.org/abs/2312.14238))
- Zhang et al. — MM1.5 (arXiv:2409.20566) ([link](https://arxiv.org/abs/2409.20566))
- [[Resources/Zhu et al. — InternVL3 (arXiv-2504.10479)|Zhu et al. — InternVL3 (arXiv:2504.10479)]] ([link](https://arxiv.org/abs/2504.10479)) ·  also cited by 1 other lesson
- [[Resources/InternVL3.5 Advancing Open-Source Multimodal Models (arXiv 2508.18265)|InternVL3.5 Advancing Open-Source Multimodal Models (arXiv 2508.18265)]] ([link](https://arxiv.org/html/2508.18265v1)) ·  also cited by 1 other lesson
- [[Resources/InternVL-U (arXiv-2603.09877)|InternVL-U (arXiv:2603.09877)]] ([link](https://arxiv.org/abs/2603.09877)) ·  also cited by 1 other lesson


%% ── my notes ── %%
