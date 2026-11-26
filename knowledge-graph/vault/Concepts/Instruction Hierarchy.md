---
id: "concept:instruction-hierarchy"
type: concept
name: Instruction Hierarchy
canonical: true
category: "Prompting & context"
taught_in: 0
community: 14
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Instruction Hierarchy

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** A rule set for resolving conflicts among instructions from sources with different authority, such as application policy, users, and untrusted retrieved content.

**Why it matters:** Agent systems mix trusted goals with external text, so the model and harness need a defined response when lower-authority content conflicts with higher-authority constraints.

**In practice:** Label untrusted tool output as data, preserve higher-priority constraints outside that content, and test direct and indirect conflict cases.

**Common confusion:** An instruction hierarchy can improve behavior but is not a security boundary; least privilege and approval controls still limit consequences.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]]
- [[Concepts/Instruction Following|Instruction Following]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/System Prompt|System Prompt]]
- [[Concepts/Tool Contract|Tool Contract]]

## Sources

- The Instruction Hierarchy ([link](https://arxiv.org/abs/2404.13208))


%% ── my notes ── %%
