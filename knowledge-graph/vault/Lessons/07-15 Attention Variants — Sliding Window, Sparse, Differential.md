---
id: "lesson:07/15"
type: lesson
ref: 07/15
phase: 7
num: 15
title: "Attention Variants — Sliding Window, Sparse, Differential"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 3
community: 70
aliases:
  - 07/15
  - 07-15
tags:
  - phase/07
  - type/build
  - community/70
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/15-attention-variants/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/15-attention-variants"
---

# 07/15 Attention Variants — Sliding Window, Sparse, Differential

> Full attention is a circle. Every token sees every token, and memory pays the price. Four variants bend the shape of the circle and recover half the cost.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/15-attention-variants/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/15-attention-variants) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/15-attention-variants) · code: main.py  
**Community:** [[Communities/70 Differential attention · Sliding window attention|70 Differential attention · Sliding window attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (Self-Attention), Phase 7 · 03 (Multi-Head), Phase 7 · 12 (KV Cache / Flash Attention)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Self-Attention
- [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]] — Multi-Head
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — KV Cache / Flash Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- depth 3: [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]

## Builds on this

- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]
- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]]

## Concepts taught

- [[Concepts/Sliding window attention|Sliding window attention]] (as *Sliding window attention (SWA)*) `lesson term` — Each query attends to its last W tokens; KV cache shrinks to O(W).
- Effective receptive field `lesson term` — In an L-layer SWA stack with window W, up to L × W tokens.
- Longformer / BigBird `lesson term` — Sparse patterns with a few always-attending global tokens; early long-context approach.
- Native Sparse Attention `lesson term` — Learn block-level sparsity; skip zero blocks at the kernel level while keeping quality.
- [[Concepts/Differential attention|Differential attention]] `lesson term` — DIFF Transformer: subtract a learned λ times a second attention map from the first to cancel attention sinks.
- Attention sink `lesson term` — Softmax normalization forces rows to sum to 1; uninformative queries dump weight on position 0.
- FlexAttention `lesson term` — PyTorch 2.5+ API that compiles arbitrary mask functions into FlashAttention-shape kernels.
- Layer type mix `lesson term` — Interleave sparse and full attention layers in a stack to keep quality at lower memory.

## Ships

- [[Artifacts/07-15 attention-variant-picker|attention-variant-picker]] `skill` — Pick a full / sliding-window / sparse / differential attention topology for a new model given context length, retrieval demands, and compute profile.

## Further reading

- Child et al. (2019). Generating Long Sequences with Sparse Transformers ([link](https://arxiv.org/abs/1904.10509)) — OpenAI's local+strided pattern.
- [[Resources/Beltagy, Peters, Cohan (2020). Longformer- The Long-Document Transformer|Beltagy, Peters, Cohan (2020). Longformer: The Long-Document Transformer]] ([link](https://arxiv.org/abs/2004.05150)) — the canonical sliding-window + global-token paper. ·  also cited by 1 other lesson
- Zaheer et al. (2020). Big Bird: Transformers for Longer Sequences ([link](https://arxiv.org/abs/2007.14062)) — local + global + random.
- [[Resources/Gemma Team (2024). Gemma 2- Improving Open Language Models at a Practical Size|Gemma Team (2024). Gemma 2: Improving Open Language Models at a Practical Size]] ([link](https://arxiv.org/abs/2408.00118)) — the 1:1 SWA:global mix. ·  also cited by 1 other lesson
- [[Resources/Ye et al. (2024). Differential Transformer|Ye et al. (2024). Differential Transformer]] ([link](https://arxiv.org/abs/2410.05258)) — DIFF Transformer paper. ·  also cited by 1 other lesson
- [[Resources/Yuan et al. (2025). Native Sparse Attention|Yuan et al. (2025). Native Sparse Attention]] ([link](https://arxiv.org/abs/2502.11089)) — DeepSeek-V3.2's learned-sparsity attention. ·  also cited by 2 other lessons
- Gemma Team (2025). Gemma 3 technical report ([link](https://arxiv.org/abs/2503.19786)) — the 5:1 mix with window=1024 that's now the textbook default.
- PyTorch — FlexAttention blog and docs ([link](https://pytorch.org/blog/flexattention/)) — API reference for the mask-as-callable pattern in Use It.


%% ── my notes ── %%
