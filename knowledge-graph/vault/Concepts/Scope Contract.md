---
id: "concept:scope-contract"
type: concept
name: Scope Contract
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

# Scope Contract

**Community:** [[Communities/36 Scope Contract · Coding Agent · Worktree|36 Scope Contract · Coding Agent · Worktree]]

**What it actually means:** A concrete agreement that defines a task's goal, allowed and forbidden surfaces, expected artifacts, verification requirements, and stopping conditions.

**Why it matters:** It prevents an agent from turning a narrow fix into an unreviewable refactor or from claiming completion without evidence.

**In practice:** State that only the parser module and its tests may change, public APIs must remain compatible, and the named test suite must pass.

**Common confusion:** A task description says what you want. A scope contract also defines boundaries and proof.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Delegation|Delegation]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Patch|Patch]]
- [[Concepts/Repository Instructions|Repository Instructions]]
- [[Concepts/Repository Map|Repository Map]]
- [[Concepts/Reviewer Agent|Reviewer Agent]]
- [[Concepts/Verification Gate|Verification Gate]]
- [[Concepts/Worktree|Worktree]]

## Taught in

- [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]] — Per-task JSON listing allowed/forbidden files, acceptance, rollback


%% ── my notes ── %%
