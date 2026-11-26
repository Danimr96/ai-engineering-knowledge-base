---
id: "concept:model-routing"
type: concept
name: Model routing
canonical: false
taught_in: 2
community: 41
tags:
  - concept/lesson-term
  - community/41
source: ai-engineering-from-scratch/phases/11-llm-engineering/11-caching-cost/docs/en.md
---

# Model routing

**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]]

> *What people say:* "Cheapskate routing"

**What it actually means:** Using a classifier to send simple queries to cheap models (GPT-4o-mini, Haiku) and complex queries to expensive models (GPT-4o, Opus) -- saves 40-70% on model costs

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]]
- [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]] — Dynamic choice of model per request


%% ── my notes ── %%
