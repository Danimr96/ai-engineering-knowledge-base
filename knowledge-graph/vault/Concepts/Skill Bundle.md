---
id: "concept:skill-bundle"
type: concept
name: Skill Bundle
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

# Skill Bundle

**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]]

**What it actually means:** The complete installable skill directory, including `SKILL.md` and every reference, script, asset, fixture, or companion file required by the workflow.

**Why it matters:** Copying only the entry file can leave valid-looking instructions that point to missing resources or lose the deterministic code the workflow depends on.

**In practice:** Install the tree as one unit, record hashes and source revision, validate the installed copy, and show collisions before replacing an existing bundle.

**Common confusion:** SKILL.md is the entry point, not necessarily the entire artifact.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Skill|Agent Skill]]
- [[Concepts/Provenance Attestation|Provenance Attestation]]
- [[Concepts/Reproducible Build|Reproducible Build]]
- [[Concepts/Skill Catalog|Skill Catalog]]
- [[Concepts/Skill Discovery|Skill Discovery]]

## Taught in

- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]]

## Sources

- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification))


%% ── my notes ── %%
