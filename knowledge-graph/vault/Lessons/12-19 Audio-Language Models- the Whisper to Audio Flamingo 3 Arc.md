---
id: "lesson:12/19"
type: lesson
ref: 12/19
phase: 12
num: 19
title: "Audio-Language Models: the Whisper to Audio Flamingo 3 Arc"
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
  - 12/19
  - 12-19
tags:
  - phase/12
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/19-audio-language-whisper-to-af3/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/19-audio-language-whisper-to-af3"
---

# 12/19 Audio-Language Models: the Whisper to Audio Flamingo 3 Arc

> Whisper (Radford et al., December 2022) settled speech recognition — 680k hours of weakly-supervised multilingual speech, a simple encoder-decoder transformer, a benchmark that made every subsequent ASR release cite it. But recognition is not reasoning. Asking "what instruments are in this recording" or "what emotion is the speaker expressing" or "what happened at minute 3" requires audio understanding, not transcription. Qwen-Audio, SALMONN, LTU, and NVIDIA's Audio Flamingo 3 (AF3, July 2025) progressively built that stack: keep Whisper-class encoders, bolt on Q-formers, train on audio-text instruction data, add chain-of-thought reasoning. This lesson walks the arc.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Build · **Time:** 180 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/19-audio-language-whisper-to-af3/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/19-audio-language-whisper-to-af3) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/19-audio-language-whisper-to-af3) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 (Speech and Audio), Phase 12 · 03 (Q-Former)`

- [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]] — Q-Former
- Whole phase: [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] — Speech and Audio ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Builds on this

- [[Lessons/12-20 Omni Models- Qwen2.5-Omni and the Thinker-Talker Split|12/20 Omni Models: Qwen2.5-Omni and the Thinker-Talker Split]]

## Concepts taught

- Log-Mel spectrogram `lesson term` — 2D (time, frequency) array of log-magnitude values after Mel filter banks
- Audio Q-former `lesson term` — Cross-attention bottleneck from audio encoder output to fixed-length queries feeding the LLM
- Cascaded `lesson term` — Pipeline where Whisper transcribes and a text LLM reasons; loses acoustic information
- [[Concepts/End-to-end|End-to-end]] `lesson term` — Audio features enter the LLM directly via Q-former; preserves acoustic signal
- [[Concepts/BEATs|BEATs]] `lesson term` — SSL transformer trained on AudioSet; strong on music + environmental sounds
- [[Concepts/MMAU|MMAU]] `lesson term` — 10k QA pairs across speech, music, environment; 2024 eval standard
- On-demand thinking `lesson term` — Model can optionally emit reasoning tokens before final answer, lifts accuracy 3-5 pts

## Ships

- [[Artifacts/12-19 audio-llm-pipeline-picker|audio-llm-pipeline-picker]] `skill` — Pick cascaded (Whisper + LLM) or end-to-end (AF3 / Qwen-Audio) for an audio task, plus the encoder and bridge config.

## Further reading

- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) ·  also cited by 5 other lessons
- Gong et al. — LTU (arXiv:2305.10790) ([link](https://arxiv.org/abs/2305.10790))
- [[Resources/Tang et al. (2023). SALMONN|Tang et al. (2023). SALMONN]] ([link](https://arxiv.org/abs/2310.13289)) ·  also cited by 1 other lesson
- Chu et al. — Qwen-Audio (arXiv:2311.07919) ([link](https://arxiv.org/abs/2311.07919))
- [[Resources/NVIDIA (2025). Audio Flamingo 3|NVIDIA (2025). Audio Flamingo 3]] ([link](https://arxiv.org/abs/2507.08128)) ·  also cited by 1 other lesson


%% ── my notes ── %%
