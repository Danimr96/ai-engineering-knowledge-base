---
id: "lesson:01/20"
type: lesson
ref: 01/20
phase: 1
num: 20
title: The Fourier Transform
lesson_type: build
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 16
prereqs: 5
community: 8
aliases:
  - 01/20
  - 01-20
tags:
  - phase/01
  - type/build
  - community/08
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/20-fourier-transform/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/20-fourier-transform"
---

# 01/20 The Fourier Transform

> Every signal is a sum of sine waves. The Fourier transform tells you which ones.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/20-fourier-transform/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/20-fourier-transform) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/20-fourier-transform) · code: fourier.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-04, 19 (complex numbers)`

- [[Lessons/01-19 Complex Numbers for AI|01/19 Complex Numbers for AI]] — complex numbers
- **01/01-04**:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]
    - [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]
    - [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- DFT (Discrete Fourier Transform) `lesson term` — Converts N time-domain samples into N frequency-domain coefficients. Each coefficient is the correlation with a complex sinusoid at that frequency
- FFT (Fast Fourier Transform) `lesson term` — An O(N log N) algorithm to compute the DFT. The Cooley-Tukey algorithm splits even/odd indices recursively
- Inverse DFT `lesson term` — Reconstructs the time-domain signal from frequency coefficients. Same formula as DFT with flipped exponent sign and 1/N scaling
- Frequency bin `lesson term` — Each index k in the DFT output represents frequency kfs/N Hz. The "bin" is the discrete frequency slot
- DC component `lesson term` — X[0], the zero-frequency coefficient. Proportional to the signal mean
- Nyquist frequency `lesson term` — fs/2, the maximum frequency representable at sampling rate fs. Frequencies above this alias
- Power spectrum `lesson term` — |X[k]|^2, the squared magnitude of each frequency coefficient. Shows energy distribution across frequencies
- Phase spectrum `lesson term` — angle(X[k]), the phase offset of each frequency component. Often ignored in analysis
- Spectral leakage `lesson term` — Spurious frequency content caused by treating a non-periodic signal as periodic. Reduced by windowing
- Window function `lesson term` — A tapering function (Hann, Hamming, Blackman) applied before DFT to reduce spectral leakage
- Twiddle factor `lesson term` — The complex exponential e^(-2piik/N) used to combine sub-DFTs in the FFT butterfly computation
- Convolution theorem `lesson term` — Convolution in time domain equals pointwise multiplication in frequency domain. Fundamental to signal processing and CNNs
- Circular convolution `lesson term` — Convolution where the signal wraps around. This is what the DFT naturally computes
- Linear convolution `lesson term` — Standard convolution without wraparound. Achieved by zero-padding before DFT
- Parseval's theorem `lesson term` — Total energy is preserved through the Fourier transform. sum |x[n]|^2 = (1/N) sum |X[k]|^2
- [[Concepts/Aliasing|Aliasing]] `lesson term` — When frequencies above Nyquist appear as lower frequencies due to insufficient sampling rate

## Ships

- [[Artifacts/01-20 prompt-spectral-analyzer|prompt-spectral-analyzer]] `prompt` — Guides analysis of frequency content in signals using Fourier transform techniques

## Further reading

- Cooley & Tukey: An Algorithm for the Machine Calculation of Complex Fourier Series (1965) ([link](https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/)) — the original FFT paper that changed computing
- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — sinusoidal positional encodings derived from Fourier frequency decomposition ·  also cited by 8 other lessons
- Lee-Thorp et al.: FNet: Mixing Tokens with Fourier Transforms (2021) ([link](https://arxiv.org/abs/2105.03824)) — replaces self-attention with FFT in transformers
- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) — speech recognition using mel-spectrograms as input representation ·  also cited by 5 other lessons
- Smith: The Scientist and Engineer's Guide to Digital Signal Processing ([link](http://www.dspguide.com/)) — free online textbook covering FFT, windowing, and spectral analysis in depth
- 3Blue1Brown: But what is the Fourier Transform? ([link](https://www.youtube.com/watch?v=spUNpyF58BY)) — the best visual introduction to Fourier transforms


%% ── my notes ── %%
