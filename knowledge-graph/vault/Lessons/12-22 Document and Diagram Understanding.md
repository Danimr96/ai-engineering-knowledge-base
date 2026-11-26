---
id: "lesson:12/22"
type: lesson
ref: 12/22
phase: 12
num: 22
title: Document and Diagram Understanding
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
community: 95
aliases:
  - 12/22
  - 12-22
tags:
  - phase/12
  - type/build
  - community/95
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/22-document-diagram-understanding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/22-document-diagram-understanding"
---

# 12/22 Document and Diagram Understanding

> Documents are not photos. A PDF, scientific paper, invoice, or handwritten form has layout, tables, diagrams, footnotes, headers, and semantic structure that plain image understanding cannot capture. The pre-VLM stack was a pipeline: Tesseract OCR + LayoutLMv3 + table-extraction heuristics. The VLM wave replaced that with OCR-free models — Donut (2022), Nougat (2023), DocLLM (2023) — that emit structured markup directly. By 2026 the frontier is just "feed the page image to Claude Opus 4.7 at 2576px native," and the structured-markup output comes for free. This lesson reads the three-era arc of document AI.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/22-document-diagram-understanding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/22-document-diagram-understanding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/22-document-diagram-understanding) · code: main.py  
**Community:** [[Communities/95 Projector|95 Projector]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 05 (LLaVA), Phase 5 (NLP)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Concepts taught

- OCR pipeline `lesson term` — Stage-wise stack: detect -> OCR -> layout -> rules; deterministic, fragile
- OCR-free `lesson term` — Image-to-output transformer that skips explicit OCR; single model
- Layout-aware `lesson term` — Input includes per-token bbox coordinates; unified masking across modalities
- VLM-native `lesson term` — Feed page image directly to Claude/GPT/Qwen VLM at high resolution; no pipeline
- DocVQA `lesson term` — Document VQA standard; most-cited score
- Markup output `lesson term` — Structured output format instead of free-form text; enables downstream automation

## Ships

- [[Artifacts/12-22 document-ai-stack-picker|document-ai-stack-picker]] `skill` — Pick between OCR pipeline, OCR-free specialist, and VLM-native for a document-AI project based on domain, scale, and regulatory needs.

## Further reading

- Li et al. — TrOCR (arXiv:2109.10282) ([link](https://arxiv.org/abs/2109.10282))
- [[Resources/Donut (Kim et al., 2022)|Donut (Kim et al., 2022)]] ([link](https://arxiv.org/abs/2111.15664)) ·  also cited by 1 other lesson
- Huang et al. — LayoutLMv3 (arXiv:2204.08387) ([link](https://arxiv.org/abs/2204.08387))
- Blecher et al. — Nougat (arXiv:2308.13418) ([link](https://arxiv.org/abs/2308.13418))
- Wang et al. — DocLLM (arXiv:2401.00908) ([link](https://arxiv.org/abs/2401.00908))


%% ── my notes ── %%
