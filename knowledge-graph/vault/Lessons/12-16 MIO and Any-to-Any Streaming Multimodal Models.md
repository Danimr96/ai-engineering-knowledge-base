---
id: "lesson:12/16"
type: lesson
ref: 12/16
phase: 12
num: 16
title: MIO and Any-to-Any Streaming Multimodal Models
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 91
aliases:
  - 12/16
  - 12-16
tags:
  - phase/12
  - type/learn
  - community/91
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/16-mio-any-to-any-streaming/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/16-mio-any-to-any-streaming"
---

# 12/16 MIO and Any-to-Any Streaming Multimodal Models

> GPT-4o ships a product most open models cannot replicate: an agent that hears voice, sees video, and speaks back in real time. The open-ecosystem answer by late 2024 was MIO (Wang et al., September 2024). MIO tokenizes text, image, speech, and music, trains one causal transformer over the interleaved sequences, and generates any modality to any modality. AnyGPT (Zhan et al., February 2024) was the proof of concept; MIO is the scale-up; Unified-IO 2 (Allen AI, December 2023) is the cousin with vision + action grounding. This lesson reads the any-to-any pattern — four tokenizers, one transformer, streaming-friendly decode.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/16-mio-any-to-any-streaming/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/16-mio-any-to-any-streaming) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/16-mio-any-to-any-streaming) · code: main.py  
**Community:** [[Communities/91 Inner monologue · TMRoPE|91 Inner monologue · TMRoPE]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 11 (Chameleon), Phase 6 (Speech and Audio)`

- [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]] — Chameleon
- Whole phase: [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] — Speech and Audio ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Builds on this

- [[Lessons/12-20 Omni Models- Qwen2.5-Omni and the Thinker-Talker Split|12/20 Omni Models: Qwen2.5-Omni and the Thinker-Talker Split]]

## Concepts taught

- Any-to-any `lesson term` — A single model that accepts and emits text, image, speech, and music in any direction
- [[Concepts/Residual VQ|Residual VQ]] (as *Residual-VQ*) `lesson term` — Multi-codebook tokenization where each layer adds information; base layer is content, later layers are prosody
- SEED-Tokenizer `lesson term` — Discrete image tokenizer with 4096-entry codebook used by MIO
- Chain-of-visual-thought `lesson term` — The model generates an intermediate image as a reasoning step before its final answer
- Time-to-first-audio-byte `lesson term` — Latency from user voice to first audio output; <500ms for conversational feel
- Four-stage curriculum `lesson term` — Alignment -> interleaved -> speech-enhanced -> SFT, in that order
- [[Concepts/Modality|Modality]] `glossary` — A form of information with its own structure and acquisition process, such as text, image, audio, video, depth, or sensor measurements.
- [[Concepts/Multimodal Model|Multimodal Model]] `glossary` — A model that learns from, relates, or generates more than one modality through representation, alignment, fusion, translation, or coordinated prediction.

## Ships

- [[Artifacts/12-16 any-to-any-pipeline-auditor|any-to-any-pipeline-auditor]] `skill` — Audit a conversational any-to-any design and compute the latency budget for a MIO / AnyGPT / Moshi-family stack.

## Further reading

- Tang et al. — CoDi (arXiv:2305.11846) ([link](https://arxiv.org/abs/2305.11846))
- Wu et al. — NExT-GPT (arXiv:2309.05519) ([link](https://arxiv.org/abs/2309.05519))
- Lu et al. — Unified-IO 2 (arXiv:2312.17172) ([link](https://arxiv.org/abs/2312.17172))
- [[Resources/Zhan et al. — AnyGPT (arXiv-2402.12226)|Zhan et al. — AnyGPT (arXiv:2402.12226)]] ([link](https://arxiv.org/abs/2402.12226)) ·  also cited by 1 other lesson
- Wang et al. — MIO (arXiv:2409.17692) ([link](https://arxiv.org/abs/2409.17692))


%% ── my notes ── %%
