---
id: "lesson:06/02"
type: lesson
ref: 06/02
phase: 6
num: 2
title: "Spectrograms, Mel Scale & Audio Features"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 9
aliases:
  - 06/02
  - 06-02
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/02-spectrograms-mel-features/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/02-spectrograms-mel-features"
---

# 06/02 Spectrograms, Mel Scale & Audio Features

> Neural nets do not consume raw waveforms well. They consume spectrograms. They consume mel spectrograms even better. Every ASR, TTS, and audio classifier in 2026 lives or dies by this single preprocessing choice.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/02-spectrograms-mel-features/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/02-spectrograms-mel-features) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/02-spectrograms-mel-features) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 01 (Audio Fundamentals)`

- [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]] — Audio Fundamentals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/06-03 Audio Classification — From k-NN on MFCCs to AST and BEATs|06/03 Audio Classification — From k-NN on MFCCs to AST and BEATs]]
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]
- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]]
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- [[Lessons/06-09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake|06/09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake]]
- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]]
- [[Lessons/06-13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split|06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split]]
- [[Lessons/08-11 Audio Generation|08/11 Audio Generation]]

## Concepts taught

- [[Concepts/Frame|Frame]] `lesson term` — 25 ms chunk of waveform fed to one FFT.
- Hop `lesson term` — Samples between consecutive frames; 10 ms is ASR default.
- Window `lesson term` — Point-wise multiplier that tapers the frame edges to zero.
- [[Concepts/STFT|STFT]] `lesson term` — Framed + windowed FFT; yields time × frequency matrix.
- Mel `lesson term` — Log-perception scale; m = 2595·log10(1 + f/700).
- Filterbank `lesson term` — Triangular filters that project STFT onto mel bins.
- [[Concepts/Log-mel|Log-mel]] `lesson term` — log(mel_spec + eps); standardized in 2026.
- MFCC `lesson term` — DCT of log-mel; 13 coeffs, decorrelated.

## Ships

- [[Artifacts/06-02 feature-extractor|feature-extractor]] `skill` — Pick feature type, mel count, frame/hop, and normalization to match a downstream audio model.

## Further reading

- NVIDIA NeMo — audio preprocessing ([link](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/asr_all.html#featurizers)) — production-scale pipeline for Parakeet + Canary models.
- OpenAI — Whisper source, log_mel_spectrogram ([link](https://github.com/openai/whisper/blob/main/whisper/audio.py)) — read the reference implementation.
- Davis, Mermelstein (1980). Comparison of parametric representations for monosyllabic word recognition ([link](https://ieeexplore.ieee.org/document/1163420)) — the MFCC paper.
- librosa feature extraction docs ([link](https://librosa.org/doc/main/feature.html)) — reference for `mfcc`, `melspectrogram`, and hop/window.
- Stevens, Volkmann, Newman (1937). A Scale for the Measurement of the Psychological Magnitude Pitch ([link](https://pubs.aip.org/asa/jasa/article-abstract/8/3/185/735757/)) — the original mel scale.


%% ── my notes ── %%
