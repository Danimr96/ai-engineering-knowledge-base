---
id: "lesson:06/05"
type: lesson
ref: 06/05
phase: 6
num: 5
title: "Whisper — Architecture & Fine-Tuning"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 3
community: 9
aliases:
  - 06/05
  - 06-05
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/05-whisper-architecture-finetuning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/05-whisper-architecture-finetuning"
---

# 06/05 Whisper — Architecture & Fine-Tuning

> Whisper is a 30-second-window transformer encoder-decoder, trained on 680k hours of multilingual weakly-supervised audio-text pairs. One architecture, multiple tasks, robust across 99 languages. The 2026 reference ASR.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/05-whisper-architecture-finetuning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/05-whisper-architecture-finetuning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/05-whisper-architecture-finetuning) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 04 (ASR), Phase 5 · 10 (Attention), Phase 7 · 05 (Full Transformer)`

- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Attention
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]] — ASR
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]

## Builds on this

- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]

## Concepts taught

- 30-sec window `lesson term` — Hard input cap; chunk longer audio.
- SOT `lesson term` — <|startoftranscript|> kicks off the decoder prompt.
- Timestamps token `lesson term` — Every 0.02 s offset is a special token in the 51k vocab.
- Turbo `lesson term` — 4-decoder layers, 8× faster, <1% WER regression.
- WhisperX `lesson term` — VAD + Whisper + wav2vec alignment + diarization.
- LoRA fine-tune `lesson term` — Add low-rank adapters to attention; train ~0.3% of params.
- [[Concepts/Hallucination|Hallucination]] `glossary` — Whisper produces fluent English from noise/silence.

## Ships

- [[Artifacts/06-05 whisper-tuner|whisper-tuner]] `skill` — Design a Whisper fine-tune or inference pipeline for a given language, domain, and latency budget.

## Further reading

- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) — the original architecture and training recipe. ·  also cited by 5 other lessons
- Bain et al. (2023). WhisperX ([link](https://arxiv.org/abs/2303.00747)) — long-form, word-aligned, diarized.
- [[Resources/Systran — faster-whisper repo|Systran — faster-whisper repo]] ([link](https://github.com/SYSTRAN/faster-whisper)) — CTranslate2-backed, 4× faster. ·  also cited by 1 other lesson
- OpenAI (2024). Whisper Large-v3-turbo release ([link](https://github.com/openai/whisper/discussions/2363)) — 4-layer decoder, 8× speedup.
- [[Resources/HuggingFace — Whisper fine-tune tutorial|HuggingFace — Whisper fine-tune tutorial]] ([link](https://huggingface.co/blog/fine-tune-whisper)) — canonical LoRA / full-FT walkthrough. ·  also cited by 1 other lesson


%% ── my notes ── %%
