---
id: "concept:regression-test"
type: concept
name: Regression Test
canonical: true
category: AI-native development
taught_in: 1
community: 24
tags:
  - concept/glossary
  - category/ai-native-development
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Regression Test

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A repeatable check that protects behavior known to work, especially after code, prompt, model, retrieval, or tool changes.

**Why it matters:** AI system changes can improve average quality while silently reintroducing a previously fixed failure.

**In practice:** Turn a corrected prompt-injection incident into a permanent eval case that must pass before the next deployment.

**Common confusion:** A regression test guards a specific expected behavior. A broad benchmark estimates performance across a wider task distribution.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Flaky Test|Flaky Test]]
- [[Concepts/Pass@k|Pass@k]]
- [[Concepts/Patch|Patch]]
- [[Concepts/Postmortem|Postmortem]]
- [[Concepts/Prompt Sensitivity|Prompt Sensitivity]]
- [[Concepts/Rollback|Rollback]]
- [[Concepts/Test Oracle|Test Oracle]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]


%% ── my notes ── %%
