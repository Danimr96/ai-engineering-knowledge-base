---
id: "concept:router"
type: concept
name: Router
canonical: false
taught_in: 3
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/11-mixture-of-experts/docs/en.md
---

# Router

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* "The gate"

**What it actually means:** A tiny linear layer that scores each token against each expert; top-k selection.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]]
- [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]] — Short root file that points the agent at deeper docs and files
- [[Lessons/19-85 Capstone 85 — Content Classifier Integration|19/85 Capstone 85 — Content Classifier Integration]] — a function from verdict list to action (block, redact, warn, log)


%% ── my notes ── %%
