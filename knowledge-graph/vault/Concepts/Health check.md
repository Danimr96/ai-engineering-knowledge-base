---
id: "concept:health-check"
type: concept
name: Health check
canonical: false
taught_in: 2
community: 13
tags:
  - concept/lesson-term
  - community/13
source: ai-engineering-from-scratch/phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md
---

# Health check

**Community:** [[Communities/13 Object Multiplex · Clip · Divided attention|13 Object Multiplex · Clip · Divided attention]]

> *What people say:* "Readiness probe"

**What it actually means:** Cheap endpoint that reports whether the service can answer; loadbalancers rely on this

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]] — An endpoint that returns the status of all dependencies (cache, LLM availability, guardrails) -- used by load balancers and Kubernetes to route traffic


%% ── my notes ── %%
