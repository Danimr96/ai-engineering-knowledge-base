---
id: "lesson:17/01"
type: lesson
ref: 17/01
phase: 17
num: 1
title: "Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 9
prereqs: 0
community: 77
aliases:
  - 17/01
  - 17-01
tags:
  - phase/17
  - type/learn
  - community/77
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/01-managed-llm-platforms/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/01-managed-llm-platforms"
---

# 17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI

> Three hyperscalers, three distinct strategies. AWS Bedrock is a model marketplace — Claude, Llama, Titan, Stability, Cohere behind one API. Azure OpenAI is an exclusive OpenAI partnership plus Provisioned Throughput Units (PTUs) for dedicated capacity. Vertex AI is Gemini-first with the best long-context and multimodal story. In 2026 Artificial Analysis measures Azure OpenAI at ~50 ms median and Bedrock at ~75 ms on Llama 3.1 405B equivalents — PTUs explain the gap because dedicated capacity beats shared on-demand. The decision rule is not "which is fastest" but "which model catalog and FinOps surface match my product." This lesson teaches you to pick with the tradeoffs written down, not vibes.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/01-managed-llm-platforms/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/01-managed-llm-platforms) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/01-managed-llm-platforms) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Togeth|77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale · GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 (LLM Engineering), Phase 13 (Tools & Protocols)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM Engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — Tools & Protocols ·  medium confidence

## Builds on this

- [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]]
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]
- [[Lessons/17-16 Model Routing as a Cost-Reduction Primitive|17/16 Model Routing as a Cost-Reduction Primitive]]
- [[Lessons/17-19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost|17/19 AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost]]

## Concepts taught

- Bedrock `lesson term` — Model marketplace across Claude, Llama, Titan, Mistral, Cohere
- Azure OpenAI `lesson term` — Exclusive OpenAI models in Azure datacenters with enterprise controls
- Vertex AI `lesson term` — Gemini-first platform with Model Garden for third-party models
- PTU `lesson term` — Provisioned Throughput Unit — reserved inference GPUs, priced per hour
- Application Inference Profile `lesson term` — Per-product cost/usage profile with tags, CloudWatch-native
- Model Garden `lesson term` — Vertex AI's third-party model section, separate from Gemini
- Two-provider minimum `lesson term` — Policy of running every critical LLM path across ≥2 hyperscalers
- BAA `lesson term` — Business Associate Agreement; required for PHI; provided by all three
- Abuse monitoring `lesson term` — Provider-side safety scan on prompts/outputs; opt-out in enterprise

## Ships

- [[Artifacts/17-01 managed-platform-picker|managed-platform-picker]] `skill` — Pick a managed LLM platform (Bedrock, Azure OpenAI, Vertex AI) and a second for redundancy, given workload, SLA, and compliance requirements — then produce a FinOps instrumentation plan.

## Further reading

- Artificial Analysis LLM Leaderboard ([link](https://artificialanalysis.ai/)) — continuous latency and throughput benchmarks across providers.
- AWS Bedrock Pricing ([link](https://aws.amazon.com/bedrock/pricing/)) — authoritative rate card and Provisioned Throughput pricing.
- Azure OpenAI Service Pricing ([link](https://azure.microsoft.com/en-us/pricing/details/azure-openai/)) — PTU economics and rate cards.
- Vertex AI Generative AI Pricing ([link](https://cloud.google.com/vertex-ai/generative-ai/pricing)) — Gemini tiers and Model Garden surcharges.
- Finout — Bedrock vs Vertex vs Azure FinOps ([link](https://www.finout.io/blog/bedrock-vs.-vertex-vs.-azure-cognitive-a-finops-comparison-for-ai-spend)) — attribution mechanics side-by-side.
- The AI Journal — AWS Bedrock vs Azure OpenAI CTO Guide 2026 ([link](https://theaijournal.co/2026/03/aws-bedrock-vs-azure-openai/)) — enterprise decision framework.


%% ── my notes ── %%
