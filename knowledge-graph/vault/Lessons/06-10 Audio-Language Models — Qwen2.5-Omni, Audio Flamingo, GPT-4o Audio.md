---
id: "lesson:06/10"
type: lesson
ref: 06/10
phase: 6
num: 10
title: "Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 3
community: 58
aliases:
  - 06/10
  - 06-10
tags:
  - phase/06
  - type/learn
  - community/58
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/10-audio-language-models/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/10-audio-language-models"
---

# 06/10 Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio

> 2026 audio-language models reason over speech + environmental sound + music. Qwen2.5-Omni-7B matches GPT-4o Audio on MMAU-Pro. Audio Flamingo Next beats Gemini 2.5 Pro on LongAudioBench. The gap between open and closed is essentially closed — except on multi-audio tasks, where everyone is near random.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/10-audio-language-models/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/10-audio-language-models) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/10-audio-language-models) · code: main.py  
**Community:** [[Communities/58 DER · EER · WER|58 DER · EER · WER]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 04 (ASR), Phase 12 · 03 (Vision-Language Models), Phase 7 · 10 (Audio Transformers)`

- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]] — ASR
- [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]] — Audio Transformers
- [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]] — Vision-Language Models

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]], [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]
- depth 3: [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]]

## Builds on this

- [[Lessons/06-17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards|06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards]]

## Concepts taught

- LALM `lesson term` — Audio encoder + projector + LLM decoder.
- [[Concepts/Projector|Projector]] `lesson term` — Small MLP mapping audio features into LLM embedding space.
- [[Concepts/MMAU|MMAU]] `lesson term` — 10k audio-QA pairs across speech, sound, music.
- MMAU-Pro `lesson term` — 1800 multi-audio / reasoning-heavy questions.
- LongAudioBench `lesson term` — Multi-minute clips with semantic queries.
- Voice-in / voice-out `lesson term` — Model ingests speech and emits speech without text detour.

## Ships

- [[Artifacts/06-10 alm-picker|alm-picker]] `skill` — Pick an audio-language model, benchmark subset, output modality (text vs speech), and guardrails for an audio-understanding task.

## Further reading

- [[Resources/Tang et al. (2023). SALMONN|Tang et al. (2023). SALMONN]] ([link](https://arxiv.org/abs/2310.13289)) — dual-encoder pioneer. ·  also cited by 1 other lesson
- Chu et al. (2024). Qwen2-Audio ([link](https://arxiv.org/abs/2407.10759)) — reference architecture.
- [[Resources/NVIDIA (2025). Audio Flamingo 3|NVIDIA (2025). Audio Flamingo 3]] ([link](https://arxiv.org/abs/2507.08128)) — the open long-audio leader. ·  also cited by 1 other lesson
- NVIDIA (2026). Audio Flamingo Next ([link](https://arxiv.org/abs/2604.10905)) — LongAudioBench SOTA.
- Alibaba (2025). Qwen2.5-Omni ([link](https://huggingface.co/Qwen/Qwen2.5-Omni-7B)) — speech-in-speech-out.
- [[Resources/MMAU-Pro leaderboard|MMAU-Pro leaderboard]] ([link](https://mmaubenchmark.github.io/)) — live 2026 rankings. ·  also cited by 1 other lesson


%% ── my notes ── %%
