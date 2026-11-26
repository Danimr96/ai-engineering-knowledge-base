---
id: "lesson:12/20"
type: lesson
ref: 12/20
phase: 12
num: 20
title: "Omni Models: Qwen2.5-Omni and the Thinker-Talker Split"
lesson_type: build
languages:
  - Python
time_min: 180
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
community: 91
aliases:
  - 12/20
  - 12-20
tags:
  - phase/12
  - type/build
  - community/91
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/20-omni-models-thinker-talker/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/20-omni-models-thinker-talker"
---

# 12/20 Omni Models: Qwen2.5-Omni and the Thinker-Talker Split

> GPT-4o's product demo in May 2024 was disruptive not because of the underlying model but because of the product shape — a voice interface where you talk, the model sees what the camera sees, and it talks back in under 250ms. The open ecosystem spent the rest of 2024 and 2025 racing to reach that product surface. Qwen2.5-Omni (March 2025) is the reference open design: a Thinker (large text-generating transformer) plus a Talker (parallel speech-generating transformer), linked by streaming speech tokens. Mini-Omni simplified it, Moshi matched its latency, GLM-4-Voice extended it to Chinese. This lesson reads the Thinker-Talker architecture and the latency budget that makes streaming real-time dialogue work.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/20-omni-models-thinker-talker/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/20-omni-models-thinker-talker) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/20-omni-models-thinker-talker) · code: main.py  
**Community:** [[Communities/91 Inner monologue · TMRoPE|91 Inner monologue · TMRoPE]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 19 (audio-LLMs), Phase 12 · 16 (any-to-any)`

- [[Lessons/12-16 MIO and Any-to-Any Streaming Multimodal Models|12/16 MIO and Any-to-Any Streaming Multimodal Models]] — any-to-any
- [[Lessons/12-19 Audio-Language Models- the Whisper to Audio Flamingo 3 Arc|12/19 Audio-Language Models: the Whisper to Audio Flamingo 3 Arc]] — audio-LLMs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]], [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]], [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]

## Concepts taught

- Thinker `lesson term` — Large text-generating transformer producing what to say
- Talker `lesson term` — Small transformer producing discrete speech tokens from Thinker's text
- TTFAB `lesson term` — Time-to-first-audio-byte: from user speech end to first audio sample out
- [[Concepts/TMRoPE|TMRoPE]] `lesson term` — Position encoding using absolute timestamps across vision, audio, text
- Half-duplex `lesson term` — User and model alternate; VAD silence detects user-done
- [[Concepts/Full duplex|Full duplex]] (as *Full-duplex*) `lesson term` — Model can speak and listen at the same time; backchannel capable
- [[Concepts/Inner monologue|Inner monologue]] `lesson term` — Single-model design where thinking-stream and speaking-stream interleave

## Ships

- [[Artifacts/12-20 omni-streaming-budget|omni-streaming-budget]] `skill` — Size a Thinker-Talker streaming voice pipeline (Qwen-Omni / Moshi / Mini-Omni) for a target TTFAB and feature set.

## Further reading

- Xie & Wu — Mini-Omni (arXiv:2408.16725) ([link](https://arxiv.org/abs/2408.16725))
- [[Resources/Défossez et al. (2024). Moshi — speech-text foundation model|Défossez et al. (2024). Moshi — speech-text foundation model]] ([link](https://arxiv.org/html/2410.00037v2)) ·  also cited by 1 other lesson
- Zeng et al. — GLM-4-Voice (arXiv:2412.02612) ([link](https://arxiv.org/abs/2412.02612))
- Xu et al. — Qwen2.5-Omni (arXiv:2503.20215) ([link](https://arxiv.org/abs/2503.20215))
- Qwen Team — Qwen3-Omni (arXiv:2509.17765) ([link](https://arxiv.org/html/2509.17765v1))


%% ── my notes ── %%
