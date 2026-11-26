---
id: "concept:tree-attention"
type: concept
name: Tree attention
canonical: false
taught_in: 2
community: 20
tags:
  - concept/lesson-term
  - community/20
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
---

# Tree attention

**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]]

> *What people say:* "Verify many candidates at once"

**What it actually means:** Branching verification that considers several draft continuations simultaneously.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — Attention with a non-causal mask that respects the topology of a draft tree; computes q_i for every node in the tree in one forward pass


%% ── my notes ── %%
