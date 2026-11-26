---
id: "concept:pass-k"
type: concept
name: "Pass@k"
canonical: true
category: "Evaluation & safety"
taught_in: 0
community: 24
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Pass@k

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** Across a task set, the fraction of tasks for which at least one of k sampled candidates passes a defined correctness test.

**Why it matters:** It measures the value of sampling several attempts for tasks such as code generation where an automatic verifier can check each candidate.

**In practice:** Generate candidates independently under a fixed configuration, run the same isolated tests on each, and report k with the sampling and estimator details.

**Common confusion:** Pass@k is not single-attempt accuracy, and a higher score can reflect a larger attempt budget rather than a better first answer.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Exact Match (EM)|Exact Match (EM)]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Test Oracle|Test Oracle]]

## Sources

- Evaluating Large Language Models Trained on Code ([link](https://arxiv.org/abs/2107.03374))


%% ── my notes ── %%
