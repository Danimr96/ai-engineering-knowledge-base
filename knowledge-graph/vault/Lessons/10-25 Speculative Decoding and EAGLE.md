---
id: "lesson:10/25"
type: lesson
ref: 10/25
phase: 10
num: 25
title: Speculative Decoding and EAGLE
lesson_type: build
languages:
  - Python
time_min: 75
status: planned
status_auto: planned
on_route: true
route_order: 15
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 2
community: 20
libraries:
  - numpy
aliases:
  - 10/25
  - 10-25
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/20
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/25-speculative-decoding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/25-speculative-decoding"
---

# 10/25 Speculative Decoding and EAGLE

> A frontier LLM generating one token requires a full forward pass over billions of parameters. That forward pass is massively over-provisioned: most of the time a much smaller model can guess the next 3-5 tokens correctly, and the big model only needs to *verify* the guess. When the guess is right you got 5 tokens for the price of one. Speculative decoding (Leviathan et al. 2023) made this exact, and EAGLE-3 (2025) pushed acceptance rates to ~4.5 tokens per verify — a 4-5x speedup at matched output distribution.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/25-speculative-decoding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/25-speculative-decoding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/25-speculative-decoding) · code: main.py  
**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10 Lesson 12 (Inference Optimization), Phase 10 Lesson 04 (Pre-training Mini-GPT)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Pre-training Mini-GPT
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Inference Optimization

### Bridges to check first (my plan)

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]] — speculative decoding

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Concepts taught

- Target model `lesson term` — The slow, high-quality model you want samples from (p distribution)
- [[Concepts/Draft model|Draft model]] `lesson term` — The small, fast predictor (q distribution); 5-30x smaller
- K / draft length `lesson term` — Number of speculated tokens per verify pass
- [[Concepts/Acceptance rate|Acceptance rate]] (as *α / acceptance rate*) `lesson term` — Per-token probability that the draft's proposal is accepted
- Exact rejection rule `lesson term` — r < p/q compare that preserves target's distribution
- [[Concepts/Residual distribution|Residual distribution]] `lesson term` — 1, the distribution to sample from on rejection
- Tree drafting `lesson term` — Draft outputs a tree of candidates, verified in one pass with tree-structured attention mask
- Tree attention mask `lesson term` — Causal mask encoding the tree topology so each node attends only to its ancestors
- Medusa heads `lesson term` — K extra prediction heads on the target itself; no separate draft model
- EAGLE feature reuse `lesson term` — Draft input is target's last hidden state, not raw tokens, shrinking the draft
- Test-time simulation loss `lesson term` — Train draft on outputs matching target's test-time distribution, not teacher forcing

## Ships

- [[Artifacts/10-25 speculative-tuning|speculative-tuning]] `skill` — Profile a decode workload and pick draft model, draft length K, temperature gate, and fallback policy for speculative decoding.

## Further reading

- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — the exact rejection rule and the theoretical speedup analysis ·  also cited by 7 other lessons
- [[Resources/Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling|Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling]] ([link](https://arxiv.org/abs/2302.01318)) — concurrent speculative-sampling paper at DeepMind ·  also cited by 2 other lessons
- [[Resources/Cai et al. (2024). Medusa- Simple LLM Inference Acceleration Framework with Multiple Decoding Heads|Cai et al. (2024). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads]] ([link](https://arxiv.org/abs/2401.10774)) — parallel-heads alternative to a draft model ·  also cited by 3 other lessons
- [[Resources/Li et al. (2024). EAGLE- Speculative Sampling Requires Rethinking Feature Uncertainty|Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty]] ([link](https://arxiv.org/abs/2401.15077)) — feature reuse and tree drafting ·  also cited by 4 other lessons
- [[Resources/Fu et al. (2024). Break the Sequential Dependency of LLM Inference Using Lookahead Decoding|Fu et al. (2024). Break the Sequential Dependency of LLM Inference Using Lookahead Decoding]] ([link](https://arxiv.org/abs/2402.02057)) — Jacobi/lookahead decoding, a speculator-free alternative ·  also cited by 1 other lesson
- [[Resources/Li et al. (2024). EAGLE-2- Faster Inference of Language Models with Dynamic Draft Trees|Li et al. (2024). EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees]] ([link](https://arxiv.org/abs/2406.16858)) — dynamic tree topology ·  also cited by 3 other lessons
- [[Resources/Li et al. (2025). EAGLE-3- Scaling up Inference Acceleration of Large Language Models via Training-Time Test|Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test]] ([link](https://arxiv.org/abs/2503.01840)) — train-time test-time matching ·  also cited by 4 other lessons

## My route

- Step 15 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Speculative decoding and EAGLE
- Previous: [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]]
- Next: [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]]


%% ── my notes ── %%
