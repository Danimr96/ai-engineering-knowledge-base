---
id: "concept:idempotency"
type: concept
name: Idempotency
canonical: true
category: AI-native development
taught_in: 3
community: 35
tags:
  - concept/glossary
  - category/ai-native-development
  - community/35
source: ai-engineering-from-scratch/glossary/terms.md
---

# Idempotency

**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]]

**What it actually means:** The property that repeating the same operation with the same identity does not create additional side effects beyond the first successful application.

**Why it matters:** Retries are normal in distributed agent systems. Without idempotency, one uncertain response can duplicate payments, comments, deployments, or records.

**In practice:** Attach an idempotency key to a tool request and persist the completed result so a retry returns that result instead of executing the write again.

**Common confusion:** Idempotency does not mean every response is byte-for-byte identical. It means the intended state change is not duplicated.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Compensating Action|Compensating Action]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Retry with Backoff|Retry with Backoff]]
- [[Concepts/Stateless MCP|Stateless MCP]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/13-29 MCP Reliability, Cancellation, and Flow Control|13/29 MCP Reliability, Cancellation, and Flow Control]] `alias` — Application identifier that deduplicates one business intent
- [[Lessons/15-15 Human-in-the-Loop- Propose-Then-Commit|15/15 Human-in-the-Loop: Propose-Then-Commit]] `alias` — Unique per proposal; second execution no-ops
- [[Lessons/16-22 Production Scaling — Queues, Checkpoints, Durability|16/22 Production Scaling — Queues, Checkpoints, Durability]] — Repeating a side effect produces the same result as one attempt.

## Sources

- HTTP Semantics: idempotent methods ([link](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods))


%% ── my notes ── %%
