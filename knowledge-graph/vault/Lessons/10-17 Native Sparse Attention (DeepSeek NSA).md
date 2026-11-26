---
id: "lesson:10/17"
type: lesson
ref: 10/17
phase: 10
num: 17
title: Native Sparse Attention (DeepSeek NSA)
lesson_type: build
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 18
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 3
community: 70
aliases:
  - 10/17
  - 10-17
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/70
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/17-native-sparse-attention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/17-native-sparse-attention"
---

# 10/17 Native Sparse Attention (DeepSeek NSA)

> At 64k tokens, attention eats 70-80% of decode latency. Every open-model lab has a plan to fix it. DeepSeek's NSA (ACL 2025 best paper) is the one that stuck: three parallel attention branches — compressed coarse-grained tokens, selectively retained fine-grained tokens, and sliding windows for local context — combined through a learned gate. It is hardware-aligned (kernel-friendly), natively trainable (works in pre-training, not bolted on at inference), and on 64k decodes it runs faster than FlashAttention while matching or beating full attention quality. This lesson builds the three branches end-to-end and shows why the sparsity is end-to-end differentiable.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/17-native-sparse-attention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/17-native-sparse-attention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/17-native-sparse-attention) · code: main.py  
**Community:** [[Communities/70 Differential attention · Sliding window attention|70 Differential attention · Sliding window attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 12 (KV cache, flash-attention), Phase 7 · 15 (attention variants), Phase 10 · 16 (differential attention)`

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — KV cache, flash-attention
- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]] — attention variants
- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]] — differential attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]]
- depth 3: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]

## Builds on this

- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]
- [[Lessons/10-21 Jamba — Hybrid SSM-Transformer|10/21 Jamba — Hybrid SSM-Transformer]]

## Concepts taught

- Compressed branch `lesson term` — Attention over block-averaged keys that provides global context in O(N/l) keys per query
- Selected branch `lesson term` — Fine-grained attention over the k blocks with highest compressed-branch scores
- [[Concepts/Sliding window|Sliding window]] `lesson term` — Attention over the last W tokens for short-range patterns
- Native trainability `lesson term` — The sparsity pattern is learned during pre-training, not bolted on at inference
- Compression block size l `lesson term` — How many tokens get merged into one summary; 32-64 typical
- Top-k `lesson term` — Number of compressed blocks whose uncompressed tokens get read; 16 typical
- Sliding window W `lesson term` — Typically 512; shorter hurts local coherence, longer wastes compute
- Branch gate `lesson term` — Per-position MLP output that weights the three branches' contributions
- Hardware alignment `lesson term` — Sparse pattern chosen so that the actual GPU kernel achieves the theoretical speedup
- DSA `lesson term` — Deepseek Sparse Attention, the architecture that followed NSA in DeepSeek's lineage

## Ships

- [[Artifacts/10-17 nsa-integrator|nsa-integrator]] `skill` — Integration plan for Native Sparse Attention in a long-context pre-training run.

## Further reading

- [[Resources/Beltagy, Peters, Cohan (2020). Longformer- The Long-Document Transformer|Beltagy, Peters, Cohan (2020). Longformer: The Long-Document Transformer]] ([link](https://arxiv.org/abs/2004.05150)) — sliding-window origins ·  also cited by 1 other lesson
- [[Resources/Dao (2023). FlashAttention-2- Faster Attention with Better Parallelism and Work Partitioning|Dao (2023). FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]] ([link](https://arxiv.org/abs/2307.08691)) — the full-attention baseline NSA kernels beat at 64k ·  also cited by 2 other lessons
- Xiao et al. — StreamingLLM: Efficient Streaming Language Models with Attention Sinks (arXiv:2309.17453) ([link](https://arxiv.org/abs/2309.17453)) — inference-time sparsity baseline NSA improves on
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — the architecture family NSA targets ·  also cited by 7 other lessons
- [[Resources/Yuan et al. (2025). Native Sparse Attention|Yuan et al. (2025). Native Sparse Attention]] ([link](https://arxiv.org/abs/2502.11089)) — the paper ·  also cited by 2 other lessons
- Moonshot AI — MoBA: Mixture of Block Attention for Long-Context LLMs (arXiv:2502.13189) ([link](https://arxiv.org/abs/2502.13189)) — concurrent work, MoE-style attention over blocks

## My route

- Step 18 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Native sparse attention (DeepSeek NSA)
- Previous: [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]
- Next: [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]]


%% ── my notes ── %%
