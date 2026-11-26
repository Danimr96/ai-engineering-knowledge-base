---
id: "concept:skill-catalog"
type: concept
name: Skill Catalog
canonical: true
category: "Agents & tools"
taught_in: 1
community: 39
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/39
source: ai-engineering-from-scratch/glossary/terms.md
---

# Skill Catalog

**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]]

**What it actually means:** The compact model-visible inventory of eligible skills, usually containing routing metadata such as name, description, and an internal source identifier rather than every skill body.

**Why it matters:** A catalog lets an agent discover relevant procedures without loading every installed package into the working context.

**In practice:** Validate packages first, apply an explicit duplicate-name policy, measure the serialized catalog budget, and retain diagnostics for entries that were shortened, omitted, or shadowed.

**Common confusion:** A catalog entry means the skill is discoverable. It does not mean the body is active or its tools are authorized.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Skill|Agent Skill]]
- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Skill Bundle|Skill Bundle]]
- [[Concepts/Skill Discovery|Skill Discovery]]
- [[Concepts/Skill Invocation|Skill Invocation]]
- [[Concepts/Token Budget|Token Budget]]

## Taught in

- [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]] — Compact model-visible routing metadata for eligible packages

## Sources

- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification))


%% ── my notes ── %%
