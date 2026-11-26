---
id: "concept:tool-call"
type: concept
name: Tool call
canonical: false
taught_in: 4
community: 7
tags:
  - concept/lesson-term
  - community/07
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/en.md
---

# Tool call

**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]]

> *What people say:* Function invocation

**What it actually means:** LLM emits a structured call with name + args. Runtime executes, returns result.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-17 Chatbots — Rule-Based to Neural to LLM Agents|05/17 Chatbots — Rule-Based to Neural to LLM Agents]]
- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]] — LLM emits JSON; runtime dispatches; result feeds back in-loop.
- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — A JSON payload with id, name, arguments emitted by the model
- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Structured output the runtime dispatches to an executable


%% ── my notes ── %%
