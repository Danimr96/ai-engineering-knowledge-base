---
id: "lesson:17/11"
type: lesson
ref: 17/11
phase: 17
num: 11
title: Multi-Region LLM Serving and KV Cache Locality
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
community: 28
aliases:
  - 17/11
  - 17-11
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/11-multi-region-kv-locality/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/11-multi-region-kv-locality"
---

# 17/11 Multi-Region LLM Serving and KV Cache Locality

> Round-robin load balancing is actively harmful for cached LLM inference. A request that does not land on the node holding its prefix pays full prefill cost — roughly 800 ms at P50 on a long prompt versus ~80 ms with a cache hit. In 2026 the production pattern is a cache-aware router (vLLM Router in Rust, llm-d router) that consumes KV-cache events and routes on prefix-hash match. Recent research (GORGO) makes cross-region network latency an explicit term in the routing objective. Commercial "cross-region inference" offerings (Bedrock cross-region inference, GKE multi-cluster gateways) treat inference as opaque — they handle availability, not TTFT. JPMorgan and Mayo Clinic ran us-east-1 failover in Nov 2024 at ~22 minutes. The DR reality: 32% of LLM DR failures are because teams backed up weights but forgot tokenizer files or quantization configs.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/11-multi-region-kv-locality/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/11-multi-region-kv-locality) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/11-multi-region-kv-locality) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (vLLM Serving), Phase 17 · 06 (SGLang RadixAttention)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — vLLM Serving
- [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]] — SGLang RadixAttention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Concepts taught

- Cache-aware routing `lesson term` — Route on prefix-hash match to KV-cache-holding replica
- KV-cache events `lesson term` — Replicas publish block add/evict; router indexes
- Prefix hash `lesson term` — Hash of first N tokens used as router lookup
- GORGO `lesson term` — arXiv 2602.11688; network latency as explicit term
- Cross-region inference `lesson term` — AWS product; availability failover, not TTFT awareness
- DR manifest `lesson term` — Every file needed to restore — not just weights
- Data residency `lesson term` — Legal constraint on which region sees user data
- RTT `lesson term` — Network latency; 75 ms US-EU, 220 ms US-APAC
- LLM-aware LB `lesson term` — Cache-aware router as a product category

## Ships

- [[Artifacts/17-11 multi-region-router|multi-region-router]] `skill` — Design a multi-region LLM routing plan with KV-cache locality, residency boundaries, DR manifest, and a quarterly failover drill.

## Further reading

- arXiv — GORGO (2602.11688) ([link](https://arxiv.org/html/2602.11688v1)) — cross-region KV-cache reuse with network latency term.
- BentoML — Multi-cloud and cross-region inference ([link](https://bentoml.com/llm/infrastructure-and-operations/multi-cloud-and-cross-region-inference))
- AWS Bedrock Cross-Region Inference ([link](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)) — availability failover documentation.
- [[Resources/vLLM Production Stack Router|vLLM Production Stack Router]] ([link](https://github.com/vllm-project/production-stack)) — cache-aware router source. ·  also cited by 1 other lesson
- TianPan — Multi-Region LLM Serving Cache Locality ([link](https://tianpan.co/blog/2026-04-17-multi-region-llm-serving-data-residency-routing))


%% ── my notes ── %%
