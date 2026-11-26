---
id: "lesson:12/21"
type: lesson
ref: 12/21
phase: 12
num: 21
title: "Embodied VLAs: RT-2, OpenVLA, π0, GR00T"
lesson_type: learn
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 95
aliases:
  - 12/21
  - 12-21
tags:
  - phase/12
  - type/learn
  - community/95
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot"
---

# 12/21 Embodied VLAs: RT-2, OpenVLA, π0, GR00T

> The first time a model read a recipe off a website and executed it in a kitchen robot was RT-2 (Google DeepMind, July 2023). RT-2 discretized actions as text tokens, co-fine-tuned a VLM on web data plus robot-action data, and proved that web-scale vision-language knowledge transfers to robotic control. OpenVLA (June 2024) shipped the open 7B reference. Physical Intelligence's π0 series (2024-2025) added flow-matching action experts. NVIDIA's GR00T N1 (March 2025) delivered dual-system (System 1 / System 2) control for humanoid robots at scale. The VLA primitive — vision-language-action, a single model that sees, reads, and acts — is the bridge between this phase's understanding models and the autonomous systems in Phase 15.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot) · code: main.py  
**Community:** [[Communities/95 Projector|95 Projector]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05 (LLaVA), Phase 15 (Autonomous Systems, referenced)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — Autonomous Systems, referenced ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Concepts taught

- VLA `lesson term` — Model that takes image + instruction and outputs action commands
- Action tokenization `lesson term` — Quantize continuous joint targets into 256 bins per dim, each a vocab ID
- FAST tokenizer `lesson term` — DCT + quantize to compress 30-step trajectories to ~10 tokens
- Co-fine-tune `lesson term` — Train on web VQA data alongside robot demos to preserve general knowledge
- Flow-matching action head `lesson term` — Small transformer that outputs a 50-step action sequence via rectified flow
- System 1 / System 2 `lesson term` — Large VLM plans slowly, small action head acts quickly; GR00T pattern
- Open X-Embodiment `lesson term` — 1M-trajectory cross-robot dataset; the training corpus

## Ships

- [[Artifacts/12-21 vla-action-format-picker|vla-action-format-picker]] `skill` — Pick an action format (discrete bin, FAST, flow-matching, dual-system) and VLA family (RT-2, OpenVLA, π0, GR00T) for a robot task.

## Further reading

- Brohan et al. — RT-2 (arXiv:2307.15818) ([link](https://arxiv.org/abs/2307.15818))
- Open X-Embodiment Collab — RT-X (arXiv:2310.08864) ([link](https://arxiv.org/abs/2310.08864))
- Kim et al. — OpenVLA (arXiv:2406.09246) ([link](https://arxiv.org/abs/2406.09246))
- Black et al. — π0 (arXiv:2410.24164) ([link](https://arxiv.org/abs/2410.24164))
- NVIDIA — GR00T N1 (arXiv:2503.14734) ([link](https://arxiv.org/abs/2503.14734))


%% ── my notes ── %%
