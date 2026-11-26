---
id: "concept:skill-discovery"
type: concept
name: Skill Discovery
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

# Skill Discovery

**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]]

**What it actually means:** A runtime pipeline that searches configured roots, identifies candidate skill directories, validates their package contract, attaches scope and provenance, resolves collisions, and publishes eligible catalog entries.

**Why it matters:** Deterministic discovery makes missing, malformed, shadowed, and unsafe packages diagnosable before model routing begins.

**In practice:** Declare search scopes and duplicate behavior, decide how symlinks are handled, reject resource escapes, and log why each candidate was accepted or rejected.

**Common confusion:** Skill discovery is not an unrestricted recursive search for filenames called SKILL.md; installation locations and precedence are runtime policy.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Skill Bundle|Skill Bundle]]
- [[Concepts/Skill Catalog|Skill Catalog]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]] — Search configured scopes, validate packages, attach provenance, and apply policy

## Sources

- [[Resources/Agent Skills client implementation guide|Agent Skills client implementation guide]] ([link](https://agentskills.io/client-implementation/adding-skills-support))


%% ── my notes ── %%
