---
id: "concept:kv-rollback"
type: concept
name: KV rollback
canonical: false
taught_in: 2
community: 20
tags:
  - concept/lesson-term
  - community/20
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
---

# KV rollback

**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]]

> *What people say:* "Undo rejected drafts"

**What it actually means:** Scratch KV buffer; commit on acceptance, discard on reject.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — Bookkeeping that resets the verifier's KV cache to the accepted-prefix length after a rejection


%% ── my notes ── %%
