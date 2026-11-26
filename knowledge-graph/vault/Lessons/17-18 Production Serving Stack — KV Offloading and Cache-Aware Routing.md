---
id: "lesson:17/18"
type: lesson
ref: 17/18
phase: 17
num: 18
title: "Production Serving Stack — KV Offloading and Cache-Aware Routing"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 28
aliases:
  - 17/18
  - 17-18
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache"
---

# 17/18 Production Serving Stack — KV Offloading and Cache-Aware Routing

> A production serving stack wires router, engines, and observability into one Kubernetes deployment — and treats KV cache as a resource that can leave the GPU. KV offloading extracts KV cache out of GPU memory and reuses it across queries and engines (CPU DRAM, then disk/Ceph). vLLM's production-stack is the reference deployment; LMCache is the offloading layer. The vLLM 0.11.0 KV Offloading Connector (January 2026) makes this asynchronous and pluggable via the Connector API (v0.9.0+). The offload path is usually hidden from the request path, though cache misses and promotions can add end-to-end latency. LMCache is valuable even without shared prefixes — when a GPU runs out of KV slots, preempted requests can be restored from CPU instead of recomputing prefill. Published benchmarks on 16x H100 (80GB HBM) across 4 a3-highgpu-4g: when KV cache exceeds HBM, both native CPU offload and LMCache substantially improve throughput; at low KV footprint, all configs match baseline with small overhead.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/18-vllm-production-stack-lmcache/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 17 · 06 (SGLang/RadixAttention)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals
- [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]] — SGLang/RadixAttention

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Concepts taught

- [[Concepts/Production-stack|Production-stack]] `lesson term` — vLLM's Kubernetes Helm chart + operator
- Connector API `lesson term` — vLLM 0.9.0+ pluggable KV store interface
- Native CPU offload `lesson term` — Store KV in host RAM of same engine
- LMCache `lesson term` — Cross-engine KV cache server on CPU DRAM + disk
- 0.11.0 async `lesson term` — Offload hidden behind engine stream
- Preemption `lesson term` — KV cache shuffle when HBM full
- Prefix reuse `lesson term` — Multiple queries share beginning; cache hit
- Ceph tier `lesson term` — Durable storage below DRAM in the cache hierarchy

## Ships

- [[Artifacts/17-18 vllm-stack-decider|vllm-stack-decider]] `skill` — Decide vLLM deployment layout — production-stack Helm chart, KV offload (native CPU or LMCache), router/observability integration — given workload and fleet size.

## Further reading

- LMCache for Enterprise-Scale LLM Inference (arXiv:2510.09665) ([link](https://arxiv.org/html/2510.09665v2))
- vLLM Blog — KV Offloading Connector (Jan 2026) ([link](https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html))
- LMCache GitHub ([link](https://github.com/LMCache/LMCache)) — Connector implementation.
- [[Resources/vLLM Production Stack Router|vLLM Production Stack Router]] ([link](https://github.com/vllm-project/production-stack)) — Helm chart + operator. ·  also cited by 1 other lesson
- [[Resources/vLLM 0.11.0 release notes|vLLM 0.11.0 release notes]] ([link](https://github.com/vllm-project/vllm/releases)) — asynchronous path details. ·  also cited by 1 other lesson


%% ── my notes ── %%
