---
id: "lesson:17/14"
type: lesson
ref: 17/14
phase: 17
num: 14
title: Prompt Caching and Semantic Caching Economics
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 2
community: 28
aliases:
  - 17/14
  - 17-14
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/14-prompt-semantic-caching/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/14-prompt-semantic-caching"
---

# 17/14 Prompt Caching and Semantic Caching Economics

> **Pricing snapshot dated 2026-04.** Numeric claims below reflect vendor rate cards captured at this lesson's publication; verify against the linked docs before quoting them downstream.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/14-prompt-semantic-caching/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/14-prompt-semantic-caching) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/14-prompt-semantic-caching) · code: main.py, main.ts · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 17 · 06 (SGLang RadixAttention)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals
- [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]] — SGLang RadixAttention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-15 Batch APIs — the 50% Discount as Industry Standard|17/15 Batch APIs — the 50% Discount as Industry Standard]]
- [[Lessons/17-27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution|17/27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution]]

## Concepts taught

- L2 prompt cache `lesson term` — Provider stores KV for repeated prefix
- [[Concepts/cache_control|cache_control]] `lesson term` — Explicit attribute marking cacheable blocks
- Cache write premium `lesson term` — Extra cost for first miss-to-cache (1.25x or 2x)
- L1 semantic cache `lesson term` — App-level hash-and-embed before calling LLM
- GPTCache `lesson term` — Popular OSS L1 cache library
- [[Concepts/Cache hit rate|Cache hit rate]] `lesson term` — Fraction of requests served from cache
- Parallelization anti-pattern `lesson term` — N parallel requests miss cache N times
- Dynamic content trap `lesson term` — Dynamic bytes in prefix kill hit rate
- [[Concepts/RadixAttention|RadixAttention]] `lesson term` — SGLang's prefix-cache implementation

## Ships

- [[Artifacts/17-14 cache-auditor|cache-auditor]] `skill` — Audit an LLM prompt template and traffic pattern for cacheability. Recommend prompt restructure, TTL choice, parallelization fix, and semantic-cache threshold.

## Further reading

- DigitalOcean / Anthropic — Prompt Caching ([link](https://www.digitalocean.com/blog/prompt-caching-with-digital-ocean))
- [[Resources/Anthropic Prompt Caching Guide|Anthropic Prompt Caching Guide]] ([link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)) — official `cache_control` semantics and TTLs. ·  also cited by 3 other lessons
- [[Resources/OpenAI Prompt Caching|OpenAI Prompt Caching]] ([link](https://platform.openai.com/docs/guides/prompt-caching)) — automatic caching behavior and eligibility. ·  also cited by 2 other lessons
- ProjectDiscovery — Cut LLM Costs 59% With Prompt Caching ([link](https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching))
- TianPan — Semantic Caching for LLMs Production ([link](https://tianpan.co/blog/2026-04-10-semantic-caching-llm-production))


%% ── my notes ── %%
