---
id: "lesson:06/04"
type: lesson
ref: 06/04
phase: 6
num: 4
title: "Speech Recognition (ASR) — CTC, RNN-T, Attention"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 9
aliases:
  - 06/04
  - 06-04
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/04-speech-recognition-asr/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/04-speech-recognition-asr"
---

# 06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention

> Speech recognition is audio classification at every timestep, glued together by a sequence model that knows English and silence. CTC, RNN-T, and attention are the three ways to do it. Pick one and understand why.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/04-speech-recognition-asr/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/04-speech-recognition-asr) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/04-speech-recognition-asr) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms & Mel), Phase 5 · 08 (CNNs & RNNs for Text), Phase 5 · 10 (Attention)`

- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]] — CNNs & RNNs for Text
- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]] — Attention
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms & Mel

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]

## Builds on this

- [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]]
- [[Lessons/06-10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio|06/10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio]]
- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]]
- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/06-17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards|06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards]]
- [[Lessons/08-11 Audio Generation|08/11 Audio Generation]]

## Concepts taught

- [[Concepts/CTC|CTC]] `lesson term` — Marginal over all frame-to-token alignments; non-AR.
- RNN-T `lesson term` — CTC + next-token predictor; handles word-order.
- Attention enc-dec `lesson term` — Encoder + cross-attending decoder; best offline quality.
- [[Concepts/WER|WER]] `lesson term` — (S+D+I)/N at word level.
- Blank `lesson term` — Special token in CTC signalling "no emission this frame".
- LM fusion `lesson term` — Add weighted LM log-probs during beam search.
- [[Concepts/VAD|VAD]] `lesson term` — Voice activity detector; trims non-speech.
- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]] `glossary` — The task and system pipeline that maps a speech signal to a transcription, often with optional token or segment timing and confidence information.

## Ships

- [[Artifacts/06-04 asr-picker|asr-picker]] `skill` — Pick ASR model, decoding strategy, chunking, and LM fusion for a given deployment target.

## Further reading

- Graves (2012). Sequence Transduction with RNNs ([link](https://arxiv.org/abs/1211.3711)) — the RNN-T paper.
- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) — the 2022 canonical paper; v3-turbo extension in 2024. ·  also cited by 5 other lessons
- [[Resources/Connectionist Temporal Classification|Connectionist Temporal Classification]] ([link](https://www.cs.toronto.edu/~graves/icml_2006.pdf)) — the CTC paper. ·  also cited by 1 other lesson
- NVIDIA NeMo — Parakeet-TDT card ([link](https://huggingface.co/nvidia/parakeet-tdt-1.1b)) — 2026 Open ASR Leaderboard leader.
- [[Resources/Hugging Face — Open ASR Leaderboard|Hugging Face — Open ASR Leaderboard]] ([link](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)) — live benchmark across 25+ models. ·  also cited by 1 other lesson


%% ── my notes ── %%
