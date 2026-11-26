---
id: "concept:eval-set"
type: concept
name: Eval Set
canonical: true
category: "Evaluation & safety"
aliases:
  - Evaluation set
taught_in: 1
community: 24
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Eval Set

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A versioned collection of inputs, expected properties, scoring rules, and metadata used to measure an AI system against a defined capability or risk.

**Why it matters:** A repeatable set turns vague quality claims into comparable evidence and catches regressions after prompts, models, tools, or retrieval change.

**In practice:** Keep representative support questions, adversarial instructions, expected citations, and failure labels in a reviewed dataset that is separate from development examples.

**Common confusion:** A development eval guides iteration, a final held-out test estimates performance after choices are fixed, and a standardized benchmark supports comparison under a shared protocol. Repeated tuning against any held-out set leaks test information and inflates results.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Benchmark Contamination|Benchmark Contamination]]
- [[Concepts/Data Augmentation|Data Augmentation]]
- [[Concepts/Data Leakage|Data Leakage]]
- [[Concepts/Dataset Split|Dataset Split]]
- [[Concepts/Distribution Shift|Distribution Shift]]
- [[Concepts/Epoch|Epoch]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Exact Match (EM)|Exact Match (EM)]]
- [[Concepts/Jailbreak|Jailbreak]]
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[Concepts/Lost in the Middle|Lost in the Middle]]
- [[Concepts/Membership Inference|Membership Inference]]
- [[Concepts/Model Card|Model Card]]
- [[Concepts/Overfitting|Overfitting]]
- [[Concepts/Pass@k|Pass@k]]
- [[Concepts/Precision & Recall|Precision & Recall]]
- [[Concepts/Prompt Sensitivity|Prompt Sensitivity]]
- [[Concepts/Recall@K|Recall@K]]
- [[Concepts/Red Teaming|Red Teaming]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Test Oracle|Test Oracle]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]


%% ── my notes ── %%
