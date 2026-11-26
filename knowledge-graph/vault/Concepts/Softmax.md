---
id: "concept:softmax"
type: concept
name: Softmax
canonical: true
category: "Math & training"
taught_in: 4
community: 5
tags:
  - concept/glossary
  - category/math-and-training
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Softmax

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* A function that turns logits into normalized positive values.

**What it actually means:** A function defined by `softmax(x_i) = exp(x_i) / sum(exp(x_j))`, implemented with numerical stabilization. Its outputs are positive and sum to one, so they can parameterize a categorical distribution.

**Common confusion:** Softmax values are not automatically calibrated probabilities about real-world correctness.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Calibration|Calibration]]
- [[Concepts/Cross-Entropy|Cross-Entropy]]
- [[Concepts/Logits|Logits]]
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]]
- [[Concepts/Temperature|Temperature]]

## Taught in

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — softmax(z_i) = exp(z_i) / sum(exp(z_j)). Maps real-valued logits to a valid probability distribution
- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — Exponentiate and normalize. Maps any real-valued vector to a valid probability distribution.
- [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]] — A function that converts a vector of scores into probabilities that sum to 1
- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — Normalizes a vector of logits into a probability distribution where all values are in (0,1) and sum to 1


%% ── my notes ── %%
