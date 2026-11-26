---
id: "lesson:06/13"
type: lesson
ref: 06/13
phase: 6
num: 13
title: "Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 9
aliases:
  - 06/13
  - 06-13
tags:
  - phase/06
  - type/learn
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/13-neural-audio-codecs/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/13-neural-audio-codecs"
---

# 06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split

> 2026 audio generation is almost all tokens. EnCodec, SNAC, Mimi, and DAC turn continuous waveforms into discrete sequences that a transformer can predict. The semantic-vs-acoustic token split — first-codebook as semantic, rest as acoustic — is the most important architectural shift since the Transformer for audio.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/13-neural-audio-codecs/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/13-neural-audio-codecs) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/13-neural-audio-codecs) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms), Phase 10 · 11 (Quantization), Phase 5 · 19 (Subword Tokenization)`

- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]] — Subword Tokenization
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]] — Quantization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/06-15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue|06/15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue]]

## Concepts taught

- [[Concepts/RVQ|RVQ]] `lesson term` — Cascade of small codebooks; each quantizes the previous residual.
- Frame rate `lesson term` — How many token-frames per second. Lower = faster LM.
- Semantic codebook `lesson term` — Codebook distilled from SSL features; encodes content.
- Acoustic codebooks `lesson term` — Timbre, prosody, noise, fine detail.
- PESQ / ViSQOL `lesson term` — Objective metrics correlating with MOS.
- [[Concepts/EnCodec|EnCodec]] `lesson term` — The RVQ baseline; used by MusicGen.
- [[Concepts/Mimi|Mimi]] `lesson term` — 12.5 Hz frame rate; semantic-acoustic split; powers Moshi.
- [[Concepts/Audio Token|Audio Token]] `glossary` — A discrete identifier produced by an audio codec or tokenizer for a short segment or feature of an audio signal, sometimes across several codebooks.

## Ships

- [[Artifacts/06-13 codec-picker|codec-picker]] `skill` — Pick a neural audio codec (EnCodec / DAC / SNAC / Mimi) for a given generative or compression task.

## Further reading

- [[Resources/SoundStream|SoundStream]] ([link](https://arxiv.org/abs/2107.03312)) — the original streamable RVQ codec. ·  also cited by 1 other lesson
- Borsos et al. (2023). AudioLM ([link](https://arxiv.org/abs/2209.03143)) — the two-stage semantic/acoustic paradigm.
- [[Resources/Défossez et al. (2023). EnCodec|Défossez et al. (2023). EnCodec]] ([link](https://arxiv.org/abs/2210.13438)) — the RVQ baseline. ·  also cited by 2 other lessons
- [[Resources/Kumar et al. (2023). Descript Audio Codec (DAC)|Kumar et al. (2023). Descript Audio Codec (DAC)]] ([link](https://arxiv.org/abs/2306.06546)) — highest-fidelity open. ·  also cited by 1 other lesson
- Siuzdak (2024). SNAC ([link](https://arxiv.org/abs/2410.14411)) — multi-scale RVQ.
- Kyutai (2024). Mimi codec ([link](https://kyutai.org/codec-explainer)) — semantic-acoustic split, WavLM distillation.


%% ── my notes ── %%
