---
id: "lesson:17/17"
type: lesson
ref: 17/17
phase: 17
num: 17
title: "Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 12
prereqs: 2
community: 21
aliases:
  - 17/17
  - 17-17
tags:
  - phase/17
  - type/learn
  - community/21
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/17-disaggregated-prefill-decode/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/17-disaggregated-prefill-decode"
---

# 17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d

> Prefill is compute-bound; decode is memory-bound. Running both on the same GPU wastes one resource. Disaggregation splits them onto separate pools and transfers KV cache between them over NIXL (RDMA/InfiniBand or TCP fallback). NVIDIA Dynamo (GTC 2025 announce, 1.0 GA) sits above vLLM/SGLang/TRT-LLM — its Planner Profiler + SLA Planner auto-rate-match prefill:decode ratios to meet SLOs. NVIDIA publishes throughput gains in this ballpark — developer.nvidia.com (2025-06) shows a ~6x improvement for DeepSeek-R1 MoE on GB200 NVL72 + Dynamo in the medium-latency regime, and the Dynamo product page (developer.nvidia.com, undated) advertises up to 50x MoE throughput on GB300 NVL72 + Dynamo vs Hopper. The "30x" figure is a community aggregate across full-stack Blackwell + Dynamo + DeepSeek-R1 reports; we have not found a single primary source stating exactly 30x, so treat it as a directional claim. llm-d (Red Hat + AWS) is Kubernetes-native: prefill / decode / router as independent Services with per-role HPA. llm-d 0.5 adds hierarchical KV offloading, cache-aware LoRA routing, UCCL networking, scale-to-zero. Economics: internal rollup of multiple customer disclosures suggests 30–40% savings on $2M-class inference spend (i.e., $600-800K/year) when switching from colocated serving to disaggregated with Dynamo at constant SLA; the specific $2M→$600-800K figure is an internal composite, not a single published case study — use it as an order-of-magnitude anchor, not a reference citation. Short prompts (<512 tokens, short output) don't justify the transfer cost.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/17-disaggregated-prefill-decode/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/17-disaggregated-prefill-decode) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/17-disaggregated-prefill-decode) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 17 · 08 (Inference Metrics)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Inference Metrics

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Concepts taught

- [[Concepts/Disaggregated Serving|Disaggregated Serving]] `glossary` — Separate GPU pools for each phase
- NIXL `lesson term` — Dynamo's inter-node KV transfer (RDMA/TCP)
- NVIDIA Dynamo `lesson term` — Stack-above coordinator for vLLM/SGLang/TRT-LLM
- llm-d `lesson term` — Red Hat + AWS K8s disaggregated stack
- Planner Profiler `lesson term` — Measures workload, configures pool ratios
- SLA Planner `lesson term` — Auto-rate-matches prefill:decode to meet SLOs
- packDomain: rack `lesson term` — Pack prefill+decode on same rack for fast KV
- UCCL `lesson term` — llm-d 0.5 networking layer for scale-to-zero
- MoE expert routing `lesson term` — DeepSeek-V3 pattern; disaggregation helps
- [[Concepts/Decode Phase|Decode Phase]] `glossary` — The iterative stage of autoregressive inference that generates new tokens one step at a time after the input prefix has been processed.
- [[Concepts/Prefill|Prefill]] `glossary` — The initial inference stage that processes all supplied input tokens to produce their representations and the attention state required for subsequent autoregressive generation.

## Ships

- [[Artifacts/17-17 disaggregation-decider|disaggregation-decider]] `skill` — Decide whether to adopt disaggregated prefill/decode (Dynamo or llm-d) for a given workload and cluster. Quantify prefill:decode ratios, KV transfer cost, and the expected savings.

## Further reading

- [[Resources/NVIDIA — Disaggregated LLM Inference on Kubernetes|NVIDIA — Disaggregated LLM Inference on Kubernetes]] ([link](https://developer.nvidia.com/blog/deploying-disaggregated-llm-inference-workloads-on-kubernetes/)) ·  also cited by 2 other lessons
- [[Resources/NVIDIA — Introducing Dynamo|NVIDIA — Introducing Dynamo]] ([link](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)) ·  also cited by 1 other lesson
- [[Resources/llm-d GitHub|llm-d GitHub]] ([link](https://github.com/llm-d/llm-d)) ·  also cited by 1 other lesson
- llm-d 0.5 release notes ([link](https://github.com/llm-d/llm-d/releases))
- TensorRT-LLM Disaggregated Serving blog ([link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog5_Disaggregated_Serving_in_TensorRT-LLM.html))


%% ── my notes ── %%
