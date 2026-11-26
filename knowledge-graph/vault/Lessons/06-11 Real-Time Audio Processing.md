---
id: "lesson:06/11"
type: lesson
ref: 06/11
phase: 6
num: 11
title: Real-Time Audio Processing
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 7
prereqs: 3
community: 9
aliases:
  - 06/11
  - 06-11
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/11-real-time-audio-processing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/11-real-time-audio-processing"
---

# 06/11 Real-Time Audio Processing

> Batch pipelines process a file. Real-time pipelines process the next 20 milliseconds before the next 20 arrive. Every conversational AI, broadcast studio, and telephony bot lives and dies by this latency budget.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/11-real-time-audio-processing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/11-real-time-audio-processing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/11-real-time-audio-processing) · code: main.py, main.rs  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms), Phase 6 · 04 (ASR), Phase 6 · 07 (TTS)`

- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]] — ASR
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]] — TTS

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]

## Builds on this

- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/06-14 Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick|06/14 Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick]]
- [[Lessons/06-15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue|06/15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue]]

## Concepts taught

- Ring buffer `lesson term` — Fixed-size, lock-free (or SPSC-locked) FIFO for audio frames.
- [[Concepts/VAD|VAD]] `lesson term` — Model or heuristic marking speech vs non-speech.
- Streaming ASR `lesson term` — Emits partial text as audio arrives; bounded lookahead.
- [[Concepts/Jitter buffer|Jitter buffer]] `lesson term` — Queue reordering out-of-order packets; 60–80 ms typical.
- AEC `lesson term` — Subtracts speaker-to-mic feedback path.
- [[Concepts/Barge-in|Barge-in]] `lesson term` — System detects user speech mid-TTS; must cancel playback.
- [[Concepts/Full duplex|Full duplex]] `lesson term` — User and bot can talk at the same time; Moshi is full duplex.

## Ships

- [[Artifacts/06-11 realtime-voice-pipeline|realtime-voice-pipeline]] `skill` — Pick transport, VAD, streaming STT, LLM, streaming TTS, and orchestration for a target end-to-end latency.

## Further reading

- Macháček et al. (2023). Whisper-Streaming ([link](https://arxiv.org/abs/2307.14743)) — chunked near-streaming Whisper.
- [[Resources/LiveKit Agents framework (2024)|LiveKit Agents framework (2024)]] ([link](https://docs.livekit.io/agents/)) — production audio agent orchestration. ·  also cited by 2 other lessons
- [[Resources/Silero VAD repo|Silero VAD repo]] ([link](https://github.com/snakers4/silero-vad)) — sub-1 ms VAD, Apache 2.0. ·  also cited by 2 other lessons
- Kyutai (2024). Moshi ([link](https://kyutai.org/Moshi.pdf)) — full-duplex 200 ms latency.
- WebRTC AEC3 paper ([link](https://webrtc.googlesource.com/src/+/main/modules/audio_processing/aec3/)) — echo cancellation under open source.


%% ── my notes ── %%
