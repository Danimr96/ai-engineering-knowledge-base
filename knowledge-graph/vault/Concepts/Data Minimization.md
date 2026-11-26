---
id: "concept:data-minimization"
type: concept
name: Data Minimization
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

# Data Minimization

**Community:** [[Communities/65 Data Classification · Data Minimization · Purpose Limitation|65 Data Classification · Data Minimization · Purpose Limitation]]

**What it actually means:** For personal data, limiting what is collected, processed, exposed, and retained to what is necessary for a specified purpose. Teams can apply the same discipline to sensitive non-personal data as an engineering control.

**Why it matters:** Every unnecessary field placed in a prompt, trace, cache, or tool call increases privacy exposure and the possible impact of misuse or compromise.

**In practice:** Define the required fields before collection, redact or aggregate at the earliest boundary, set retention limits, and verify that optional context improves a measured task outcome before keeping it.

**Common confusion:** Minimization does not mean keeping no data. It means being able to justify each data element, use, recipient, and retention period against the stated purpose.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Data Classification|Data Classification]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Membership Inference|Membership Inference]]
- [[Concepts/Purpose Limitation|Purpose Limitation]]

## Sources

- General Data Protection Regulation, Article 5(1)(c) ([link](https://eur-lex.europa.eu/eli/reg/2016/679/oj))


%% ── my notes ── %%
