---
id: "concept:worktree"
type: concept
name: Worktree
canonical: true
category: AI-native development
taught_in: 2
community: 36
tags:
  - concept/glossary
  - category/ai-native-development
  - community/36
source: ai-engineering-from-scratch/glossary/terms.md
---

# Worktree

**Community:** [[Communities/36 Scope Contract · Coding Agent · Worktree|36 Scope Contract · Coding Agent · Worktree]]

**What it actually means:** In Git, a working directory attached to a repository and branch or commit, with shared object storage but its own checked-out files and index.

**Why it matters:** Separate worktrees let people and agents work concurrently without constantly switching or overwriting one checkout.

**In practice:** Give each coding agent a named feature branch and exact worktree path, then review and integrate patches through normal Git history.

**Common confusion:** A worktree isolates checked-out files, not every process, port, cache, database, or secret on the machine.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Patch|Patch]]
- [[Concepts/Scope Contract|Scope Contract]]

## Taught in

- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/19-01 Capstone 01 — Terminal-Native Coding Agent|19/01 Capstone 01 — Terminal-Native Coding Agent]] — A linked git checkout at a separate path; disposable without touching the main clone

## Sources

- git-worktree documentation ([link](https://git-scm.com/docs/git-worktree))


%% ── my notes ── %%
