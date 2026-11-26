---
id: "lesson:17/28"
type: lesson
ref: 17/28
phase: 17
num: 28
title: "Self-Hosted Serving Selection — Matching Engine to Hardware and Scale"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 10
prereqs: 5
community: 28
aliases:
  - 17/28
  - 17-28
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/28-self-hosted-serving-selection/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/28-self-hosted-serving-selection"
---

# 17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale

> Engine selection is a function of hardware, scale, and ecosystem — not a leaderboard read. Four engines dominate self-hosted inference in 2026: llama.cpp, Ollama, vLLM, SGLang, with TGI trailing in maintenance mode. **llama.cpp** is fastest on CPU — widest model support, full control over quantization and threading. **Ollama** is the dev-laptop one-command install, ~15-30% slower than llama.cpp (Go + CGo + HTTP serialization), 3x throughput gap under prod-like load. **TGI entered maintenance mode December 11, 2025** — only bug fixes, ~10% slower raw throughput than vLLM but historically top observability and HF-ecosystem integration. That maintenance status makes it a risky long-term bet — SGLang or vLLM are safer defaults for new projects. **vLLM** is the general-purpose production default — v0.15.1 (February 2026) adds PyTorch 2.10, RTX Blackwell SM120, H200 optimization. **SGLang** is the agentic multi-turn / prefix-heavy specialist — 400,000+ GPUs in production (xAI, LinkedIn, Cursor, Oracle, GCP, Azure, AWS). Hardware constraints: CPU-first → llama.cpp. AMD / non-NVIDIA → vLLM is the strongest-supported path (TRT-LLM is NVIDIA-locked). 2026 pipeline pattern: dev = Ollama, staging = llama.cpp, prod = vLLM or SGLang. The engines take different weight formats — GGUF for the llama.cpp family, HF safetensors for the GPU engines — so a format conversion may sit between stages.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/28-self-hosted-serving-selection/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/28-self-hosted-serving-selection) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/28-self-hosted-serving-selection) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `All Phase 17 lessons covering engines (04, 06, 07, 09, 18)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]]
- [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]]
- [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]]
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]]
- [[Lessons/17-18 Production Serving Stack — KV Offloading and Cache-Aware Routing|17/18 Production Serving Stack — KV Offloading and Cache-Aware Routing]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]], [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]

## Concepts taught

- llama.cpp `lesson term` — Widest model support, fastest on CPU
- Ollama `lesson term` — One-command install, dev-grade throughput
- TGI `lesson term` — Maintenance mode since Dec 2025
- vLLM `lesson term` — Broad production baseline 2026
- SGLang `lesson term` — Prefix-heavy, RadixAttention
- TRT-LLM `lesson term` — Blackwell throughput leader, NVIDIA only
- [[Concepts/GGUF|GGUF]] `lesson term` — Bundled K-quant variants
- [[Concepts/Production-stack|Production-stack]] `lesson term` — Phase 17 · 18 reference deployment
- Pipeline pattern `lesson term` — Ollama → llama.cpp → vLLM; weight formats differ per engine
- [[Concepts/Model Serving|Model Serving]] `glossary` — The runtime and API layer that loads versioned model artifacts, accepts inference requests, schedules execution, manages resources, and returns results under an operational contract.

## Ships

- [[Artifacts/17-28 engine-picker|engine-picker]] `skill` — Pick a self-hosted LLM engine (llama.cpp, Ollama, TGI, vLLM, SGLang) given hardware, scale, and workload. Name 2026 TGI maintenance mode as a migration trigger.

## Further reading

- AI Made Tools — vLLM vs Ollama vs llama.cpp vs TGI 2026 ([link](https://www.aimadetools.com/blog/vllm-vs-ollama-vs-llamacpp-vs-tgi/))
- PremAI — 10 Best vLLM Alternatives 2026 ([link](https://blog.premai.io/10-best-vllm-alternatives-for-llm-inference-in-production-2026/))
- n1n.ai — Comprehensive LLM Inference Engine Comparison ([link](https://explore.n1n.ai/blog/llm-inference-engine-comparison-vllm-tgi-tensorrt-sglang-2026-03-13))
- TGI maintenance announcement ([link](https://github.com/huggingface/text-generation-inference)) — release notes.
- [[Resources/vLLM 0.11.0 release notes|vLLM 0.11.0 release notes]] ([link](https://github.com/vllm-project/vllm/releases)) ·  also cited by 1 other lesson
- Morph — llama.cpp vs Ollama 2026 ([link](https://www.morphllm.com/comparisons/llama-cpp-vs-ollama))


%% ── my notes ── %%
