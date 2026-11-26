---
id: "concept:tool-contract"
type: concept
name: Tool Contract
canonical: true
category: "Agents & tools"
taught_in: 2
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Tool Contract

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** The complete agreement for a tool boundary: purpose, typed inputs, outputs, validation, permissions, side effects, errors, timeouts, idempotency, and evidence returned to the caller.

**Why it matters:** A schema tells a model what fields exist; a contract tells the system when the tool is safe and how failures must be handled.

**In practice:** Define a file-write tool with an allowed root, expected base revision, maximum size, dry-run mode, explicit conflict errors, and a returned patch hash.

**Common confusion:** A JSON Schema is part of a tool contract, not the whole contract.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Function Calling|Function Calling]]
- [[Concepts/Idempotency|Idempotency]]
- [[Concepts/Instruction Hierarchy|Instruction Hierarchy]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Stateless MCP|Stateless MCP]]
- [[Concepts/Structured Output|Structured Output]]

## Taught in

- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]] — Inputs, outputs, permissions, side effects, errors, and evidence for a capability
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]


%% ── my notes ── %%
