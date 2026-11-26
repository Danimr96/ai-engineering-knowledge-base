---
id: "concept:mode-collapse"
type: concept
name: Mode collapse
canonical: false
taught_in: 3
community: 37
tags:
  - concept/lesson-term
  - community/37
source: ai-engineering-from-scratch/phases/04-computer-vision/09-image-generation-gans/docs/en.md
---

# Mode collapse

**Community:** [[Communities/37 Discriminator · Generator · Minimax|37 Discriminator · Generator · Minimax]]

> *What people say:* "Generator makes one thing"

**What it actually means:** G produces only a small subset of the data distribution; fix with SN, minibatch discrimination, or larger batch

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-09 Image Generation — GANs|04/09 Image Generation — GANs]]
- [[Lessons/08-03 GANs — Generator vs Discriminator|08/03 GANs — Generator vs Discriminator]] — Generator produces few distinct outputs despite diverse data.
- [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]] — Post-training policy concentrates on a narrow region of the response space; measured as falling reward std across a group


%% ── my notes ── %%
