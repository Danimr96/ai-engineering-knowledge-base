---
id: "concept:reviewer-agent"
type: concept
name: Reviewer Agent
canonical: true
category: AI-native development
taught_in: 1
community: 36
tags:
  - concept/glossary
  - category/ai-native-development
  - community/36
source: ai-engineering-from-scratch/glossary/terms.md
---

# Reviewer Agent

**Community:** [[Communities/36 Scope Contract · Coding Agent · Worktree|36 Scope Contract · Coding Agent · Worktree]]

**What it actually means:** An agent assigned to inspect another agent's artifact or decision against explicit criteria and return findings or a verdict.

**Why it matters:** Separation of roles can catch omissions, but it only helps when the reviewer receives independent evidence and a concrete rubric.

**In practice:** After one agent produces a patch, give a separate reviewer the diff, scope contract, repository rules, and test output, then require line-specific findings.

**Common confusion:** A second model call is not automatically independent or correct. Shared context, model bias, and vague criteria can reproduce the same mistake.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Delegation|Delegation]]
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[Concepts/Scope Contract|Scope Contract]]
- [[Concepts/Separation of Duties|Separation of Duties]]
- [[Concepts/Swarm|Swarm]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]]


%% ── my notes ── %%
