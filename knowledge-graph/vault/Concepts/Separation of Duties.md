---
id: "concept:separation-of-duties"
type: concept
name: Separation of Duties
canonical: true
category: "Security & governance"
taught_in: 0
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Separation of Duties

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** Dividing conflicting responsibilities or authority across independent roles so one principal cannot complete a high-risk action without another authorized decision.

**Why it matters:** A compromised account or mistaken agent should not be able to propose, approve, execute, and conceal the same consequential change.

**In practice:** Separate artifact creation from release approval, use distinct identities, preserve both decisions in the audit log, and define emergency access with later review.

**Common confusion:** Separation of duties is about conflicting authority, not simply assigning work to several people or agents that share the same credentials.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Reviewer Agent|Reviewer Agent]]

## Sources

- NIST SP 800-53 Rev. 5 ([link](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final))


%% ── my notes ── %%
