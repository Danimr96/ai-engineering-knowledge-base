---
id: "concept:patch"
type: concept
name: Patch
canonical: true
category: AI-native development
taught_in: 5
community: 36
tags:
  - concept/glossary
  - category/ai-native-development
  - community/36
source: ai-engineering-from-scratch/glossary/terms.md
---

# Patch

**Community:** [[Communities/36 Scope Contract · Coding Agent · Worktree|36 Scope Contract · Coding Agent · Worktree]]

**What it actually means:** A reviewable representation of changes to one or more files, usually expressed as additions and deletions against a known base revision.

**Why it matters:** A patch gives people and agents a narrow artifact to inspect, test, apply, or reject without accepting an entire working directory.

**In practice:** Ask a coding agent to return a unified diff, then verify that it touches only allowed files and applies cleanly to the expected commit.

**Common confusion:** A patch captures file changes, not the reasoning, test evidence, or approval needed to ship them.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Scope Contract|Scope Contract]]
- [[Concepts/Worktree|Worktree]]

## Taught in

- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]] — Flat vector of pixel values for a P × P × C region of the image.
- [[Lessons/08-10 Video Generation|08/10 Video Generation]] `normalized` — Fixed-size 3-D blocks of the latent; input to the DiT.
- [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]] — A fixed-size non-overlapping region of the input image; becomes one token
- [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]
- [[Lessons/19-58 Vision Encoder Patches|19/58 Vision Encoder Patches]] — A square sub-region of the image, typically 14x14 or 16x16


%% ── my notes ── %%
