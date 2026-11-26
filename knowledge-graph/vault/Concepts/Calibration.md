---
id: "concept:calibration"
type: concept
name: Calibration
canonical: true
category: "Evaluation & safety"
taught_in: 2
community: 5
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Calibration

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** The agreement between a system's stated confidence and the observed frequency with which predictions at that confidence are correct.

**Why it matters:** A system can be accurate on average yet dangerously overconfident on the cases where people rely on its score.

**In practice:** Bucket predictions by confidence, compare confidence with empirical accuracy, and recalibrate or abstain when the gap is unacceptable.

**Common confusion:** Calibration measures confidence reliability, not overall accuracy, factuality, or reasoning quality.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Logits|Logits]]
- [[Concepts/Precision & Recall|Precision & Recall]]
- [[Concepts/Softmax|Softmax]]

## Taught in

- [[Lessons/05-27 LLM Evaluation — RAGAS, DeepEval, G-Eval|05/27 LLM Evaluation — RAGAS, DeepEval, G-Eval]] — Spearman correlation between judge score and human score.
- [[Lessons/19-84 Capstone 84 — Refusal Evaluation|19/84 Capstone 84 — Refusal Evaluation]] — the gap between stated confidence and observed accuracy, summarized by Expected Calibration Error

## Sources

- On Calibration of Modern Neural Networks ([link](https://proceedings.mlr.press/v70/guo17a.html))


%% ── my notes ── %%
