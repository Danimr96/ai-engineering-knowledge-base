---
id: "concept:provenance-attestation"
type: concept
name: Provenance Attestation
canonical: true
category: "Security & governance"
taught_in: 0
tags:
  - concept/glossary
  - category/security-and-governance
source: ai-engineering-from-scratch/glossary/terms.md
---

# Provenance Attestation

**What it actually means:** Authenticated, machine-readable metadata that binds an artifact to claims about how, where, when, and from which inputs it was produced.

**Why it matters:** It lets automated policy and reviewers verify supply-chain claims instead of trusting an unsigned build note.

**In practice:** Generate an attestation in the build system, bind it to artifact digests, sign it with a controlled identity, and verify it before release.

**Common confusion:** A signature identifies the attester and protects integrity; it does not prove that every claim inside the attestation is true.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Content Provenance|Content Provenance]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Reproducible Build|Reproducible Build]]
- [[Concepts/Skill Bundle|Skill Bundle]]
- [[Concepts/Software Bill of Materials (SBOM)|Software Bill of Materials (SBOM)]]
- [[Concepts/Verification Gate|Verification Gate]]

## Sources

- SLSA Software Attestations ([link](https://slsa.dev/spec/v1.2/attestation-model))


%% ── my notes ── %%
