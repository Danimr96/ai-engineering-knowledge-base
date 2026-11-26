---
id: "lesson:06/07"
type: lesson
ref: 06/07
phase: 6
num: 7
title: "Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 9
aliases:
  - 06/07
  - 06-07
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/07-text-to-speech/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/07-text-to-speech"
---

# 06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro

> ASR inverts speech to text; TTS inverts text to speech. The 2026 stack is three parts: text → tokens, tokens → mel, mel → waveform. Each part has a default model that fits in a laptop.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/07-text-to-speech/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/07-text-to-speech) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/07-text-to-speech) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms & Mel), Phase 5 · 09 (Seq2Seq), Phase 7 · 05 (Full Transformer)`

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]] — Seq2Seq
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms & Mel
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/06-08 Voice Cloning & Voice Conversion|06/08 Voice Cloning & Voice Conversion]]
- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]]
- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/06-17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards|06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards]]

## Concepts taught

- Phoneme `lesson term` — Abstract sound class; 39 in English (ARPABet).
- Duration predictor `lesson term` — Non-AR model output; integer frames per phoneme.
- [[Concepts/Vocoder|Vocoder]] `lesson term` — Neural net mapping mel-spec to raw samples.
- HiFi-GAN `lesson term` — GAN-based; dominant 2020–2024.
- [[Concepts/MOS|MOS]] `lesson term` — 1–5 mean opinion score from human raters.
- [[Concepts/SECS|SECS]] `lesson term` — Cosine similarity between target and output speaker embedding.
- F5-TTS `lesson term` — Flow-matching diffusion; zero-shot cloning.
- Kokoro `lesson term` — 82M-param model, Apache 2.0.

## Ships

- [[Artifacts/06-07 tts-designer|tts-designer]] `skill` — Pick TTS model, voice, text-normalization scope, and evaluation plan for a given language, style, and latency target.

## Further reading

- Shen et al. (2017). Tacotron 2 ([link](https://arxiv.org/abs/1712.05884)) — the seq2seq baseline.
- Kong, Kim, Bae (2020). HiFi-GAN ([link](https://arxiv.org/abs/2010.05646)) — the vocoder that still ships in 2026.
- Kim, Kong, Son (2021). VITS ([link](https://arxiv.org/abs/2106.06103)) — end-to-end flow-based.
- [[Resources/Chen et al. (2024). F5-TTS|Chen et al. (2024). F5-TTS]] ([link](https://arxiv.org/abs/2410.06885)) — current open-source SOTA. ·  also cited by 1 other lesson
- Kokoro-82M on HuggingFace ([link](https://huggingface.co/hexgrad/Kokoro-82M)) — 2024 CPU-friendly English TTS.


%% ── my notes ── %%
