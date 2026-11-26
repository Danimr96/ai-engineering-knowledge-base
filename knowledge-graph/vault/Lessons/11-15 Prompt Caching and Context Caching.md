---
id: "lesson:11/15"
type: lesson
ref: 11/15
phase: 11
num: 15
title: Prompt Caching and Context Caching
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 9
prereqs: 3
community: 41
aliases:
  - 11/15
  - 11-15
tags:
  - phase/11
  - type/build
  - community/41
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/15-prompt-caching/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/15-prompt-caching"
---

# 11/15 Prompt Caching and Context Caching

> Your system prompt is 4,000 tokens. Your RAG context is 20,000 tokens. You send both with every request. You also pay for both — every time. Prompt caching lets the provider keep that prefix warm on their side and bill you 10% of the normal rate on reuse. Used correctly, it cuts inference cost by 50–90% and first-token latency by 40–85%.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/15-prompt-caching/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/15-prompt-caching) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/15-prompt-caching) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 · 01 (Prompt Engineering), Phase 11 · 05 (Context Engineering), Phase 11 · 11 (Caching and Cost)`

- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — Prompt Engineering
- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]] — Context Engineering
- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]] — Caching and Cost

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]], [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]

## Concepts taught

- [[Concepts/Prompt Cache|Prompt Cache]] (as *Prompt caching*) `glossary` — Reusing a provider-side KV-cache for matching prefixes; 50-90% discount on repeated input tokens.
- [[Concepts/cache_control|cache_control]] `lesson term` — Content-block attribute that declares "everything up to here is cacheable"; {"type": "ephemeral"}.
- Cache write `lesson term` — The first request that populates the cache; billed at ~1.25x input rate on Anthropic, free on OpenAI.
- Cache read `lesson term` — Subsequent requests matching the prefix; billed at 10% (Anthropic), 50% (OpenAI), ~25% (Gemini).
- TTL `lesson term` — Seconds the cache stays warm; Anthropic 5m default (extendable 1h), OpenAI best-effort up to 1h, Gemini user-set.
- Extended TTL `lesson term` — {"type": "ephemeral", "ttl": "1h"}; 2x write premium but worth it for batch reuse.
- Prefix match `lesson term` — Caches only hit when every token from the start up to the breakpoint is byte-identical.
- Context caching (as *Context caching (Gemini)*) `lesson term` — Google's named, storage-billed cache object; best for multi-day reuse of large corpora.

## Ships

- [[Artifacts/11-15 prompt-caching-planner|prompt-caching-planner]] `skill` — Design a cache-friendly prompt layout and pick the right provider caching mode.

## Further reading

- Google — Context caching ([link](https://ai.google.dev/gemini-api/docs/caching)) — `CachedContent` API and storage pricing.
- Anthropic engineering — Prompt caching for long-context workloads ([link](https://www.anthropic.com/news/prompt-caching)) — original launch post with latency numbers.
- [[Resources/Pope et al., 2022 - -Efficiently Scaling Transformer Inference|Pope et al., 2022 -- "Efficiently Scaling Transformer Inference]] ([link](https://arxiv.org/abs/2211.05102)) — the KV-cache memory model that prompt caching exposes to users; explains why a cached prefix is ~10× cheaper to reread than to recompute. ·  also cited by 2 other lessons
- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — prompt caching sits alongside speculative decoding, Flash Attention, and MQA/GQA as levers that bend the inference cost curve; read this for the other three. ·  also cited by 7 other lessons
- [[Resources/Agrawal et al., -SARATHI- Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills- (2023)|Agrawal et al., "SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills" (2023)]] ([link](https://arxiv.org/abs/2308.16369)) — prefill is the phase prompt caching shortcuts; this paper explains why TTFT drops dramatically on cache hit while TPOT is unaffected. ·  also cited by 1 other lesson
- [[Resources/Anthropic Prompt Caching Guide|Anthropic Prompt Caching Guide]] ([link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)) — `cache_control`, 1h TTL, break-even tables. ·  also cited by 3 other lessons
- [[Resources/OpenAI Prompt Caching|OpenAI Prompt Caching]] ([link](https://platform.openai.com/docs/guides/prompt-caching)) — automatic prefix matching. ·  also cited by 2 other lessons


%% ── my notes ── %%
