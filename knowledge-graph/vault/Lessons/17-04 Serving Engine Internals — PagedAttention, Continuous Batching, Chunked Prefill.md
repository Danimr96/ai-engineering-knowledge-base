---
id: "lesson:17/04"
type: lesson
ref: 17/04
phase: 17
num: 4
title: "Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 12
prereqs: 1
community: 28
aliases:
  - 17/04
  - 17-04
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/04-vllm-serving-internals/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/04-vllm-serving-internals"
---

# 17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill

> Modern serving-engine throughput rests on three compounding defaults, not a single trick. PagedAttention is always on. Continuous batching injects new requests into the active batch between decode iterations. Chunked prefill slices long prompts so decode tokens never starve. Turn all three on and a Llama 3.3 70B FP8 on one H100 SXM5 pushes 2,200-2,400 tok/s at 128 concurrent — roughly 25% above vLLM's own default and 3-4x a naive PyTorch loop. This lesson reads the scheduler and attention kernel of vLLM — the reference engine for all three techniques — at a level you can diagram, and ends with a toy continuous batcher in `code/main.py` that schedules prefill and decode the way vLLM does.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/04-vllm-serving-internals/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/04-vllm-serving-internals) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/04-vllm-serving-internals) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 01 (Model Serving), Phase 11 (LLM Engineering)`

- [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]] — Model Serving
- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM Engineering ·  medium confidence

## Builds on this

- [[Lessons/17-02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale|17/02 Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale]]
- [[Lessons/17-03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling|17/03 GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling]]
- [[Lessons/17-05 EAGLE-3 Speculative Decoding in Production|17/05 EAGLE-3 Speculative Decoding in Production]]
- [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]]
- [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]]
- [[Lessons/17-08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99|17/08 Inference Metrics — TTFT, TPOT, ITL, Goodput, P99]]
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]]
- [[Lessons/17-11 Multi-Region LLM Serving and KV Cache Locality|17/11 Multi-Region LLM Serving and KV Cache Locality]]
- [[Lessons/17-12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU-WebLLM, Jetson|17/12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson]]
- [[Lessons/17-14 Prompt Caching and Semantic Caching Economics|17/14 Prompt Caching and Semantic Caching Economics]]
- [[Lessons/17-17 Disaggregated Prefill-Decode — NVIDIA Dynamo and llm-d|17/17 Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d]]
- [[Lessons/17-18 Production Serving Stack — KV Offloading and Cache-Aware Routing|17/18 Production Serving Stack — KV Offloading and Cache-Aware Routing]]
- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Concepts taught

- [[Concepts/PagedAttention|PagedAttention]] `lesson term` — Fixed-size block allocator for KV cache; fragmentation <4%
- Block table `lesson term` — Per-sequence map from logical token position to physical KV block
- [[Concepts/Continuous Batching|Continuous Batching]] `glossary` — Admit/release decisions made every decode iteration
- [[Concepts/Chunked Prefill|Chunked Prefill]] `glossary` — Break long prefill into 512-token slices interleaved with decode
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]] (as *TTFT*) `glossary` — Prefill + queue + network; dominated by prefill at long prompts
- [[Concepts/Inter-Token Latency (ITL)|Inter-Token Latency (ITL)]] (as *ITL*) `glossary` — Time between consecutive decode tokens; dominated by batch size
- [[Concepts/Goodput|Goodput]] `glossary` — Tokens/sec where every request still hit TTFT and ITL targets
- V1 scheduler `lesson term` — vLLM's 2026 scheduler; N-gram spec decode is the chunked-prefill-compatible path
- --gpu-memory-utilization `lesson term` — Fraction of HBM reserved for KV blocks after weights and activations
- [[Concepts/Dynamic Batching|Dynamic Batching]] `glossary` — A runtime policy that forms inference batches from queued requests according to compatible shapes, maximum size, priority, and allowed queue delay.
- [[Concepts/Paged KV Cache|Paged KV Cache]] `glossary` — A KV-cache memory manager that stores attention state in fixed-size blocks and maps logical sequence positions to physical blocks instead of requiring one contiguous allocation per sequence.

## Ships

- [[Artifacts/17-04 vllm-scheduler-reader|vllm-scheduler-reader]] `skill` — Diagnose a vLLM serving config by reading the scheduler-level knobs and identifying which of PagedAttention, continuous batching, and chunked prefill is the bottleneck.

## Further reading

- Aleksa Gordic — Inside vLLM ([link](https://www.aleksagordic.com/blog/vllm)) — detailed V1 scheduler walkthrough with flame graphs.
- [[Resources/Efficient Memory Management for Large Language Model Serving with PagedAttention|Efficient Memory Management for Large Language Model Serving with PagedAttention]] ([link](https://arxiv.org/abs/2309.06180)) — fragmentation analysis and scheduler design. ·  also cited by 2 other lessons
- vLLM Blog — PagedAttention ([link](https://blog.vllm.ai/2023/06/20/vllm.html)) — the original write-up that still defines how to think about the allocator.
- vLLM Release Notes (NVIDIA) ([link](https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html)) — 2026 release cadence and version-specific behavior.
- [[Resources/vLLM documentation — Speculative Decoding|vLLM documentation — Speculative Decoding]] ([link](https://docs.vllm.ai/en/latest/features/spec_decode/)) — official source on chunked-prefill and speculative-decoding compatibility. ·  also cited by 1 other lesson


%% ── my notes ── %%
