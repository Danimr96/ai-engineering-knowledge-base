---
id: "concept:kl-divergence"
type: concept
name: KL divergence
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/01-math-foundations/09-information-theory/docs/en.md
---

# KL divergence

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Distance between distributions"

**What it actually means:** Extra bits wasted by using Q instead of P. Equals cross-entropy minus entropy. Not symmetric.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-09 Information Theory|01/09 Information Theory]]
- [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]] — Not a true distance (not symmetric). Measures extra bits from using Q to encode P
- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — A measure of the difference between the policy model's token distribution and the reference model's -- used as a penalty to prevent reward hacking


%% ── my notes ── %%
