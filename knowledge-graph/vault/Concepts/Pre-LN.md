---
id: "concept:pre-ln"
type: concept
name: Pre-LN
canonical: false
taught_in: 3
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/04-computer-vision/14-vision-transformers/docs/en.md
---

# Pre-LN

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "LayerNorm before sublayer"

**What it actually means:** The stable transformer variant: x + sublayer(LN(x)) instead of LN(x + sublayer(x))

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]
- [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]] — LayerNorm inside the residual branch, before each sublayer; the residual carries the unnormalized signal
- [[Lessons/19-59 Vision Transformer Encoder|19/59 Vision Transformer Encoder]] — LayerNorm applied before each sub-layer instead of after


%% ── my notes ── %%
