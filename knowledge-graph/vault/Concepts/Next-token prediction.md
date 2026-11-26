---
id: "concept:next-token-prediction"
type: concept
name: Next-token prediction
canonical: false
taught_in: 2
tags:
  - concept/lesson-term
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/en.md
---

# Next-token prediction

> *What people say:* "The loss"

**What it actually means:** Cross-entropy of the model's distribution against the true next token at every position.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- [[Lessons/12-12 Emu3- Next-Token Prediction for Image and Video Generation|12/12 Emu3: Next-Token Prediction for Image and Video Generation]] — Standard autoregressive loss: predict token[i+1] given token[0..i]; works for every modality when tokenized


%% ── my notes ── %%
