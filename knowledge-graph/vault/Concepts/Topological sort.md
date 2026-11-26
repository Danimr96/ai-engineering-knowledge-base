---
id: "concept:topological-sort"
type: concept
name: Topological sort
canonical: false
taught_in: 2
community: 82
tags:
  - concept/lesson-term
  - community/82
source: ai-engineering-from-scratch/phases/01-math-foundations/05-chain-rule-and-autodiff/docs/en.md
---

# Topological sort

**Community:** [[Communities/82 Computational graph · Gradient checking · Topological sort|82 Computational graph · Gradient checking · Topological sort]]

> *What people say:* "Dependency order"

**What it actually means:** Ordering graph nodes so every node comes after all its dependencies. Required for correct gradient propagation.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — An ordering of graph nodes where each node appears after all nodes it depends on -- ensures gradients are fully accumulated before propagation


%% ── my notes ── %%
