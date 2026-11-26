---
id: "concept:speculative-decoding"
type: concept
name: Speculative Decoding
canonical: true
category: "Models & inference"
taught_in: 4
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Speculative Decoding

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** An inference method in which a cheaper draft process proposes several tokens and the target model scores those draft positions in parallel. In exact sampling variants, an acceptance and correction rule preserves the target model's output distribution.

**Why it matters:** It can reduce serial target-model decoding work when drafts are accepted, without requiring a change to the target model's trained weights.

**In practice:** Measure acceptance rate and end-to-end latency on real prompts, include draft-model overhead, and verify that the implementation preserves the intended decoding distribution.

**Common confusion:** Speculative decoding is not ordinary model routing or unverified autocomplete. Exact variants preserve the target distribution through acceptance and correction, while approximate variants may trade that guarantee for speed.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Tokens per Second (TPS)|Tokens per Second (TPS)]]

## Taught in

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — Cheap model proposes N tokens; big model verifies in parallel.
- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — Cheap draft model proposes tokens; big model verifies k in one pass.
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Using a fast draft model to propose multiple tokens, then verifying them all in one target model forward pass -- mathematically exact, 2-3x speedup
- [[Lessons/17-05 EAGLE-3 Speculative Decoding in Production|17/05 EAGLE-3 Speculative Decoding in Production]] — Propose K tokens with a cheap model, verify all K in one target forward

## Sources

- Fast Inference from Transformers via Speculative Decoding ([link](https://proceedings.mlr.press/v202/leviathan23a.html))


%% ── my notes ── %%
