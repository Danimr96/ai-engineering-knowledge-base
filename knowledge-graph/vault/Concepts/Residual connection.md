---
id: "concept:residual-connection"
type: concept
name: Residual connection
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/en.md
---

# Residual connection

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Skip connection"

**What it actually means:** y = F(x) + x; lets the optimiser learn identity by setting F to zero, which makes arbitrary depth trainable

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]]
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Adding the input directly to the output of a sublayer (x + sublayer(x)) -- enables gradient flow in deep networks


%% ── my notes ── %%
