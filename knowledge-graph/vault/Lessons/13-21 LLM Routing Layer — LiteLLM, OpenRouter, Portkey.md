---
id: "lesson:13/21"
type: lesson
ref: 13/21
phase: 13
num: 21
title: "LLM Routing Layer — LiteLLM, OpenRouter, Portkey"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 2
community: 19
aliases:
  - 13/21
  - 13-21
tags:
  - phase/13
  - type/learn
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/21-llm-routing-layer/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/21-llm-routing-layer"
---

# 13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey

> Provider lock-in is expensive. Different tool-calling workloads suit different models. Routing gateways give one API surface, retries, failover, cost tracking, and guardrails. Three archetypes dominate 2026: LiteLLM (open-source self-hosted), OpenRouter (managed SaaS), Portkey (production-grade, open-sourced in March 2026). This lesson names the decision criteria and walks a stdlib routing gateway.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/21-llm-routing-layer/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/21-llm-routing-layer) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/21-llm-routing-layer) · code: main.py  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 02 (function calling), Phase 13 · 17 (gateways)`

- [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]] — function calling
- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]] — gateways

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]], [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]]
- depth 3: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- Routing gateway `lesson term` — One-API-surface layer in front of many providers
- OpenAI-compatible `lesson term` — Accepts /v1/chat/completions shape, translates to any backend
- Model alias `lesson term` — Name in your code that the gateway maps to a concrete model
- [[Concepts/Fallback Chain|Fallback Chain]] `lesson term` — Ordered list of providers attempted on failure
- [[Concepts/Semantic caching|Semantic caching]] `lesson term` — Key is embedding of the prompt; near-duplicates share a cache hit
- [[Concepts/Guardrails|Guardrails]] `glossary` — Redact PII, reject policy violations
- Per-key rate limit `lesson term` — Quota scoped to an API key
- [[Concepts/Cost tracking|Cost tracking]] `lesson term` — Aggregate token usage x price per model
- [[Concepts/LiteLLM|LiteLLM]] `lesson term` — Self-hostable OSS routing gateway
- OpenRouter `lesson term` — Hosted gateway with credit-based billing
- [[Concepts/Portkey|Portkey]] `lesson term` — Open-source + managed with guardrails built in

## Ships

- [[Artifacts/13-21 routing-config-designer|routing-config-designer]] `skill` — Given a workload profile, pick LiteLLM / OpenRouter / Portkey and produce a routing config.

## Further reading

- LiteLLM — docs ([link](https://docs.litellm.ai/)) — self-hosted routing gateway
- OpenRouter — quickstart ([link](https://openrouter.ai/docs/quickstart)) — managed routing SaaS
- Portkey — docs ([link](https://portkey.ai/docs)) — production routing with guardrails
- Relayplane — LLM gateway comparison 2026 ([link](https://relayplane.com/blog/llm-gateway-comparison-2026)) — vendor survey
- TrueFoundry — LiteLLM vs OpenRouter ([link](https://www.truefoundry.com/blog/litellm-vs-openrouter)) — decision guide


%% ── my notes ── %%
