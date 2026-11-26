---
id: "concept:canary-release"
type: concept
name: Canary Release
canonical: true
category: "Reliability & operations"
taught_in: 2
community: 46
tags:
  - concept/glossary
  - category/reliability-and-operations
  - community/46
source: ai-engineering-from-scratch/glossary/terms.md
---

# Canary Release

**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]]

**What it actually means:** A deployment strategy that exposes a new version to a limited slice of traffic or infrastructure before expanding the rollout.

**Why it matters:** It limits the impact of defects and gives you production evidence before the new model, prompt, agent, or service reaches everyone.

**In practice:** Route a small eligible cohort to the release, compare quality and operational metrics with the control, and stop or roll back on predefined failures.

**Common confusion:** A canary release limits exposure; it does not replace pre-deployment tests, approval, or rollback preparation.

**Category:** [[Categories/Reliability & operations|Reliability & operations]]

## Related concepts

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Rollback|Rollback]]
- [[Concepts/Shadow Traffic|Shadow Traffic]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]] `alias` — Gradual user-exposed rollout with gates
- [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]] `alias` — Unique training example used to measure DP leakage

## Sources

- Kubernetes Deployments: Canary Deployment ([link](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#canary-deployment))


%% ── my notes ── %%
