---
id: "lesson:08/11"
type: lesson
ref: 08/11
phase: 8
num: 11
title: Audio Generation
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 5
aliases:
  - 08/11
  - 08-11
tags:
  - phase/08
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/11-audio-generation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/11-audio-generation"
---

# 08/11 Audio Generation

> Audio is a 1-D signal at 16-48 kHz. A five-second clip is 80-240k samples. No transformer attends to that sequence directly. The solution for every production audio model in 2026 is the same: a neural codec (Encodec, SoundStream, DAC) compresses audio to discrete tokens at 50-75 Hz, and a transformer or diffusion model generates tokens.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/11-audio-generation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/11-audio-generation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/11-audio-generation) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Audio Features), Phase 6 · 04 (ASR), Phase 8 · 06 (DDPM)`

- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Audio Features
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]] — ASR
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]] — DDPM

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- Codec `lesson term` — Encoder / decoder for audio; typical output is 50-75 Hz tokens.
- [[Concepts/RVQ|RVQ]] `lesson term` — Cascade of K quantizers; each models the residual of the previous.
- [[Concepts/Token|Token]] `glossary` — Discrete index into a codebook; 1024 or 2048 typical.
- Delayed parallel `lesson term` — Emit K token streams with staggered offsets to reduce sequence length.
- [[Concepts/Flow matching|Flow matching]] `lesson term` — Straighter-path alternative to diffusion; faster sampling.
- Voice prompt `lesson term` — Speaker embedding or token prefix that steers the cloned voice.
- [[Concepts/Mel spectrogram|Mel spectrogram]] `lesson term` — Log-magnitude perceptual spectrogram; used by many TTS systems.
- [[Concepts/Vocoder|Vocoder]] `lesson term` — Neural component that converts mel spectrograms back to audio.

## Ships

- [[Artifacts/08-11 audio-brief|audio-brief]] `skill` — Translate an audio brief into a model + prompt + eval plan across TTS, music, and SFX.

## Further reading

- [[Resources/SoundStream|SoundStream]] ([link](https://arxiv.org/abs/2107.03312)) — the first widely used neural audio codec. ·  also cited by 1 other lesson
- [[Resources/Défossez et al. (2023). EnCodec|Défossez et al. (2023). EnCodec]] ([link](https://arxiv.org/abs/2210.13438)) — the codec standard. ·  also cited by 2 other lessons
- [[Resources/Baevski et al. - Microsoft (2023). VALL-E|Baevski et al. / Microsoft (2023). VALL-E]] ([link](https://arxiv.org/abs/2301.02111)) — VALL-E. ·  also cited by 1 other lesson
- [[Resources/Copet et al. (2023). MusicGen|Copet et al. (2023). MusicGen]] ([link](https://arxiv.org/abs/2306.05284)) — MusicGen. ·  also cited by 1 other lesson
- [[Resources/Kumar et al. (2023). Descript Audio Codec (DAC)|Kumar et al. (2023). Descript Audio Codec (DAC)]] ([link](https://arxiv.org/abs/2306.06546)) — DAC. ·  also cited by 1 other lesson
- [[Resources/AudioLDM2|AudioLDM2]] ([link](https://arxiv.org/abs/2308.05734)) — AudioLDM 2. ·  also cited by 1 other lesson
- Stability AI (2024). Stable Audio 2.5 ([link](https://stability.ai/news/introducing-stable-audio-2-5)) — 2025 text-to-music with flow matching.


%% ── my notes ── %%
