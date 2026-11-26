---
id: "concept:multi-head-attention"
type: concept
name: Multi-head attention
canonical: false
taught_in: 3
community: 12
tags:
  - concept/lesson-term
  - community/12
source: ai-engineering-from-scratch/phases/04-computer-vision/14-vision-transformers/docs/en.md
---

# Multi-head attention

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

> *What people say:* "Parallel attention"

**What it actually means:** Standard transformer attention split into num_heads independent subspaces, concatenated afterwards

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]
- [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]] — Running multiple attention functions with different projections, then concatenating results for richer representations
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Splitting Q, K, V into parallel heads (e.g., 12 heads of 64 dims each for GPT-2) so each head can learn different relationship types


%% ── my notes ── %%
