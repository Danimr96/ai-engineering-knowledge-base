---
id: "lesson:17/02"
type: lesson
ref: 17/02
phase: 17
num: 2
title: "Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
community: 77
aliases:
  - 17/02
  - 17-02
tags:
  - phase/17
  - type/learn
  - community/77
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/02-inference-platform-economics/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/02-inference-platform-economics"
---

# 17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale

> The 2026 inference market is no longer GPU time rental. It bifurcates into custom silicon (Groq, Cerebras, SambaNova), GPU platforms (Baseten, Together, Fireworks, Modal), and API-first marketplaces (Replicate, DeepInfra). Fireworks raised price $1/hr per GPU on May 1, 2026, and $4B valuation on 10T+ tokens/day tells you the volume-driven model works. Baseten closed $300M Series E at $5B in January 2026. The competitive positioning rule is simple: Fireworks optimizes latency, Together optimizes catalog breadth, Baseten optimizes enterprise polish, Modal optimizes Python-native DX, Replicate optimizes multimodal reach, Anyscale optimizes distributed Python. This lesson gives you a matrix you can hand a founder.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/02-inference-platform-economics/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/02-inference-platform-economics) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/02-inference-platform-economics) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Togeth|77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale · GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 01 (Managed LLM Platforms), Phase 17 · 04 (Serving Engine Internals)`

- [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]] — Managed LLM Platforms
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

## Builds on this

- [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]]
- [[Lessons/17-10 Cold Start Mitigation for Serverless LLMs|17/10 Cold Start Mitigation for Serverless LLMs]]

## Concepts taught

- Custom silicon `lesson term` — Groq LPU, Cerebras WSE, SambaNova RDU — optimized for decode
- FireAttention `lesson term` — Custom attention kernel; marketed at 4x lower latency than vLLM
- Truss `lesson term` — Model packaging manifest; dependencies + secrets + serving config
- Per-token `lesson term` — Charge by tokens consumed; pay for no idle
- Per-minute `lesson term` — Charge by wall-clock GPU time; wins at high utilization
- Per-prediction `lesson term` — Charge per model invocation; common for image/video
- RayTurbo `lesson term` — Proprietary inference on Ray; competes with vLLM on Ray clusters
- Batch tier `lesson term` — Non-interactive queue at reduced rate; common on Fireworks, OpenAI
- Fine-tuned at base rate `lesson term` — Charge LoRA-served requests at base model's rate (differentiator)

## Ships

- [[Artifacts/17-02 inference-platform-picker|inference-platform-picker]] `skill` — Pick an inference platform (Fireworks, Together, Baseten, Modal, Replicate, Anyscale, or custom silicon) given workload, SLA, budget, and operational constraints. Normalize per-token, per-minute, and per-prediction pricing.

## Further reading

- Anyscale Pricing ([link](https://www.anyscale.com/pricing)) — RayTurbo and managed Ray pricing.
- Baseten Pricing ([link](https://www.baseten.co/pricing/)) — per-minute rates, committed capacity, enterprise tiers.
- Fireworks Pricing ([link](https://fireworks.ai/pricing)) — per-token rates, batch tier, GPU rental.
- Infrabase — AI Inference API Providers 2026 ([link](https://infrabase.ai/blog/ai-inference-api-providers-compared)) — vendor landscape.
- Modal Pricing ([link](https://modal.com/pricing)) — per-second GPU rates and free tier.
- Northflank — Fireworks AI Alternatives ([link](https://northflank.com/blog/7-best-fireworks-ai-alternatives-for-inference)) — comparative assessment.
- Together AI Pricing ([link](https://www.together.ai/pricing)) — model catalog and per-token rates.


%% ── my notes ── %%
