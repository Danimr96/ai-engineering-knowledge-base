---
id: "lesson:11/17"
type: lesson
ref: 11/17
phase: 11
num: 17
title: "Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 90
aliases:
  - 11/17
  - 11-17
tags:
  - phase/11
  - type/learn
  - community/90
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/17-agent-framework-tradeoffs/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/17-agent-framework-tradeoffs"
---

# 11/17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration

> Every framework sells the same demo (research agent builds a report) and hides the same bug (state schema fights with the orchestration layer). Pick the framework whose abstractions match the shape of your problem; everything else is glue you write twice.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/17-agent-framework-tradeoffs/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/17-agent-framework-tradeoffs) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/17-agent-framework-tradeoffs) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/90 StateGraph · GroupChat|90 StateGraph · GroupChat]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 · 09 (Function Calling), Phase 11 · 16 (LangGraph)`

- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling
- [[Lessons/11-16 Agent State Machines — Graphs, Nodes, Checkpoints|11/16 Agent State Machines — Graphs, Nodes, Checkpoints]] — LangGraph

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]], [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

## Concepts taught

- [[Concepts/Orchestration|Orchestration]] `glossary` — The layer that decides which node/role/agent runs next.
- Durable state `lesson term` — State that survives process death, attached to a checkpoint or session store.
- LLM-selected routing `lesson term` — A planner LLM picks the next step each turn; flexible but pays tokens on every decision.
- Explicit routing `lesson term` — A Python function or static edge picks the next step; cheap and auditable.
- [[Concepts/Crew|Crew]] `lesson term` — Roles + tasks + process (sequential or hierarchical) bound into a single runnable.
- [[Concepts/GroupChat|GroupChat]] `lesson term` — A managed conversation between N agents with a speaker selector.
- Team (as *Team (Agno)*) `lesson term` — Route / coordinate / collaborate mode over a set of agents.
- [[Concepts/StateGraph|StateGraph]] `lesson term` — Typed-state, node, conditional-edge, checkpointer abstraction.

## Ships

- [[Artifacts/11-17 framework-picker|framework-picker]] `skill` — Pick LangGraph, CrewAI, AutoGen, Agno, or plain Python for an agent task by matching abstraction to problem shape.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — pattern library (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) framework-agnostic. ·  also cited by 16 other lessons
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — the loop every framework dresses up. ·  also cited by 5 other lessons
- [[Resources/Generative Agents|Generative Agents]] ([link](https://arxiv.org/abs/2304.03442)) — role-play foundation that CrewAI-style persona stacks build on. ·  also cited by 1 other lesson
- [[Resources/AutoGen|AutoGen]] ([link](https://arxiv.org/abs/2308.08155)) — AutoGen's design paper. ·  also cited by 1 other lesson
- Agno documentation ([link](https://docs.agno.com/)) — Agent, Team, Workflow, storage, memory.
- [[Resources/CrewAI documentation|CrewAI documentation]] ([link](https://docs.crewai.com/)) — Crews, Flows, Agents, Tasks, Processes. ·  also cited by 1 other lesson
- [[Resources/LangGraph documentation|LangGraph documentation]] ([link](https://langchain-ai.github.io/langgraph/)) — StateGraph, checkpointers, interrupts, time-travel. ·  also cited by 3 other lessons
- AutoGen documentation ([link](https://microsoft.github.io/autogen/)) — ConversableAgent, GroupChat, teams, tools.


%% ── my notes ── %%
