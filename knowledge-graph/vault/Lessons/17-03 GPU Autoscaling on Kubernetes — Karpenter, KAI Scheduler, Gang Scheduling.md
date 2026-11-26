---
id: "lesson:17/03"
type: lesson
ref: 17/03
phase: 17
num: 3
title: "GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling"
lesson_type: learn
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
  - 17/03
  - 17-03
tags:
  - phase/17
  - type/learn
  - community/77
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes"
---

# 17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling

> Three layers, not one. Karpenter provisions nodes dynamically (under one minute, 40% faster than Cluster Autoscaler). KAI Scheduler handles gang scheduling, topology awareness, and hierarchical queues — it prevents the 7-of-8 partial allocation trap where seven nodes wait and burn on one missing GPU. Application-level autoscalers (NVIDIA Dynamo Planner, llm-d Workload Variant Autoscaler) scale on inference-specific signals — queue depth, KV cache utilization — not CPU/DCGM duty cycle. The classic HPA trap is that `DCGM_FI_DEV_GPU_UTIL` is a duty-cycle measurement: 100% could be 10 requests or 100. vLLM pre-allocates KV cache memory, so memory never triggers scale-down. This lesson teaches you to compose the three layers and avoid the default Karpenter `WhenEmptyOrUnderutilized` policy that terminates running GPU jobs mid-inference.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Togeth|77 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI · Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale · GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 02 (Inference Platform Economics), Phase 17 · 04 (Serving Engine Internals)`

- [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]] — Inference Platform Economics
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Builds on this

- [[Lessons/17-10 Cold Start Mitigation for Serverless LLMs|17/10 Cold Start Mitigation for Serverless LLMs]]
- [[Lessons/17-22 Load Testing LLM APIs — Why k6 and Locust Lie|17/22 Load Testing LLM APIs — Why k6 and Locust Lie]]

## Concepts taught

- Karpenter `lesson term` — Kubernetes node autoscaler; sub-minute provisioning
- Cluster Autoscaler `lesson term` — Kubernetes node autoscaler predecessor; slower, group-based
- KAI Scheduler `lesson term` — Secondary scheduler for gang + topology + queues
- Gang scheduling `lesson term` — Schedule N pods atomically or defer all of them
- Topology awareness `lesson term` — Place pods based on NVLink/IB/rack placement
- DCGM_FI_DEV_GPU_UTIL `lesson term` — Duty-cycle metric; NOT a scaling signal for LLMs
- Queue depth `lesson term` — Correct HPA signal for prefill-bound scaling
- KV cache utilization `lesson term` — Correct HPA signal for decode-bound scaling
- Consolidation `lesson term` — Node termination to cheaper instance type
- WhenEmpty + 1h `lesson term` — Policy that doesn't evict running GPU jobs
- [[Concepts/Autoscaling|Autoscaling]] `glossary` — A control loop that changes the number or capacity of serving workers from observed demand, resource use, or application metrics within configured bounds.

## Ships

- [[Artifacts/17-03 gpu-autoscaler-plan|gpu-autoscaler-plan]] `skill` — Design a three-layer GPU autoscaling plan (Karpenter + KAI Scheduler + application signals) for a Kubernetes-based LLM serving cluster. Diagnose DCGM_FI_DEV_GPU_UTIL traps and partial-allocation failures.

## Further reading

- [[Resources/NVIDIA — Disaggregated LLM Inference on Kubernetes|NVIDIA — Disaggregated LLM Inference on Kubernetes]] ([link](https://developer.nvidia.com/blog/deploying-disaggregated-llm-inference-workloads-on-kubernetes/)) — Dynamo Planner scaling signals. ·  also cited by 2 other lessons
- AWS EKS Compute and Autoscaling Best Practices ([link](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)) — managed-Kubernetes-specific guidance.
- Ray docs — KAI Scheduler for RayClusters ([link](https://docs.ray.io/en/latest/cluster/kubernetes/k8s-ecosystem/kai-scheduler.html)) — Ray integration pattern.
- KAI Scheduler GitHub ([link](https://github.com/kai-scheduler/KAI-Scheduler)) — design docs and configuration examples.
- [[Resources/llm-d GitHub|llm-d GitHub]] ([link](https://github.com/llm-d/llm-d)) — Workload Variant Autoscaler design. ·  also cited by 1 other lesson
- Karpenter Disruption Controls ([link](https://karpenter.sh/docs/concepts/disruption/)) — consolidation policy semantics and GPU-safe defaults.


%% ── my notes ── %%
