---
id: "concept:data-lineage"
type: concept
name: Data Lineage
canonical: true
category: "Security & governance"
taught_in: 1
community: 43
tags:
  - concept/glossary
  - category/security-and-governance
  - community/43
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Lineage

**Community:** [[Communities/43 Data Provenance · Dataset Split · Datasheet for Datasets|43 Data Provenance · Dataset Split · Datasheet for Datasets]]

**What it actually means:** A record of how a data artifact was derived across sources, transformations, joins, filters, versions, and downstream uses.

**Why it matters:** When a source is corrected, revoked, or found unsafe, lineage identifies which datasets, embeddings, evaluations, and model artifacts may be affected.

**In practice:** Give inputs and outputs stable identifiers, record each transformation and version, preserve parent-child relationships, and test whether an affected source can be traced to every derivative.

**Common confusion:** Data provenance explains origin and custody broadly. Lineage emphasizes the transformation path and dependencies between data artifacts.

**Category:** [[Categories/Security & governance|Security & governance]]

## Related concepts

- [[Concepts/Audit Log|Audit Log]]
- [[Concepts/Content Provenance|Content Provenance]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Datasheet for Datasets|Datasheet for Datasets]]

## Taught in

- [[Lessons/15-15 Human-in-the-Loop- Propose-Then-Commit|15/15 Human-in-the-Loop: Propose-Then-Commit]] — The specific source content that led to the proposal

## Sources

- W3C PROV-O ([link](https://www.w3.org/TR/prov-o/))


%% ── my notes ── %%
