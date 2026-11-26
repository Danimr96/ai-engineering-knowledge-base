---
id: "lesson:12/23"
type: lesson
ref: 12/23
phase: 12
num: 23
title: ColPali and Vision-Native Document RAG
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
aliases:
  - 12/23
  - 12-23
tags:
  - phase/12
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/23-colpali-vision-native-rag/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/23-colpali-vision-native-rag"
---

# 12/23 ColPali and Vision-Native Document RAG

> Traditional RAG parses PDFs into text, splits into chunks, embeds chunks, stores vectors. Every step loses signal: OCR drops chart data, chunking breaks table rows, text embeddings ignore figures. ColPali (Faysse et al., July 2024) asked the simpler question: why extract text at all? Embed the page image directly via PaliGemma, use ColBERT-style late interaction for retrieval, and keep all the layout, figures, fonts, and formatting signal the document carries. Published benchmarks: 20-40% better end-to-end accuracy than text-RAG on visually-rich documents. ColQwen2, ColSmol, and VisRAG extended the pattern. This lesson reads the vision-native RAG thesis and builds a tiny ColPali-like indexer.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/23-colpali-vision-native-rag/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/23-colpali-vision-native-rag) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/23-colpali-vision-native-rag) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 (LLM Engineering — RAG basics), Phase 12 · 05 (LLaVA)`

- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — LLaVA
- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM Engineering — RAG basics ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Builds on this

- [[Lessons/12-24 Multimodal RAG and Cross-Modal Retrieval|12/24 Multimodal RAG and Cross-Modal Retrieval]]

## Concepts taught

- [[Concepts/Late interaction|Late interaction]] `lesson term` — Retrieval using per-token or per-patch embeddings + MaxSim, not a single doc vector
- [[Concepts/MaxSim|MaxSim]] `lesson term` — For each query token, pick the highest-similarity document token; sum across query
- [[Concepts/Bi-encoder|Bi-encoder]] `lesson term` — One vector per document; faster but loses granularity
- [[Concepts/Multi-vector|Multi-vector]] `lesson term` — Store N_p vectors per document / page; storage cost grows but recall improves
- [[Concepts/Patch Embedding|Patch Embedding]] `glossary` — One vector per image patch from a VLM encoder, cached per page
- ViDoRe `lesson term` — ColPali's benchmark suite for visual document retrieval
- PQ quantization `lesson term` — Compression that maintains vector similarity while shrinking storage ~8x

## Ships

- [[Artifacts/12-23 vision-rag-designer|vision-rag-designer]] `skill` — Design a vision-native document RAG using ColPali / ColQwen2 / VisRAG, with storage estimate and generator-pick.

## Further reading

- [[Resources/Khattab and Zaharia (2020). ColBERT- Efficient and Effective Passage Search|Khattab and Zaharia (2020). ColBERT: Efficient and Effective Passage Search]] ([link](https://arxiv.org/abs/2004.12832)) ·  also cited by 1 other lesson
- [[Resources/Faysse et al. — ColPali (arXiv-2407.01449)|Faysse et al. — ColPali (arXiv:2407.01449)]] ([link](https://arxiv.org/abs/2407.01449)) ·  also cited by 1 other lesson
- Yu et al. — VisRAG (arXiv:2410.10594) ([link](https://arxiv.org/abs/2410.10594))
- [[Resources/Cho et al. — M3DocRAG (arXiv-2411.04952)|Cho et al. — M3DocRAG (arXiv:2411.04952)]] ([link](https://arxiv.org/abs/2411.04952)) ·  also cited by 1 other lesson
- [[Resources/illuin-tech-colpali GitHub|illuin-tech/colpali GitHub]] ([link](https://github.com/illuin-tech/colpali)) ·  also cited by 1 other lesson


%% ── my notes ── %%
