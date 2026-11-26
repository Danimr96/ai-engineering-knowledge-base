---
id: "lesson:06/15"
type: lesson
ref: 06/15
phase: 6
num: 15
title: "Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 3
community: 9
aliases:
  - 06/15
  - 06-15
tags:
  - phase/06
  - type/learn
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki"
---

# 06/15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue

> 2024-2026 redefined voice AI. Moshi ships a single model that listens and speaks simultaneously at 200 ms latency. Hibiki does speech-to-speech translation chunk-by-chunk. Both abandon the ASR → LLM → TTS pipeline for a unified full-duplex architecture over Mimi codec tokens. This is the new reference design.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 13 (Neural Audio Codecs), Phase 6 · 11 (Real-Time Audio), Phase 7 · 05 (Full Transformer)`

- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]] — Real-Time Audio
- [[Lessons/06-13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split|06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split]] — Neural Audio Codecs
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]], [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- depth 3: [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]

## Concepts taught

- [[Concepts/Full duplex|Full duplex]] (as *Full-duplex*) `lesson term` — Two audio streams active simultaneously on the same model.
- [[Concepts/Inner monologue|Inner monologue]] `lesson term` — Moshi emits text tokens alongside its audio output.
- Depth transformer `lesson term` — Small transformer that predicts 8 codebooks within one 80 ms frame.
- [[Concepts/Mimi|Mimi]] `lesson term` — 12.5 Hz × 8 codebooks; semantic+acoustic; powers Moshi.
- Streaming S2S `lesson term` — Chunk-by-chunk translation/dialogue, no pipeline stages.
- Back-channeling `lesson term` — Moshi can emit small acknowledgments without breaking its turn.

## Ships

- [[Artifacts/06-15 duplex-pipeline|duplex-pipeline]] `skill` — Pick full-duplex (Moshi) vs pipeline (VAD + STT + LLM + TTS) architecture for a voice-agent workload.

## Further reading

- [[Resources/Défossez et al. (2024). Moshi — speech-text foundation model|Défossez et al. (2024). Moshi — speech-text foundation model]] ([link](https://arxiv.org/html/2410.00037v2)) — the paper. ·  also cited by 1 other lesson
- Kyutai Labs (2026). Hibiki-Zero ([link](https://arxiv.org/abs/2602.12345)) — streaming translation without aligned data.
- Kyutai — Delayed Streams Modeling ([link](https://github.com/kyutai-labs/delayed-streams-modeling)) — the STT/TTS framework under the hood.
- [[Resources/Kyutai Moshi|Kyutai Moshi]] ([link](https://github.com/kyutai-labs/moshi)) — install + server. ·  also cited by 1 other lesson
- [[Resources/OpenAI Realtime API|OpenAI Realtime API]] ([link](https://platform.openai.com/docs/guides/realtime)) — closed commercial peer. ·  also cited by 2 other lessons
- Sesame (2025). Crossing the uncanny valley of voice ([link](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice)) — CSM spec.


%% ── my notes ── %%
