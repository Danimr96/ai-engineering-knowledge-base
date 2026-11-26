---
id: "concept:beam-search"
type: concept
name: Beam search
canonical: false
taught_in: 2
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/en.md
---

# Beam search

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* Better decoding

**What it actually means:** Keep top-k partial sequences alive at each step instead of committing greedily.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]] — Keep top-k partial sequences at each step; standard for translation/summarization.


%% ── my notes ── %%
