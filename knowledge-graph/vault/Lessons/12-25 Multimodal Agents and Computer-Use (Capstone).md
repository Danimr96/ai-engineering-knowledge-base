---
id: "lesson:12/25"
type: lesson
ref: 12/25
phase: 12
num: 25
title: Multimodal Agents and Computer-Use (Capstone)
lesson_type: capstone
languages:
  - Python
time_min: 240
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 31
aliases:
  - 12/25
  - 12-25
tags:
  - phase/12
  - type/capstone
  - community/31
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/25-multimodal-agents-computer-use/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/25-multimodal-agents-computer-use"
---

# 12/25 Multimodal Agents and Computer-Use (Capstone)

> The 2026 frontier product is a multimodal agent that reads screenshots, clicks buttons, navigates web UIs, fills forms, and completes workflows end-to-end. SeeClick and CogAgent (2024) proved the GUI-grounding primitive. Ferret-UI added mobile. ChartAgent introduced visual tool-use for charts. VisualWebArena and AgentVista (2026) are the benchmarks the frontier chases — and even Gemini 3 Pro and Claude Opus 4.7 score ~30% on AgentVista's hard tasks. This capstone pulls together every thread of Phase 12: perception (high-res VLM), reasoning (LLM with tool use), grounding (coordinate output), long-horizon memory, and evaluation.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Capstone · **Time:** 240 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/25-multimodal-agents-computer-use/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/25-multimodal-agents-computer-use) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/25-multimodal-agents-computer-use) · code: main.py  
**Community:** [[Communities/31 GUI grounding · VisualWebArena · OSWorld|31 GUI grounding · VisualWebArena · OSWorld]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05 (LLaVA), Phase 12 · 09 (Qwen-VL JSON), Phase 14 (Agent Engineering)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA
- [[Lessons/12-09 Qwen-VL Family and Dynamic-FPS Video|12/09 Qwen-VL Family and Dynamic-FPS Video]] — Qwen-VL JSON
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agent Engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]], [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Concepts taught

- [[Concepts/GUI grounding|GUI grounding]] `lesson term` — Model outputs (x,y) for the target of an instruction on a screenshot
- Action schema `lesson term` — JSON description of valid actions (click, type, scroll, drag)
- Accessibility tree `lesson term` — Machine-readable UI hierarchy from browser/iOS APIs
- Hybrid agent `lesson term` — Uses both image and structured info; more reliable than either alone
- Visual tool use `lesson term` — Agent calls external vision tools (OCR, detection) mid-plan
- Summary-chain `lesson term` — Periodic text summaries replace long screenshot history
- [[Concepts/VisualWebArena|VisualWebArena]] `lesson term` — 2024 benchmark for end-to-end web tasks
- AgentVista `lesson term` — 12-domain realistic workflows; even Gemini 3 Pro scores ~30%

## Ships

- [[Artifacts/12-25 multimodal-agent-designer|multimodal-agent-designer]] `skill` — Design a multimodal agent (computer-use, GUI grounding, web or mobile) with action schema, memory strategy, and benchmark evaluation plan.

## Further reading

- Hong et al. — CogAgent (arXiv:2312.08914) ([link](https://arxiv.org/abs/2312.08914))
- Cheng et al. — SeeClick (arXiv:2401.10935) ([link](https://arxiv.org/abs/2401.10935))
- Koh et al. — VisualWebArena (arXiv:2401.13649) ([link](https://arxiv.org/abs/2401.13649))
- You et al. — Ferret-UI (arXiv:2404.05719) ([link](https://arxiv.org/abs/2404.05719))
- ChartAgent (arXiv:2510.04514) ([link](https://arxiv.org/abs/2510.04514))
- AgentVista (arXiv:2602.23166) ([link](https://arxiv.org/abs/2602.23166))


%% ── my notes ── %%
