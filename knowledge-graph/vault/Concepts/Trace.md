---
id: "concept:trace"
type: concept
name: Trace
canonical: true
category: AI-native development
taught_in: 4
community: 10
tags:
  - concept/glossary
  - category/ai-native-development
  - community/10
source: ai-engineering-from-scratch/glossary/terms.md
---

# Trace

**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]]

**What it actually means:** A correlated record of one request or task across model calls, retrieval, tools, state transitions, retries, approvals, and evaluations.

**Why it matters:** It lets you reconstruct where time, cost, and failure entered a multi-step workflow.

**In practice:** Propagate one trace identifier through the agent harness and attach redacted spans for each model and tool operation.

**Common confusion:** A trace should record operational evidence, not expose hidden model reasoning, secrets, or unredacted sensitive content.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Observability|Observability]]
- [[Concepts/Shadow Traffic|Shadow Traffic]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]

## Taught in

- [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]] — Tree of spans sharing a trace id
- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Full record of thought, action, observation tuples for a run
- [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]
- [[Lessons/19-87 Capstone 87 — End-to-End Safety Gate|19/87 Capstone 87 — End-to-End Safety Gate]] — a structured per-request record with every checkpoint's verdict, the final action, and latency

## Sources

- OpenTelemetry traces ([link](https://opentelemetry.io/docs/concepts/signals/traces/))


%% ── my notes ── %%
