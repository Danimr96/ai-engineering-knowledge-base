---
id: "concept:epoch"
type: concept
name: Epoch
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

# Epoch

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* One pass through the training data.

**What it actually means:** One traversal of the defined training dataset. In distributed or sampled training, the exact implementation of an epoch depends on the data loader and sampling policy.

**Common confusion:** More epochs do not guarantee better generalization; evaluate on held-out data.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Batch Size|Batch Size]]
- [[Concepts/Data Augmentation|Data Augmentation]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Learning Rate Schedule|Learning Rate Schedule]]
- [[Concepts/Overfitting|Overfitting]]


%% ── my notes ── %%
