---
id: "concept:semantic-caching"
type: concept
name: Semantic caching
canonical: false
taught_in: 2
community: 41
tags:
  - concept/lesson-term
  - community/41
source: ai-engineering-from-scratch/phases/11-llm-engineering/11-caching-cost/docs/en.md
---

# Semantic caching

**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]]

> *What people say:* "Smart caching"

**What it actually means:** Embedding the query, computing similarity to past queries, and returning the cached response if similarity exceeds a threshold -- catches paraphrases that exact matching misses

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]]
- [[Lessons/13-21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey|13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey]] — Key is embedding of the prompt; near-duplicates share a cache hit


%% ── my notes ── %%
