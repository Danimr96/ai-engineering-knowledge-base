---
id: "concept:reproducible-build"
type: concept
name: Reproducible Build
canonical: true
category: AI-native development
taught_in: 0
tags:
  - concept/glossary
  - category/ai-native-development
source: ai-engineering-from-scratch/glossary/terms.md
---

# Reproducible Build

**What it actually means:** A build whose declared source, environment, and instructions can be independently rerun to produce bit-for-bit identical specified artifacts.

**Why it matters:** It makes an artifact verifiable beyond the machine or agent that originally produced it and exposes hidden build inputs.

**In practice:** Pin toolchains and dependencies, remove timestamps and unstable ordering, capture the environment, then compare independently rebuilt artifact digests.

**Common confusion:** A build that succeeds twice is repeatable evidence, but reproducibility requires the declared independent conditions and identical outputs.

**Category:** [[Categories/AI-native development|AI-native development]]

## Related concepts

- [[Concepts/Provenance Attestation|Provenance Attestation]]
- [[Concepts/Repository Instructions|Repository Instructions]]
- [[Concepts/Skill Bundle|Skill Bundle]]
- [[Concepts/Software Bill of Materials (SBOM)|Software Bill of Materials (SBOM)]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- Reproducible Builds definition ([link](https://reproducible-builds.org/docs/definition/))


%% ── my notes ── %%
