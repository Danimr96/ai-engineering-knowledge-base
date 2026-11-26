---
id: "concept:kv-cache"
type: concept
name: KV Cache
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

# KV Cache

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* A cache that makes token generation faster.

**What it actually means:** Stored key and value tensors from earlier positions in autoregressive generation. Reusing them avoids recomputing attention projections for the unchanged prefix at every decoding step.

**Why it matters:** It reduces repeated computation but consumes memory that grows with sequence length, layers, batch, and model configuration.

**Common confusion:** A KV cache is runtime attention state for a sequence. Prefix caching reuses eligible KV state across requests, while prompt caching is a broader provider or application reuse contract.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/FlashAttention|FlashAttention]]
- [[Concepts/Inference|Inference]]
- [[Concepts/Paged KV Cache|Paged KV Cache]]
- [[Concepts/Prefill|Prefill]]
- [[Concepts/Prefix Caching|Prefix Caching]]
- [[Concepts/Prompt Cache|Prompt Cache]]
- [[Concepts/Speculative Decoding|Speculative Decoding]]

## Taught in

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]] — Stored K and V from every prefix token; new queries attend to them instead of recomputing.
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Storing computed Key and Value tensors from previous tokens to avoid redundant computation during autoregressive generation
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Storing the key and value projections for all previous tokens so they are not recomputed at each decode step -- trades memory for compute
- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]] — Image keys and values stored once and reused for every decode step


%% ── my notes ── %%
