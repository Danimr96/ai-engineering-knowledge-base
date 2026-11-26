---
id: "lesson:12/18"
type: lesson
ref: 12/18
phase: 12
num: 18
title: Long-Video Understanding at Million-Token Context
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
community: 84
aliases:
  - 12/18
  - 12-18
tags:
  - phase/12
  - type/build
  - community/84
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/18-long-video-million-token/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/18-long-video-million-token"
---

# 12/18 Long-Video Understanding at Million-Token Context

> A 1-hour 4K video at 24 FPS, patched and embedded, produces on the order of 60 million tokens. A 2-hour podcast episode transcribed is 30,000 tokens. A full Blu-ray feature film, even compressed with aggressive pooling, is hundreds of thousands of tokens. Google's Gemini 1.5 (March 2024) opened this era with a 10-million-token context, doing reliable needle-in-a-haystack recall over hour-long videos. LWM (Liu et al., February 2024) showed ring attention's scaling path. LongVILA and Video-XL scaled ingestion further. VideoAgent swapped raw context for agentic retrieval. Each approach is a different trade-off on compute, recall, and engineering complexity. This lesson reads them side by side.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/18-long-video-million-token/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/18-long-video-million-token) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/18-long-video-million-token) · code: main.py  
**Community:** [[Communities/84 Curriculum|84 Curriculum]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 17 (video temporal tokens)`

- [[Lessons/12-17 Video-Language Models- Temporal Tokens and Grounding|12/17 Video-Language Models: Temporal Tokens and Grounding]] — video temporal tokens

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-08 LLaVA-OneVision- Single-Image, Multi-Image, Video in One Model|12/08 LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model]]
- depth 3: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]], [[Lessons/12-06 Any-Resolution Vision- Patch-n'-Pack and NaFlex|12/06 Any-Resolution Vision: Patch-n'-Pack and NaFlex]]

## Concepts taught

- Brute context `lesson term` — Scale LLM context to millions of tokens; process everything in one pass
- Ring attention `lesson term` — Distributed attention pattern where each device holds a chunk and rotates
- Token compression `lesson term` — Reduce per-clip tokens via a learned compressor before the LLM
- Needle-in-haystack `lesson term` — Insert a unique marker at a random point, ask model to recall it at test time
- Agentic retrieval `lesson term` — LLM asks a retrieval tool for relevant clips, reads them via a VLM, composes answer
- VideoAgent `lesson term` — Canonical agentic-retrieval design: question -> tool -> clip -> answer

## Ships

- [[Artifacts/12-18 long-video-strategy-planner|long-video-strategy-planner]] `skill` — Pick brute-context, ring-attention, token-compression, or agentic-retrieval for a long-video understanding task and compute latency + recall expectations.

## Further reading

- [[Resources/Liu et al. — LWM (arXiv-2402.08268)|Liu et al. — LWM (arXiv:2402.08268)]] ([link](https://arxiv.org/abs/2402.08268)) ·  also cited by 1 other lesson
- Gemini Team — Gemini 1.5 (arXiv:2403.05530) ([link](https://arxiv.org/abs/2403.05530))
- Wang et al. — VideoAgent (arXiv:2403.10517) ([link](https://arxiv.org/abs/2403.10517))
- Xue et al. — LongVILA (arXiv:2408.10188) ([link](https://arxiv.org/abs/2408.10188))
- Shu et al. — Video-XL (arXiv:2409.14485) ([link](https://arxiv.org/abs/2409.14485))


%% ── my notes ── %%
