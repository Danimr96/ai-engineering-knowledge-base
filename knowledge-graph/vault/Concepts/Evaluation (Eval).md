---
id: "concept:evaluation-eval"
type: concept
name: Evaluation (Eval)
canonical: true
category: "Evaluation & safety"
aliases:
  - Eval
taught_in: 3
community: 30
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/30
source: ai-engineering-from-scratch/glossary/terms.md
---

# Evaluation (Eval)

**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]]

**What it actually means:** A defined process for measuring model or system behavior on representative tasks using explicit success criteria, data, scorers, and review procedures.

**Why it matters:** You cannot improve reliability if success is only a subjective impression from a few demos.

**In practice:** Run the same customer-support scenarios before and after changing retrieval, score correctness and citation support, and inspect failures by category.

**Common confusion:** A benchmark score is one evaluation result, not a complete account of production quality.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Alignment|Alignment]]
- [[Concepts/Calibration|Calibration]]
- [[Concepts/Canary Release|Canary Release]]
- [[Concepts/Chain of Thought (CoT)|Chain of Thought (CoT)]]
- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Late Fusion|Late Fusion]]
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[Concepts/Loss Function|Loss Function]]
- [[Concepts/Model Router|Model Router]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Perplexity|Perplexity]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/ROUGE|ROUGE]]
- [[Concepts/Shadow Traffic|Shadow Traffic]]
- [[Concepts/Trace|Trace]]
- [[Concepts/Visual Grounding|Visual Grounding]]

## Taught in

- [[Lessons/11-10 Evaluation & Testing LLM Applications|11/10 Evaluation & Testing LLM Applications]] — Systematically scoring LLM outputs against defined criteria using automated metrics, LLM judges, or human review
- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] `alias` — Running candidate model/prompt over labeled dataset
- [[Lessons/17-21 A-B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem|17/21 A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem]] `alias` — Labeled-set evaluation of model capability


%% ── my notes ── %%
