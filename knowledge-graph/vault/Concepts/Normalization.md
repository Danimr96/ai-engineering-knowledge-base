---
id: "concept:normalization"
type: concept
name: Normalization
canonical: true
category: "Math & training"
taught_in: 0
community: 34
tags:
  - concept/glossary
  - category/math-and-training
  - community/34
source: ai-engineering-from-scratch/glossary/terms.md
---

# Normalization

**Community:** [[Communities/34 Tensor · CUDA · Mixed Precision|34 Tensor · CUDA · Mixed Precision]]

> *What people say:* Scaling data to a standard range.

**What it actually means:** A family of transformations that rescale or recenter inputs, activations, or features using defined statistics. Batch normalization and layer normalization use different axes and behave differently across training and inference.

**Common confusion:** Normalization can improve optimization stability, but it does not always permit a larger learning rate or improve every architecture.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Function|Activation Function]]
- [[Concepts/Mixed Precision|Mixed Precision]]
- [[Concepts/Tensor|Tensor]]


%% ── my notes ── %%
