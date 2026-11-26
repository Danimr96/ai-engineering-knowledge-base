---
id: "concept:precision-and-recall"
type: concept
name: "Precision & Recall"
canonical: true
category: "Evaluation & safety"
taught_in: 0
tags:
  - concept/glossary
  - category/evaluation-and-safety
source: ai-engineering-from-scratch/glossary/terms.md
---

# Precision & Recall

> *What people say:* Two metrics for classification or retrieval quality.

**What it actually means:** Precision asks how many flagged items were correct; recall asks how many relevant items were found. When you change the decision threshold for one fixed scoring model, improving recall often lowers precision and vice versa. A better model can improve both. F1 is their harmonic mean.

**Common confusion:** The right threshold and metric depend on the cost of each error and the prevalence of the target class.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Calibration|Calibration]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[Concepts/Recall@K|Recall@K]]
- [[Concepts/ROUGE|ROUGE]]
- [[Concepts/Semantic Search|Semantic Search]]


%% ── my notes ── %%
