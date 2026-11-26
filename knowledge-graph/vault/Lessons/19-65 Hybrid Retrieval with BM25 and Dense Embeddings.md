---
id: "lesson:19/65"
type: lesson
ref: 19/65
phase: 19
num: 65
title: Hybrid Retrieval with BM25 and Dense Embeddings
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 6
prereqs: 13
community: 3
aliases:
  - 19/65
  - 19-65
tags:
  - phase/19
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense"
---

# 19/65 Hybrid Retrieval with BM25 and Dense Embeddings

> Lexical and semantic retrieval fail on opposite query distributions. Hybrid retrieval with reciprocal rank fusion does not interpolate, it votes - and the vote wins on every query class.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/65-hybrid-retrieval-bm25-dense/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense) · code: main.py, tests/test_hybrid.py · quiz: 6 questions  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 lessons 04 (embeddings), 06 (RAG); Phase 19 Track B foundations (lessons 20-29); Phase 19 lesson 64 (chunking strategies)`

- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]] — embeddings
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — RAG
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]] — chunking strategies
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

- depth 2: [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]], [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]], [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]], [[Lessons/11-07 Advanced RAG (Chunking, Reranking, Hybrid Search)|11/07 Advanced RAG (Chunking, Reranking, Hybrid Search)]], [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]], [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]], [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-38 Verification Gates|14/38 Verification Gates]], [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]], [[Lessons/14-42 Capstone- Ship a Reusable Agent Workbench Pack|14/42 Capstone: Ship a Reusable Agent Workbench Pack]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]], [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]], [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]], [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]], [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]], [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]], [[Lessons/14-11 Planning with HTN and Evolutionary Search|14/11 Planning with HTN and Evolutionary Search]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]], [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]], [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]], [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]], [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]], [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]], [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]], [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]], [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]], [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]], [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]], [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]], [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]], [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]], [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]], [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]], [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]

## Builds on this

- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]]
- [[Lessons/19-67 Query Rewriting- HyDE, Multi-Query, and Decomposition|19/67 Query Rewriting: HyDE, Multi-Query, and Decomposition]]
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]]
- [[Lessons/19-69 End-to-End RAG System|19/69 End-to-End RAG System]]

## Concepts taught

- [[Concepts/BM25|BM25]] `glossary` — Probabilistic ranking with idf x saturating tf x length normalization
- [[Concepts/Reciprocal Rank Fusion (RRF)|Reciprocal Rank Fusion (RRF)]] (as *RRF*) `glossary` — Sum of 1 / (k + rank) across ranked lists; k = 60 default
- k1 `lesson term` — Controls how fast a repeated term stops adding more score
- b `lesson term` — 0 means ignore document length, 1 means full normalization
- Field weighting `lesson term` — Repeat tokens during indexing to boost matches in that field
- Rank-based vs score-based fusion `lesson term` — Ranks are comparable across modalities; scores are not

## Further reading

- Vespa: Hybrid Retrieval with BM25 and Embeddings ([link](https://docs.vespa.ai/en/tutorials/hybrid-search.html))
- Weaviate: Hybrid Search ([link](https://weaviate.io/developers/weaviate/search/hybrid))


%% ── my notes ── %%
