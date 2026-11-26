---
id: "lesson:06/09"
type: lesson
ref: 06/09
phase: 6
num: 9
title: "Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 2
aliases:
  - 06/09
  - 06-09
tags:
  - phase/06
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/09-music-generation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/09-music-generation"
---

# 06/09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake

> 2026 music generation: Suno v5 and Udio v4 dominate commercial; MusicGen, Stable Audio Open, and ACE-Step lead open-source. The technical problem is mostly solved. The legal problem (Warner Music $500M settlement, UMG settlement) reshaped the field in 2025-2026.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/09-music-generation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/09-music-generation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/09-music-generation) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms), Phase 4 · 10 (Diffusion Models)`

- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]] — Diffusion Models
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-04 Image Classification|04/04 Image Classification]]

## Builds on this

- [[Lessons/06-17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards|06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards]]

## Concepts taught

- [[Concepts/FAD|FAD]] `lesson term` — Fréchet distance between embedding distributions of real vs generated.
- Chromagram `lesson term` — 12-dim per-frame vector; input to melody conditioning.
- Stems `lesson term` — Separated bass / drums / vocals / melody as WAV.
- [[Concepts/Inpainting|Inpainting]] `lesson term` — Mask a time window; model regenerates just that.
- CLAP `lesson term` — Contrastive audio-text embedding; eval text-audio alignment.
- [[Concepts/EnCodec|EnCodec]] `lesson term` — Meta's neural codec used by MusicGen; 32 kHz, 4 codebooks.

## Ships

- [[Artifacts/06-09 music-designer|music-designer]] `skill` — Pick a music-generation model, license strategy, length plan, and disclosure metadata for a deployment.

## Further reading

- [[Resources/Copet et al. (2023). MusicGen|Copet et al. (2023). MusicGen]] ([link](https://arxiv.org/abs/2306.05284)) — the open autoregressive benchmark. ·  also cited by 1 other lesson
- [[Resources/AudioLDM2|AudioLDM2]] ([link](https://arxiv.org/abs/2308.05734)) — latent diffusion for music + sound effects. ·  also cited by 1 other lesson
- Evans et al. (2024). Stable Audio Open ([link](https://arxiv.org/abs/2407.14358)) — the sound-design default.
- ACE-Step ([link](https://github.com/ace-step/ACE-Step)) — open 4B full-song generator, April 2026.
- WMG-Suno settlement coverage ([link](https://www.musicbusinessworldwide.com/suno-warner-music-settlement/)) — Nov 2025 precedent.
- Suno v5 platform docs ([link](https://suno.com)) — the commercial quality leader.


%% ── my notes ── %%
