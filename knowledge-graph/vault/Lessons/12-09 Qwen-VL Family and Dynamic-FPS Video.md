---
id: "lesson:12/09"
type: lesson
ref: 12/09
phase: 12
num: 9
title: Qwen-VL Family and Dynamic-FPS Video
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 53
aliases:
  - 12/09
  - 12-09
tags:
  - phase/12
  - type/learn
  - community/53
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps"
---

# 12/09 Qwen-VL Family and Dynamic-FPS Video

> The Qwen-VL family — Qwen-VL (2023), Qwen2-VL (2024), Qwen2.5-VL (2025), Qwen3-VL (2025) — is the most influential open vision-language model lineage in 2026. Each generation made a single decisive architectural bet that the rest of the open ecosystem copied within twelve months: native dynamic resolution via M-RoPE, dynamic-FPS sampling with absolute time alignment, window attention in the ViT, and structured agent output formats. By Qwen3-VL, the recipe had stabilized: a 2D-RoPE-ViT encoder with native-aspect-ratio inputs, an MLP projector into a large Qwen3 language base, and training stages that emphasized OCR, grounding, and agent behavior as first-class targets. This lesson reads the family chronologically so you understand why every knob is where it is.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/09-qwen-vl-family-dynamic-fps/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps) · code: main.py  
**Community:** [[Communities/53 M-RoPE · min_pixels - max_pixels · AnyRes|53 M-RoPE · min_pixels / max_pixels · AnyRes]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 06 (patch-n'-pack)`

- [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]] — patch-n'-pack

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]], [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-25 Multimodal Agents and Computer-Use (Capstone)|12/25 Multimodal Agents and Computer-Use (Capstone)]]

## Concepts taught

- [[Concepts/M-RoPE|M-RoPE]] `lesson term` — 3D rotary position embedding with temporal, height, and width bands in the hidden dim
- [[Concepts/Dynamic FPS|Dynamic FPS]] `lesson term` — Frame sampling rate chosen per video based on motion, duration, and token budget
- Absolute time token `lesson term` — <time>t</time> interleaved in the sequence so the model sees actual seconds not frame index
- Window attention `lesson term` — Spatial self-attention restricted to small windows for speed; global attention added periodically
- Structured agent output `lesson term` — Training data supervision teaching the VLM to emit parseable JSON with coords and tool names
- [[Concepts/min_pixels - max_pixels|min_pixels / max_pixels]] `lesson term` — Per-request Qwen2.5-VL controls bounding total pixel count and therefore token count
- [[Concepts/Grounding|Grounding]] `glossary` — Outputting bounding-box coordinates as text tokens; used since Qwen-VL v1

## Ships

- [[Artifacts/12-09 qwen-vl-pipeline-designer|qwen-vl-pipeline-designer]] `skill` — Configure a Qwen2.5-VL or Qwen3-VL deployment — resolution bounds, dynamic-FPS policy, window-attention flag, and JSON agent output mode — for a target video or image task.

## Further reading

- Bai et al. — Qwen-VL (arXiv:2308.12966) ([link](https://arxiv.org/abs/2308.12966))
- [[Resources/Wang et al. — Qwen2-VL (arXiv-2409.12191)|Wang et al. — Qwen2-VL (arXiv:2409.12191)]] ([link](https://arxiv.org/abs/2409.12191)) ·  also cited by 2 other lessons
- [[Resources/Qwen Team — Qwen2.5-VL Technical Report (arXiv-2502.13923)|Qwen Team — Qwen2.5-VL Technical Report (arXiv:2502.13923)]] ([link](https://arxiv.org/abs/2502.13923)) ·  also cited by 2 other lessons
- [[Resources/Zhu et al. — InternVL3 (arXiv-2504.10479)|Zhu et al. — InternVL3 (arXiv:2504.10479)]] ([link](https://arxiv.org/abs/2504.10479)) ·  also cited by 1 other lesson
- [[Resources/Qwen3-VL Technical Report (arXiv 2511.21631)|Qwen3-VL Technical Report (arXiv 2511.21631)]] ([link](https://arxiv.org/abs/2511.21631)) ·  also cited by 1 other lesson


%% ── my notes ── %%
