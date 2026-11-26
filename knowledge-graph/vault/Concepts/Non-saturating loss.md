---
id: "concept:non-saturating-loss"
type: concept
name: Non-saturating loss
canonical: false
taught_in: 2
community: 37
tags:
  - concept/lesson-term
  - community/37
source: ai-engineering-from-scratch/phases/04-computer-vision/09-image-generation-gans/docs/en.md
---

# Non-saturating loss

**Community:** [[Communities/37 Discriminator · Generator · Minimax|37 Discriminator · Generator · Minimax]]

> *What people say:* "The numerically sane version"

**What it actually means:** G's loss is -log(D(G(z))) instead of log(1 - D(G(z))) to avoid vanishing gradients early in training

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]] — Use -log D(G(z)) for G instead of log(1 - D(G(z))).


%% ── my notes ── %%
