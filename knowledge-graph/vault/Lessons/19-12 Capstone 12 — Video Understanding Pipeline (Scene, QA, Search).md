---
id: "lesson:19/12"
type: lesson
ref: 19/12
phase: 19
num: 12
title: "Capstone 12 — Video Understanding Pipeline (Scene, QA, Search)"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 7
concepts: 7
prereqs: 0
libraries:
  - hono
aliases:
  - 19/12
  - 19-12
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/12-video-understanding-pipeline/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/12-video-understanding-pipeline"
---

# 19/12 Capstone 12 — Video Understanding Pipeline (Scene, QA, Search)

> Twelve Labs productized Marengo + Pegasus. VideoDB shipped the CRUD-for-video API. AI2's Molmo 2 published open VLM checkpoints. Gemini long-context handles hours of video natively. TimeLens-100K defined temporal grounding at scale. The 2026 pipeline is settled: scene segmentation, per-scene caption + embedding, transcript alignment, multi-vector index, and a query that answers with (start, end) timestamps plus frame previews. The capstone is ingesting 100 hours, hitting public benchmarks, and measuring hallucination on counting and action questions.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/12-video-understanding-pipeline/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/12-video-understanding-pipeline) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/12-video-understanding-pipeline) · code: main.py, ts/src/index.ts, ts/src/jobs.ts, ts/src/server.ts, ts/src/stages.ts, ts/src/types.ts … · quiz: 7 questions  
**Libraries:** [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 4 (CV), Phase 6 (speech), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 12 (multimodal), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] — multimodal ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/04 Computer Vision|Phase 4: Computer Vision]] — CV ·  medium confidence
- Whole phase: [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] — speech ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- Scene segmentation `lesson term` — Cutting video into scenes at shot boundaries
- Multi-vector index `lesson term` — Qdrant collection with named vectors per representation
- [[Concepts/Temporal grounding|Temporal grounding]] `lesson term` — Refining the (start, end) window for a query answer
- Frame embedding `lesson term` — A vector embedding of a keyframe; used for scene-visual similarity
- RRF fusion `lesson term` — Merge strategy across multiple ranked lists; a classic hybrid-retrieval trick
- Counting hallucination `lesson term` — Known failure mode of VLMs on "how many X" questions
- ActivityNet-QA `lesson term` — Long-form video QA accuracy benchmark

## Ships

- [[Artifacts/19-12 video-qa|video-qa]] `skill` — Build a video understanding pipeline with scene segmentation, multi-vector indexing, temporal grounding, and timestamped citations.

## Further reading

- AI2 Molmo 2 ([link](https://allenai.org/blog/molmo2)) — open VLM checkpoints
- ActivityNet-QA ([link](https://arxiv.org/abs/1906.02467)) — reference eval benchmark
- Gemini Video long-context ([link](https://deepmind.google/technologies/gemini)) — the hosted reference
- PySceneDetect ([link](https://github.com/Breakthrough/PySceneDetect)) — classic open alternative
- TimeLens (CVPR 2026) ([link](https://github.com/TencentARC/TimeLens)) — temporal grounding at scale
- TransNetV2 ([link](https://github.com/soCzech/TransNetV2)) — scene segmentation model
- Twelve Labs Marengo + Pegasus ([link](https://www.twelvelabs.io)) — commercial reference
- VideoDB ([link](https://videodb.io)) — CRUD-for-video API reference


%% ── my notes ── %%
