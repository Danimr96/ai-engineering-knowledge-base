---
id: "concept:dualpipe"
type: concept
name: DualPipe
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/19-dualpipe-parallelism/docs/en.md
---

# DualPipe

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "DeepSeek-V3 schedule"

**What it actually means:** Bidirectional pipeline + compute-comm overlap; bubbles do not grow with micro-batch count

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]]
- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]] — Training schedule that overlaps forward/backward compute with cross-node all-to-all


%% ── my notes ── %%
