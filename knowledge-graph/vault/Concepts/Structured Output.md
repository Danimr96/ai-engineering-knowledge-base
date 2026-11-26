---
id: "concept:structured-output"
type: concept
name: Structured Output
canonical: true
category: "Agents & tools"
taught_in: 1
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Structured Output

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** Model output constrained or validated against a machine-readable schema so application code can consume fields without parsing free-form prose.

**Why it matters:** It reduces format ambiguity at the model-to-software boundary and enables field-level validation and retries.

**In practice:** Require an incident triage result with an allowed severity enum, evidence array, and nullable escalation reason, then reject any response that fails the schema.

**Common confusion:** Schema-valid output can still contain incorrect values. Structure is not factual verification.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Exact Match (EM)|Exact Match (EM)]]
- [[Concepts/Function Calling|Function Calling]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Stop Sequence|Stop Sequence]]
- [[Concepts/Tool Contract|Tool Contract]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]] — Output that matches a specific JSON Schema with correct keys, types, and constraints


%% ── my notes ── %%
