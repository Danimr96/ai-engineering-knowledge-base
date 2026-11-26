---
id: "concept:gradient-checking"
type: concept
name: Gradient checking
canonical: false
taught_in: 3
community: 82
tags:
  - concept/lesson-term
  - community/82
source: ai-engineering-from-scratch/phases/01-math-foundations/05-chain-rule-and-autodiff/docs/en.md
---

# Gradient checking

**Community:** [[Communities/82 Computational graph · Gradient checking · Topological sort|82 Computational graph · Gradient checking · Topological sort]]

> *What people say:* "Numerical verification"

**What it actually means:** Comparing autodiff gradients against numerical finite-difference gradients to verify correctness. Essential for debugging.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]
- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]] — Comparing analytical gradients from backpropagation against numerical gradients from finite differences to catch implementation bugs.
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]] — Comparing analytical gradients from backprop to numerical gradients from finite differences


%% ── my notes ── %%
