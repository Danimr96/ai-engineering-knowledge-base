---
id: "concept:kl-budget"
type: concept
name: KL budget
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/09-constitutional-ai-self-improvement/docs/en.md
---

# KL budget

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "How far you can drift"

**What it actually means:** The total KL divergence from the reference model that the optimizer is allowed to accumulate before training stops

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]] — reference) across alignment stages, enforced as a gate
- [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]] — sqrt(KL(pi || pi_init)); Gao et al. plot reward against this


%% ── my notes ── %%
