---
id: "lesson:12/17"
type: lesson
ref: 12/17
phase: 12
num: 17
title: "Video-Language Models: Temporal Tokens and Grounding"
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
community: 84
aliases:
  - 12/17
  - 12-17
tags:
  - phase/12
  - type/build
  - community/84
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/17-video-language-temporal-grounding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/17-video-language-temporal-grounding"
---

# 12/17 Video-Language Models: Temporal Tokens and Grounding

> Video is not a stack of photos. A 5-second clip has causal ordering, action verbs, and event timing that an image model cannot represent. Video-LLaMA (Zhang et al., June 2023) shipped the first open video-LLM with audio-visual grounding. VideoChat and Video-LLaVA scaled the pattern. By 2025 Qwen2.5-VL's TMRoPE closed the gap with frontier proprietary models. Each system solved temporal tokens differently — Q-former per clip, concat-pool per frame, TMRoPE per token. This lesson reads the patterns, builds a uniform-vs-dynamic frame sampler, and evaluates on temporal grounding tasks.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/17-video-language-temporal-grounding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/17-video-language-temporal-grounding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/17-video-language-temporal-grounding) · code: main.py  
**Community:** [[Communities/84 Curriculum|84 Curriculum]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 08 (LLaVA-OneVision)`

- [[Lessons/12-08 LLaVA-OneVision- Single-Image, Multi-Image, Video in One Model|12/08 LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model]] — LLaVA-OneVision

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]], [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]], [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-18 Long-Video Understanding at Million-Token Context|12/18 Long-Video Understanding at Million-Token Context]]

## Concepts taught

- [[Concepts/Temporal grounding|Temporal grounding]] `lesson term` — VLM outputs a specific timestamp range for when an event happens
- [[Concepts/TMRoPE|TMRoPE]] `lesson term` — 3D rotary position with absolute timestamps, used by Qwen2.5-VL
- [[Concepts/Dynamic FPS|Dynamic FPS]] `lesson term` — Sample more frames in high-motion segments, fewer in static ones
- Frame pooling `lesson term` — Reduce patches per frame with bilinear interpolation before the LLM
- Video Q-former `lesson term` — Cross-attention bottleneck mapping N frames to K learned queries
- VideoMME `lesson term` — Comprehensive short/medium/long video benchmark, 2500+ samples

## Ships

- [[Artifacts/12-17 video-vlm-frame-planner|video-vlm-frame-planner]] `skill` — Plan frame sampling, per-frame pooling, output format, and benchmark targets for a video-language model deployment.

## Further reading

- Li et al. — VideoChat (arXiv:2305.06355) ([link](https://arxiv.org/abs/2305.06355))
- Zhang et al. — Video-LLaMA (arXiv:2306.02858) ([link](https://arxiv.org/abs/2306.02858))
- [[Resources/Lin et al. — Video-LLaVA (arXiv-2311.10122)|Lin et al. — Video-LLaVA (arXiv:2311.10122)]] ([link](https://arxiv.org/abs/2311.10122)) ·  also cited by 1 other lesson
- [[Resources/Lin et al. — VILA (arXiv-2312.07533)|Lin et al. — VILA (arXiv:2312.07533)]] ([link](https://arxiv.org/abs/2312.07533)) ·  also cited by 1 other lesson
- [[Resources/Qwen Team — Qwen2.5-VL Technical Report (arXiv-2502.13923)|Qwen Team — Qwen2.5-VL Technical Report (arXiv:2502.13923)]] ([link](https://arxiv.org/abs/2502.13923)) ·  also cited by 2 other lessons


%% ── my notes ── %%
