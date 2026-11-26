---
id: "lesson:17/22"
type: lesson
ref: 17/22
phase: 17
num: 22
title: "Load Testing LLM APIs — Why k6 and Locust Lie"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 11
prereqs: 2
community: 77
aliases:
  - 17/22
  - 17-22
tags:
  - phase/17
  - type/build
  - community/77
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/22-load-testing-llm-apis/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/22-load-testing-llm-apis"
---

# 17/22 Load Testing LLM APIs — Why k6 and Locust Lie

> Traditional load testers were not designed for streaming responses, variable output lengths, token-level metrics, or GPU saturation. Two traps bite most teams. The GIL trap: Locust's token-level measurement runs tokenization under the Python GIL, which competes with request generation under heavy concurrency; tokenization backlog then inflates reported inter-token latency — your client is the bottleneck, not the server. The prompt-uniformity trap: identical prompts in a loop test one point on the token distribution; real traffic has variable length and diverse prefix matches. LLMPerf fixes this with `--mean-input-tokens` + `--stddev-input-tokens`. Tool mapping in 2026: LLM-specialized (GenAI-Perf, LLMPerf, LLM-Locust, guidellm) for token-level accuracy; **k6 v2026.1.0** + **k6 Operator 1.0 GA (Sept 2025)** — streaming-aware, Kubernetes-native distributed via TestRun/PrivateLoadZone CRDs, best for CI/CD gates; Vegeta for Go constant-rate saturation; Locust 2.43.3 only with LLM-Locust extension for streaming. Load patterns: steady-state, ramp, spike (autoscaling test), soak (memory leaks).

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/22-load-testing-llm-apis/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/22-load-testing-llm-apis) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/22-load-testing-llm-apis) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Togeth|77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale · GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 08 (Inference Metrics), Phase 17 · 03 (GPU Autoscaling)`

- [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] — GPU Autoscaling
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] — Inference Metrics

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]], [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]
- depth 3: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Concepts taught

- LLMPerf `lesson term` — Anyscale benchmark tool, streaming-aware
- GenAI-Perf `lesson term` — NVIDIA reference harness
- LLM-Locust `lesson term` — Locust extension fixing GIL trap
- guidellm `lesson term` — Large-scale synthetic tool
- k6 Operator `lesson term` — CRD-based distributed k6
- GIL trap `lesson term` — Tokenization backlog inflates reported latency
- Prompt-uniformity trap `lesson term` — Loop with same prompt hits cache, inflates throughput
- Steady-state `lesson term` — Flat RPS for N minutes
- Ramp `lesson term` — 0 to target over duration
- Spike `lesson term` — Sudden multiplier then revert
- Soak `lesson term` — Hours for leak detection

## Ships

- [[Artifacts/17-22 load-test-plan|load-test-plan]] `skill` — Design a realistic LLM load test — pick tool (LLMPerf, k6, GenAI-Perf, guidellm), build four patterns (steady, ramp, spike, soak), and gate in CI.

## Further reading

- PremAI — Load Testing LLMs 2026 ([link](https://blog.premai.io/load-testing-llms-tools-metrics-realistic-traffic-simulation-2026/))
- NVIDIA NIM — Introduction to LLM Inference Benchmarking ([link](https://docs.nvidia.com/nim/large-language-models/1.0.0/benchmarking.html))
- k6 Operator ([link](https://github.com/grafana/k6-operator))
- [[Resources/LLMPerf|LLMPerf]] ([link](https://github.com/ray-project/llmperf)) ·  also cited by 1 other lesson
- TianPan — Load Testing LLM Applications ([link](https://tianpan.co/blog/2026-03-19-load-testing-llm-applications))
- TrueFoundry — LLM-Locust ([link](https://www.truefoundry.com/blog/llm-locust-a-tool-for-benchmarking-llm-performance))

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 9, required


%% ── my notes ── %%
