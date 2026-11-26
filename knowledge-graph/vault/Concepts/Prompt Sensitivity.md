---
id: "concept:prompt-sensitivity"
type: concept
name: Prompt Sensitivity
canonical: true
category: "Prompting & context"
taught_in: 0
community: 24
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Prompt Sensitivity

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** Variation in model output or measured performance caused by changes to prompt wording, order, formatting, or examples that preserve the intended task.

**Why it matters:** A system that succeeds under one convenient phrasing may be unreliable for real users or misleading in evaluation.

**In practice:** Create semantically equivalent prompt variants, measure variance by case, and keep variants in regression tests instead of optimizing one prompt against one eval set.

**Common confusion:** Sensitivity is not always a prompt defect; it can reveal ambiguity, weak model robustness, unstable decoding, or an inadequate scoring rule.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Few-Shot|Few-Shot]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Regression Test|Regression Test]]

## Sources

- ProSA ([link](https://aclanthology.org/2024.findings-emnlp.108/))


%% ── my notes ── %%
