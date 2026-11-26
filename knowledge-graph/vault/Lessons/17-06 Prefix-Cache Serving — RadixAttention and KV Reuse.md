---
id: "lesson:17/06"
type: lesson
ref: 17/06
phase: 17
num: 6
title: "Prefix-Cache Serving — RadixAttention and KV Reuse"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 1
community: 28
aliases:
  - 17/06
  - 17-06
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/06-sglang-radixattention/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/06-sglang-radixattention"
---

# 17/06 Prefix-Cache Serving — RadixAttention and KV Reuse

> Treat the KV cache as a first-class, reusable resource stored in a radix tree, and scheduling changes with it: instead of FCFS (first-come, first-served) as vLLM schedules, a cache-aware scheduler prioritizes requests with longer shared prefixes — effectively a depth-first radix traversal so hot branches stay resident in HBM. SGLang is the engine that built serving around this idea. On Llama 3.1 8B with ShareGPT-like 1K prompts, SGLang hits ~16,200 tok/s to vLLM's ~12,500, a ~29% edge. On prefix-heavy RAG workloads the advantage reaches 6.4x. On voice-cloning-shaped workloads cache hit rate cleared 86%. Deployed on 400,000+ GPUs in 2026 across xAI, LinkedIn, Cursor, Oracle, GCP, Azure, AWS. The gotcha is that the 6.4x number evaporates when prefix ordering is inconsistent — ordering is the engineer's lever.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/06-sglang-radixattention/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/06-sglang-radixattention) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/06-sglang-radixattention) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 14 (Agentic RAG)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agentic RAG ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-11 Multi-Region LLM Serving and KV Cache Locality|17/11 Multi-Region LLM Serving and KV Cache Locality]]
- [[Lessons/17-14 Prompt Caching and Semantic Caching Economics|17/14 Prompt Caching and Semantic Caching Economics]]
- [[Lessons/17-18 Production Serving Stack — KV Offloading and Cache-Aware Routing|17/18 Production Serving Stack — KV Offloading and Cache-Aware Routing]]
- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Concepts taught

- [[Concepts/RadixAttention|RadixAttention]] `lesson term` — KV cache indexed as a radix tree so shared prefixes reuse blocks
- Radix tree `lesson term` — Tree where each node owns a token range and its KV blocks
- Cache-aware scheduler `lesson term` — Scheduler that prefers requests sharing the resident branch
- Prefix-cache hit rate `lesson term` — Fraction of prompt tokens served from reused KV blocks
- FCFS `lesson term` — Default scheduling that breaks prefix locality
- Branch-level LRU `lesson term` — Eviction policy matched to radix shape
- Prompt template ordering `lesson term` — The prompt's component order determines what the tree can share
- System prompt pinning `lesson term` — Keep the immutable system portion pinned to avoid eviction thrash

## Ships

- [[Artifacts/17-06 radix-scheduler-advisor|radix-scheduler-advisor]] `skill` — Advise on SGLang adoption and prompt-ordering discipline for prefix-heavy workloads that want RadixAttention's cache reuse.

## Further reading

- SGLang ([link](https://arxiv.org/abs/2312.07104)) — the design reference.
- vLLM — Prefix Caching ([link](https://docs.vllm.ai/en/latest/features/prefix_caching.html)) — vLLM's own radix-like implementation, for comparison.
- SGLang GitHub ([link](https://github.com/sgl-project/sglang)) — source and docs.
- LMSYS blog — SGLang with RadixAttention ([link](https://www.lmsys.org/blog/2024-01-17-sglang/)) — benchmark numbers and scheduler rationale.
- SGLang documentation ([link](https://sgl-project.github.io/)) — RadixAttention and scheduling details.


%% ── my notes ── %%
