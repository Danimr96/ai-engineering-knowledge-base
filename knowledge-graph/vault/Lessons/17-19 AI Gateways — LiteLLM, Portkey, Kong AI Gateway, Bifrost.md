---
id: "lesson:17/19"
type: lesson
ref: 17/19
phase: 17
num: 19
title: "AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 11
prereqs: 2
community: 92
aliases:
  - 17/19
  - 17-19
tags:
  - phase/17
  - type/learn
  - community/92
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/19-ai-gateways/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/19-ai-gateways"
---

# 17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost

> A gateway sits between your apps and model providers. Core features are provider routing, fallback, retries, rate limiting, secret references, observability, guardrails. Market split in 2026: **LiteLLM** is MIT OSS with 100+ providers, OpenAI-compatible, but breaks down around ~2000 RPS (8 GB memory, cascading failures in published benchmarks); best for Python, <500 RPS, dev/prototyping. **Portkey** is control-plane-positioned (guardrails, PII redaction, jailbreak detection, audit trails), went Apache 2.0 open-source March 2026, 20-40 ms latency overhead, $49/mo production tier. **Kong AI Gateway** built on Kong Gateway — Kong's own benchmark on same 12 CPUs: 228% faster than Portkey, 859% faster than LiteLLM; $100/model/month pricing (max 5 on Plus tier); enterprise-fit if you're already on Kong. **Bifrost** (Maxim AI) — automatic retries with configurable backoff, fallback to Anthropic on OpenAI 429. **Cloudflare / Vercel AI Gateways** — managed, zero-ops, basic retry. Data residency drives the self-host decision; Portkey and Kong sit in the middle with OSS + optional managed.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/19-ai-gateways/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/19-ai-gateways) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/19-ai-gateways) · code: main.py, main.ts · quiz: 6 questions  
**Community:** [[Communities/92 LiteLLM · Sliding window · Token bucket|92 LiteLLM · Sliding window · Token bucket]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 01 (Managed LLM Platforms), Phase 17 · 16 (Model Routing)`

- [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]] — Managed LLM Platforms
- [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]] — Model Routing

## Builds on this

- [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]]
- [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|17/25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails]]

## Concepts taught

- Gateway `lesson term` — Process sitting between apps and providers
- [[Concepts/LiteLLM|LiteLLM]] `lesson term` — Python OSS, 100+ providers, breaks at 2K RPS
- [[Concepts/Portkey|Portkey]] `lesson term` — Control plane + observability, Apache 2.0
- Kong AI Gateway `lesson term` — Built on Kong Gateway, benchmark leader
- Bifrost `lesson term` — Retries + Anthropic fallback recipe
- Cloudflare AI Gateway `lesson term` — Edge-deployed managed gateway, zero-ops
- PII redaction `lesson term` — Regex + NER mask before sending to model
- Jailbreak detection `lesson term` — Classifier on user input
- Audit trail `lesson term` — Immutable record of every LLM call
- [[Concepts/Token bucket|Token bucket]] (as *Token-bucket*) `lesson term` — Refill-based rate limiter
- [[Concepts/Sliding window|Sliding window]] (as *Sliding-window*) `lesson term` — Time-windowed rate limiter; better fairness

## Ships

- [[Artifacts/17-19 gateway-picker|gateway-picker]] `skill` — Pick an AI gateway (LiteLLM, Portkey, Kong AI, Cloudflare/Vercel) given scale, latency budget, compliance, ops posture, and pricing tolerance.

## Further reading

- Kong AI Gateway docs ([link](https://docs.konghq.com/gateway/latest/ai-gateway/))
- LiteLLM GitHub ([link](https://github.com/BerriAI/litellm))
- Portkey GitHub ([link](https://github.com/Portkey-AI/gateway))
- Kong AI Gateway Benchmark ([link](https://konghq.com/blog/engineering/ai-gateway-benchmark-kong-ai-gateway-portkey-litellm))
- Techsy — Top LLM Gateway Tools 2026 ([link](https://techsy.io/en/blog/best-llm-gateway-tools))
- TrueFoundry — AI Gateways 2026 Comparison ([link](https://www.truefoundry.com/blog/a-definitive-guide-to-ai-gateways-in-2026-competitive-landscape-comparison))

## In learning paths

- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 11, required


%% ── my notes ── %%
