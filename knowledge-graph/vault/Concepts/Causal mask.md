---
id: "concept:causal-mask"
type: concept
name: Causal mask
canonical: false
taught_in: 4
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/en.md
---

# Causal mask

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "The triangle"

**What it actually means:** Upper-triangular -inf matrix added to attention scores so position i only sees positions ≤ i.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]]
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — An upper-triangular matrix of -infinity values that prevents attention to future positions during training
- [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]] — The upper triangle of the attention logits set to negative infinity so token i cannot read token j when j is greater than i
- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]] — Lower-triangular boolean mask that prevents looking ahead during autoregression


%% ── my notes ── %%
