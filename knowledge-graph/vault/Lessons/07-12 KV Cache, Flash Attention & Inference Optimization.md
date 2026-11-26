---
id: "lesson:07/12"
type: lesson
ref: 07/12
phase: 7
num: 12
title: "KV Cache, Flash Attention & Inference Optimization"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 3
community: 5
aliases:
  - 07/12
  - 07-12
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/12-kv-cache-flash-attention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/12-kv-cache-flash-attention"
---

# 07/12 KV Cache, Flash Attention & Inference Optimization

> Training is parallel and FLOP-bound. Inference is serial and memory-bound. Different bottleneck, different tricks.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/12-kv-cache-flash-attention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/12-kv-cache-flash-attention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/12-kv-cache-flash-attention) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention), Phase 7 · 05 (Full Transformer), Phase 7 · 07 (GPT)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — GPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]
- depth 3: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]

## Builds on this

- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]]
- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]]

## Concepts taught

- [[Concepts/KV Cache|KV Cache]] `glossary` — Stored K and V from every prefix token; new queries attend to them instead of recomputing.
- HBM `lesson term` — High Bandwidth Memory; 80 GB on H100, 192 GB on B200. ~3 TB/s bandwidth.
- SRAM `lesson term` — Per-SM fast memory, ~256 KB per SM on H100. ~30 TB/s bandwidth.
- Flash Attention `lesson term` — Computes attention without materializing N×N in HBM.
- [[Concepts/Continuous Batching|Continuous Batching]] `glossary` — Swap finished sequences out, new ones in, without draining the batch.
- [[Concepts/PagedAttention|PagedAttention]] `lesson term` — KV cache allocated in fixed blocks with a page table; eliminates fragmentation.
- [[Concepts/Prefix Caching|Prefix Caching]] `glossary` — Cache KV for a shared prefix across requests; major cost cut for agents.
- [[Concepts/Speculative Decoding|Speculative Decoding]] `glossary` — Cheap draft model proposes tokens; big model verifies k in one pass.
- [[Concepts/FlashAttention|FlashAttention]] `glossary` — An exact attention algorithm that tiles the computation to reduce transfers between accelerator memory levels while avoiding materialization of the full attention matrix in high-bandwidth memory.

## Ships

- [[Artifacts/07-12 inference-optimizer|inference-optimizer]] `skill` — Pick attention implementation, KV cache strategy, quantization, and speculative decoding for a new inference deployment.

## Further reading

- FlashAttention ([link](https://arxiv.org/abs/2205.14135)) — Flash 1.
- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — spec decoding. ·  also cited by 7 other lessons
- [[Resources/Dao (2023). FlashAttention-2- Faster Attention with Better Parallelism and Work Partitioning|Dao (2023). FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]] ([link](https://arxiv.org/abs/2307.08691)) — Flash 2. ·  also cited by 2 other lessons
- [[Resources/Efficient Memory Management for Large Language Model Serving with PagedAttention|Efficient Memory Management for Large Language Model Serving with PagedAttention]] ([link](https://arxiv.org/abs/2309.06180)) — vLLM paper. ·  also cited by 2 other lessons
- [[Resources/Cai et al. (2024). Medusa- Simple LLM Inference Acceleration Framework with Multiple Decoding Heads|Cai et al. (2024). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads]] ([link](https://arxiv.org/abs/2401.10774)) — the Medusa approach referenced alongside EAGLE. ·  also cited by 3 other lessons
- [[Resources/Li et al. (2024). EAGLE- Speculative Sampling Requires Rethinking Feature Uncertainty|Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty]] ([link](https://arxiv.org/abs/2401.15077)) — EAGLE-1/2 paper for the integrated-draft approach the lesson cites. ·  also cited by 4 other lessons
- Shah et al. (2024). FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision ([link](https://arxiv.org/abs/2407.08608)) — Flash 3.
- vLLM docs — PagedAttention ([link](https://docs.vllm.ai/en/latest/design/kernel/paged_attention.html)) — the canonical deep dive on the 16-token block and page-table design.
- FlashAttention-4 release notes (Dao-AILab, 2026) ([link](https://github.com/Dao-AILab/flash-attention)) — Blackwell 5-stage pipeline and the software-exp2 trick; read the repo README for the forward-only launch caveats this lesson mentions.


%% ── my notes ── %%
