---
id: "concept:label-smoothing"
type: concept
name: Label smoothing
canonical: false
taught_in: 2
community: 22
tags:
  - concept/lesson-term
  - community/22
source: ai-engineering-from-scratch/phases/03-deep-learning-core/05-loss-functions/docs/en.md
---

# Label smoothing

**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]]

> *What people say:* "Softening the targets"

**What it actually means:** Replacing hard 0/1 targets with soft values (e.g., 0.1/0.9) to prevent overconfidence and improve generalization

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Replace one-hot with (1-eps, eps/(C-1), ...); improves calibration and slightly boosts accuracy


%% ── my notes ── %%
