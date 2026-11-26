---
id: "concept:batch-size"
type: concept
name: Batch Size
canonical: true
category: "Math & training"
taught_in: 0
community: 11
tags:
  - concept/glossary
  - category/math-and-training
  - community/11
source: ai-engineering-from-scratch/glossary/terms.md
---

# Batch Size

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* How many examples are processed at once.

**What it actually means:** The number of examples whose losses contribute to one gradient estimate before an optimizer update. Larger batches can improve hardware utilization and reduce gradient noise, but they require more memory and may need different learning-rate or scheduling choices.

**Common confusion:** There is no universal batch-size range or rule that says every batch increase should produce the same learning-rate increase.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Epoch|Epoch]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/Gradient Accumulation|Gradient Accumulation]]
- [[Concepts/Hyperparameter|Hyperparameter]]
- [[Concepts/Learning Rate|Learning Rate]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]]
- [[Concepts/Stochastic Gradient Descent (SGD)|Stochastic Gradient Descent (SGD)]]
- [[Concepts/Warmup|Warmup]]


%% ── my notes ── %%
