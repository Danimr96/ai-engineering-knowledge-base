---
id: "lesson:17/24"
type: lesson
ref: 17/24
phase: 17
num: 24
title: Chaos Engineering for LLM Production
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
aliases:
  - 17/24
  - 17-24
tags:
  - phase/17
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/24-chaos-engineering-llm/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/24-chaos-engineering-llm"
---

# 17/24 Chaos Engineering for LLM Production

> Chaos engineering for LLMs is its own discipline in 2026. Prerequisites before running experiments in production: defined SLI/SLO, trace+metric+log observability, automated rollback, runbooks, on-call. Architecture has four planes: control (experiment scheduler), target (services, infra, data stores), safety (guards + abort + traffic filters), observability (metrics + traces + logs), feedback (into SLO adjustments). Guardrails are mandatory: burn-rate alerts pause experiments if daily error-budget burn > 2x expected; suppression windows + trace-ID correlation dedupe alert noise. Cadence: weekly small canary + SLO review; monthly game day + postmortem; quarterly cross-team resilience audit + dependency mapping. LLM-specific experiments: memory overload, network failures, provider outages, malformed prompts, KV cache eviction storms. Tooling: Harness Chaos Engineering (LLM-derived recommendations, blast-radius downscaling, MCP tool integration); LitmusChaos (CNCF); Chaos Mesh (CNCF Kubernetes-native).

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/24-chaos-engineering-llm/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/24-chaos-engineering-llm) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/24-chaos-engineering-llm) · code: main.py · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 23 (SRE for AI), Phase 17 · 13 (Observability)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection|17/23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection]] — SRE for AI

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- depth 3: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Builds on this

- [[Lessons/17-23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection|17/23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection]]

## Concepts taught

- SLI / SLO `lesson term` — Indicator + objective; required prerequisite
- [[Concepts/Blast radius|Blast radius]] `lesson term` — Set of services / users affected by experiment
- Burn-rate alert `lesson term` — Fires when error-budget burn rate > 2x expected
- Game day `lesson term` — Scheduled cross-team chaos exercise
- LitmusChaos `lesson term` — Graduated CNCF Kubernetes chaos tool
- Chaos Mesh `lesson term` — CNCF sandbox Kubernetes-native chaos
- Harness CE `lesson term` — Harness chaos with AI recommendations
- Malformed prompt `lesson term` — Input that stalls tokenization
- KV eviction storm `lesson term` — Mass eviction triggering re-prefills

## Ships

- [[Artifacts/17-24 chaos-plan|chaos-plan]] `skill` — Design an LLM chaos engineering plan — verify prerequisites, build four planes, pick tool, start with three safe experiments, enforce safety-plane gates.

## Further reading

- Ankush Sharma — Observability for LLMs (book) ([link](https://www.amazon.com/Observability-Large-Language-Models-Engineering-ebook/dp/B0DJSR65TR))
- AWS FIS ([link](https://aws.amazon.com/fis/))
- Chaos Mesh (CNCF) ([link](https://chaos-mesh.org/))
- DevSecOps School — Chaos Engineering 2026 Guide ([link](https://devsecopsschool.com/blog/chaos-engineering/))
- Harness Chaos Engineering ([link](https://www.harness.io/products/chaos-engineering))
- LitmusChaos (CNCF) ([link](https://litmuschaos.io/))

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 11, required


%% ── my notes ── %%
