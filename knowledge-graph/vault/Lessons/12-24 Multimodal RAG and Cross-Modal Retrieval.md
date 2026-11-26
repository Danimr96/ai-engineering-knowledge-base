---
id: "lesson:12/24"
type: lesson
ref: 12/24
phase: 12
num: 24
title: Multimodal RAG and Cross-Modal Retrieval
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
aliases:
  - 12/24
  - 12-24
tags:
  - phase/12
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/24-multimodal-rag-cross-modal/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/24-multimodal-rag-cross-modal"
---

# 12/24 Multimodal RAG and Cross-Modal Retrieval

> Vision-native document RAG is one slice. Production multimodal RAG goes wider — retrieving across text, images, audio, and video for workflows like trip planning ("find me a quiet vegan brunch with natural light"), medical triage ("what injury matches this photo + these notes"), e-commerce ("outfits similar to this selfie, in my size"), and field service ("diagnose this engine sound plus photo of the part"). Three 2025 surveys — Abootorabi et al., Mei et al., Zhao et al. — codified the sub-problems: cross-modal retrieval, retrieval fusion, generation grounding, multimodal evaluation. This lesson reads the surveys and designs a production pipeline.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/24-multimodal-rag-cross-modal/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/24-multimodal-rag-cross-modal) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/24-multimodal-rag-cross-modal) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 23 (ColPali), Phase 11 (RAG basics)`

- [[Lessons/12-23 ColPali and Vision-Native Document RAG|12/23 ColPali and Vision-Native Document RAG]] — ColPali
- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — RAG basics ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Concepts taught

- Cross-modal retrieval `lesson term` — Text query retrieves images; image query retrieves text; requires a shared space or translator
- Score fusion `lesson term` — Weighted sum of per-modality retrieval scores; simplest fusion
- MoE fusion `lesson term` — Gating network picks which modality's scores to trust per query
- Grounded generation `lesson term` — Each claim in the answer tagged with the source index
- MuRAG `lesson term` — 2022 paper that established the multimodal RAG pattern
- Agentic multi-hop `lesson term` — LLM re-queries retrievers when first-pass confidence is low

## Ships

- [[Artifacts/12-24 multimodal-rag-designer|multimodal-rag-designer]] `skill` — Design a production multimodal RAG across text, images, audio, video with retrievers, fusion strategy, and grounded generator.

## Further reading

- Chen et al. — MuRAG (arXiv:2210.02928) ([link](https://arxiv.org/abs/2210.02928))
- Liu et al. — REACT (arXiv:2301.10382) ([link](https://arxiv.org/abs/2301.10382))
- Abootorabi et al. — Ask in Any Modality (arXiv:2502.08826) ([link](https://arxiv.org/abs/2502.08826))
- Zhao et al. — Vision RAG Survey (arXiv:2503.18016) ([link](https://arxiv.org/abs/2503.18016))
- Mei et al. — A Survey of Multimodal RAG (arXiv:2504.08748) ([link](https://arxiv.org/abs/2504.08748))


%% ── my notes ── %%
