---
id: "concept:teacher-forcing"
type: concept
name: Teacher forcing
canonical: false
taught_in: 3
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/en.md
---

# Teacher forcing

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* Use true tokens

**What it actually means:** Feed the ground-truth previous token at training time. Stabilizes learning.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — During training, feed the true previous token, not the model's prediction. Standard for every seq2seq LM.
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]] — During training, feed the true previous output token to the decoder, not the sampled one.


%% ── my notes ── %%
