---
id: "lesson:11/16"
type: lesson
ref: 11/16
phase: 11
num: 16
title: "Agent State Machines — Graphs, Nodes, Checkpoints"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 90
libraries:
  - langchain_anthropic
  - langchain_core
  - langgraph
aliases:
  - 11/16
  - 11-16
tags:
  - phase/11
  - type/build
  - community/90
source: ai-engineering-from-scratch/phases/11-llm-engineering/16-langgraph-state-machines/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/16-langgraph-state-machines"
---

# 11/16 Agent State Machines — Graphs, Nodes, Checkpoints

> A ReAct loop written by hand is a `while True`. The same loop written as an explicit graph is something you can checkpoint, interrupt, branch, and time-travel through. The agent hasn't changed. The harness around it has.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/16-langgraph-state-machines/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/16-langgraph-state-machines) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/16-langgraph-state-machines) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/90 StateGraph · GroupChat|90 StateGraph · GroupChat]] · **Libraries:** [[Libraries/langchain_anthropic (python)|langchain_anthropic]], [[Libraries/langchain_core (python)|langchain_core]], [[Libraries/langgraph (python)|langgraph]]  

## Prerequisites

Stated upstream: `Phase 11 · 09 (Function Calling), Phase 11 · 14 (Model Context Protocol)`

- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling
- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]] — Model Context Protocol

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

## Builds on this

- [[Lessons/11-17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration|11/17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration]]

## Concepts taught

- [[Concepts/StateGraph|StateGraph]] `lesson term` — The builder object you add nodes and edges to before compile.
- [[Concepts/Reducer|Reducer]] `lesson term` — A function (old, new) -> merged applied when a node returns an update for that field; default is overwrite, add_messages appends.
- Thread `lesson term` — A thread_id string that scopes all checkpoints for one session.
- [[Concepts/Checkpoint|Checkpoint]] `glossary` — A persisted snapshot of the full graph state after a node transition, keyed on (thread_id, checkpoint_id).
- [[Concepts/Interrupt|Interrupt]] `lesson term` — interrupt_before / interrupt_after stop execution at a node boundary; resume with Command(resume=...).
- Time-travel `lesson term` — graph.invoke(None, config_with_old_checkpoint_id) replays from that checkpoint forward.
- Send `lesson term` — A constructor a node can return to spawn N parallel executions of a target node.
- [[Concepts/Subgraph|Subgraph]] `lesson term` — A compiled StateGraph used as a node in another graph; preserves its own state scope.

## Ships

- [[Artifacts/11-16 stategraph-designer|stategraph-designer]] `skill` — Turn an agent task into a LangGraph StateGraph with named nodes, typed state, reducers, checkpointer, and human interrupts.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — which graph shapes (chain, router, orchestrator-workers, evaluator-optimizer) to prefer and when. ·  also cited by 16 other lessons
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — the pattern every LangGraph agent implements; read it for the reasoning trace rationale. ·  also cited by 5 other lessons
- [[Resources/LangGraph documentation|LangGraph documentation]] ([link](https://langchain-ai.github.io/langgraph/)) — canonical reference for StateGraph, reducers, checkpointers, and interrupts. ·  also cited by 3 other lessons
- [[Resources/LangGraph Human-in-the-loop|LangGraph Human-in-the-loop]] ([link](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)) — `interrupt_before`, `interrupt_after`, `Command(resume=...)`, and the edit-state pattern. ·  also cited by 1 other lesson
- LangGraph concepts: state, reducers, checkpointers ([link](https://langchain-ai.github.io/langgraph/concepts/low_level/)) — the mental model this lesson uses, straight from the source.
- [[Resources/LangGraph Persistence and Checkpoints|LangGraph Persistence and Checkpoints]] ([link](https://langchain-ai.github.io/langgraph/concepts/persistence/)) — the detail on Postgres/SQLite/Redis stores, checkpoint namespaces, and thread IDs. ·  also cited by 1 other lesson


%% ── my notes ── %%
