---
id: "lesson:12/15"
type: lesson
ref: 12/15
phase: 12
num: 15
title: "Janus-Pro: Decoupled Encoders for Unified Multimodal Models"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 2
aliases:
  - 12/15
  - 12-15
tags:
  - phase/12
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders"
---

# 12/15 Janus-Pro: Decoupled Encoders for Unified Multimodal Models

> Unified multimodal models have an unavoidable tension. Understanding wants semantic features — SigLIP or DINOv2 output vectors rich with concept-level information. Generation wants reconstruction-friendly codes — VQ tokens that compose back into crisp pixels. The two goals are not compatible in a single encoder. Janus (DeepSeek, October 2024) and Janus-Pro (DeepSeek, January 2025) argue the fix is to stop trying: decouple the two encoders. Share the transformer body between tasks, but route understanding through SigLIP and generation through a VQ tokenizer. At 7B, Janus-Pro beats DALL-E 3 on GenEval while matching LLaVA on MMMU. This lesson reads why two encoders work where one fails.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/15-janus-pro-decoupled-encoders/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/15-janus-pro-decoupled-encoders) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 13 (Transfusion), Phase 12 · 14 (Show-o)`

- [[Lessons/12-13 Transfusion- Autoregressive Text + Diffusion Image in One Transformer|12/13 Transfusion: Autoregressive Text + Diffusion Image in One Transformer]] — Transfusion
- [[Lessons/12-14 Show-o and Discrete-Diffusion Unified Models|12/14 Show-o and Discrete-Diffusion Unified Models]] — Show-o

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]]
- depth 3: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]

## Concepts taught

- Decoupled encoding `lesson term` — Separate tokenizer or encoder per direction: semantic for understanding, reconstruction for generation
- Shared body `lesson term` — Single transformer processes either encoder's output; no modality-specific weights
- SigLIP for understanding `lesson term` — CLIP-family vision tower providing rich conceptual features but poor reconstruction
- VQ for generation `lesson term` — Vector-quantized tokens that decode cleanly back to pixels
- JanusFlow `lesson term` — Janus-Pro with a continuous flow-matching generation head instead of VQ
- Routing tag `lesson term` — Prompt marker (<understand> / <generate>) that picks the input encoder

## Ships

- [[Artifacts/12-15 decoupled-encoder-picker|decoupled-encoder-picker]] `skill` — Decide whether a unified VLM should decouple its visual encoders and pick between Janus-Pro, JanusFlow, and InternVL-U.

## Further reading

- Dong et al. — DreamLLM (arXiv:2309.11499) ([link](https://arxiv.org/abs/2309.11499))
- Wu et al. — Janus (arXiv:2410.13848) ([link](https://arxiv.org/abs/2410.13848))
- Ma et al. — JanusFlow (arXiv:2411.07975) ([link](https://arxiv.org/abs/2411.07975))
- Chen et al. — Janus-Pro (arXiv:2501.17811) ([link](https://arxiv.org/abs/2501.17811))
- [[Resources/InternVL-U (arXiv-2603.09877)|InternVL-U (arXiv:2603.09877)]] ([link](https://arxiv.org/abs/2603.09877)) ·  also cited by 1 other lesson


%% ── my notes ── %%
