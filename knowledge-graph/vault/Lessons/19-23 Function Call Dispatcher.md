---
id: "lesson:19/23"
type: lesson
ref: 19/23
phase: 19
num: 23
title: Function Call Dispatcher
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 7
code_files: 2
concepts: 0
prereqs: 8
community: 3
aliases:
  - 19/23
  - 19-23
tags:
  - phase/19
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/23-function-call-dispatcher/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/23-function-call-dispatcher"
---

# 19/23 Function Call Dispatcher

> The dispatcher is where the harness pays for every promise the schema made. Timeouts, retries, dedupe, error mapping. All on one seam.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/23-function-call-dispatcher/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/23-function-call-dispatcher) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/23-function-call-dispatcher) · code: main.py, tests/test_dispatcher.py · quiz: 7 questions  
**Track:** [[Tracks/19-A Agent harness from scratch|Phase 19 Track A: Agent harness from scratch]]  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 lessons 01-07, Phase 14 lesson 01`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]
- **13/01-07**:
    - [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]
    - [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]
    - [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]
    - [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]
    - [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]
    - [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
    - [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]

## Builds on this

- [[Lessons/19-25 Capstone Lesson 25- Verification Gates and the Observation Budget|19/25 Capstone Lesson 25: Verification Gates and the Observation Budget]]
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


%% ── my notes ── %%
