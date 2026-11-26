---
id: "concept:dataset-split"
type: concept
name: Dataset Split
canonical: true
category: "Data & representations"
taught_in: 1
community: 43
tags:
  - concept/glossary
  - category/data-and-representations
  - community/43
source: ai-engineering-from-scratch/glossary/terms.md
---

# Dataset Split

**Community:** [[Communities/43 Data Provenance · Dataset Split · Datasheet for Datasets|43 Data Provenance · Dataset Split · Datasheet for Datasets]]

**What it actually means:** A documented partition of examples into separate subsets for fitting, development decisions, and final evaluation.

**Why it matters:** Separation prevents the evidence used to choose a system from also serving as independent proof that the chosen system generalizes.

**In practice:** Split by the real deployment unit, such as user, repository, organization, or time, rather than randomly dividing correlated rows.

**Common confusion:** A random split is not automatically independent. Near duplicates, future observations, or records from the same entity can cross the boundary.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Data Deduplication|Data Deduplication]]
- [[Concepts/Data Leakage|Data Leakage]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Datasheet for Datasets|Datasheet for Datasets]]
- [[Concepts/Distribution Shift|Distribution Shift]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Model Card|Model Card]]
- [[Concepts/Overfitting|Overfitting]]

## Taught in

- [[Lessons/00-09 Data Management|00/09 Data Management]] — A named subset (train/val/test) used at different stages of the ML lifecycle

## Sources

- Datasheets for Datasets ([link](https://cacm.acm.org/research/datasheets-for-datasets/))


%% ── my notes ── %%
