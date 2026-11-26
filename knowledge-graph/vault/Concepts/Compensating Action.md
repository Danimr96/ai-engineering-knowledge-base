---
id: "concept:compensating-action"
type: concept
name: Compensating Action
canonical: true
category: "Agents & tools"
taught_in: 0
community: 35
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/35
source: ai-engineering-from-scratch/glossary/terms.md
---

# Compensating Action

**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]]

**What it actually means:** A deliberate operation that semantically counteracts a completed side effect when the original operation cannot be rolled back atomically.

**Why it matters:** Multi-step agent workflows cross databases and external services where a later failure cannot undo earlier writes through one transaction.

**In practice:** If a booking workflow charges a card but the reservation fails, issue a tracked refund and preserve both events rather than deleting history.

**Common confusion:** Compensation is a new business action, not time travel. It can fail and therefore needs idempotency, monitoring, and escalation.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Durable Execution|Durable Execution]]
- [[Concepts/Idempotency|Idempotency]]

## Sources

- Sagas ([link](https://dl.acm.org/doi/10.1145/38713.38742))


%% ── my notes ── %%
