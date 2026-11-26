---
id: "concept:token-bucket"
type: concept
name: Token bucket
canonical: false
taught_in: 2
community: 92
tags:
  - concept/lesson-term
  - community/92
source: ai-engineering-from-scratch/phases/11-llm-engineering/11-caching-cost/docs/en.md
---

# Token bucket

**Community:** [[Communities/92 LiteLLM · Sliding window · Token bucket|92 LiteLLM · Sliding window · Token bucket]]

> *What people say:* "Rate limiter"

**What it actually means:** An algorithm where each user has a bucket of N tokens that refills at rate R per second -- allows bursts up to N while enforcing an average rate of R

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]]
- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]] — Refill-based rate limiter


%% ── my notes ── %%
