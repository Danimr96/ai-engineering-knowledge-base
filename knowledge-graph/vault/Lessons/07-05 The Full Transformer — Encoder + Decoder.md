---
id: "lesson:07/05"
type: lesson
ref: 07/05
phase: 7
num: 5
title: "The Full Transformer — Encoder + Decoder"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 9
prereqs: 3
community: 5
aliases:
  - 07/05
  - 07-05
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/05-full-transformer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/05-full-transformer"
---

# 07/05 The Full Transformer — Encoder + Decoder

> Attention is the star. Everything else — residuals, normalization, feed-forward, cross-attention — is the scaffolding that lets you stack it deep.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/05-full-transformer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/05-full-transformer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/05-full-transformer) · code: main.jl, main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention), Phase 7 · 03 (Multi-Head Attention), Phase 7 · 04 (Positional Encoding)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention
- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]] — Multi-Head Attention
- [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]] — Positional Encoding

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]]
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- [[Lessons/06-15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue|06/15 Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue]]
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]]
- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]]
- [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]]
- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]
- [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- Block `lesson term` — Stack of norm + attention + norm + FFN, wrapped in residual connections.
- Residual `lesson term` — x + f(x) output; enables gradient flow through deep stacks.
- Pre-norm `lesson term` — Modern: x + sublayer(LN(x)). Trains deeper without warmup gymnastics.
- [[Concepts/RMSNorm|RMSNorm]] `lesson term` — Divide by RMS; one less op, same empirical stability.
- [[Concepts/SwiGLU|SwiGLU]] `lesson term` — Swish(W1 x) ⊙ W3 x → W2. Beats ReLU/GELU on LM ppl.
- [[Concepts/Cross-Attention|Cross-Attention]] `glossary` — MHA with Q from decoder, K/V from encoder outputs.
- [[Concepts/FFN expansion|FFN expansion]] `lesson term` — Ratio of hidden-size to d_model, usually 4 (LayerNorm) or 2.6 (SwiGLU).
- Bias-free `lesson term` — Modern stacks omit biases in linear layers; slight ppl improvement, smaller model.
- [[Concepts/Transformer|Transformer]] `glossary` — A neural-network architecture built from attention, position information, feed-forward sublayers, residual connections, and normalization. Encoder, decoder, and encoder-decoder variants use different masks and information flows.

## Ships

- [[Artifacts/07-05 transformer-block-reviewer|transformer-block-reviewer]] `skill` — Review a transformer block implementation against 2026 defaults and flag drift.

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — original block spec. ·  also cited by 8 other lessons
- Zhang, Sennrich (2019). Root Mean Square Layer Normalization ([link](https://arxiv.org/abs/1910.07467)) — RMSNorm.
- Xiong et al. (2020). On Layer Normalization in the Transformer Architecture ([link](https://arxiv.org/abs/2002.04745)) — why pre-norm beats post-norm deeply.
- [[Resources/Shazeer (2020). GLU Variants Improve Transformer|Shazeer (2020). GLU Variants Improve Transformer]] ([link](https://arxiv.org/abs/2002.05202)) — the SwiGLU paper. ·  also cited by 1 other lesson
- [[Resources/HuggingFace `modeling_llama.py`|HuggingFace `modeling_llama.py`]] ([link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py)) — canonical 2026 decoder-only block. ·  also cited by 1 other lesson


%% ── my notes ── %%
