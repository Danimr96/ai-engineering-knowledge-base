---
id: "lesson:07/03"
type: lesson
ref: 07/03
phase: 7
num: 3
title: Multi-Head Attention
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 8
prereqs: 1
community: 1
aliases:
  - 07/03
  - 07-03
tags:
  - phase/07
  - type/build
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/03-multi-head-attention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/03-multi-head-attention"
---

# 07/03 Multi-Head Attention

> One attention head learns one relation at a time. Eight heads learn eight. Heads are free. Take more of them.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/03-multi-head-attention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/03-multi-head-attention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/03-multi-head-attention) · code: main.py, main.rs  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention from Scratch)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention from Scratch

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- depth 3: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]
- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]]
- [[Lessons/08-19 Visual Autoregressive Modeling (VAR)- Next-Scale Prediction|08/19 Visual Autoregressive Modeling (VAR): Next-Scale Prediction]]

## Concepts taught

- [[Concepts/Head|Head]] `lesson term` — One Q/K/V projection of dimension d_head = d_model / n_heads with its own attention matrix.
- d_head `lesson term` — Per-head hidden width; almost always 64 or 128 in production.
- Split / combine `lesson term` — (N, d_model) ↔ (n_heads, N, d_head) reshape+transpose around attention.
- W_o `lesson term` — (d_model, d_model) matrix applied after concatenating heads; where heads mix.
- MQA `lesson term` — Multi-Query Attention: single shared K/V projection. Smallest KV cache, some quality loss.
- [[Concepts/GQA|GQA]] `lesson term` — Grouped-Query Attention with n_kv_heads < n_heads; repeats to match Q.
- [[Concepts/MLA|MLA]] `lesson term` — Multi-head Latent Attention: K,V compressed to low-rank latent, decompressed at attend time.
- Induction head `lesson term` — A pair of heads that detect previous occurrences and copy what followed them.

## Ships

- [[Artifacts/07-03 mha-configurator|mha-configurator]] `skill` — Recommend head count, KV-head count, and projection strategy (MHA / MQA / GQA / MLA) for a new transformer.

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the original multi-head spec. ·  also cited by 8 other lessons
- Shazeer (2019). Fast Transformer Decoding: One Write-Head is All You Need ([link](https://arxiv.org/abs/1911.02150)) — the MQA paper.
- [[Resources/Ainslie et al. (2023). GQA- Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints|Ainslie et al. (2023). GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]] ([link](https://arxiv.org/abs/2305.13245)) — how to convert MHA to GQA after training. ·  also cited by 2 other lessons
- [[Resources/DeepSeek-AI (2024). DeepSeek-V2 Technical Report|DeepSeek-AI (2024). DeepSeek-V2 Technical Report]] ([link](https://arxiv.org/abs/2405.04434)) — MLA and why it beats MHA/GQA on cache memory. ·  also cited by 1 other lesson
- Olsson et al. (2022). In-context Learning and Induction Heads ([link](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)) — mechanistic look at what heads actually do.


%% ── my notes ── %%
