---
id: "lesson:19/27"
type: lesson
ref: 19/27
phase: 19
num: 27
title: "Capstone Lesson 27: Eval Harness with Fixture Tasks"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 12
concepts: 0
prereqs: 4
community: 3
aliases:
  - 19/27
  - 19-27
tags:
  - phase/19
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/27-eval-harness-fixture-tasks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/27-eval-harness-fixture-tasks"
---

# 19/27 Capstone Lesson 27: Eval Harness with Fixture Tasks

> A coding agent is only as good as the suite of tasks you measure it against. This lesson builds an evaluation harness that takes a folder of fixture tasks, runs each through a candidate agent, scores pass or fail through a deterministic verifier, and aggregates the results into pass@1, pass@k, mean latency, and mean cost. The harness is the source of truth that lets you tell a regression from a refactor.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/27-eval-harness-fixture-tasks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/27-eval-harness-fixture-tasks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/27-eval-harness-fixture-tasks) · code: main.py, tasks/task_001_fizzbuzz_offbyone/buggy/fizzbuzz.py, tasks/task_001_fizzbuzz_offbyone/expected/fizzbuzz.py, tasks/task_002_factorial_missing_return/buggy/factorial.py, tasks/task_002_factorial_missing_return/expected/factorial.py, tasks/task_003_error_message_typo/buggy/errors.py … · quiz: 6 questions  
**Track:** [[Tracks/19-A Agent harness from scratch|Phase 19 Track A: Agent harness from scratch]]  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 19 · 25 (verification gates), Phase 19 · 26 (sandbox runner), Phase 14 · 30 (eval-driven agent development), Phase 14 · 19 (SWE-bench and GAIA benchmarks)`

- [[Lessons/14-19 Benchmarks- SWE-bench, GAIA, AgentBench|14/19 Benchmarks: SWE-bench, GAIA, AgentBench]] — SWE-bench and GAIA benchmarks
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]] — eval-driven agent development
- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]] — verification gates
- [[Lessons/19-26 Capstone Lesson 26- Sandbox Runner with Denylist and Path Jail|19/26 Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail]] — sandbox runner

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]], [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]], [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]], [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]], [[Lessons/14-07 Agent Memory — Virtual Context and Memory Paging|14/07 Agent Memory — Virtual Context and Memory Paging]], [[Lessons/14-08 Memory Blocks and Sleep-Time Compute|14/08 Memory Blocks and Sleep-Time Compute]], [[Lessons/14-09 Hybrid Memory- Vector + Graph + KV|14/09 Hybrid Memory: Vector + Graph + KV]], [[Lessons/14-10 Skill Libraries and Lifelong Learning (Voyager)|14/10 Skill Libraries and Lifelong Learning (Voyager)]], [[Lessons/14-11 Planning with HTN and Evolutionary Search|14/11 Planning with HTN and Evolutionary Search]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]], [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]], [[Lessons/14-14 The Actor Model for Agents — Async Messages and Typed Runtimes|14/14 The Actor Model for Agents — Async Messages and Typed Runtimes]], [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]], [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]], [[Lessons/14-17 The Harness as a Library — Subagents and Session Store|14/17 The Harness as a Library — Subagents and Session Store]], [[Lessons/14-18 Production Agent Runtimes — Fast Instantiation and Typed Workflows|14/18 Production Agent Runtimes — Fast Instantiation and Typed Workflows]], [[Lessons/14-20 Benchmarks- WebArena and OSWorld|14/20 Benchmarks: WebArena and OSWorld]], [[Lessons/14-21 Computer Use- Claude, OpenAI CUA, Gemini|14/21 Computer Use: Claude, OpenAI CUA, Gemini]], [[Lessons/14-22 Voice Agents- Pipecat and LiveKit|14/22 Voice Agents: Pipecat and LiveKit]], [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]], [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]], [[Lessons/14-27 Prompt Injection and the PVE Defense|14/27 Prompt Injection and the PVE Defense]], [[Lessons/14-28 Orchestration Patterns- Supervisor, Swarm, Hierarchical|14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical]], [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]], [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-38 Verification Gates|14/38 Verification Gates]], [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]], [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]], [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]], [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]], [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]

## Builds on this

- [[Lessons/19-28 Capstone Lesson 28- Observability with OTel GenAI Spans and Prometheus Metrics|19/28 Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics]]
- [[Lessons/19-29 Capstone Lesson 29- End-to-End Coding Agent on the Harness|19/29 Capstone Lesson 29: End-to-End Coding Agent on the Harness]]
- [[Lessons/19-50 Hypothesis Generator|19/50 Hypothesis Generator]]
- [[Lessons/19-51 Literature Retrieval|19/51 Literature Retrieval]]
- [[Lessons/19-52 Experiment Runner|19/52 Experiment Runner]]
- [[Lessons/19-53 Result Evaluator|19/53 Result Evaluator]]
- [[Lessons/19-64 Chunking Strategies, Compared|19/64 Chunking Strategies, Compared]]
- [[Lessons/19-65 Hybrid Retrieval with BM25 and Dense Embeddings|19/65 Hybrid Retrieval with BM25 and Dense Embeddings]]
- [[Lessons/19-66 Cross-Encoder Reranker|19/66 Cross-Encoder Reranker]]
- [[Lessons/19-67 Query Rewriting- HyDE, Multi-Query, and Decomposition|19/67 Query Rewriting: HyDE, Multi-Query, and Decomposition]]
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]]
- [[Lessons/19-69 End-to-End RAG System|19/69 End-to-End RAG System]]
- [[Lessons/19-82 Capstone 82 — Jailbreak Taxonomy|19/82 Capstone 82 — Jailbreak Taxonomy]]
- [[Lessons/19-83 Capstone 83 — Prompt Injection Detector|19/83 Capstone 83 — Prompt Injection Detector]]
- [[Lessons/19-84 Capstone 84 — Refusal Evaluation|19/84 Capstone 84 — Refusal Evaluation]]
- [[Lessons/19-85 Capstone 85 — Content Classifier Integration|19/85 Capstone 85 — Content Classifier Integration]]
- [[Lessons/19-86 Capstone 86 — Constitutional Rules Engine|19/86 Capstone 86 — Constitutional Rules Engine]]
- [[Lessons/19-87 Capstone 87 — End-to-End Safety Gate|19/87 Capstone 87 — End-to-End Safety Gate]]


%% ── my notes ── %%
