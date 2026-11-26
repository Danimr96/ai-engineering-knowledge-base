---
id: "concept:distribution-shift"
type: concept
name: Distribution Shift
canonical: true
category: "Evaluation & safety"
taught_in: 0
community: 43
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/43
source: ai-engineering-from-scratch/glossary/terms.md
---

# Distribution Shift

**Community:** [[Communities/43 Data Provenance · Dataset Split · Datasheet for Datasets|43 Data Provenance · Dataset Split · Datasheet for Datasets]]

**What it actually means:** A difference between the data distribution used to build or evaluate a system and the distribution it encounters after deployment.

**Why it matters:** A model can pass held-out tests yet fail when users, tasks, language, tools, or operating conditions change.

**In practice:** Define expected deployment slices, monitor performance and input characteristics by slice, and add new failures to a versioned eval set.

**Common confusion:** Distribution shift is not always model drift. The model may be unchanged while its environment or user population changes.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Dataset Split|Dataset Split]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Model Card|Model Card]]
- [[Concepts/Overfitting|Overfitting]]

## Sources

- WILDS ([link](https://proceedings.mlr.press/v139/koh21a.html))


%% ── my notes ── %%
