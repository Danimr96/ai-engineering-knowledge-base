---
id: "lesson:11/09"
type: lesson
ref: 11/09
phase: 11
num: 9
title: "Function Calling & Tool Use"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 3
concepts: 11
prereqs: 1
community: 79
libraries:
  - ", "
  - child_process
aliases:
  - 11/09
  - 11-09
tags:
  - phase/11
  - type/build
  - community/79
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/09-function-calling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/09-function-calling"
---

# 11/09 Function Calling & Tool Use

> LLMs cannot do anything. They generate text. That is the entire capability. They cannot check the weather, query a database, send an email, run code, or read a file. Every "AI agent" you have ever seen is an LLM generating JSON that says which function to call -- and then your code actually calling it. The model is the brain. Tools are the hands. Function calling is the nervous system connecting them.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/09-function-calling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/09-function-calling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/09-function-calling) · code: function_calling.py, main.ts, tests/test_main.py  
**Community:** [[Communities/79 Agent loop · Tool choice · Tool result|79 Agent loop · Tool choice · Tool result]] · **Libraries:** [[Libraries/, (typescript)|, ]], [[Libraries/child_process (typescript)|child_process]]  

## Prerequisites

Stated upstream: `Phase 11 Lesson 03 (Structured Outputs)`

- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]] — Structured Outputs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/11-10 Evaluation & Testing LLM Applications|11/10 Evaluation & Testing LLM Applications]]
- [[Lessons/11-11 Caching, Rate Limiting & Cost Optimization|11/11 Caching, Rate Limiting & Cost Optimization]]
- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]]
- [[Lessons/11-16 Agent State Machines — Graphs, Nodes, Checkpoints|11/16 Agent State Machines — Graphs, Nodes, Checkpoints]]
- [[Lessons/11-17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration|11/17 Agent Framework Tradeoffs — Graph, Role, and Actor Orchestration]]

## Concepts taught

- [[Concepts/Function Calling|Function Calling]] `glossary` — The model outputs structured JSON describing a function to invoke with specific arguments -- your code executes it, not the model
- Tool definition `lesson term` — A JSON Schema object describing a tool's name, purpose, parameters, and types -- the model reads this to decide when and how to use the tool
- [[Concepts/Tool choice|Tool choice]] `lesson term` — Controls whether the model must call a tool (required), may call a tool (auto), or must call a specific tool (named)
- Parallel calling `lesson term` — The model outputs multiple tool calls in a single turn, reducing round trips -- GPT-4o and Claude both support this
- [[Concepts/Tool result|Tool result]] `lesson term` — The return value from executing a tool, sent back to the model as a message so it can use real data in its response
- Argument validation `lesson term` — Verifying that model-generated arguments match the expected types, ranges, and constraints before executing the tool
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]] (as *MCP*) `glossary` — Model Context Protocol -- Anthropic's open standard for exposing tools via servers that any compatible client can discover and call
- [[Concepts/Agent loop|Agent loop]] `lesson term` — The iterative cycle of model-decides-tool, code-executes-tool, result-feeds-back until the model has enough information to respond
- [[Concepts/Tool poisoning|Tool poisoning]] `lesson term` — An attack where tool results contain instructions that manipulate the model's behavior -- sanitize all tool outputs
- Rate limiting `lesson term` — Setting a maximum number of tool calls per conversation to prevent infinite loops and runaway API costs

## Ships

- [[Artifacts/11-09 prompt-tool-designer|prompt-tool-designer]] `prompt` — Design complete tool definitions (JSON Schema) for function calling from a natural language description
- [[Artifacts/11-09 skill-function-calling-patterns|skill-function-calling-patterns]] `skill` — Decision framework for implementing function calling in production -- tool design, error handling, security, and provider patterns

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — five composable patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) built from the single tool-use primitive. ·  also cited by 16 other lessons
- [[Resources/ReAct|ReAct]] ([link](https://arxiv.org/abs/2210.03629)) — the Thought-Action-Observation loop that is the outer agent loop around every tool call; where this lesson ends, Phase 14 picks up. ·  also cited by 5 other lessons
- [[Resources/Schick et al., 2023 - -Toolformer- Language Models Can Teach Themselves to Use Tools|Schick et al., 2023 -- "Toolformer: Language Models Can Teach Themselves to Use Tools]] ([link](https://arxiv.org/abs/2302.04761)) — the foundational paper on training LLMs to decide when and how to call external tools ·  also cited by 1 other lesson
- Patil et al., 2023 -- "Gorilla: Large Language Model Connected with Massive APIs ([link](https://arxiv.org/abs/2305.15334)) — fine-tuning LLMs for accurate API calls across 1,645 APIs with hallucination reduction
- [[Resources/Anthropic Tool Use Guide|Anthropic Tool Use Guide]] ([link](https://docs.anthropic.com/en/docs/tool-use)) — Claude's tool use implementation with input_schema, multi-tool responses, and tool_choice configuration ·  also cited by 1 other lesson
- [[Resources/Berkeley Function Calling Leaderboard|Berkeley Function Calling Leaderboard]] ([link](https://gorilla.cs.berkeley.edu/leaderboard.html)) — real-time benchmark comparing function calling accuracy across GPT-4o, Claude, Gemini, and open models ·  also cited by 2 other lessons
- [[Resources/Model Context Protocol Specification|Model Context Protocol Specification]] ([link](https://modelcontextprotocol.io)) — the open standard for tool interoperability across AI applications, with server/client architecture ·  also cited by 1 other lesson
- [[Resources/OpenAI Function Calling Guide|OpenAI Function Calling Guide]] ([link](https://platform.openai.com/docs/guides/function-calling)) — the definitive reference for tool use with GPT-4o, including parallel calls, forced calling, and structured arguments ·  also cited by 4 other lessons

## In learning paths

- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 6, required


%% ── my notes ── %%
