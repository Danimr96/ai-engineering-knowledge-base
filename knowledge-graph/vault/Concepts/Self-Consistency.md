---
id: "concept:self-consistency"
type: concept
name: Self-Consistency
canonical: false
taught_in: 2
community: 42
tags:
  - concept/lesson-term
  - community/42
source: ai-engineering-from-scratch/phases/11-llm-engineering/02-few-shot-cot/docs/en.md
---

# Self-Consistency

**Community:** [[Communities/42 Few-Shot · Prompt Engineering · In-Context Learning|42 Few-Shot · Prompt Engineering · In-Context Learning]]

> *What people say:* "Run it multiple times"

**What it actually means:** Sampling N diverse reasoning paths at temperature > 0 and selecting the most common final answer by majority vote

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]]
- [[Lessons/16-15 Voting, Self-Consistency, and Debate Topology|16/15 Voting, Self-Consistency, and Debate Topology]] — Wang 2022. Single model, N temperature>0 samples, majority vote on reasoning paths.


%% ── my notes ── %%
