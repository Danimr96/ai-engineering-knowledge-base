---
id: "lesson:12/14"
type: lesson
ref: 12/14
phase: 12
num: 14
title: Show-o and Discrete-Diffusion Unified Models
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
aliases:
  - 12/14
  - 12-14
tags:
  - phase/12
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified"
---

# 12/14 Show-o and Discrete-Diffusion Unified Models

> Transfusion mixes continuous and discrete representations. Show-o (Xie et al., August 2024) goes the other way: text tokens use causal next-token prediction, image tokens use masked discrete diffusion in the spirit of MaskGIT. Both sit inside one transformer with a hybrid attention mask. The result unifies VQA, text-to-image, inpainting, and mixed-modality generation on one backbone, one tokenizer per modality, one loss formulation (next-token extended to masked prediction). This lesson walks the Show-o design — why masked discrete diffusion is a parallel, few-step image generator — and contrasts with Transfusion and Emu3.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/14-show-o-discrete-diffusion-unified/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 13 (Transfusion)`

- [[Lessons/12-13 Transfusion- Autoregressive Text + Diffusion Image in One Transformer|12/13 Transfusion: Autoregressive Text + Diffusion Image in One Transformer]] — Transfusion

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]]
- depth 3: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]

## Builds on this

- [[Lessons/12-15 Janus-Pro- Decoupled Encoders for Unified Multimodal Models|12/15 Janus-Pro: Decoupled Encoders for Unified Multimodal Models]]

## Concepts taught

- Masked discrete diffusion `lesson term` — Training to predict masked tokens; at inference, iteratively unmask the most-confident predictions
- Cosine schedule `lesson term` — Decay of mask ratio over inference steps; concentrates confidence growth at mid-range
- Parallel decoding `lesson term` — Every step predicts the full sequence of masked tokens in one forward pass, then commits top-K
- Hybrid attention `lesson term` — Mask that is causal over text tokens and bidirectional within image blocks
- [[Concepts/Inpainting|Inpainting]] `lesson term` — Condition on an image with some tokens masked, predict the missing ones; free from the training objective
- Commitment rate `lesson term` — How many tokens are declared "done" per iteration; controls inference vs quality trade-off

## Ships

- [[Artifacts/12-14 unified-gen-model-picker|unified-gen-model-picker]] `skill` — Pick between Show-o / Transfusion / Emu3 / Janus-Pro families for a product that needs both multimodal understanding and generation with open weights.

## Further reading

- Chang et al. — MaskGIT (arXiv:2202.04200) ([link](https://arxiv.org/abs/2202.04200))
- Chang et al. — Muse (arXiv:2301.00704) ([link](https://arxiv.org/abs/2301.00704))
- Sun et al. — LlamaGen (arXiv:2406.06525) ([link](https://arxiv.org/abs/2406.06525))
- [[Resources/Xie et al. — Show-o (arXiv-2408.12528)|Xie et al. — Show-o (arXiv:2408.12528)]] ([link](https://arxiv.org/abs/2408.12528)) ·  also cited by 1 other lesson
- Show-o2 (arXiv:2506.15564) ([link](https://arxiv.org/abs/2506.15564))


%% ── my notes ── %%
