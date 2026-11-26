---
id: "concept:termination-condition"
type: concept
name: Termination Condition
canonical: true
category: "Agents & tools"
taught_in: 0
community: 24
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Termination Condition

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** An explicit rule that ends or pauses an agent run when it succeeds, fails, exhausts a budget, reaches a safe boundary, or requires escalation.

**Why it matters:** Without a termination condition, an agent can loop, repeat side effects, waste budget, or claim completion without satisfying the goal.

**In practice:** Define success evidence, maximum steps and cost, non-retryable errors, and escalation states before starting the loop.

**Common confusion:** A stop sequence ends text generation; a termination condition decides whether the task or workflow should stop.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Stop Sequence|Stop Sequence]]
- [[Concepts/Token Budget|Token Budget]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- [[Resources/AutoGen|AutoGen]] ([link](https://arxiv.org/abs/2308.08155))


%% ── my notes ── %%
