---
id: "concept:chain-rule"
type: concept
name: Chain rule
canonical: false
taught_in: 3
community: 8
tags:
  - concept/lesson-term
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/04-calculus-for-ml/docs/en.md
---

# Chain rule

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* "Multiply the derivatives"

**What it actually means:** The rule for differentiating composed functions: df/dx = df/dg dg/dx. The mathematical basis of backpropagation.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]
- [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]] — The derivative of composed functions equals the product of each function's local derivative, evaluated at the right point
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — If y = f(g(x)), then dy/dx = f'(g(x)) g'(x) -- the mathematical foundation of backpropagation


%% ── my notes ── %%
