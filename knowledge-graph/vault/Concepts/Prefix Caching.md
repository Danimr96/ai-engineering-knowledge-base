---
id: "concept:prefix-caching"
type: concept
name: Prefix Caching
canonical: true
category: "Infrastructure & serving"
taught_in: 2
community: 5
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Prefix Caching

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** Reusing KV-cache blocks produced for an identical eligible token prefix across requests so the serving runtime can skip repeated prefix computation.

**Why it matters:** Shared system instructions, templates, or documents can consume substantial prefill work, but reuse only helps when token sequences and cache eligibility match.

**In practice:** Place stable tokens before request-specific content, include model and tokenizer versions in cache identity, isolate tenant-sensitive state, monitor hit rate, and treat eviction as normal.

**Common confusion:** Prefix caching reuses runtime attention state for exact token prefixes. Prompt caching is a broader provider or application contract, while semantic caching reuses a prior result for a similar request.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Paged KV Cache|Paged KV Cache]]
- [[Concepts/Prompt Cache|Prompt Cache]]
- [[Concepts/Semantic Cache|Semantic Cache]]

## Taught in

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — Cache KV for a shared prefix across requests; major cost cut for agents.
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Storing computed KV cache entries for common prefixes (system prompts, few-shot examples) and reusing them across requests to skip redundant prefill

## Sources

- SGLang ([link](https://arxiv.org/abs/2312.07104))


%% ── my notes ── %%
