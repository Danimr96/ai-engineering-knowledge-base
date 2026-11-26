---
id: "lesson:17/20"
type: lesson
ref: 17/20
phase: 17
num: 20
title: "Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 2
community: 30
aliases:
  - 17/20
  - 17-20
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/20-shadow-canary-progressive/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/20-shadow-canary-progressive"
---

# 17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs

> LLM rollouts combine the hardest parts of software deployment: no unit tests, diffuse failure modes, delayed signals. The sequence is (1) shadow mode — duplicate prod requests to candidate model, log, compare with zero user impact; catches obvious distribution issues but is not a quality guarantee; (2) canary rollout — progressive traffic shift 10% → 25% → 50% → 75% → 100% with gates at each step; track latency percentiles, cost/request, error/refusal rate, output length distribution, user-feedback rate; (3) A/B testing for distinct alternatives after stability confirmed. Non-determinism is irreducible — up to 15% accuracy variation across runs with identical inputs due to GPU FP non-associativity plus batch-size variance. Cost is a variable, not constant — a 20% better model can be 3x more expensive per call. Rollback speed is decisive: if rollback requires redeploy, you are too slow. Policy lives in config/flags; model lives in registry with pinned digests; rollback = flip policy + revert threshold + pin old model in seconds.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/20-shadow-canary-progressive/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/20-shadow-canary-progressive) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/20-shadow-canary-progressive) · code: main.py, main.ts · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 13 (Observability), Phase 17 · 21 (A/B Testing)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-21 A-B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem|17/21 A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem]] — A/B Testing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- depth 3: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Builds on this

- [[Lessons/17-21 A-B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem|17/21 A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem]]

## Concepts taught

- [[Concepts/Shadow Mode|Shadow Mode]] `lesson term` — Zero-impact send-to-candidate for logging
- [[Concepts/Canary Release|Canary Release]] (as *Canary*) `glossary` — Gradual user-exposed rollout with gates
- Gates `lesson term` — Metric thresholds that block progression
- [[Concepts/Non-determinism|Non-determinism]] `lesson term` — Irreducible run-to-run differences
- Policy flag `lesson term` — Config-level rollback, seconds not hours
- Model pin `lesson term` — Immutable reference to a model version
- Argo Rollouts `lesson term` — Kubernetes-native canary/rollback controller
- KServe `lesson term` — Model serving with canary primitives
- Istio weighted `lesson term` — Service-mesh traffic splitter
- [[Concepts/Shadow Traffic|Shadow Traffic]] `glossary` — A copy of live request traffic sent to a candidate system for observation while the candidate response remains outside the primary user response path. Because the copied request still executes, its side effects must be isolated.

## Ships

- [[Artifacts/17-20 rollout-runbook|rollout-runbook]] `skill` — Design a shadow → canary → A/B → 100% rollout plan for a new LLM model or prompt template, with five canary gates, noise-floor-aware thresholds, and a seconds-fast rollback path.

## Further reading

- APXML — Advanced LLM Deployment Patterns ([link](https://apxml.com/courses/mlops-for-large-models-llmops/chapter-4-llm-deployment-serving-optimization/advanced-llm-deployment-patterns))
- Argo Rollouts docs ([link](https://argo-rollouts.readthedocs.io/))
- Flagger docs ([link](https://docs.flagger.app/))
- MarkTechPost — Safely Deploying ML Models ([link](https://www.marktechpost.com/2026/03/21/safely-deploying-ml-models-to-production-four-controlled-strategies-a-b-canary-interleaved-shadow-testing/))
- TianPan — Releasing AI Features Without Breaking Production ([link](https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing))

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 10, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 12, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 11, required
- [[Paths/Customer AI Deployment|Customer AI Deployment]] — step 11, required
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 11, required


%% ── my notes ── %%
