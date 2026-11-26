---
id: "concept:sharded-checkpoint"
type: concept
name: Sharded checkpoint
canonical: false
taught_in: 2
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/19-capstone-projects/47-checkpoint-save-resume/docs/en.md
---

# Sharded checkpoint

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "Big model file"

**What it actually means:** Multiple files, one per shard, plus a meta file and a JSON index with sha256s

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]]
- [[Lessons/19-80 Sharded Checkpoint and Atomic Resume|19/80 Sharded Checkpoint and Atomic Resume]] — Each rank writes its own shard file in parallel


%% ── my notes ── %%
