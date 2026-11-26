---
id: "lesson:17/27"
type: lesson
ref: 17/27
phase: 17
num: 27
title: "FinOps for LLMs — Unit Economics and Multi-Tenant Attribution"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 10
prereqs: 2
community: 30
aliases:
  - 17/27
  - 17-27
tags:
  - phase/17
  - type/learn
  - community/30
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/27-finops-llms/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/27-finops-llms"
---

# 17/27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution

> Traditional FinOps breaks on LLM spend. Costs are token-transactions, not resource-uptime. Tags don't map — an API call is a transaction, not an asset. Engineering decisions (prompt design, context window, output length) are financial decisions. The 2026 playbook has three attribution dimensions to instrument on day one: per-user (`user_id`) for seat pricing and expansion, per-task (`task_id` + `route`) for product surface cost and prioritization, per-tenant (`tenant_id`) for unit economics and renewal. Four token layers — prompt, tool, memory, response — one bucket hides spend. Enforcement ladder for multi-tenant products: rate limits per tenant (2-3x expected peak, clear 429 + retry-after); daily spend cap (1.5-3x contracted ceiling; triggers rate tightening + alert); kill switches on spend z-score > 4 (auto-pause + page on-call). Attribution patterns: tag-and-aggregate, telemetry-joiner (trace-ID → billing; highest accuracy), sampling-and-extrapolation, model-based allocation, event-sourced, real-time streaming. Unit metric: cost per resolved query, cost per generated artifact — not $/M tokens. Retroactive tagging always misses; instrument at request creation.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/27-finops-llms/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/27-finops-llms) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/27-finops-llms) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/30 Evaluation (Eval) · Kill switch · Non-determinism|30 Evaluation (Eval) · Kill switch · Non-determinism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 13 (Observability), Phase 17 · 14 (Caching)`

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]] — Observability
- [[Lessons/17-14 Prompt Caching and Semantic Caching Economics|17/14 Prompt Caching and Semantic Caching Economics]] — Caching

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]], [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]], [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- depth 3: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Concepts taught

- Per-user attribution `lesson term` — user_id stamped on every call
- Per-task attribution `lesson term` — task_id + route identify product surface
- Per-tenant attribution `lesson term` — tenant_id; drives unit economics
- Four token layers `lesson term` — prompt + tool + memory + response
- [[Concepts/Rate Limit|Rate Limit]] `glossary` — Per-tenant ceiling enforced at gateway
- Daily spend cap `lesson term` — Tenant-scoped budget with alert
- [[Concepts/Kill switch|Kill switch]] `lesson term` — Spend z-score > 4 triggers auto-suspension
- Cost per resolved `lesson term` — Cost tied to product outcome, not tokens
- Telemetry joiner `lesson term` — Highest-accuracy attribution pattern
- Stacked optimization `lesson term` — Compounding savings to ~5-10% baseline

## Ships

- [[Artifacts/17-27 finops-plan|finops-plan]] `skill` — Design an LLM FinOps program — attribution schema (user/task/tenant + four token layers), three-tier enforcement ladder, and unit metric (cost per resolved / artifact).

## Further reading

- Digital Applied — LLM Agent Cost Attribution 2026 ([link](https://www.digitalapplied.com/blog/llm-agent-cost-attribution-guide-production-2026))
- FinOps Foundation — FinOps for AI Overview ([link](https://www.finops.org/wg/finops-for-ai-overview/))
- FinOps School — Cost per Unit 2026 Guide ([link](https://finopsschool.com/blog/cost-per-unit/))
- PointFive — Managed LLMs in Azure OpenAI ([link](https://www.pointfive.co/blog/finops-for-ai-economics-of-managed-llms-in-azure-open-ai))


%% ── my notes ── %%
