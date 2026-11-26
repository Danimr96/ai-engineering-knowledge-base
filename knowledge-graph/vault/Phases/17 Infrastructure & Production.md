---
id: "phase:17"
type: phase
num: 17
title: "Infrastructure & Production"
hours: 32.0
lessons: 28
done: 0
aliases:
  - Phase 17
tags:
  - phase
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production"
---

# Phase 17: Infrastructure & Production

**Lessons:** 28 · **Estimated:** 32 h · **Done:** 0 · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production)

## Position in the curriculum

- Requires: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]]
- Unlocks: [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]]

## Lessons

| # | Lesson | Type | Time | Status | Concepts |
|---|---|---|---|---|---|
| 01 | [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]] | learn | 60 |  | 9 |
| 02 | [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]] | learn | 60 |  | 9 |
| 03 | [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] | learn | 75 |  | 11 |
| 04 | [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] | learn | 75 |  | 12 |
| 05 | [[Lessons/17-05 EAGLE-3 Speculative Decoding in Production|EAGLE-3 Speculative Decoding in Production]] | learn | 60 |  | 9 |
| 06 | [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|Prefix-Cache Serving — RadixAttention and KV Reuse]] | learn | 75 |  | 8 |
| 07 | [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]] | learn | 75 |  | 8 |
| 08 | [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]] | learn | 60 |  | 14 |
| 09 | [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]] | learn | 75 |  | 9 |
| 10 | [[Lessons/17-10 Cold Start Mitigation for Serverless LLMs|Cold Start Mitigation for Serverless LLMs]] | learn | 60 |  | 10 |
| 11 | [[Lessons/17-11 Multi-Region LLM Serving and KV Cache Locality|Multi-Region LLM Serving and KV Cache Locality]] | learn | 60 |  | 9 |
| 12 | [[Lessons/17-12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU-WebLLM, Jetson|Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson]] | learn | 60 |  | 10 |
| 13 | [[Lessons/17-13 LLM Observability Stack Selection|LLM Observability Stack Selection]] | learn | 60 |  | 10 |
| 14 | [[Lessons/17-14 Prompt Caching and Semantic Caching Economics|Prompt Caching and Semantic Caching Economics]] | learn | 60 |  | 9 |
| 15 | [[Lessons/17-15 Batch APIs — the 50% Discount as Industry Standard|Batch APIs — the 50% Discount as Industry Standard]] | learn | 45 |  | 8 |
| 16 | [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|Model Routing as a Cost-Reduction Primitive]] | learn | 60 |  | 9 |
| 17 | [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]] | learn | 75 |  | 12 |
| 18 | [[Lessons/17-18 Production Serving Stack — KV Offloading and Cache-Aware Routing|Production Serving Stack — KV Offloading and Cache-Aware Routing]] | learn | 60 |  | 8 |
| 19 | [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]] | learn | 60 |  | 11 |
| 20 | [[Lessons/17-20 Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs|Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs]] | learn | 60 |  | 10 |
| 21 | [[Lessons/17-21 A-B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem|A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem]] | learn | 60 |  | 11 |
| 22 | [[Lessons/17-22 Load Testing LLM APIs — Why k6 and Locust Lie|Load Testing LLM APIs — Why k6 and Locust Lie]] | build | 75 |  | 11 |
| 23 | [[Lessons/17-23 SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection|SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection]] | learn | 60 |  | 10 |
| 24 | [[Lessons/17-24 Chaos Engineering for LLM Production|Chaos Engineering for LLM Production]] | learn | 60 |  | 9 |
| 25 | [[Lessons/17-25 Security — Secrets, API Key Rotation, Audit Logs, Guardrails|Security — Secrets, API Key Rotation, Audit Logs, Guardrails]] | learn | 60 |  | 11 |
| 26 | [[Lessons/17-26 Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001|Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001]] | learn | 60 |  | 9 |
| 27 | [[Lessons/17-27 FinOps for LLMs — Unit Economics and Multi-Tenant Attribution|FinOps for LLMs — Unit Economics and Multi-Tenant Attribution]] | learn | 60 |  | 10 |
| 28 | [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]] | learn | 45 |  | 10 |


%% ── my notes ── %%
