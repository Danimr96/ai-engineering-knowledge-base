---
id: "concept:divided-attention"
type: concept
name: Divided attention
canonical: false
taught_in: 2
community: 13
tags:
  - concept/lesson-term
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/12-video-understanding/docs/en.md
---

# Divided attention

**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]]

> *What people say:* "Time then space"

**What it actually means:** Transformer block with two attentions per layer: one over tokens at the same frame, one over tokens at the same position

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-12 Video Understanding — Temporal Modeling|04/12 Video Understanding — Temporal Modeling]]
- [[Lessons/04-28 World Models & Video Diffusion|04/28 World Models & Video Diffusion]] — Two attention operations per block — across time then across space — to keep O(N^2) manageable


%% ── my notes ── %%
