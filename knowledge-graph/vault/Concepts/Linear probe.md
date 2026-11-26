---
id: "concept:linear-probe"
type: concept
name: Linear probe
canonical: false
taught_in: 3
community: 13
tags:
  - concept/lesson-term
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/05-transfer-learning/docs/en.md
---

# Linear probe

**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]]

> *What people say:* "Frozen backbone + linear head"

**What it actually means:** Evaluation of pretrained features — accuracy of the best linear classifier on top of the frozen representation

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- [[Lessons/04-17 Self-Supervised Vision — SimCLR, DINO, MAE|04/17 Self-Supervised Vision — SimCLR, DINO, MAE]] — Standard SSL evaluation: train only a linear classifier on top of frozen features
- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]] — Train only a linear classifier on top of frozen features; measures feature quality


%% ── my notes ── %%
