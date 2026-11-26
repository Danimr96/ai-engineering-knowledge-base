---
id: "lesson:06/03"
type: lesson
ref: 06/03
phase: 6
num: 3
title: "Audio Classification — From k-NN on MFCCs to AST and BEATs"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 3
aliases:
  - 06/03
  - 06-03
tags:
  - phase/06
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/03-audio-classification/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/03-audio-classification"
---

# 06/03 Audio Classification — From k-NN on MFCCs to AST and BEATs

> Everything from "dog barking vs siren" to "which language is this" is audio classification. The features are mels. The architecture moves each decade. The evaluation stays AUC, F1, and per-class recall.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/03-audio-classification/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/03-audio-classification) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/03-audio-classification) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms & Mel), Phase 3 · 06 (CNNs), Phase 5 · 08 (CNNs & RNNs for Text)`

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — CNNs
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]] — CNNs & RNNs for Text
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms & Mel

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]

## Concepts taught

- AudioSet `lesson term` — Google's 2M-clip, 632-class weakly-labeled YouTube dataset.
- ESC-50 `lesson term` — 50 classes × 40 clips of environmental sounds.
- AST `lesson term` — ViT on log-mel patches; 2021 SOTA.
- [[Concepts/BEATs|BEATs]] `lesson term` — Microsoft model, iter3 leads AudioSet as of 2026.
- Mixup `lesson term` — x = λ·x1 + (1-λ)·x2; y = λ·y1 + (1-λ)·y2.
- SpecAugment `lesson term` — Zero-out random time and frequency bands of the spectrogram.
- [[Concepts/MAP|MAP]] `lesson term` — Mean average precision across classes and thresholds.

## Ships

- [[Artifacts/06-03 classifier-designer|classifier-designer]] `skill` — Pick architecture, augmentation, class-balance strategy, and eval metric for an audio classification task.

## Further reading

- Park et al. (2019). SpecAugment ([link](https://arxiv.org/abs/1904.08779)) — the dominant audio augmentation.
- Gong, Chung, Glass (2021). AST: Audio Spectrogram Transformer ([link](https://arxiv.org/abs/2104.01778)) — the architecture of record from 2021–2024.
- Chen et al. (2022, rev. 2024). BEATs: Audio Pre-Training with Acoustic Tokenizers ([link](https://arxiv.org/abs/2212.09058)) — the 2024+ default.
- Piczak (2015). ESC-50 dataset ([link](https://github.com/karolpiczak/ESC-50)) — 50-class benchmark that lives on.
- Gemmeke et al. (2017). AudioSet ([link](https://research.google.com/audioset/)) — 632-class YouTube taxonomy; still the gold standard.


%% ── my notes ── %%
