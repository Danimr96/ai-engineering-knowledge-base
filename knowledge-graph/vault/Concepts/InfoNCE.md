---
id: "concept:infonce"
type: concept
name: InfoNCE
canonical: false
taught_in: 4
community: 40
tags:
  - concept/lesson-term
  - community/40
source: ai-engineering-from-scratch/phases/03-deep-learning-core/05-loss-functions/docs/en.md
---

# InfoNCE

**Community:** [[Communities/40 NaFlex · Backbone · Hard negative|40 NaFlex · Backbone · Hard negative]]

> *What people say:* "The CLIP/SimCLR loss"

**What it actually means:** Normalized temperature-scaled cross-entropy over similarity scores; treats contrastive learning as classification

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]]
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]] — softmax over cosine similarities; positive pair is the target class, all others are negatives
- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]] — Cross-entropy over a batch's similarity matrix; each item's positive is its paired item, negatives are everything else
- [[Lessons/19-62 Vision-Language Pretraining|19/62 Vision-Language Pretraining]] — Noise contrastive estimation: cross-entropy on a similarity matrix


%% ── my notes ── %%
