---
id: "lesson:06/16"
type: lesson
ref: 06/16
phase: 6
num: 16
title: "Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
community: 64
aliases:
  - 06/16
  - 06-16
tags:
  - phase/06
  - type/build
  - community/64
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking"
---

# 06/16 Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify

> Voice cloning shipped faster than defenses. 2026 production voice systems need two things: a detector (AASIST, RawNet2) that classifies real vs fake speech, and a watermark (AudioSeal) that survives compression and editing. Ship both or do not ship voice cloning.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/16-anti-spoofing-audio-watermarking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking) · code: main.py  
**Community:** [[Communities/64 AASIST · C2PA · SECS|64 AASIST · C2PA · SECS]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 06 (Speaker Recognition), Phase 6 · 08 (Voice Cloning)`

- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]] — Speaker Recognition
- [[Lessons/06-08 Voice Cloning & Voice Conversion|06/08 Voice Cloning & Voice Conversion]] — Voice Cloning

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- depth 3: [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]

## Concepts taught

- ASVspoof `lesson term` — Biennial challenge; 2024 = ASVspoof 5.
- CM (countermeasure) `lesson term` — Classifier: real speech vs synthetic / converted.
- SASV `lesson term` — Integrated biometric + spoof detection.
- AudioSeal `lesson term` — Localized, 16-bit payload, 485× faster than WavMark.
- Bit Recovery Accuracy `lesson term` — Fraction of payload bits recovered after attack.
- [[Concepts/C2PA|C2PA]] `lesson term` — Cryptographic metadata about creation / authorship.
- [[Concepts/AASIST|AASIST]] `lesson term` — Graph-attention-based anti-spoofing SOTA.

## Ships

- [[Artifacts/06-16 spoof-defender|spoof-defender]] `skill` — Pick detection model, watermark, provenance manifest, and operational playbook for a voice-generation / voice-auth deployment.

## Further reading

- Jung et al. (2022). AASIST ([link](https://arxiv.org/abs/2110.01200)) — the SOTA detection backbone.
- Defossez et al. (2024). AudioSeal ([link](https://arxiv.org/abs/2401.17264)) — the watermark default.
- Chen et al. (2025). WaveVerify ([link](https://arxiv.org/abs/2507.21150)) — MoE detector for temporal attacks.
- C2PA specification ([link](https://c2pa.org/specifications/specifications/)) — provenance manifest format.
- Todisco et al. (2024). ASVspoof 5 ([link](https://dl.acm.org/doi/10.1016/j.csl.2025.101825)) — the current benchmark.
- AudioMarkBench (2024) ([link](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d9b7775296a641a1913ab6b4425d5e8-Paper-Datasets_and_Benchmarks_Track.pdf)) — robustness evaluation.


%% ── my notes ── %%
