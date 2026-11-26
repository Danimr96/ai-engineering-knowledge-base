---
id: "lesson:07/10"
type: lesson
ref: 07/10
phase: 7
num: 10
title: "Audio Transformers — Whisper Architecture"
lesson_type: learn
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
  - 07/10
  - 07-10
tags:
  - phase/07
  - type/learn
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/10-audio-transformers-whisper/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/10-audio-transformers-whisper"
---

# 07/10 Audio Transformers — Whisper Architecture

> Audio is an image of frequency over time. Whisper is a ViT that eats mel spectrograms and speaks back.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/10-audio-transformers-whisper/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/10-audio-transformers-whisper) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/10-audio-transformers-whisper) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 05 (Full Transformer), Phase 7 · 08 (Encoder-Decoder), Phase 7 · 09 (ViT)`

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]] — Encoder-Decoder
- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]] — ViT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/06-10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio|06/10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- [[Concepts/Mel spectrogram|Mel spectrogram]] `lesson term` — 2D representation: frequency bins on one axis, time frames on the other; log-scaled energy per cell.
- [[Concepts/Log-mel|Log-mel]] `lesson term` — Mel spectrogram passed through log; approximates human perception of loudness.
- [[Concepts/Frame|Frame]] `lesson term` — A 25 ms window of samples; overlapping at 10 ms stride.
- Task token `lesson term` — Special tokens like <|transcribe|> / <|translate|> in the decoder prompt.
- Voice activity detection (as *Voice activity detection (VAD)*) `lesson term` — Gate that removes silence before ASR; cuts cost massively.
- [[Concepts/CTC|CTC]] `lesson term` — Classic ASR loss for alignment-free training; Whisper does NOT use it.
- Whisper-turbo `lesson term` — large-v3 encoder + 4-layer decoder; 8× faster decoding.
- Faster-whisper `lesson term` — CTranslate2 reimplementation; int8 quantization; 4× faster than OpenAI's reference.

## Ships

- [[Artifacts/07-10 asr-configurator|asr-configurator]] `skill` — Pick an ASR model (Whisper variant / Moonshine / faster-whisper) and decoding parameters for a new speech pipeline.

## Further reading

- Baevski et al. (2020). wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations ([link](https://arxiv.org/abs/2006.11477)) — precursor; still SOTA features in some settings.
- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) — Whisper paper. ·  also cited by 5 other lessons
- Jia et al. (2024). Moonshine: Speech Recognition for Live Transcription and Voice Commands ([link](https://arxiv.org/abs/2410.15608)) — 2024 edge-friendly ASR, Whisper-shaped but smaller.
- [[Resources/Systran — faster-whisper repo|Systran — faster-whisper repo]] ([link](https://github.com/SYSTRAN/faster-whisper)) — production wrapper, 4× faster than reference. ·  also cited by 1 other lesson
- HuggingFace `modeling_whisper.py` ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/whisper/modeling_whisper.py)) — full implementation (encoder, decoder, cross-attention, generation) that mirrors the lesson's architecture diagram.
- OpenAI Whisper repo ([link](https://github.com/openai/whisper)) — reference code + model weights. Read `whisper/model.py` to see the Conv1D stem + encoder + decoder top-to-bottom in ~400 lines.
- OpenAI Whisper — `whisper/decoding.py` ([link](https://github.com/openai/whisper/blob/main/whisper/decoding.py)) — the beam-search + task-token logic described in Steps 5–6 is here; 500 lines, fully readable.
- [[Resources/HuggingFace — Whisper fine-tune tutorial|HuggingFace — Whisper fine-tune tutorial]] ([link](https://huggingface.co/blog/fine-tune-whisper)) — canonical fine-tuning recipe including mel spectrogram preprocessor and token-timestamp handling. ·  also cited by 1 other lesson


%% ── my notes ── %%
