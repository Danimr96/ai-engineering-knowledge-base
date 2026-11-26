---
id: "concept:atomic-write"
type: concept
name: Atomic write
canonical: false
taught_in: 2
community: 15
tags:
  - concept/lesson-term
  - community/15
source: ai-engineering-from-scratch/phases/14-agent-engineering/34-repo-memory-and-state/docs/en.md
---

# Atomic write

**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]]

> *What people say:* "Just rename"

**What it actually means:** Write to temp, fsync, rename, so partial failures cannot corrupt

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
- [[Lessons/19-80 Sharded Checkpoint and Atomic Resume|19/80 Sharded Checkpoint and Atomic Resume]] — Write to .tmp then POSIX rename so a crash leaves the previous file live


%% ── my notes ── %%
