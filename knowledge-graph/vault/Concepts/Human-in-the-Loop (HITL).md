---
id: "concept:human-in-the-loop-hitl"
type: concept
name: Human-in-the-Loop (HITL)
canonical: true
category: "Agents & tools"
aliases:
  - Human oversight
  - human review
taught_in: 0
community: 24
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Human-in-the-Loop (HITL)

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A workflow design in which a person supplies judgment, correction, approval, or escalation at defined points in an AI-driven process.

**Why it matters:** Human involvement is most useful at high-impact, ambiguous, or irreversible boundaries, not as an undefined fallback after every step.

**In practice:** Let the agent classify routine requests automatically, but route uncertain or high-value cases to a reviewer with the evidence and proposed action.

**Common confusion:** HITL does not automatically make a system safe. Reviewers need time, context, authority, and a clear decision standard.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent|Agent]]
- [[Concepts/AI Risk Assessment|AI Risk Assessment]]
- [[Concepts/Alignment|Alignment]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]]
- [[Concepts/Test Oracle|Test Oracle]]
- [[Concepts/Verification Gate|Verification Gate]]


%% ── my notes ── %%
