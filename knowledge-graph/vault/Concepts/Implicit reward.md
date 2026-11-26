---
id: "concept:implicit-reward"
type: concept
name: Implicit reward
canonical: false
taught_in: 2
community: 45
tags:
  - concept/lesson-term
  - community/45
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/08-dpo/docs/en.md
---

# Implicit reward

**Community:** [[Communities/45 Implicit reward · KTO · ORPO|45 Implicit reward · KTO · ORPO]]

> *What people say:* "The reward is in the model"

**What it actually means:** The reward function is determined by the log-probability ratio between the policy and reference models -- no separate reward model needed

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]] — beta log(pi(y|x) / pi_ref(y|x)) — the DPO-implied reward


%% ── my notes ── %%
