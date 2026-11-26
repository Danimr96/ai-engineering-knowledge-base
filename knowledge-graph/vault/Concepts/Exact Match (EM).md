---
id: "concept:exact-match-em"
type: concept
name: Exact Match (EM)
canonical: true
category: "Evaluation & safety"
taught_in: 1
community: 24
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Exact Match (EM)

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A metric that counts an output as correct only when its normalized representation exactly equals an accepted reference answer.

**Why it matters:** It is deterministic and easy to audit for tasks with one canonical answer, but it exposes no partial credit.

**In practice:** Define normalization and all accepted references before evaluation, then pair exact match with task-specific checks when several outputs can be valid.

**Common confusion:** A low exact-match score can reflect harmless formatting differences, while a matching string can still be unsupported or unsafe in context.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Benchmark Contamination|Benchmark Contamination]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Pass@k|Pass@k]]
- [[Concepts/ROUGE|ROUGE]]
- [[Concepts/Structured Output|Structured Output]]

## Taught in

- [[Lessons/19-63 Multimodal Evaluation|19/63 Multimodal Evaluation]] `alias` — The simplest VQA scoring: predicted answer equals reference

## Sources

- SQuAD ([link](https://aclanthology.org/D16-1264/))


%% ── my notes ── %%
