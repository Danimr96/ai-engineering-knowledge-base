---
id: "concept:sliding-window"
type: concept
name: Sliding window
canonical: false
taught_in: 4
community: 92
tags:
  - concept/lesson-term
  - community/92
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/15-time-series/docs/en.md
---

# Sliding window

**Community:** [[Communities/92 LiteLLM · Sliding window · Token bucket|92 LiteLLM · Sliding window · Token bucket]]

> *What people say:* "Fixed-size history"

**What it actually means:** Walk-forward validation where the training set is a fixed-length window that slides forward

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/02-15 Time Series Fundamentals|02/15 Time Series Fundamentals]]
- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]] — Attention over the last W tokens for short-range patterns
- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]] — Time-windowed rate limiter; better fairness
- [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]] — A fixed-length slice of the global token stream that the trainer pairs with its shift-by-one target


%% ── my notes ── %%
