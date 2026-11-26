---
id: "lesson:10/21"
type: lesson
ref: 10/21
phase: 10
num: 21
title: "Jamba — Hybrid SSM-Transformer"
lesson_type: learn
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 22
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
aliases:
  - 10/21
  - 10-21
tags:
  - phase/10
  - type/learn
  - status/planned
  - route
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer"
---

# 10/21 Jamba — Hybrid SSM-Transformer

> State space models (SSMs) and transformers want different things. Transformers buy quality via attention at quadratic cost. SSMs buy linear-time inference and constant memory via a recurrence but lag quality. AI21's Jamba (March 2024) and Jamba 1.5 (August 2024) put them in the same model: 1 Transformer layer for every 7 Mamba layers, MoE on every other block, and a 256k context window that fits on a single 80GB GPU. Mamba-3 (ICLR 2026) tightens the SSM side with complex-valued state spaces and MIMO projections. This lesson reads both architectures end to end and explains why the hybrid recipe has survived three years of scaling when pure-SSM and pure-Transformer long-context attempts have not.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 14 (open-model architectures), Phase 10 · 17 (native sparse attention)`

- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — open-model architectures
- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]] — native sparse attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]], [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Concepts taught

- [[Concepts/State-space model|State-space model]] (as *State space model (SSM)*) `lesson term` — A layer with a learned recurrence h_t = A h{t-1} + B x_t; constant memory per token
- Selective SSM `lesson term` — Data-dependent A, B, C parameters that give the model gating-like selectivity at linear time
- Attention-to-Mamba ratio `lesson term` — In Jamba, l = 8 means 1 attention layer per 7 Mamba layers
- Jamba block `lesson term` — One attention + seven Mamba + MoE on alternate positions
- SSM state `lesson term` — Fixed-size per-layer state that replaces the KV cache for Mamba layers
- 256k context `lesson term` — The sequence length Jamba-1 fits on a single 80GB GPU; pure Transformer cannot at that size
- Mamba-3 `lesson term` — Current-best pure-SSM architecture with complex state + MIMO; the baseline hybrids rebuild around
- MIMO `lesson term` — Mamba-3 innovation using matrix-valued projections instead of scalar per-feature
- Exponential-trapezoidal discretization `lesson term` — More expressive recurrence that subsumes Mamba-2's Euler-method discretization
- Hybrid architecture `lesson term` — Any model that interleaves Transformer and SSM layers; Jamba is the production archetype

## Ships

- [[Artifacts/10-21 hybrid-picker|hybrid-picker]] `skill` — Pick between pure Transformer, Jamba-style hybrid, and pure SSM for a given workload.

## Further reading

- Gu et al. — Efficiently Modeling Long Sequences with Structured State Spaces (arXiv:2111.00396) ([link](https://arxiv.org/abs/2111.00396)) — the S4 paper, the SSM genealogy's starting point for LLMs
- [[Resources/Gu, Dao (2023). Mamba- Linear-Time Sequence Modeling with Selective State Spaces|Gu, Dao (2023). Mamba: Linear-Time Sequence Modeling with Selective State Spaces]] ([link](https://arxiv.org/abs/2312.00752)) — the selective SSM paper Jamba builds on ·  also cited by 1 other lesson
- Lieber et al. — Jamba: A Hybrid Transformer-Mamba Language Model (arXiv:2403.19887) ([link](https://arxiv.org/abs/2403.19887)) — the original Jamba paper, ratio ablations, 256k context claim
- Dao, Gu — Mamba-2 (arXiv:2405.21060) ([link](https://arxiv.org/abs/2405.21060)) — the simplified structured-state-space successor
- AI21 — Jamba 1.5: Hybrid Transformer-Mamba at Scale (arXiv:2408.12570) ([link](https://arxiv.org/abs/2408.12570)) — the scaled-up family, 398B/94B and 12B/52B public releases
- Lahoti et al. — Mamba-3 (arXiv:2603.15569, ICLR 2026) ([link](https://arxiv.org/abs/2603.15569)) — complex-valued state, MIMO, the 2026 pure-SSM frontier

## My route

- Step 22 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Jamba: hybrid SSM-transformer
- Previous: [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]
- Next: [[Lessons/10-22 Async and Hogwild! Inference|10/22 Async and Hogwild! Inference]]


%% ── my notes ── %%
