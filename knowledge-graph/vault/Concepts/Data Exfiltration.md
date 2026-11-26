---
id: "concept:data-exfiltration"
type: concept
name: Data Exfiltration
canonical: true
category: "Security & governance"
taught_in: 1
community: 14
tags:
  - concept/glossary
  - category/security-and-governance
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Exfiltration

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** Unauthorized transfer of protected data from a system or trust zone to a person, tool, service, or storage location that is not permitted to receive it.

**Why it matters:** An agent can expose secrets through generated text, tool arguments, URLs, logs, or side effects even when the original data store remains intact.

**In practice:** Minimize readable data, allowlist destinations, inspect outbound tool calls, redact sensitive fields, and alert on unusual transfers across trust boundaries.

**Common confusion:** Exfiltration is about unauthorized movement or disclosure. Ordinary retrieval of data by an authorized component is not exfiltration, although later use can become one.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Indirect Prompt Injection|Indirect Prompt Injection]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/18-25 EchoLeak and the Emergence of CVEs for AI|18/25 EchoLeak and the Emergence of CVEs for AI]]

## Sources

- NIST SP 800-53 Rev. 5: AC-4 Information Flow Enforcement ([link](https://csrc.nist.gov/files/pubs/sp/800/53/r5/upd1/final/docs/sp800-53r5-controls.xlsx))


%% ── my notes ── %%
