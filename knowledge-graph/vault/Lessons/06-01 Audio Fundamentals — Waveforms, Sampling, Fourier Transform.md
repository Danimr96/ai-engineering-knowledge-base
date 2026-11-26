---
id: "lesson:06/01"
type: lesson
ref: 06/01
phase: 6
num: 1
title: "Audio Fundamentals — Waveforms, Sampling, Fourier Transform"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 9
aliases:
  - 06/01
  - 06-01
tags:
  - phase/06
  - type/learn
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/01-audio-fundamentals/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/01-audio-fundamentals"
---

# 06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform

> Waveforms are the raw signal. Spectrograms are the representation. Mel features are the ML-friendly form. Every modern ASR and TTS pipeline walks this ladder, and the first rung is understanding sampling and Fourier.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/01-audio-fundamentals/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/01-audio-fundamentals) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/01-audio-fundamentals) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1 · 06 (Vectors & Matrices), Phase 1 · 14 (Probability Distributions)`

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Vectors & Matrices
- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Probability Distributions

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]]

## Concepts taught

- Sample rate `lesson term` — Frequency in Hz at which the ADC measures the signal.
- Nyquist `lesson term` — sr/2; energy above it aliases back down.
- Bit depth `lesson term` — int16 = 65,536 levels; float32 = 24-bit precision in [-1, 1].
- [[Concepts/DFT|DFT]] `lesson term` — N samples → N complex frequency coefficients.
- FFT `lesson term` — O(N log N) algorithm requiring N = power of 2.
- Bin `lesson term` — k · sr / N Hz; resolution = sr / N.
- [[Concepts/STFT|STFT]] `lesson term` — Framed + windowed FFT over time.
- [[Concepts/Aliasing|Aliasing]] `lesson term` — Energy above Nyquist mirroring down to lower bins.

## Ships

- [[Artifacts/06-01 audio-loader|audio-loader]] `skill` — Validate a raw audio file against a target model's expectations and resample it safely.

## Further reading

- Steve Eddins — FFT Interpretation notebook ([link](https://blogs.mathworks.com/steve/2020/03/30/fft-spectrum-and-spectral-densities/)) — frequency bin intuition cleared up in 10 minutes.
- Smith — The Scientist and Engineer's Guide to Digital Signal Processing ([link](https://www.dspguide.com/ch8.htm)) — free, canonical DSP textbook.
- librosa docs — audio primer ([link](https://librosa.org/doc/latest/tutorial.html)) — practical walkthrough with code.
- [[Resources/Shannon 1948- A Mathematical Theory of Communication|Shannon 1948: A Mathematical Theory of Communication]] ([link](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)) — the paper behind the sampling theorem. ·  also cited by 1 other lesson
- Heinrich Kuttruff — Room Acoustics (6th ed.) ([link](https://www.routledge.com/Room-Acoustics/Kuttruff/p/book/9781482260434)) — reference for why real-world audio is not a clean sinusoid.


%% ── my notes ── %%
