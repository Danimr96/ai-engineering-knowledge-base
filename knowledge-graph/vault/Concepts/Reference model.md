---
id: "concept:reference-model"
type: concept
name: Reference model
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/07-rlhf/docs/en.md
---

# Reference model

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "The frozen SFT checkpoint"

**What it actually means:** A copy of the SFT model whose weights never change -- used as the anchor for KL divergence computation

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]]
- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]] — A copy of the SFT model whose weights never change -- serves as the anchor for computing probability ratios


%% ── my notes ── %%
