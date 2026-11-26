---
id: "lesson:06/17"
type: lesson
ref: 06/17
phase: 6
num: 17
title: "Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 6
community: 58
aliases:
  - 06/17
  - 06-17
tags:
  - phase/06
  - type/learn
  - community/58
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/17-audio-evaluation-metrics/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/17-audio-evaluation-metrics"
---

# 06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards

> You cannot ship what you cannot measure. This lesson names the 2026 metrics for every audio task: ASR (WER, CER, RTFx), TTS (MOS, UTMOS, SECS, WER-on-ASR-round-trip), audio-language (MMAU, LongAudioBench), music (FAD, CLAP), and speaker (EER). Plus the leaderboards where you compare.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/17-audio-evaluation-metrics/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/17-audio-evaluation-metrics) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/17-audio-evaluation-metrics) · code: main.py  
**Community:** [[Communities/58 DER · EER · WER|58 DER · EER · WER]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 04, 06, 07, 09, 10; Phase 2 · 09 (Model Evaluation)`

- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]] — Model Evaluation
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]
- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]]
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- [[Lessons/06-09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake|06/09 Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake]]
- [[Lessons/06-10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio|06/10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]], [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]], [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]], [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Concepts taught

- [[Concepts/WER|WER]] `lesson term` — (S+D+I)/N at word level after normalization.
- CER `lesson term` — For tone languages or char-level systems.
- [[Concepts/MOS|MOS]] `lesson term` — 1-5 rating; 20+ listeners × 100 samples.
- UTMOS `lesson term` — Learned model; correlates ~0.9 with human MOS.
- [[Concepts/SECS|SECS]] `lesson term` — ECAPA cosine between reference and clone.
- [[Concepts/EER|EER]] `lesson term` — Threshold where FAR = FRR.
- [[Concepts/DER|DER]] `lesson term` — (FA + Miss + Confusion) / total.
- [[Concepts/FAD|FAD]] `lesson term` — Fréchet distance on VGGish embeddings.
- RTFx `lesson term` — Audio seconds per wall-clock second.

## Ships

- [[Artifacts/06-17 audio-evaluator|audio-evaluator]] `skill` — Pick metrics, benchmarks, normalization rules, and reporting format for any audio model release.

## Further reading

- Fréchet Audio Distance (Kilgour et al. 2019) ([link](https://arxiv.org/abs/1812.08466)) — the music-gen standard.
- UTMOS (Saeki et al. 2022) ([link](https://arxiv.org/abs/2204.02152)) — learned MOS predictor.
- jiwer ([link](https://github.com/jitsi/jiwer)) — WER/CER library with normalization utilities.
- HEAR benchmark ([link](https://hearbenchmark.com/)) — audio SSL benchmarks.
- TTS Arena ([link](https://huggingface.co/spaces/TTS-AGI/TTS-Arena)) — human-vote TTS leaderboard.
- [[Resources/Hugging Face — Open ASR Leaderboard|Hugging Face — Open ASR Leaderboard]] ([link](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)) — 2026 live rankings. ·  also cited by 1 other lesson
- [[Resources/MMAU-Pro leaderboard|MMAU-Pro leaderboard]] ([link](https://mmaubenchmark.github.io/)) — LALM reasoning leaderboard. ·  also cited by 1 other lesson


%% ── my notes ── %%
