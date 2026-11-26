---
id: "lesson:06/12"
type: lesson
ref: 06/12
phase: 6
num: 12
title: "Build a Voice Assistant Pipeline — The Phase 6 Capstone"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 7
community: 9
aliases:
  - 06/12
  - 06-12
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/12-voice-assistant-pipeline/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/12-voice-assistant-pipeline"
---

# 06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone

> Everything from lessons 01-11, stitched together. Build a voice assistant that listens, reasons, and talks back. In 2026 that is a solved engineering problem, not a research problem — but the integration details decide whether it ships.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/12-voice-assistant-pipeline/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/12-voice-assistant-pipeline) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/12-voice-assistant-pipeline) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 04, 05, 06, 07, 11; Phase 11 · 09 (Function Calling); Phase 14 · 01 (Agent Loop)`

- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]
- [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]]
- [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]]
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]]
- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling
- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

## Builds on this

- [[Lessons/06-14 Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick|06/14 Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick]]

## Concepts taught

- Turn `lesson term` — One VAD-bounded user speech + one LLM-TTS response.
- [[Concepts/Barge-in|Barge-in]] `lesson term` — User speaks while assistant talks; assistant stops.
- Wake word `lesson term` — Short keyword detector; Porcupine, Snowboy, openWakeWord.
- End-pointing `lesson term` — VAD + min-silence decision that user has finished.
- [[Concepts/Pre-roll|Pre-roll]] `lesson term` — Keep 200-400 ms of audio before VAD fires to avoid first-word clip.
- [[Concepts/Tool call|Tool call]] `lesson term` — LLM emits JSON; runtime dispatches; result feeds back in-loop.

## Ships

- [[Artifacts/06-12 voice-assistant-architect|voice-assistant-architect]] `skill` — Produce a full-stack voice-assistant spec — components, latency budget, observability, compliance — for a given workload.

## Further reading

- Anthropic — tool use guide ([link](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)) — LLM function calling.
- [[Resources/LiveKit Agents framework (2024)|LiveKit Agents framework (2024)]] ([link](https://docs.livekit.io/agents/)) — production-grade reference. ·  also cited by 2 other lessons
- [[Resources/Kyutai Moshi|Kyutai Moshi]] ([link](https://github.com/kyutai-labs/moshi)) — full-duplex reference (Lesson 15). ·  also cited by 1 other lesson
- [[Resources/Pipecat — voice agent examples|Pipecat — voice agent examples]] ([link](https://github.com/pipecat-ai/pipecat)) — DIY-friendly framework. ·  also cited by 1 other lesson
- Porcupine wake-word ([link](https://picovoice.ai/products/porcupine/)) — wake-word gating.
- [[Resources/OpenAI Realtime API|OpenAI Realtime API]] ([link](https://platform.openai.com/docs/guides/realtime)) — the managed voice-native path. ·  also cited by 2 other lessons


%% ── my notes ── %%
