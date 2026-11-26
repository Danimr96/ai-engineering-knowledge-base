---
id: "lesson:11/11"
type: lesson
ref: 11/11
phase: 11
num: 11
title: "Caching, Rate Limiting & Cost Optimization"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 41
aliases:
  - 11/11
  - 11-11
tags:
  - phase/11
  - type/build
  - community/41
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/11-caching-cost/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/11-caching-cost"
---

# 11/11 Caching, Rate Limiting & Cost Optimization

> Most AI startups do not die from bad models. They die from bad unit economics. A single GPT-4o call costs fractions of a cent. Ten thousand users making ten calls per day costs $250 in input tokens alone -- before you charge a single dollar. The companies that survive are the ones that treat every API call as a financial transaction, not a function call.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/11-caching-cost/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/11-caching-cost) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/11-caching-cost) · code: caching_cost.py  
**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 Lesson 09 (Function Calling)`

- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-15 Prompt Caching and Context Caching|11/15 Prompt Caching and Context Caching]]

## Concepts taught

- [[Concepts/Prompt Cache|Prompt Cache]] (as *Prompt caching*) `glossary` — Provider-level caching where repeated prompt prefixes get a discount (90% Anthropic, 50% OpenAI) -- no code changes for OpenAI, explicit markers for Anthropic
- [[Concepts/Semantic caching|Semantic caching]] `lesson term` — Embedding the query, computing similarity to past queries, and returning the cached response if similarity exceeds a threshold -- catches paraphrases that exact matching misses
- Exact caching `lesson term` — Hashing the full prompt (model + messages + temperature) and returning the cached response for identical inputs -- only works for temperature=0 deterministic calls
- [[Concepts/Token bucket|Token bucket]] `lesson term` — An algorithm where each user has a bucket of N tokens that refills at rate R per second -- allows bursts up to N while enforcing an average rate of R
- [[Concepts/Model routing|Model routing]] `lesson term` — Using a classifier to send simple queries to cheap models (GPT-4o-mini, Haiku) and complex queries to expensive models (GPT-4o, Opus) -- saves 40-70% on model costs
- [[Concepts/Cost tracking|Cost tracking]] `lesson term` — Logging every API call with model, tokens, latency, cost, and user ID so you know exactly where money goes and which features are expensive
- [[Concepts/Circuit Breaker|Circuit Breaker]] `glossary` — Automatically degrading service (cheaper models, cached-only) or stopping requests entirely when spending approaches the budget limit
- [[Concepts/Batch API|Batch API]] `lesson term` — OpenAI's asynchronous processing at 50% discount -- submit up to 50,000 requests, get results within 24 hours
- Prompt compression `lesson term` — Rewriting system prompts and context to use fewer tokens while preserving meaning -- shorter prompts cost less and often perform better
- [[Concepts/Cache hit rate|Cache hit rate]] `lesson term` — The percentage of requests served from cache instead of calling the LLM -- 40-60% is typical for production chatbots, saves proportionally on cost

## Ships

- [[Artifacts/11-11 prompt-cost-optimizer|prompt-cost-optimizer]] `prompt` — Analyze an LLM application and recommend specific cost optimizations with projected savings
- [[Artifacts/11-11 skill-cost-patterns|skill-cost-patterns]] `skill` — Decision framework for LLM cost optimization -- caching strategies, rate limiting, model routing, and budget controls

## Further reading

- [[Resources/Dao (2023). FlashAttention-2- Faster Attention with Better Parallelism and Work Partitioning|Dao (2023). FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]] ([link](https://arxiv.org/abs/2307.08691)) — kernel-level cost reduction orthogonal to prompt caching; read alongside speculative decoding and GQA for the full cost-curve picture. ·  also cited by 2 other lessons
- [[Resources/Efficient Memory Management for Large Language Model Serving with PagedAttention|Efficient Memory Management for Large Language Model Serving with PagedAttention]] ([link](https://arxiv.org/abs/2309.06180)) — the vLLM paper; why paged KV-cache + continuous batching beat naive servers 24× on throughput, the infra layer under "caching and cost." ·  also cited by 2 other lessons
- [[Resources/Anthropic Prompt Caching Guide|Anthropic Prompt Caching Guide]] ([link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)) — the official docs for Anthropic's explicit cache_control markers, pricing, and cache lifetime behavior ·  also cited by 3 other lessons
- Martian Model Router ([link](https://docs.withmartian.com)) — production model routing that automatically selects the cheapest model capable of handling each query
- [[Resources/GPTCache|GPTCache]] ([link](https://github.com/zilliztech/GPTCache)) — open-source semantic caching library supporting multiple embedding backends, vector stores, and eviction policies ·  also cited by 1 other lesson
- [[Resources/Helicone|Helicone]] ([link](https://www.helicone.ai)) — LLM observability platform with cost tracking, caching, rate limiting, and budget alerts as a proxy layer ·  also cited by 1 other lesson
- [[Resources/Not Diamond|Not Diamond]] ([link](https://www.notdiamond.ai)) — ML-based model router that learns from your traffic patterns to optimize cost/quality tradeoffs across providers ·  also cited by 1 other lesson
- [[Resources/OpenAI Batch API|OpenAI Batch API]] ([link](https://platform.openai.com/docs/guides/batch)) — 50% discount for asynchronous processing, JSONL format, 24-hour completion window, and 50K request limits ·  also cited by 1 other lesson
- [[Resources/OpenAI Prompt Caching|OpenAI Prompt Caching]] ([link](https://platform.openai.com/docs/guides/prompt-caching)) — OpenAI's automatic caching, how to verify cache hits via usage fields, and minimum prefix lengths ·  also cited by 2 other lessons
- The Tail at Scale ([link](https://research.google/pubs/the-tail-at-scale/)) — latency, throughput, TTFT/TPOT percentiles, and hedged requests; the cost model behind "pick the cheapest model that still meets P95."

## In learning paths

- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 8, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 7, required


%% ── my notes ── %%
