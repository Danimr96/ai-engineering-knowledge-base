---
id: "concept:function-calling"
type: concept
name: Function Calling
canonical: true
category: "Agents & tools"
taught_in: 5
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Function Calling

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

> *What people say:* A model using tools.

**What it actually means:** A provider or application interface through which a model emits a structured request naming a tool and its arguments. Application code validates the request, performs the operation, and can return the result for another model step.

**Common confusion:** The model requests a function call; your trusted code decides whether and how to execute it. Function calling alone is not a complete agent.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/ReAct|ReAct]]
- [[Concepts/Structured Output|Structured Output]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]] — LLM outputs a structured function invocation (name + typed arguments) instead of free text -- OpenAI and Anthropic both support this
- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — The model outputs structured JSON describing a function to invoke with specific arguments -- your code executes it, not the model
- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — Provider-level API support for emitting structured tool calls instead of prose
- [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]] — Provider-level API for structured tool-call emission
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]] — Structured-output tool invocation with validated schema


%% ── my notes ── %%
