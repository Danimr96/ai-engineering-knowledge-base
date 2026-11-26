---
id: "lesson:11/13"
type: lesson
ref: 11/13
phase: 11
num: 13
title: Building a Production LLM Application
lesson_type: capstone
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 13
prereqs: 14
community: 41
aliases:
  - 11/13
  - 11-13
tags:
  - phase/11
  - type/capstone
  - community/41
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/13-production-app/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/13-production-app"
---

# 11/13 Building a Production LLM Application

> You have built prompts, embeddings, RAG pipelines, function calling, caching layers, and guardrails. Separately. In isolation. Like practicing guitar scales without ever playing a song. This lesson is the song. You will wire every component from Lessons 01-12 into a single production-ready service. Not a toy. Not a demo. A system that handles real traffic, fails gracefully, streams tokens, tracks costs, and survives its first 10,000 users.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build (Capstone) · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/13-production-app/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/13-production-app) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/13-production-app) · code: production_app.py  
**Community:** [[Communities/41 Prompt Cache · Cache hit rate · Model routing|41 Prompt Cache · Cache hit rate · Model routing]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 Lessons 01-15`

- **11/01-15**:
    - [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
    - [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]]
    - [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
    - [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]]
    - [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]]
    - [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
    - [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]]
    - [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]]
    - [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]]
    - [[Lessons/11-10 Evaluation & Testing LLM Applications|11/10 Evaluation & Testing LLM Applications]]
    - [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]]
    - [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]]
    - [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]]
    - [[Lessons/11-15 Prompt Caching and Context Caching|11/15 Prompt Caching and Context Caching]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Concepts taught

- API Gateway `lesson term` — The entry point that handles authentication, rate limiting, CORS, and request routing before any LLM logic runs
- Prompt Router `lesson term` — Logic that picks the right prompt template based on request type, A/B experiment assignment, and user context
- [[Concepts/Semantic Cache|Semantic Cache]] `glossary` — A cache keyed by embedding similarity rather than exact string match -- two differently-phrased identical questions return the same cached response
- SSE (Server-Sent Events) `lesson term` — A unidirectional HTTP protocol where the server pushes events to the client -- used by OpenAI, Anthropic, and Google for token-by-token delivery
- Exponential Backoff `lesson term` — Waiting 1s, 2s, 4s, 8s between retries (doubling each time) with random jitter to prevent all clients retrying simultaneously
- [[Concepts/Fallback Chain|Fallback Chain]] `lesson term` — An ordered list of models tried in sequence -- when the primary fails, fall through to cheaper or more available alternatives
- [[Concepts/Graceful Degradation|Graceful Degradation]] `glossary` — When a secondary component fails (cache, RAG, guardrails), the system continues with reduced functionality rather than crashing
- Cost Per Request `lesson term` — The total LLM spend (input tokens + output tokens at model pricing) for a single user request -- the number that determines if your business model works
- [[Concepts/Shadow Mode|Shadow Mode]] `lesson term` — Running a new prompt or model on real traffic but only logging results, not showing them to users -- risk-free A/B testing
- [[Concepts/Health check|Health check]] `lesson term` — An endpoint that returns the status of all dependencies (cache, LLM availability, guardrails) -- used by load balancers and Kubernetes to route traffic
- [[Concepts/Readiness Probe|Readiness Probe]] `glossary` — A diagnostic that tells the traffic-routing layer whether a service instance is currently able to accept requests.
- [[Concepts/Streaming|Streaming]] `glossary` — Delivering incremental response events before the complete result is ready. A stream may contain token text, structured deltas, tool-call arguments, usage metadata, or status events depending on the API.

## Ships

- [[Artifacts/11-13 prompt-architecture-reviewer|prompt-architecture-reviewer]] `prompt` — Review the architecture of any LLM application against a production readiness checklist -- identifies gaps, risks, and missing components
- [[Artifacts/11-13 skill-production-checklist|skill-production-checklist]] `skill` — Decision framework for shipping LLM applications to production -- covers every component with specific thresholds and pass/fail criteria

## Further reading

- [[Resources/Anthropic API Reference|Anthropic API Reference]] ([link](https://docs.anthropic.com/en/api/messages-streaming)) — streaming implementation details for Claude, including server-sent events and tool use during streaming ·  also cited by 1 other lesson
- [[Resources/vLLM documentation|vLLM documentation]] ([link](https://docs.vllm.ai/)) — PagedAttention-based serving: the default self-hosted inference layer used under the FastAPI capstone in this lesson. ·  also cited by 2 other lessons
- Eugene Yan, "Patterns for Building LLM-based Systems ([link](https://eugeneyan.com/writing/llm-patterns/)) — architectural patterns (guardrails, RAG, caching, routing) seen across production LLM deployments at major tech companies
- FastAPI Documentation ([link](https://fastapi.tiangolo.com/)) — the async Python framework used in this lesson, with native SSE streaming and automatic OpenAPI docs
- [[Resources/GPTCache|GPTCache]] ([link](https://github.com/zilliztech/GPTCache)) — production semantic caching library that implements the concepts from this lesson at scale ·  also cited by 1 other lesson
- Hamel Husain, "Your AI Product Needs Evals ([link](https://hamel.dev/blog/posts/evals/)) — the definitive guide on evaluation-driven development for LLM applications, complementing the eval component in this capstone
- Hamel Husain -- Optimizing Latency: TGI vs vLLM vs CTranslate2 vs mlc ([link](https://hamel.dev/notes/llm/inference/03_inference.html)) — measured comparison of throughput and latency across the main serving frameworks.
- Hugging Face TGI ([link](https://huggingface.co/docs/text-generation-inference/index)) — Text Generation Inference: Rust server with continuous batching, Flash Attention, and Medusa speculative decoding; the HF-native alternative to vLLM.
- [[Resources/NVIDIA TensorRT-LLM documentation|NVIDIA TensorRT-LLM documentation]] ([link](https://nvidia.github.io/TensorRT-LLM/)) — the highest-throughput path on NVIDIA hardware; quantization, in-flight batching, and FP8 kernels for enterprise deployments. ·  also cited by 1 other lesson
- OpenTelemetry Python SDK ([link](https://opentelemetry.io/docs/languages/python/)) — the standard for distributed tracing, used to instrument every component of an LLM pipeline
- OpenAI Production Best Practices ([link](https://platform.openai.com/docs/guides/production-best-practices)) — rate limits, error handling, and scaling guidance from the largest LLM API provider

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 10, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 10, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 9, required
- [[Paths/Customer AI Deployment|Customer AI Deployment]] — step 8, required


%% ── my notes ── %%
