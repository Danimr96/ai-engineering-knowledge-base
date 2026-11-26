---
id: "lesson:10/15"
type: lesson
ref: 10/15
phase: 10
num: 15
title: Speculative Decoding and EAGLE-3
lesson_type: build
languages:
  - Python
time_min: 75
status: planned
status_auto: planned
on_route: true
route_order: 16
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 20
aliases:
  - 10/15
  - 10-15
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/20
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/15-speculative-decoding-eagle3/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/15-speculative-decoding-eagle3"
---

# 10/15 Speculative Decoding and EAGLE-3

> Phase 7 · Lesson 16 proved the math: the Leviathan rejection rule preserves the verifier's distribution exactly. This lesson is the training-stack view of 2026 production speculative decoding. EAGLE-3 turned the draft model from a cheap approximation into a purpose-built tiny network trained on the verifier's own hidden states, then added a training-time test loop that aligns its train and inference distributions. Result: 3× to 6.5× end-to-end speedup, accepted per-token rates above 0.9 on chat, no distributional tradeoff. Every production inference stack in 2026 ships it by default.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/15-speculative-decoding-eagle3/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/15-speculative-decoding-eagle3) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/15-speculative-decoding-eagle3) · code: main.py  
**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 16 (speculative decoding math), Phase 10 · 12 (inference optimization)`

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]] — speculative decoding math
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — inference optimization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]]
- [[Lessons/10-22 Async and Hogwild! Inference|10/22 Async and Hogwild! Inference]]

## Concepts taught

- Leviathan rule `lesson term` — Bernoulli accept/reject with probability min(1, q(d)/p(d)), preserves the verifier distribution exactly when you sample from the residual on rejection
- [[Concepts/Residual distribution|Residual distribution]] `lesson term` — (q - p)+ clamped at zero and renormalized — the correct distribution to sample from on rejection
- [[Concepts/Acceptance rate|Acceptance rate]] (as *Acceptance rate α*) `lesson term` — Expected per-token Bernoulli-success probability under the rejection rule; governs all speedup math
- EAGLE-1 `lesson term` — Tiny transformer draft conditioned on the verifier's last-layer hidden state (Li et al., 2024)
- EAGLE-2 `lesson term` — EAGLE-1 plus a tree of candidate continuations scored with tree attention in one verifier pass
- [[Concepts/EAGLE-3|EAGLE-3]] `lesson term` — Drops the feature-prediction loss, trains on direct token prediction with the draft fed its own outputs during training
- Training-time test (as *Training-time test (TTT)*) `lesson term` — Run the draft autoregressively during training so train and test input distributions match — the direct analog of scheduled sampling
- [[Concepts/KV rollback|KV rollback]] `lesson term` — Bookkeeping that resets the verifier's KV cache to the accepted-prefix length after a rejection
- [[Concepts/Bonus token|Bonus token]] `lesson term` — When all N drafts accept, sample one extra from q{N+1} at no additional verifier cost
- [[Concepts/Tree attention|Tree attention]] `lesson term` — Attention with a non-causal mask that respects the topology of a draft tree; computes q_i for every node in the tree in one forward pass

## Ships

- [[Artifacts/10-15 eagle3-tuner|eagle3-tuner]] `skill` — Pick and tune a speculative decoding strategy (vanilla / Medusa / EAGLE-1/2/3 / lookahead) for a new inference workload.

## Further reading

- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — the foundational paper and equivalence theorem ·  also cited by 7 other lessons
- [[Resources/Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling|Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling]] ([link](https://arxiv.org/abs/2302.01318)) — concurrent independent introduction with a clean proof ·  also cited by 2 other lessons
- [[Resources/Cai et al. (2024). Medusa- Simple LLM Inference Acceleration Framework with Multiple Decoding Heads|Cai et al. (2024). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads]] ([link](https://arxiv.org/abs/2401.10774)) — alternative draft-free approach ·  also cited by 3 other lessons
- [[Resources/Li et al. (2024). EAGLE- Speculative Sampling Requires Rethinking Feature Uncertainty|Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty]] ([link](https://arxiv.org/abs/2401.15077)) — EAGLE-1, hidden-state-conditioned draft ·  also cited by 4 other lessons
- [[Resources/Li et al. (2024). EAGLE-2- Faster Inference of Language Models with Dynamic Draft Trees|Li et al. (2024). EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees]] ([link](https://arxiv.org/abs/2406.16858)) — dynamic tree search ·  also cited by 3 other lessons
- [[Resources/Li et al. (2025). EAGLE-3- Scaling up Inference Acceleration of Large Language Models via Training-Time Test|Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test]] ([link](https://arxiv.org/abs/2503.01840)) — the 2026 production default ·  also cited by 4 other lessons
- [[Resources/vLLM docs — Speculative Decoding|vLLM docs — Speculative Decoding]] ([link](https://docs.vllm.ai/en/latest/features/spec_decode.html)) — canonical production reference with all strategies wired up ·  also cited by 1 other lesson

## My route

- Step 16 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Speculative decoding and EAGLE-3 (overlaps 10/25, so skim whichever comes second)
- Previous: [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]]
- Next: [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]


%% ── my notes ── %%
