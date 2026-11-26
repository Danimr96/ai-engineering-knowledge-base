---
id: "concept:data-classification"
type: concept
name: Data Classification
canonical: true
category: "Security & governance"
taught_in: 0
community: 65
tags:
  - concept/glossary
  - category/security-and-governance
  - community/65
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Classification

**Community:** [[Communities/65 Data Classification · Data Minimization · Purpose Limitation|65 Data Classification · Data Minimization · Purpose Limitation]]

**What it actually means:** Assigning data to documented sensitivity or impact classes so handling, access, retention, sharing, and incident rules follow the consequences of disclosure or loss.

**Why it matters:** An AI pipeline cannot apply proportionate controls if source documents, prompts, traces, and generated artifacts are treated as equally sensitive.

**In practice:** Classify data at ingestion, carry the label through derived artifacts, restrict tools and destinations by class, and define how labels change after transformation or aggregation.

**Common confusion:** Data classification describes protection requirements. It is not the same as a machine-learning classification task or a claim that the data is accurate.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/AI Risk Assessment|AI Risk Assessment]]
- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Data Minimization|Data Minimization]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Membership Inference|Membership Inference]]
- [[Concepts/Purpose Limitation|Purpose Limitation]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Sources

- NIST FIPS 199: Federal Information and Information System Categorization ([link](https://csrc.nist.gov/pubs/fips/199/final))
- NIST SP 1800-39 Initial Public Draft: Data Classification Practices ([link](https://www.nccoe.nist.gov/sites/default/files/2026-02/nist-sp-1800-39-ipd.pdf))


%% ── my notes ── %%
