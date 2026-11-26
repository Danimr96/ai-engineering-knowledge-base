---
id: "concept:bias-correction"
type: concept
name: Bias correction
canonical: false
taught_in: 2
community: 11
tags:
  - concept/lesson-term
  - community/11
source: ai-engineering-from-scratch/phases/01-math-foundations/08-optimization/docs/en.md
---

# Bias correction

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* "Fix the cold start"

**What it actually means:** Adam's first and second moments are initialized to zero. Bias correction divides by (1 - beta^t) to compensate during early steps.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-08 Optimization|01/08 Optimization]]
- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Dividing by (1 - beta^t) to compensate for the zero-initialization of Adam's moment estimates


%% ── my notes ── %%
