---
id: "concept:llm-as-a-judge"
type: concept
name: LLM-as-a-Judge
canonical: true
category: "Evaluation & safety"
taught_in: 5
tags:
  - concept/glossary
  - category/evaluation-and-safety
source: ai-engineering-from-scratch/glossary/terms.md
---

# LLM-as-a-Judge

**What it actually means:** Using a language model to score, compare, classify, or critique another system's output against a rubric.

**Why it matters:** It can scale evaluation of qualities that are difficult to express as exact-match tests, such as clarity or instruction adherence.

**In practice:** Give a separate evaluator model the task, candidate answer, reference evidence, and a structured rubric, then calibrate its scores against human-reviewed examples.

**Common confusion:** A judge model is not ground truth. It can be biased by order, verbosity, style, prompt wording, or shared model failures.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Precision & Recall|Precision & Recall]]
- [[Concepts/Reviewer Agent|Reviewer Agent]]
- [[Concepts/ROUGE|ROUGE]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/05-27 LLM Evaluation — RAGAS, DeepEval, G-Eval|05/27 LLM Evaluation — RAGAS, DeepEval, G-Eval]] `alias` — Prompt a judge model to score outputs 0-1 given a rubric.
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]] `alias` — A strong model scores a weaker model's outputs against a rubric, ~80% agreement with human judges at ~$0.01/judgment
- [[Lessons/11-10 Evaluation & Testing LLM Applications|11/10 Evaluation & Testing LLM Applications]] `alias` — Using a strong model (GPT-4o, Claude) to score outputs against a rubric -- correlates 80-85% with human judgment
- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]] `alias` — Separate LLM scores agent output against a rubric
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]


%% ── my notes ── %%
