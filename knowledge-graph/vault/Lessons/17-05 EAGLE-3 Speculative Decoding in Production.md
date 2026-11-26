---
id: "lesson:17/05"
type: lesson
ref: 17/05
phase: 17
num: 5
title: EAGLE-3 Speculative Decoding in Production
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
aliases:
  - 17/05
  - 17-05
tags:
  - phase/17
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/05-eagle3-speculative-decoding/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/05-eagle3-speculative-decoding"
---

# 17/05 EAGLE-3 Speculative Decoding in Production

> Speculative decoding pairs a fast draft model with the target model. The draft proposes K tokens; the target verifies in a single forward; accepted tokens are free. In 2026, EAGLE-3 is the production-grade variant — it trains a draft head on the target model's hidden states rather than on raw tokens, pushing acceptance rate alpha into the 0.6-0.8 band on general chat. The right question is not "how fast is the draft" but "what is alpha on my traffic?" If alpha drops below ~0.55, speculative decoding is net negative at high concurrency because every rejected draft costs a second target forward pass. This lesson teaches you to measure alpha first and flip the flag second.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/05-eagle3-speculative-decoding/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/05-eagle3-speculative-decoding) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/05-eagle3-speculative-decoding) · code: main.py · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 10 · 18 (Multi-Token Prediction)`

- [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]] — Multi-Token Prediction
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]], [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]

## Concepts taught

- [[Concepts/Speculative Decoding|Speculative Decoding]] `glossary` — Propose K tokens with a cheap model, verify all K in one target forward
- Acceptance rate alpha `lesson term` — Fraction of draft tokens accepted by the target; the only metric that matters
- Draft length K `lesson term` — How many tokens the draft proposes per target forward; typical 4-8
- Verify overhead epsilon `lesson term` — Extra cost to verify-and-reroll vs a plain target forward; grows with batch
- [[Concepts/EAGLE-3|EAGLE-3]] `lesson term` — 2025-2026 variant; trains draft head on multiple target layers; alpha 0.6-0.8 on general chat
- speculative_config `lesson term` — The explicit opt-in in vLLM V1; no default means no acceleration
- N-gram spec decode `lesson term` — GPU-side draft using N-gram lookups in the prompt; chunked-prefill-compatible
- Break-even alpha `lesson term` — Alpha at which spec decode gives zero speedup; watch this at production concurrency
- Rejected-draft two-pass `lesson term` — Two target forwards when drafts reject; drives P99 tail

## Ships

- [[Artifacts/17-05 eagle3-rollout|eagle3-rollout]] `skill` — Produce a staged EAGLE-3 speculative-decoding rollout plan that measures acceptance rate alpha on real traffic before shipping.

## Further reading

- [[Resources/Li et al. (2024). EAGLE- Speculative Sampling Requires Rethinking Feature Uncertainty|Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty]] ([link](https://arxiv.org/abs/2401.15077)) — original EAGLE draft-head formulation. ·  also cited by 4 other lessons
- [[Resources/Li et al. (2024). EAGLE-2- Faster Inference of Language Models with Dynamic Draft Trees|Li et al. (2024). EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees]] ([link](https://arxiv.org/abs/2406.16858)) — adaptive drafts and trees. ·  also cited by 3 other lessons
- BentoML — Speculative Decoding ([link](https://bentoml.com/llm/inference-optimization/speculative-decoding)) — production rollout checklist.
- vLLM Speculative Config API ([link](https://docs.vllm.ai/en/latest/api/vllm/config/speculative/)) — the exact field set.
- [[Resources/vLLM documentation — Speculative Decoding|vLLM documentation — Speculative Decoding]] ([link](https://docs.vllm.ai/en/latest/features/spec_decode/)) — authoritative source on `speculative_config` and chunked-prefill compatibility in V1. ·  also cited by 1 other lesson
- UC Berkeley EECS-2025-224 ([link](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-224.html)) — efficient LLM system with speculative decoding.


%% ── my notes ── %%
