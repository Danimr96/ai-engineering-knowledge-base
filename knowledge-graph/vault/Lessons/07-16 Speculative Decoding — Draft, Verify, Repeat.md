---
id: "lesson:07/16"
type: lesson
ref: 07/16
phase: 7
num: 16
title: "Speculative Decoding — Draft, Verify, Repeat"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 20
aliases:
  - 07/16
  - 07-16
tags:
  - phase/07
  - type/build
  - community/20
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/16-speculative-decoding"
---

# 07/16 Speculative Decoding — Draft, Verify, Repeat

> Autoregressive decoding is serial. Each token waits for the previous one. Speculative decoding breaks the chain: a cheap model drafts N tokens, the expensive model verifies all N in one forward pass. When the draft is right you paid one big forward for N generations.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/16-speculative-decoding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/16-speculative-decoding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding) · code: main.py  
**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 07 (GPT Causal LM), Phase 7 · 12 (KV Cache & Flash Attention)`

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — GPT Causal LM
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — KV Cache & Flash Attention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]
- depth 3: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]]

## Builds on this

- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]]

## Concepts taught

- [[Concepts/Draft model|Draft model]] `lesson term` — A smaller model that proposes candidate tokens; usually 10–50× cheaper than the verifier.
- [[Concepts/Verifier|Verifier]] `lesson term` — The target model whose distribution we preserve; runs once per speculative step.
- [[Concepts/Acceptance rate|Acceptance rate]] (as *Acceptance rate (α)*) `lesson term` — Per-token probability that the verifier accepts the draft. 0.7–0.9 typical.
- [[Concepts/Residual distribution|Residual distribution]] `lesson term` — (q - p)+ normalized; sampling from this on rejection preserves the verifier's distribution.
- [[Concepts/Bonus token|Bonus token]] `lesson term` — When all N drafts accepted, sample one more from the verifier's next-step distribution.
- Medusa `lesson term` — Multiple LM heads on the verifier predict positions t+1..t+k in parallel.
- [[Concepts/EAGLE|EAGLE]] `lesson term` — Tiny transformer draft conditioned on the verifier's last-layer hidden states.
- Lookahead decoding `lesson term` — Self-speculation using a fixed-point iteration; no draft model.
- [[Concepts/Tree attention|Tree attention]] `lesson term` — Branching verification that considers several draft continuations simultaneously.
- [[Concepts/KV rollback|KV rollback]] `lesson term` — Scratch KV buffer; commit on acceptance, discard on reject.

## Ships

- [[Artifacts/07-16 spec-decode-picker|spec-decode-picker]] `skill` — Pick a speculative decoding strategy (vanilla / Medusa / EAGLE / lookahead) and tuning parameters for a new LLM inference workload.

## Further reading

- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — the core algorithm and the equivalence theorem. ·  also cited by 7 other lessons
- [[Resources/Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling|Chen et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling]] ([link](https://arxiv.org/abs/2302.01318)) — concurrent introduction; clean Bernoulli-rejection proof. ·  also cited by 2 other lessons
- [[Resources/Cai et al. (2024). Medusa- Simple LLM Inference Acceleration Framework with Multiple Decoding Heads|Cai et al. (2024). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads]] ([link](https://arxiv.org/abs/2401.10774)) — Medusa paper; tree-attention verification. ·  also cited by 3 other lessons
- [[Resources/Li et al. (2024). EAGLE- Speculative Sampling Requires Rethinking Feature Uncertainty|Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty]] ([link](https://arxiv.org/abs/2401.15077)) — EAGLE-1; hidden-state-conditioned draft. ·  also cited by 4 other lessons
- [[Resources/Fu et al. (2024). Break the Sequential Dependency of LLM Inference Using Lookahead Decoding|Fu et al. (2024). Break the Sequential Dependency of LLM Inference Using Lookahead Decoding]] ([link](https://arxiv.org/abs/2402.02057)) — lookahead, no-draft approach. ·  also cited by 1 other lesson
- [[Resources/Li et al. (2024). EAGLE-2- Faster Inference of Language Models with Dynamic Draft Trees|Li et al. (2024). EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees]] ([link](https://arxiv.org/abs/2406.16858)) — EAGLE-2; dynamic tree depth. ·  also cited by 3 other lessons
- [[Resources/Li et al. (2025). EAGLE-3- Scaling up Inference Acceleration of Large Language Models via Training-Time Test|Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test]] ([link](https://arxiv.org/abs/2503.01840)) — EAGLE-3. ·  also cited by 4 other lessons
- [[Resources/vLLM docs — Speculative Decoding|vLLM docs — Speculative Decoding]] ([link](https://docs.vllm.ai/en/latest/features/spec_decode.html)) — canonical production reference with all four strategies wired up. ·  also cited by 1 other lesson
- SafeAILab / EAGLE reference implementation ([link](https://github.com/SafeAILab/EAGLE)) — the reference code for EAGLE-1/2/3.


%% ── my notes ── %%
