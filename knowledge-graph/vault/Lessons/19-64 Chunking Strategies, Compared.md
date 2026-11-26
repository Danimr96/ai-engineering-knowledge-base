---
id: "lesson:19/64"
type: lesson
ref: 19/64
phase: 19
num: 64
title: "Chunking Strategies, Compared"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 5
prereqs: 13
community: 3
aliases:
  - 19/64
  - 19-64
tags:
  - phase/19
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/64-chunking-strategies-advanced/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/64-chunking-strategies-advanced"
---

# 19/64 Chunking Strategies, Compared

> Chunking decides what your retriever can ever surface. Get the boundaries wrong and no embedding model, no reranker, no LLM can repair the damage downstream.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/64-chunking-strategies-advanced/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/64-chunking-strategies-advanced) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/64-chunking-strategies-advanced) · code: main.py, tests/test_chunkers.py · quiz: 6 questions  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 lessons 04 (embeddings), 06 (RAG), 07 (advanced RAG); Phase 19 Track B foundations (lessons 20-29)`

- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — embeddings
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — RAG
- [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]] — advanced RAG
- **19/20-29**:
    - [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
    - [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
    - [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
    - [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
    - [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]
    - [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]]
    - [[Lessons/19-26 Capstone Lesson 26- Sandbox Runner with Denylist and Path Jail|19/26 Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail]]
    - [[Lessons/19-27 Capstone Lesson 27- Eval Harness with Fixture Tasks|19/27 Capstone Lesson 27: Eval Harness with Fixture Tasks]]
    - [[Lessons/19-28 Capstone Lesson 28- Observability with OTel GenAI Spans and Prometheus Metrics|19/28 Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics]]
    - [[Lessons/19-29 Capstone Lesson 29- End-to-End Coding Agent on the Harness|19/29 Capstone Lesson 29: End-to-End Coding Agent on the Harness]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]], [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]], [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]], [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]], [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]], [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-38 Verification Gates|14/38 Verification Gates]], [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]], [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]], [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]], [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]], [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]], [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]], [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]], [[Lessons/14-11 Planning with HTN and Evolutionary Search|14/11 Planning with HTN and Evolutionary Search]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]], [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]], [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]], [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]], [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]], [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]], [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]], [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]], [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]], [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]], [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]], [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]], [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]], [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]], [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]], [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]], [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]

## Builds on this

- [[Lessons/19-65 Hybrid Retrieval with BM25 and Dense Embeddings|19/65 Hybrid Retrieval with BM25 and Dense Embeddings]]
- [[Lessons/19-67 Query Rewriting- HyDE, Multi-Query, and Decomposition|19/67 Query Rewriting: HyDE, Multi-Query, and Decomposition]]
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]]
- [[Lessons/19-69 End-to-End RAG System|19/69 End-to-End RAG System]]

## Concepts taught

- [[Concepts/Recall@K|Recall@K]] `glossary` — Fraction of queries where any of the top-k chunks overlaps the gold answer span
- Chunk overlap `lesson term` — Re-include the last N characters of the previous chunk in the next chunk
- Structural splitter `lesson term` — Cut at H1/H2/H3 boundaries; the heading text is part of the chunk
- Semantic chunker `lesson term` — Embed sentences, cluster by centroid similarity, cut on drift
- Centroid drift `lesson term` — Cosine similarity between the running mean and the next sentence drops past a threshold

## Further reading

- [[Resources/Anthropic — Contextual Retrieval|Anthropic — Contextual Retrieval]] ([link](https://www.anthropic.com/news/contextual-retrieval)) ·  also cited by 3 other lessons
- LongRAG: Enhancing Retrieval-Augmented Generation with Long-context LLMs (arXiv 2406.15319) ([link](https://arxiv.org/abs/2406.15319))
- LlamaIndex, Chunking strategies for production RAG ([link](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/))


%% ── my notes ── %%
