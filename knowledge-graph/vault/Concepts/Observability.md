---
id: "concept:observability"
type: concept
name: Observability
canonical: true
category: AI-native development
taught_in: 1
community: 46
tags:
  - concept/glossary
  - category/ai-native-development
  - community/46
source: ai-engineering-from-scratch/glossary/terms.md
---

# Observability

**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]]

**What it actually means:** The ability to understand an AI system's behavior from recorded inputs, outputs, state transitions, tool calls, timings, costs, errors, and evaluation signals.

**Why it matters:** AI failures often span model, retrieval, tools, and orchestration. You need correlated evidence to locate the failing boundary.

**In practice:** Record a trace ID across retrieval, model calls, tool execution, approvals, and final scoring while applying redaction and access controls.

**Common confusion:** Logging collects events. Observability makes those events structured and connected enough to answer operational questions.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Canary Release|Canary Release]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Incident Response|Incident Response]]
- [[Concepts/Model Serving|Model Serving]]
- [[Concepts/Postmortem|Postmortem]]
- [[Concepts/Saturation|Saturation]]
- [[Concepts/Service Level Indicator (SLI)|Service Level Indicator (SLI)]]
- [[Concepts/Streaming|Streaming]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]
- [[Concepts/Tokens per Second (TPS)|Tokens per Second (TPS)]]
- [[Concepts/Trace|Trace]]

## Taught in

- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]


%% ── my notes ── %%
