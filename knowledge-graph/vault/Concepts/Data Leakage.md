---
id: "concept:data-leakage"
type: concept
name: Data Leakage
canonical: true
category: "Data & representations"
taught_in: 4
community: 4
tags:
  - concept/glossary
  - category/data-and-representations
  - community/04
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Leakage

**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]]

**What it actually means:** Unintended use of information during training or feature construction that would not be available at the real prediction point or belongs to a held-out evaluation boundary.

**Why it matters:** Leakage produces optimistic metrics that collapse when the system encounters genuinely unseen inputs.

**In practice:** Split data before fitting preprocessors, keep future information out of historical features, and isolate test labels and benchmark answers from prompts and tuning loops.

**Common confusion:** Leakage is not limited to duplicate rows. Global normalization statistics, timestamps, target-derived features, and repeated test-driven prompt edits can all leak information.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Benchmark Contamination|Benchmark Contamination]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Dataset Split|Dataset Split]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Membership Inference|Membership Inference]]

## Taught in

- [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]] — Using information during training that would not be available at prediction time, giving falsely optimistic results
- [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]] — Using information during training that would not be available at prediction time, leading to optimistic evaluation
- [[Lessons/02-13 ML Pipelines|02/13 ML Pipelines]] — Using information from outside the training set to build the model, inflating performance estimates
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]] — When information from the test set contaminates training, producing artificially high accuracy

## Sources

- scikit-learn: Data leakage ([link](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage))


%% ── my notes ── %%
