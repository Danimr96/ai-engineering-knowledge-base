---
id: "concept:tracing"
type: concept
name: Tracing
canonical: false
taught_in: 3
community: 17
tags:
  - concept/lesson-term
  - community/17
source: ai-engineering-from-scratch/phases/03-deep-learning-core/12-intro-to-jax/docs/en.md
---

# Tracing

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

> *What people say:* "Recording the computation"

**What it actually means:** JAX executes the function with abstract values to build a computation graph, without computing real results

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/14-16 OpenAI Agents SDK- Handoffs, Guardrails, Tracing|14/16 OpenAI Agents SDK: Handoffs, Guardrails, Tracing]] — Built-in observability over LLM + tool + handoff + guardrail
- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]] — Ingest OTel / SDK spans; index by session


%% ── my notes ── %%
