---
id: "concept:dropout"
type: concept
name: Dropout
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

# Dropout

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* Randomly turning off activations.

**What it actually means:** During training, randomly setting a fraction of activations to zero encourages the network not to rely on one activation path. It is normally disabled for standard inference, although Monte Carlo dropout deliberately keeps it active to estimate uncertainty.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Function|Activation Function]]
- [[Concepts/Overfitting|Overfitting]]
- [[Concepts/Weight Decay|Weight Decay]]

## Taught in

- [[Lessons/03-07 Regularization|03/07 Regularization]] — Zeroing random neurons during training with probability p, forcing redundant representations; equivalent to training an ensemble


%% ── my notes ── %%
