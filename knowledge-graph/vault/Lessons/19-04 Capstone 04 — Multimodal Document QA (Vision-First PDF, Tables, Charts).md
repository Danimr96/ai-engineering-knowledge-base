---
id: "lesson:19/04"
type: lesson
ref: 19/04
phase: 19
num: 4
title: "Capstone 04 — Multimodal Document QA (Vision-First PDF, Tables, Charts)"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 9
concepts: 7
prereqs: 0
libraries:
  - hono
aliases:
  - 19/04
  - 19-04
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/04-multimodal-document-qa/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/04-multimodal-document-qa"
---

# 19/04 Capstone 04 — Multimodal Document QA (Vision-First PDF, Tables, Charts)

> The 2026 document-QA frontier moved away from OCR-then-text and toward vision-first late interaction. ColPali, ColQwen2.5, and ColQwen3-omni treat each PDF page as an image, embed it with multi-vector late interaction, and let the query attend to patches directly. On financial 10-Ks, scientific papers, and handwritten notes this pattern beats OCR-first by a large margin. Build the pipeline end to end on 10k pages and publish the side-by-side against OCR-then-text.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/04-multimodal-document-qa/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/04-multimodal-document-qa) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/04-multimodal-document-qa) · code: main.py, ts/src/fixtures.ts, ts/src/index.ts, ts/src/render.ts, ts/src/server.ts, ts/src/types.ts … · quiz: 7 questions  
**Libraries:** [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 4 (computer vision), Phase 5 (NLP), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 12 (multimodal), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] — multimodal ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/04 Computer Vision|Phase 4: Computer Vision]] — computer vision ·  medium confidence
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- [[Concepts/Late interaction|Late interaction]] `lesson term` — Query tokens score against page patches independently; MaxSim aggregates
- [[Concepts/Multi-vector|Multi-vector]] `lesson term` — Each document has many vectors, not one pooled vector
- [[Concepts/MaxSim|MaxSim]] `lesson term` — For every query token, take max similarity over document vectors; sum
- DocPruner `lesson term` — 2026 pruning that keeps 50% of patches with negligible accuracy loss
- ViDoRe v3 `lesson term` — The 2026 standard for measuring visual-document retrieval
- Evidence region `lesson term` — A bbox on the source page that localizes the answer span
- OCR fallback `lesson term` — Text pipeline used alongside vision for equation- or table-heavy pages

## Ships

- [[Artifacts/19-04 doc-qa|doc-qa]] `skill` — Build a vision-first multimodal document QA system on 10k pages with late-interaction retrieval and evidence-region citations.

## Further reading

- [[Resources/Faysse et al. — ColPali (arXiv-2407.01449)|Faysse et al. — ColPali (arXiv:2407.01449)]] ([link](https://arxiv.org/abs/2407.01449)) — the foundational method paper ·  also cited by 1 other lesson
- [[Resources/Cho et al. — M3DocRAG (arXiv-2411.04952)|Cho et al. — M3DocRAG (arXiv:2411.04952)]] ([link](https://arxiv.org/abs/2411.04952)) — multi-page multimodal RAG baseline ·  also cited by 1 other lesson
- AstraDB multi-vector ([link](https://docs.datastax.com/en/astra-db-serverless/databases/vector-search.html)) — alternate managed index
- Vespa multi-vector tutorial ([link](https://docs.vespa.ai/en/colpali.html)) — reference serving stack
- Nougat OCR ([link](https://github.com/facebookresearch/nougat)) — equation-capable OCR fallback
- [[Resources/illuin-tech-colpali GitHub|illuin-tech/colpali GitHub]] ([link](https://github.com/illuin-tech/colpali)) — reference late-interaction doc retrieval ·  also cited by 1 other lesson
- ColQwen family on Hugging Face ([link](https://huggingface.co/vidore)) — production-ready checkpoints
- Qdrant multi-vector support ([link](https://qdrant.tech/documentation/concepts/vectors/#multivectors)) — alternate index


%% ── my notes ── %%
