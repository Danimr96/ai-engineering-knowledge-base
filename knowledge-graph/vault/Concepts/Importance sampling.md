---
id: "concept:importance-sampling"
type: concept
name: Importance sampling
canonical: false
taught_in: 2
community: 49
tags:
  - concept/lesson-term
  - community/49
source: ai-engineering-from-scratch/phases/01-math-foundations/16-sampling-methods/docs/en.md
---

# Importance sampling

**Community:** [[Communities/49 MCMC · Metropolis-Hastings · Importance sampling|49 MCMC · Metropolis-Hastings · Importance sampling]]

> *What people say:* "Reweight samples"

**What it actually means:** Estimate expectations under p(x) using samples from q(x) by weighting each sample by p(x)/q(x). Core to PPO in RL

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]]
- [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]] — Reweight returns by π(a|s)/μ(a|s) products to estimate V^π from μ data.


%% ── my notes ── %%
