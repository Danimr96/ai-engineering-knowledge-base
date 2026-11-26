---
id: "concept:baseline"
type: concept
name: Baseline
canonical: false
taught_in: 3
community: 33
tags:
  - concept/lesson-term
  - community/33
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/06-policy-gradients-reinforce/docs/en.md
---

# Baseline

**Community:** [[Communities/33 Advantage · Baseline · Actor|33 Advantage · Baseline · Actor]]

> *What people say:* "Variance reduction"

**What it actually means:** Any b(s) subtracted from G; unbiased because E[b · ∇ log π] = 0.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]]
- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]] — The same model, tools, task, and budget under the comparison condition
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]] — Reference score to detect regression


%% ── my notes ── %%
