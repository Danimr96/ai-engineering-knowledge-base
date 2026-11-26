---
id: "concept:adamw"
type: concept
name: AdamW
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

# AdamW

**Community:** [[Communities/11 Learning Rate · Optimizer · Batch Size|11 Learning Rate · Optimizer · Batch Size]]

> *What people say:* Adam with weight decay fixed.

**What it actually means:** An Adam variant that decouples weight decay from the gradient-based parameter update. That makes the shrinkage behavior easier to reason about than adding an L2 penalty inside Adam's adaptively scaled gradient.

**Common confusion:** Decoupled weight decay does not make AdamW universally optimal. Model, data, and training scale still determine the best optimizer and schedule.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Adam (Optimizer)|Adam (Optimizer)]]
- [[Concepts/Optimizer|Optimizer]]
- [[Concepts/Warmup|Warmup]]
- [[Concepts/Weight Decay|Weight Decay]]

## Taught in

- [[Lessons/03-06 Optimizers|03/06 Optimizers]] — Adam with decoupled weight decay; applies regularization directly to weights rather than through the gradient

## Sources

- Decoupled Weight Decay Regularization ([link](https://arxiv.org/abs/1711.05101))


%% ── my notes ── %%
