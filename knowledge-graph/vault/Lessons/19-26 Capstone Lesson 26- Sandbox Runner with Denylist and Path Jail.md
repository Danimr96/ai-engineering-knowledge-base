---
id: "lesson:19/26"
type: lesson
ref: 19/26
phase: 19
num: 26
title: "Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 3
community: 3
aliases:
  - 19/26
  - 19-26
tags:
  - phase/19
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/26-sandbox-runner-denylist/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/26-sandbox-runner-denylist"
---

# 19/26 Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail

> The verification gate decides whether a tool call should run. The sandbox decides what happens when it does. This lesson ships a subprocess runner that refuses dangerous executables, refuses dangerous argv shapes, jails every file path to a project root, truncates oversized output, and kills runaway processes on a wall-clock timeout. It is the second of two layers that sit between the model and the operating system.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/26-sandbox-runner-denylist/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/26-sandbox-runner-denylist) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/26-sandbox-runner-denylist) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Track:** [[Tracks/19-A Agent harness from scratch|Phase 19 Track A: Agent harness from scratch]]  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 19 · 25 (verification gates and observation budget), Phase 14 · 33 (instructions as constraints), Phase 14 · 38 (verification gates)`

- [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]] — instructions as constraints
- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]] — verification gates
- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]] — verification gates and observation budget

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]], [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]], [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]], [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]], [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]], [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]], [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]], [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]], [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]

## Builds on this

- [[Lessons/19-27 Capstone Lesson 27- Eval Harness with Fixture Tasks|19/27 Capstone Lesson 27: Eval Harness with Fixture Tasks]]
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
