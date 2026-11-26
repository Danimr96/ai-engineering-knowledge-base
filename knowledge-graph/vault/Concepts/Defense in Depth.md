---
id: "concept:defense-in-depth"
type: concept
name: Defense in Depth
canonical: true
category: "Security & governance"
taught_in: 1
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Defense in Depth

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** Using independent preventive, detective, and corrective controls at several system boundaries so one failed control does not determine the outcome.

**Why it matters:** AI systems combine probabilistic models, untrusted content, tools, and external services, making any single filter or prompt an inadequate security boundary.

**In practice:** Pair instruction controls with narrow permissions, sandboxing, schema validation, approval for consequential actions, monitoring, and a tested recovery path.

**Common confusion:** More controls are not automatically better. Layers should address distinct failure modes and remain testable rather than repeat the same assumption.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Sandbox|Sandbox]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]] — Using multiple independent security layers so that no single point of failure compromises the entire system

## Sources

- NIST Glossary: Defense in Depth ([link](https://csrc.nist.gov/glossary/term/defense_in_depth))


%% ── my notes ── %%
