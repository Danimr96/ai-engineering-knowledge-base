---
id: "lesson:12/08"
type: lesson
ref: 12/08
phase: 12
num: 8
title: "LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model"
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
community: 84
aliases:
  - 12/08
  - 12-08
tags:
  - phase/12
  - type/build
  - community/84
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/08-llava-onevision-single-multi-video/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/08-llava-onevision-single-multi-video"
---

# 12/08 LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model

> Before LLaVA-OneVision (Li et al., August 2024) the open-VLM world had separate lineages: LLaVA-1.5 for single images, multi-image models like Mantis and VILA, video models like Video-LLaVA and Video-LLaMA. Each won its benchmark and failed at the others. LLaVA-OneVision argued a single curriculum could train one model to dominate all three scenarios, and that the emergent task-transfer effects (single-image skills exported to video, multi-image reasoning exported to single-image) beat the sum of specialists. The recipe is deceptively simple: a visual-token budget that stays constant across scenarios, plus an explicit curriculum that moves from single-image to OneVision (multi-image) to video. This lesson reads the budget, the curriculum, and the emergent behaviors.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/08-llava-onevision-single-multi-video/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/08-llava-onevision-single-multi-video) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/08-llava-onevision-single-multi-video) · code: main.py  
**Community:** [[Communities/84 Curriculum|84 Curriculum]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05 (LLaVA), Phase 12 · 06 (any-resolution)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA
- [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]] — any-resolution

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]], [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-17 Video-Language Models- Temporal Tokens and Grounding|12/17 Video-Language Models: Temporal Tokens and Grounding]]

## Concepts taught

- OneVision scenario `lesson term` — One of three input shapes the unified VLM handles; the budget stays constant across
- [[Concepts/Token Budget|Token Budget]] `glossary` — Total visual tokens the LLM sees per training / inference sample, typically 3000-4000
- [[Concepts/Curriculum|Curriculum]] `lesson term` — Stage ordering (single-image → multi-image → video) chosen for emergent transfer
- Bilinear pooling `lesson term` — Applying bilinear interpolation to the patch grid (2D) to reduce token count while preserving locality
- Emergent skill `lesson term` — Capability that appears at inference without matching training data, due to curriculum composition
- AnyRes-k `lesson term` — k sub-tiles of fixed resolution plus one thumbnail, typical k ∈ {4, 9}
- Task transfer `lesson term` — Skills learned on single-image that apply to video (and vice versa) via shared backbone

## Ships

- [[Artifacts/12-08 onevision-budget-planner|onevision-budget-planner]] `skill` — Allocate LLaVA-OneVision-style unified visual-token budgets across single-image, multi-image, and video scenarios for a target product mix.

## Further reading

- [[Resources/Lin et al. — Video-LLaVA (arXiv-2311.10122)|Lin et al. — Video-LLaVA (arXiv:2311.10122)]] ([link](https://arxiv.org/abs/2311.10122)) ·  also cited by 1 other lesson
- [[Resources/Lin et al. — VILA (arXiv-2312.07533)|Lin et al. — VILA (arXiv:2312.07533)]] ([link](https://arxiv.org/abs/2312.07533)) ·  also cited by 1 other lesson
- [[Resources/Li et al. — LLaVA-OneVision (arXiv-2408.03326)|Li et al. — LLaVA-OneVision (arXiv:2408.03326)]] ([link](https://arxiv.org/abs/2408.03326)) ·  also cited by 1 other lesson
- [[Resources/Wang et al. — Qwen2-VL (arXiv-2409.12191)|Wang et al. — Qwen2-VL (arXiv:2409.12191)]] ([link](https://arxiv.org/abs/2409.12191)) ·  also cited by 2 other lessons
- LLaVA-OneVision-1.5: Fully Open Framework (arXiv:2509.23661) ([link](https://arxiv.org/abs/2509.23661))


%% ── my notes ── %%
