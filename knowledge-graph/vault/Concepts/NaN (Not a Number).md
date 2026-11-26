---
id: "concept:nan-not-a-number"
type: concept
name: NaN (Not a Number)
canonical: true
category: "Math & training"
taught_in: 1
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# NaN (Not a Number)

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* A sign that numerical computation failed.

**What it actually means:** A floating-point value representing an undefined or unrepresentable numerical result. In training, NaNs can come from invalid operations, overflow, unstable normalization, excessive updates, or earlier corrupted values.

**In practice:** Find the first non-finite tensor, inspect its inputs, and add assertions or anomaly detection near that operation.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Gradient|Gradient]]
- [[Concepts/Gradient Clipping|Gradient Clipping]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Mixed Precision|Mixed Precision]]

## Taught in

- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]] `alias` — Special float value from undefined operations (0/0, inf-inf, sqrt(-1)). Propagates through all subsequent arithmetic.


%% ── my notes ── %%
