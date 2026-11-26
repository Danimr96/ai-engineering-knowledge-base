---
id: "concept:loss-scaling"
type: concept
name: Loss scaling
canonical: false
taught_in: 2
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/01-math-foundations/13-numerical-stability/docs/en.md
---

# Loss scaling

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "Prevent gradient underflow"

**What it actually means:** Multiplying the loss by a large constant before backprop so gradients stay in float16's representable range, then dividing by the same constant before weight updates.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]]
- [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]] — Per-micro-batch division so summed gradients match full batch


%% ── my notes ── %%
