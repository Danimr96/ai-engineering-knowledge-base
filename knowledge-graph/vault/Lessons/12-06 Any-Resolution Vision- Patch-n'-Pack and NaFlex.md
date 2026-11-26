---
id: "lesson:12/06"
type: lesson
ref: 12/06
phase: 12
num: 6
title: "Any-Resolution Vision: Patch-n'-Pack and NaFlex"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 53
aliases:
  - 12/06
  - 12-06
tags:
  - phase/12
  - type/build
  - community/53
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/06-any-resolution-patch-n-pack/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/06-any-resolution-patch-n-pack"
---

# 12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex

> Real images are not 224x224 squares. A receipt is 9:16, a chart is 16:9, a medical scan might be 4096x4096, a mobile screenshot is 9:19.5. The pre-2024 VLM answer — resize everything to a fixed square — threw away the signal that makes OCR, document understanding, and high-resolution scene parsing work. NaViT (Google, 2023) showed you could pack variable-resolution patches into a single transformer batch with block-diagonal masking. Qwen2-VL's M-RoPE (2024) dropped absolute positional tables entirely. LLaVA-NeXT's AnyRes tiled high-resolution images into a base + sub-images. SigLIP 2's NaFlex variant (2025) is now the default encoder for open VLMs that want a single checkpoint to serve every aspect ratio. This lesson implements patch-n'-pack end to end.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/06-any-resolution-patch-n-pack/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/06-any-resolution-patch-n-pack) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/06-any-resolution-patch-n-pack) · code: main.py  
**Community:** [[Communities/53 M-RoPE · min_pixels - max_pixels · AnyRes|53 M-RoPE · min_pixels / max_pixels · AnyRes]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 01 (ViT patches), Phase 12 · 05 (LLaVA)`

- [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]] — ViT patches
- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-08 LLaVA-OneVision- Single-Image, Multi-Image, Video in One Model|12/08 LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model]]
- [[Lessons/12-09 Qwen-VL Family and Dynamic-FPS Video|12/09 Qwen-VL Family and Dynamic-FPS Video]]

## Concepts taught

- Patch-n'-pack `lesson term` — Concatenate variable-length patch sequences from different images into one batch dimension
- Block-diagonal mask `lesson term` — Attention mask that confines each image's patches to attend only to themselves, not neighbors in the pack
- [[Concepts/AnyRes|AnyRes]] `lesson term` — Split a high-res image into a grid of fixed-size tiles plus a global thumbnail; encode every tile with a fixed encoder
- [[Concepts/NaFlex|NaFlex]] `lesson term` — Single SigLIP 2 checkpoint that serves 256/729/1024-token budgets at inference without retraining
- [[Concepts/M-RoPE|M-RoPE]] `lesson term` — 3D rotary position encoding (time, row, column) that handles arbitrary H, W, T without position tables
- cu_seqlens `lesson term` — Cumulative-length tensor the FlashAttention varlen path uses instead of a dense block-diagonal mask
- [[Concepts/min_pixels - max_pixels|min_pixels / max_pixels]] `lesson term` — Qwen2.5-VL per-request knobs capping token count on very small or very large inputs
- Visual token budget `lesson term` — Rough count of patch tokens emitted per image; sets the LLM's prompt budget and attention cost

## Ships

- [[Artifacts/12-06 resolution-budget-planner|resolution-budget-planner]] `skill` — Pick between square-resize, AnyRes, M-RoPE, and NaFlex for a mixed-aspect-ratio VLM workload and emit a per-task token budget plan.

## Further reading

- Dehghani et al. — Patch n' Pack: NaViT (arXiv:2307.06304) ([link](https://arxiv.org/abs/2307.06304))
- [[Resources/Laurençon et al. — Idefics2 (arXiv-2405.02246)|Laurençon et al. — Idefics2 (arXiv:2405.02246)]] ([link](https://arxiv.org/abs/2405.02246)) ·  also cited by 2 other lessons
- [[Resources/Wang et al. — Qwen2-VL (arXiv-2409.12191)|Wang et al. — Qwen2-VL (arXiv:2409.12191)]] ([link](https://arxiv.org/abs/2409.12191)) ·  also cited by 2 other lessons
- [[Resources/Qwen Team — Qwen2.5-VL Technical Report (arXiv-2502.13923)|Qwen Team — Qwen2.5-VL Technical Report (arXiv:2502.13923)]] ([link](https://arxiv.org/abs/2502.13923)) ·  also cited by 2 other lessons
- [[Resources/Tschannen et al. — SigLIP 2 (arXiv-2502.14786)|Tschannen et al. — SigLIP 2 (arXiv:2502.14786)]] ([link](https://arxiv.org/abs/2502.14786)) ·  also cited by 2 other lessons


%% ── my notes ── %%
