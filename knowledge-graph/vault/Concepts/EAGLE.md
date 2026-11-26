---
id: "concept:eagle"
type: concept
name: EAGLE
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
---

# EAGLE

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Hidden-state draft"

**What it actually means:** Tiny transformer draft conditioned on the verifier's last-layer hidden states.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — A speculative decoding variant that trains a lightweight head on the target model's own hidden states, achieving higher acceptance rates than a separate draft model


%% ── my notes ── %%
