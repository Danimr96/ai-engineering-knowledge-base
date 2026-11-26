---
id: "concept:data-deduplication"
type: concept
name: Data Deduplication
canonical: true
category: "Data & representations"
taught_in: 0
community: 43
tags:
  - concept/glossary
  - category/data-and-representations
  - community/43
source: ai-engineering-from-scratch/glossary/terms.md
---

# Data Deduplication

**Community:** [[Communities/43 Data Provenance · Dataset Split · Datasheet for Datasets|43 Data Provenance · Dataset Split · Datasheet for Datasets]]

**What it actually means:** Detecting and removing exact and near-duplicate examples within or across datasets.

**Why it matters:** Repetition can distort the training distribution, increase memorization, leak test material, and make evaluation appear stronger than it is.

**In practice:** Normalize content, use exact hashes and similarity methods, review borderline clusters, and record which version and rule removed each example.

**Common confusion:** Deduplication is not ordinary data cleaning. Two distinct records can legitimately share text, and two paraphrases can still carry the same leaked information.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Benchmark Contamination|Benchmark Contamination]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Dataset Split|Dataset Split]]
- [[Concepts/Overfitting|Overfitting]]

## Sources

- Deduplicating Training Data Makes Language Models Better ([link](https://arxiv.org/abs/2107.06499))


%% ── my notes ── %%
