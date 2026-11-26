---
id: "concept:verification-gate"
type: concept
name: Verification Gate
canonical: true
category: "Evaluation & safety"
taught_in: 1
community: 24
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/24
source: ai-engineering-from-scratch/glossary/terms.md
---

# Verification Gate

**Community:** [[Communities/24 Eval Set · Regression Test · Test Oracle|24 Eval Set · Regression Test · Test Oracle]]

**What it actually means:** A control point that blocks progress until defined evidence satisfies a correctness or quality criterion.

**Why it matters:** It converts a model's claim of completion into an evidence-backed decision.

**In practice:** Prevent a coding task from completing until the patch applies, scoped tests pass, forbidden files remain unchanged, and required artifacts exist.

**Common confusion:** Verification checks whether evidence meets criteria. Approval grants authority to proceed, even when the evidence is already known.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Canary Release|Canary Release]]
- [[Concepts/Chain of Thought (CoT)|Chain of Thought (CoT)]]
- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Flaky Test|Flaky Test]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Hallucination|Hallucination]]
- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]]
- [[Concepts/Planning|Planning]]
- [[Concepts/Provenance Attestation|Provenance Attestation]]
- [[Concepts/Regression Test|Regression Test]]
- [[Concepts/Reproducible Build|Reproducible Build]]
- [[Concepts/Reviewer Agent|Reviewer Agent]]
- [[Concepts/Scope Contract|Scope Contract]]
- [[Concepts/Structured Output|Structured Output]]
- [[Concepts/Termination Condition|Termination Condition]]
- [[Concepts/Test Oracle|Test Oracle]]

## Taught in

- [[Lessons/14-38 Verification Gates|14/38 Verification Gates]] — Deterministic function over workbench artifacts producing a pass/fail verdict


%% ── my notes ── %%
