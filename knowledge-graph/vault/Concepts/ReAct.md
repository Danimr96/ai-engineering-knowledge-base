---
id: "concept:react"
type: concept
name: ReAct
canonical: true
category: "Agents & tools"
taught_in: 2
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# ReAct

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** An agent pattern that interleaves task reasoning, a concrete action, and an observation returned by the environment before deciding the next step.

**Why it matters:** Environment feedback can correct assumptions and ground later decisions instead of forcing the model to complete the entire task from internal generation alone.

**In practice:** Expose a small set of typed tools, return concise observations, cap the loop, and verify the final artifact rather than storing private reasoning traces.

**Common confusion:** ReAct is a prompting and control pattern, not a guarantee of autonomy, correctness, or safe tool use.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/Function Calling|Function Calling]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Planning|Planning]]

## Taught in

- [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]] — Interleaving reasoning traces with external actions (search, compute, API calls) in a Thought-Action-Observation loop
- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Yao et al. 2022 — interleave Thought, Action, Observation in one stream

## Sources

- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629))


%% ── my notes ── %%
