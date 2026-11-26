---
id: "lesson:07/08"
type: lesson
ref: 07/08
phase: 7
num: 8
title: "T5, BART — Encoder-Decoder Models"
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
  - 07/08
  - 07-08
tags:
  - phase/07
  - type/learn
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder"
---

# 07/08 T5, BART — Encoder-Decoder Models

> Encoders understand. Decoders generate. Put them back together and you get a model built for input → output tasks: translate, summarize, rewrite, transcribe.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/08-t5-bart-encoder-decoder/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 05 (Full Transformer), Phase 7 · 06 (BERT), Phase 7 · 07 (GPT)`

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]] — BERT
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — GPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- depth 3: [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- Encoder-decoder `lesson term` — Two stacks: bidirectional encoder for input, causal decoder with cross-attention for output.
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — Decoder's Q × encoder's K/V. The only place encoder information enters the decoder.
- Span corruption `lesson term` — Replace random spans with sentinel tokens; decoder outputs the spans.
- Denoising objective `lesson term` — Apply a noise function to the input, train the decoder to reconstruct the clean sequence.
- Sentinel token `lesson term` — Special tokens that tag corrupted spans in the source and re-tag them in the target.
- Flan `lesson term` — T5 fine-tuned on >1,800 tasks; made encoder-decoder competitive at instruction-following.
- [[Concepts/Beam search|Beam search]] `lesson term` — Keep top-k partial sequences at each step; standard for translation/summarization.
- [[Concepts/Teacher forcing|Teacher forcing]] `lesson term` — During training, feed the true previous output token to the decoder, not the sampled one.

## Ships

- [[Artifacts/07-08 seq2seq-picker|seq2seq-picker]] `skill` — Choose encoder-decoder vs decoder-only for a new sequence-to-sequence task.

## Further reading

- Raffel et al. (2019). Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer ([link](https://arxiv.org/abs/1910.10683)) — T5.
- [[Resources/Lewis et al. (2019). BART- Denoising Sequence-to-Sequence Pre-training|Lewis et al. (2019). BART: Denoising Sequence-to-Sequence Pre-training]] ([link](https://arxiv.org/abs/1910.13461)) — BART. ·  also cited by 1 other lesson
- Chung et al. (2022). Scaling Instruction-Finetuned Language Models ([link](https://arxiv.org/abs/2210.11416)) — Flan-T5.
- [[Resources/Radford et al.- Whisper (2022)|Radford et al.: Whisper (2022)]] ([link](https://arxiv.org/abs/2212.04356)) — Whisper, the canonical 2026 encoder-decoder. ·  also cited by 5 other lessons
- HuggingFace `modeling_t5.py` ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/t5/modeling_t5.py)) — reference implementation.


%% ── my notes ── %%
