---
id: "lesson:17/08"
type: lesson
ref: 17/08
phase: 17
num: 8
title: "Inference Metrics — TTFT, TPOT, ITL, Goodput, P99"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 14
prereqs: 1
community: 21
aliases:
  - 17/08
  - 17-08
tags:
  - phase/17
  - type/learn
  - community/21
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/08-inference-metrics-goodput/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/08-inference-metrics-goodput"
---

# 17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99

> Four metrics decide whether an inference deployment is working. TTFT is prefill plus queue plus network. TPOT (equivalently ITL) is the memory-bound decode cost per token. End-to-end latency is TTFT plus TPOT times output length. Throughput is tokens per second aggregated across the fleet. But the one that matters for product is goodput — the fraction of requests that met every SLO simultaneously. High throughput at low goodput means you are processing tokens that never reach users on time. Reference numbers for Llama-3.1-8B-Instruct on TRT-LLM in 2026: mean TTFT 162 ms, mean TPOT 7.33 ms, mean E2E 1,093 ms. Always report P50, P90, P99 — never just mean. And watch the measurement trap: GenAI-Perf excludes TTFT from ITL calculation, LLMPerf includes it; two tools disagree on TPOT for the same run.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/08-inference-metrics-goodput/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/08-inference-metrics-goodput) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/08-inference-metrics-goodput) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill|21 Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-13 LLM Observability Stack Selection|17/13 LLM Observability Stack Selection]]
- [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]]
- [[Lessons/17-22 Load Testing LLM APIs — Why k6 and Locust Lie|17/22 Load Testing LLM APIs — Why k6 and Locust Lie]]

## Concepts taught

- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]] (as *TTFT*) `glossary` — Queue + network + prefill; dominated by prefill at long prompts
- [[Concepts/Time per Output Token (TPOT)|Time per Output Token (TPOT)]] (as *TPOT*) `glossary` — Memory-bound decode cost per token after first
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]] (as *ITL*) `glossary` — Same as TPOT in most tools (not all — see GenAI-Perf)
- E2E `lesson term` — TTFT + TPOT output_len; response-side network on top
- Throughput `lesson term` — Fleet efficiency; useless without latency percentiles
- [[Concepts/Goodput|Goodput]] `glossary` — Fraction of requests meeting every SLO constraint simultaneously
- P99 `lesson term` — 1-in-100 worst-case latency; the user experience metric
- SLO multi-constraint `lesson term` — AND of all three latency bounds; a request fails if any one is violated
- GenAI-Perf vs LLMPerf `lesson term` — Tools disagree on whether ITL includes TTFT
- [[Concepts/Service Level Objective (SLO)|Service Level Objective (SLO)]] `glossary` — A target range or threshold for a service-level indicator over a stated population and measurement window.
- [[Concepts/Tail Latency|Tail Latency]] `glossary` — The latency experienced by the slowest portion of requests, commonly summarized with a high percentile under a stated workload and time window.

## Ships

- [[Artifacts/17-08 slo-goodput-gate|slo-goodput-gate]] `skill` — Produce a CI/CD-ready benchmark recipe that gates LLM deploys on goodput, not throughput, with P50/P90/P99 percentiles and a documented tool choice.

## Further reading

- BentoML — LLM Inference Metrics ([link](https://bentoml.com/llm/inference-optimization/llm-inference-metrics)) — applied measurement on real deployments.
- Anyscale — LLM Serving Benchmarking Metrics ([link](https://docs.anyscale.com/llm/serving/benchmarking/metrics)) — alternative definitions and measurement recipe.
- NVIDIA NIM — LLM Benchmarking Metrics ([link](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html)) — canonical definition of TTFT, ITL, TPOT.
- [[Resources/LLMPerf|LLMPerf]] ([link](https://github.com/ray-project/llmperf)) — Ray-based open-source benchmark. ·  also cited by 1 other lesson
- GenAI-Perf ([link](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/README.md)) — NVIDIA's benchmark tool.
- [[Resources/MLPerf Inference|MLPerf Inference]] ([link](https://mlcommons.org/benchmarks/inference-datacenter/)) — the industry-accepted goodput-based benchmark. ·  also cited by 1 other lesson

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 6, required


%% ── my notes ── %%
