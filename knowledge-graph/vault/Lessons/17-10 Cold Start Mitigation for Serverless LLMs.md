---
id: "lesson:17/10"
type: lesson
ref: 17/10
phase: 17
num: 10
title: Cold Start Mitigation for Serverless LLMs
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 10
prereqs: 2
community: 77
aliases:
  - 17/10
  - 17-10
tags:
  - phase/17
  - type/learn
  - community/77
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/10-cold-start-mitigation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/10-cold-start-mitigation"
---

# 17/10 Cold Start Mitigation for Serverless LLMs

> A 20 GB model image takes 5-10 minutes (7B) to 20+ minutes (70B) to go from cold to serving. In a true serverless world, that is not a warm-up — it is an outage. Mitigations operate at five layers: pre-seeded node images (Bottlerocket on AWS, dual-volume arch), model streaming (NVIDIA Run:ai Model Streamer, native in vLLM), GPU memory snapshots (Modal checkpoints, up to 10x faster restart), warm pools (`min_workers=1`), tiered loading (ServerlessLLM's NVMe→DRAM→HBM pipeline, 10-200x latency reduction), and live migration that moves input tokens (KB) rather than KV cache (GB). Modal publishes 2-4s cold starts as a floor; Baseten 5-10s default, sub-second with pre-warming. This lesson teaches you to measure, budget, and stack the five layers.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/10-cold-start-mitigation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/10-cold-start-mitigation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/10-cold-start-mitigation) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Togeth|77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale · GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 02 (Inference Platform Economics), Phase 17 · 03 (GPU Autoscaling)`

- [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]] — Inference Platform Economics
- [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] — GPU Autoscaling

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]], [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]

## Concepts taught

- Cold start `lesson term` — Time from request to first token on a fresh replica
- Warm pool `lesson term` — min_workers >= 1 to keep at least one replica ready
- Pre-seeded image `lesson term` — Node image with container weights pre-resident
- Bottlerocket `lesson term` — AWS container-optimized OS with dual-volume snapshot support
- Model streamer `lesson term` — Overlap weights I/O with compute setup
- GPU snapshot `lesson term` — Serialize post-load GPU state; deserialize on restart
- Tiered loading `lesson term` — Hierarchy of storage tiers; load on demand
- Live migration `lesson term` — Transfer input (KB), recompute KV on destination
- min_workers `lesson term` — Serverless minimum keep-alive count
- Scale-to-zero `lesson term` — No cost when idle; accept full cold-start tax

## Ships

- [[Artifacts/17-10 cold-start-planner|cold-start-planner]] `skill` — Pick and stack cold-start mitigations for serverless LLM deployments. Budget phases (node, image, weights, engine, first forward) and match mitigations to SLA.

## Further reading

- Baseten — Cold-start mitigation ([link](https://www.baseten.co/blog/cold-start-mitigation/)) — pre-warming playbook.
- [[Resources/NVIDIA — Disaggregated LLM Inference on Kubernetes|NVIDIA — Disaggregated LLM Inference on Kubernetes]] ([link](https://developer.nvidia.com/blog/deploying-disaggregated-llm-inference-workloads-on-kubernetes/)) — live migration for disaggregated deployments. ·  also cited by 2 other lessons
- AWS Bottlerocket ([link](https://github.com/bottlerocket-os/bottlerocket)) — pre-seeded data volume snapshot pattern.
- NVIDIA Run:ai Model Streamer ([link](https://github.com/run-ai/runai-model-streamer)) — overlap weights load with compute setup.
- Modal — Cold start performance ([link](https://modal.com/docs/guide/cold-start)) — Modal's published benchmarks and checkpoint architecture.
- ServerlessLLM paper (USENIX OSDI'24) ([link](https://www.usenix.org/conference/osdi24/presentation/fu)) — tiered loading design.


%% ── my notes ── %%
