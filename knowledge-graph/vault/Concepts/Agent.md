---
id: "concept:agent"
type: concept
name: Agent
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

# Agent

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

> *What people say:* An autonomous model that thinks and acts alone.

**What it actually means:** A software system that lets a model select actions toward a goal, observe tool or environment results, and continue under an orchestration policy. An agent may use a loop, a state machine, a workflow engine, or human approvals. The model is one component, not the entire system.

**Why it matters:** Reliability comes from the harness, tool contracts, state, permissions, and verification around the model.

**In practice:** A coding agent reads repository context, proposes a patch, runs tests in a sandbox, and stops for approval before deployment.

**Common confusion:** Autonomy is a degree of delegated authority, not a required property of every agent.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Agent State|Agent State]]
- [[Concepts/Function Calling|Function Calling]]
- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/ReAct|ReAct]]
- [[Concepts/Swarm|Swarm]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — A loop: LLM thinks, picks a tool, result feeds back, repeat until stop
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Model-owned graph; dynamic tool direction
- [[Lessons/14-15 Role-Based Agent Teams — Roles, Tasks, Processes|14/15 Role-Based Agent Teams — Roles, Tasks, Processes]] — Role + goal + backstory + tools
- [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]] — Agent type in the SDK; owns tools and handoffs
- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — A (system_prompt, tools, model) triple. Stateless.


%% ── my notes ── %%
