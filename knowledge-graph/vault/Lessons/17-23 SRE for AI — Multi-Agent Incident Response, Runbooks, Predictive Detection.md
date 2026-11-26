---
id: "lesson:17/23"
type: lesson
ref: 17/23
phase: 17
num: 23
title: "SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 10
prereqs: 2
aliases:
  - 17/23
  - 17-23
tags:
  - phase/17
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/23-sre-for-ai/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/23-sre-for-ai"
---

# 17/23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection

> AI SRE uses LLMs grounded in infrastructure data (logs, runbooks, service topology) via RAG to automate investigation, documentation, and coordination phases. The 2026 architecture pattern is multi-agent orchestration — specialized agents (logs, metrics, runbooks) coordinated by a supervisor; AI proposes hypotheses and queries, humans approve judgment calls. Datadog Bits AI and Azure SRE Agent ship this as managed products. Runbooks are evolving: NeuBird Hawkeye uses adversarial evaluation (two models analyze the same incident; agreement = confidence, disagreement = uncertainty); operational memory persists across team changes. Auto-remediation stays cautious: AI suggests, humans approve. Fully autonomous action is narrow (restart pod, rollback specific deploy) with tight guardrails — anyone selling "set it and forget it" is overselling. Emerging frontier: pre-incident prediction. MIT research reports an LLM trained on historical logs + GPU temps + API error patterns predicted 89% of outages 10-15 min early. Projection: 95% of enterprise LLMs have automated failover by end-2026.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/23-sre-for-ai/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/23-sre-for-ai) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/23-sre-for-ai) · code: main.py · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 13 (Observability), Phase 17 · 24 (Chaos Engineering)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-24 Chaos Engineering for LLM Production|17/24 Chaos Engineering for LLM Production]] — Chaos Engineering

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- depth 3: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Builds on this

- [[Lessons/17-24 Chaos Engineering for LLM Production|17/24 Chaos Engineering for LLM Production]]

## Concepts taught

- AI SRE `lesson term` — LLM-backed incident investigation + coordination
- Supervisor agent `lesson term` — Top-level agent breaking incidents into sub-queries
- Specialized agent `lesson term` — Sub-agent with tool access (logs, metrics, runbooks)
- Auto-remediation `lesson term` — Narrow pre-approved action; NOT broad re-architecture
- Operational memory `lesson term` — Post-mortems + runbooks in vector DB for RAG
- Adversarial eval `lesson term` — Independent analyses; agreement = confidence
- NeuBird Hawkeye `lesson term` — Product with adversarial-eval + memory pattern
- Bits AI `lesson term` — Datadog-managed AI SRE
- Pre-incident prediction `lesson term` — 10-15 min lead time on outage prediction
- [[Concepts/Incident Response|Incident Response]] `glossary` — The coordinated process for detecting, analyzing, containing, recovering from, communicating, and learning from an event that threatens service, data, safety, or security.

## Ships

- [[Artifacts/17-23 ai-sre-plan|ai-sre-plan]] `skill` — Design an AI SRE rollout for a team — multi-agent triage architecture, structured runbooks, adversarial evaluation, narrow auto-remediation, and predictive-detection posture.

## Further reading

- Datadog Bits AI ([link](https://www.datadoghq.com/product/bits-ai/))
- DZone — AI in SRE 2026 ([link](https://dzone.com/articles/ai-in-sre-whats-actually-coming-in-2026))
- awesome-ai-sre ([link](https://github.com/agamm/awesome-ai-sre))
- incident.io — AI SRE Complete Guide 2026 ([link](https://incident.io/blog/what-is-ai-sre-complete-guide-2026))
- InfoQ — Human-Centred AI for SRE ([link](https://www.infoq.com/news/2026/01/opsworker-ai-sre/))
- [[Resources/NeuBird Hawkeye|NeuBird Hawkeye]] ([link](https://www.neubird.ai/)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 12, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 12, required
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 13, required


%% ── my notes ── %%
