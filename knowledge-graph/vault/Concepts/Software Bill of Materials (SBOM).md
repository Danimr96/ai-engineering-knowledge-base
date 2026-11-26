---
id: "concept:software-bill-of-materials-sbom"
type: concept
name: Software Bill of Materials (SBOM)
canonical: true
category: "Security & governance"
aliases:
  - SBOM
taught_in: 0
tags:
  - concept/glossary
  - category/security-and-governance
source: ai-engineering-from-scratch/glossary/terms.md
---

# Software Bill of Materials (SBOM)

**What it actually means:** A structured inventory of software components and relationships associated with a product or artifact, often including versions, suppliers, licenses, and identifiers.

**Why it matters:** You need a component inventory to assess affected dependencies, license obligations, and supply-chain exposure when software changes or vulnerabilities emerge.

**In practice:** Generate the SBOM during the trusted build, bind it to the release artifact, verify it in policy checks, and update it whenever dependencies or packaging change.

**Common confusion:** An SBOM is an inventory, not proof that components are secure, correctly licensed, or actually present unless generation and provenance are trustworthy.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Provenance Attestation|Provenance Attestation]]
- [[Concepts/Reproducible Build|Reproducible Build]]

## Sources

- SPDX 3.0.1 specification ([link](https://spdx.github.io/spdx-spec/v3.0/))


%% ── my notes ── %%
