---
id: "concept:membership-inference"
type: concept
name: Membership Inference
canonical: true
category: "Security & governance"
taught_in: 1
community: 65
tags:
  - concept/glossary
  - category/security-and-governance
  - community/65
source: ai-engineering-from-scratch/glossary/terms.md
---

# Membership Inference

**Community:** [[Communities/65 Data Classification · Data Minimization · Purpose Limitation|65 Data Classification · Data Minimization · Purpose Limitation]]

**What it actually means:** An attack that estimates whether a particular record or example was included in a model's training data by observing model outputs or other accessible signals.

**Why it matters:** Even when the model does not reproduce a record verbatim, distinguishable behavior can reveal information about participation in a sensitive dataset.

**In practice:** Test representative members and non-members under the real query interface, limit unnecessary confidence signals, reduce data exposure, and evaluate privacy defenses against utility requirements.

**Common confusion:** Membership inference asks whether a record participated in training. Model extraction tries to reproduce model behavior, while direct memorization tests whether content can be recovered.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Data Classification|Data Classification]]
- [[Concepts/Data Leakage|Data Leakage]]
- [[Concepts/Data Minimization|Data Minimization]]
- [[Concepts/Eval Set|Eval Set]]

## Taught in

- [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]]

## Sources

- Membership Inference Attacks Against Machine Learning Models ([link](https://doi.org/10.1109/SP.2017.41))


%% ── my notes ── %%
