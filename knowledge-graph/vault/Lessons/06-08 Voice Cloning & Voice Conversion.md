---
id: "lesson:06/08"
type: lesson
ref: 06/08
phase: 6
num: 8
title: "Voice Cloning & Voice Conversion"
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
  - 06/08
  - 06-08
tags:
  - phase/06
  - type/build
  - community/64
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/08-voice-cloning-conversion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/08-voice-cloning-conversion"
---

# 06/08 Voice Cloning & Voice Conversion

> Voice cloning reads your text in someone else's voice. Voice conversion rewrites your voice into someone else's while preserving what you said. Both hang on the same decomposition: separate speaker identity from content.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/08-voice-cloning-conversion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/08-voice-cloning-conversion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/08-voice-cloning-conversion) · code: main.py  
**Community:** [[Communities/64 AASIST · C2PA · SECS|64 AASIST · C2PA · SECS]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 06 (Speaker Recognition), Phase 6 · 07 (TTS)`

- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]] — Speaker Recognition
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]] — TTS

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]

## Builds on this

- [[Lessons/06-16 Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify|06/16 Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify]]

## Concepts taught

- Zero-shot clone `lesson term` — Pretrained model + speaker embedding; no training.
- PPG `lesson term` — Per-frame ASR posteriors used as language-agnostic content rep.
- KNN-VC `lesson term` — Replace each source frame with nearest target-pool frame.
- Neural codec TTS `lesson term` — AR model over EnCodec/SoundStream tokens.
- Watermark `lesson term` — Bits embedded in audio, survive re-encode.
- [[Concepts/SECS|SECS]] `lesson term` — Cosine between target and clone speaker embeddings.
- [[Concepts/AASIST|AASIST]] `lesson term` — Anti-spoof model; detects synthesized speech.

## Ships

- [[Artifacts/06-08 voice-cloner|voice-cloner]] `skill` — Pick cloning approach (zero-shot / conversion / adaptation), consent artifact, watermark, and safety filters for a voice-cloning deployment.

## Further reading

- Qian et al. (2019). AutoVC ([link](https://arxiv.org/abs/1905.05879)) — disentanglement-based voice conversion.
- [[Resources/Baevski et al. - Microsoft (2023). VALL-E|Baevski et al. / Microsoft (2023). VALL-E]] ([link](https://arxiv.org/abs/2301.02111)) — and [VALL-E 2 (2024)](https://arxiv.org/abs/2406.05370) — neural-codec TTS. ·  also cited by 1 other lesson
- Baas, Waubert de Puiseau, Kamper (2023). KNN-VC ([link](https://arxiv.org/abs/2305.18975)) — retrieval-based VC.
- VALL-E 2 (2024) ([link](https://arxiv.org/abs/2406.05370)) — neural-codec TTS.
- [[Resources/Chen et al. (2024). F5-TTS|Chen et al. (2024). F5-TTS]] ([link](https://arxiv.org/abs/2410.06885)) — open-source SOTA zero-shot cloning. ·  also cited by 1 other lesson
- ASVspoof 2025 results ([link](https://www.asvspoof.org/)) — detector vs synthesizer arms race, updated 2026.
- SilentCipher (2024) — Audio Watermarking ([link](https://github.com/sony/silentcipher)) — production-ready 32-bit audio watermark.


%% ── my notes ── %%
