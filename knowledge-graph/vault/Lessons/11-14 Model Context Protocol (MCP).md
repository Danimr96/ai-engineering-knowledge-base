---
id: "lesson:11/14"
type: lesson
ref: 11/14
phase: 11
num: 14
title: Model Context Protocol (MCP)
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 2
community: 17
aliases:
  - 11/14
  - 11-14
tags:
  - phase/11
  - type/build
  - community/17
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/14-model-context-protocol/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/14-model-context-protocol"
---

# 11/14 Model Context Protocol (MCP)

> MCP gives an AI host one protocol for discovering and invoking tools, resources, and prompts. The 2026-07-28 revision makes that protocol stateless: capability and version context travels with every request, not in a connection-bound handshake.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/14-model-context-protocol/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/14-model-context-protocol) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/14-model-context-protocol) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 · 09 (Function Calling), Phase 11 · 03 (Structured Outputs)`

- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]] — Structured Outputs
- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-16 Agent State Machines — Graphs, Nodes, Checkpoints|11/16 Agent State Machines — Graphs, Nodes, Checkpoints]]

## Concepts taught

- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]] (as *MCP*) `glossary` — JSON-RPC protocol for server discovery, tools, resources, prompts, and extensions
- [[Concepts/Host|Host]] `lesson term` — Owns the model and UI and mounts one or more MCP clients
- Client `lesson term` — Speaks MCP to one server on behalf of a host
- [[Concepts/Stateless MCP|Stateless MCP]] `glossary` — Every request carries version and capabilities; no protocol state is keyed by a connection
- [[Concepts/server-discover|server/discover]] `lesson term` — Required server method advertising versions, capabilities, and identity
- [[Concepts/resultType|resultType]] `lesson term` — Marks a result as complete or input_required
- State handle `lesson term` — Server-minted application identifier passed as an ordinary argument
- [[Concepts/Streamable HTTP|Streamable HTTP]] `lesson term` — One POST endpoint with JSON or request-scoped SSE responses
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]] (as *MRTR*) `glossary` — Input request embedded in a result, followed by a retry of the original operation

## Ships

- [[Artifacts/11-14 mcp-server-designer|mcp-server-designer]] `skill` — Design a stateless MCP 2026-07-28 server with explicit discovery, state, transport, and safety contracts.

## Further reading

- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)) ·  also cited by 4 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) ·  also cited by 6 other lessons
- [[Resources/MCP deprecated features|MCP deprecated features]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)) ·  also cited by 1 other lesson
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons


%% ── my notes ── %%
