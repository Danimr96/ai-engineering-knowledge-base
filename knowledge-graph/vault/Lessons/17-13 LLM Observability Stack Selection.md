---
id: "lesson:17/13"
type: lesson
ref: 17/13
phase: 17
num: 13
title: LLM Observability Stack Selection
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 1
community: 30
aliases:
  - 17/13
  - 17-13
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/13-llm-observability/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/13-llm-observability"
---

# 17/13 LLM Observability Stack Selection

> The 2026 observability market splits into two categories. Development platforms (LangSmith, Langfuse, Comet Opik) bundle monitoring with evals, prompt management, session replays. Gateway/instrumentation tools (Helicone, SigNoz, OpenLLMetry, Phoenix) focus on telemetry. Langfuse is MIT-licensed core with strong OSS balance (50K events/month free cloud). Phoenix is OpenTelemetry-native under Elastic License 2.0 — excellent for drift/RAG visualization, not a persistent production backend. Arize AX uses zero-copy Iceberg/Parquet integration claiming 100x cheaper than monolithic observability. LangSmith leads for LangChain/LangGraph, $39/user/mo, self-host in Enterprise only. Helicone is proxy-based with 15-30 min setup, 100K req/mo free, but less depth on agent traces. Common production pattern: Gateway (Helicone/Portkey) + eval platform (Phoenix/TruLens) glued by OpenTelemetry.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/13-llm-observability/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/13-llm-observability) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/13-llm-observability) · code: main.py, main.ts · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 08 (Inference Metrics), Phase 14 (Agent Engineering)`

- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Inference Metrics
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agent Engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]
- depth 3: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|17/20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]]
- [[Lessons/17-21 A-B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem|17/21 A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem]]
- [[Lessons/17-23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection|17/23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection]]
- [[Lessons/17-24 Chaos Engineering for LLM Production|17/24 Chaos Engineering for LLM Production]]
- [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails]]
- [[Lessons/17-26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001|17/26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001]]
- [[Lessons/17-27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution|17/27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution]]

## Concepts taught

- OpenLLMetry `lesson term` — Open-source OpenTelemetry instrumentation for LLMs
- GenAI conventions `lesson term` — Standard OTel attribute names for LLM calls
- LangSmith `lesson term` — Commercial platform bundled with LangChain ecosystem
- Langfuse `lesson term` — MIT OSS with similar feature set
- Phoenix `lesson term` — OpenTelemetry-native dev/eval platform
- Arize AX `lesson term` — Commercial zero-copy Iceberg/Parquet observability
- Helicone `lesson term` — HTTP proxy collecting LLM telemetry + gateway features
- Opik `lesson term` — Apache 2.0 OSS dev platform from Comet
- [[Concepts/Session replay|Session replay]] `lesson term` — Replay a full agent session with tool calls
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]] (as *Eval*) `glossary` — Running candidate model/prompt over labeled dataset

## Ships

- [[Artifacts/17-13 observability-stack|observability-stack]] `skill` — Pick an LLM observability stack (development platform + gateway + optional scale layer) given stack, scale, budget, and license posture, and define the OpenTelemetry GenAI attribute set.

## Further reading

- PremAI — Setting Up Langfuse, LangSmith, Helicone, Phoenix ([link](https://blog.premai.io/llm-observability-setting-up-langfuse-langsmith-helicone-phoenix/))
- [[Resources/Arize Phoenix docs|Arize Phoenix docs]] ([link](https://docs.arize.com/phoenix)) ·  also cited by 2 other lessons
- Helicone docs ([link](https://docs.helicone.ai/))
- Langfuse — Arize AX Alternative analysis ([link](https://langfuse.com/faq/all/best-phoenix-arize-alternatives))
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) ·  also cited by 9 other lessons
- SigNoz — Top LLM Observability Tools 2026 ([link](https://signoz.io/comparisons/llm-observability-tools/))

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 11, required
- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 7, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 10, required


%% ── my notes ── %%
