---
id: "concept:planning"
type: concept
name: Planning
canonical: true
category: "Agents & tools"
taught_in: 0
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Planning

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** Constructing, selecting, or revising a sequence of actions and dependencies intended to move from the current state to a goal.

**Why it matters:** Explicit plans make assumptions and ordering visible before an agent commits to expensive or irreversible actions.

**In practice:** Ask for a short dependency-aware plan, validate it against available tools and permissions, then re-plan when observations invalidate an assumption.

**Common confusion:** A generated plan is a proposal, not proof that the steps are feasible, sufficient, or safe.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Orchestration|Orchestration]]
- [[Concepts/ReAct|ReAct]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- LLM+P ([link](https://arxiv.org/abs/2304.11477))


%% ── my notes ── %%
