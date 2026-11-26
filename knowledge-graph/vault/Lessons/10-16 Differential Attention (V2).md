---
id: "lesson:10/16"
type: lesson
ref: 10/16
phase: 10
num: 16
title: Differential Attention (V2)
lesson_type: build
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 17
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 3
community: 70
aliases:
  - 10/16
  - 10-16
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/70
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/16-differential-attention-v2/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/16-differential-attention-v2"
---

# 10/16 Differential Attention (V2)

> Softmax attention spreads a small amount of probability over every non-matching token. Over 100k tokens that noise adds up and drowns the signal. Differential Transformer (Ye et al., ICLR 2025) fixes it by computing attention as the difference of two softmaxes, subtracting the shared noise floor. DIFF V2 (Microsoft, January 2026) is the production-stack rewrite: matching decode latency to baseline Transformer, no custom kernels, FlashAttention-compatible. This lesson is V1 to V2 end-to-end, with a working toy implementation of the difference operation you can run in stdlib Python.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/16-differential-attention-v2/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/16-differential-attention-v2) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/16-differential-attention-v2) · code: main.py  
**Community:** [[Communities/70 Differential attention · Sliding window attention|70 Differential attention · Sliding window attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 02 (self-attention), Phase 7 · 15 (attention variants), Phase 10 · 14 (architecture walkthrough)`

- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — self-attention
- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]] — attention variants
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — architecture walkthrough

### Bridges to check first (my plan)

- [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]] — attention variants

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]]

## Concepts taught

- [[Concepts/Differential attention|Differential attention]] `lesson term` — Split Q, K into two halves, compute two softmax maps, subtract the second (scaled by lambda) from the first, then multiply by V
- Noise floor `lesson term` — The O(1/N) weight softmax puts on every unrelated token, which sums to O(1) across long contexts
- lambda `lesson term` — Per-head learnable scalar parameterized as exp(lq1.lk1) - exp(lq2.lk2) + lambda_init; can be negative
- DIFF V1 `lesson term` — Original Differential Transformer; halves head dim to preserve parameter count, needs custom kernel, slower decode
- DIFF V2 `lesson term` — Doubles Q heads keeping KV heads; matches baseline decode speed and works with FlashAttention
- Per-head RMSNorm `lesson term` — Extra norm V1 applied after the difference; V2 removed it to prevent late-training instability
- Signal-to-noise ratio `lesson term` — Ratio of weight on the true signal position to average weight on unrelated positions
- [[Concepts/Lost in the Middle|Lost in the Middle]] `glossary` — Empirical phenomenon where retrieval accuracy dips for documents in the middle of a long context — DIFF attention reduces this
- Arithmetic intensity `lesson term` — Ratio V2 increased at decode by doubling queries per KV load; important for memory-bound decode

## Ships

- [[Artifacts/10-16 diff-attention-integrator|diff-attention-integrator]] `skill` — Integration plan for adding Differential Attention V2 to a new pre-training run or LoRA fine-tune.

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the baseline Transformer DIFF subtracts from ·  also cited by 8 other lessons
- [[Resources/Liu et al. (2024). Lost in the Middle- How Language Models Use Long Contexts|Liu et al. (2024). Lost in the Middle: How Language Models Use Long Contexts]] ([link](https://arxiv.org/abs/2307.03172)) — the long-context benchmark DIFF attention targets ·  also cited by 2 other lessons
- [[Resources/Ye et al. (2024). Differential Transformer|Ye et al. (2024). Differential Transformer]] ([link](https://arxiv.org/abs/2410.05258)) — the original paper with noise-cancellation theory and long-context ablations ·  also cited by 1 other lesson
- Shared DIFF Transformer (arXiv:2501.17900) ([link](https://arxiv.org/html/2501.17900)) — parameter-sharing variant
- Understanding Differential Transformer Unchains Pretrained Self-Attentions (arXiv:2505.16333) ([link](https://arxiv.org/abs/2505.16333)) — theoretical analysis of why the subtraction recovers pretrained attention structure
- Microsoft unilm — Differential Transformer V2 (Hugging Face blog, January 2026) ([link](https://huggingface.co/blog/microsoft/diff-attn-v2)) — the production-stack rewrite, matching baseline decode, FlashAttention-compatible

## My route

- Step 17 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Differential attention V2
- Previous: [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]]
- Next: [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]]


%% ── my notes ── %%
