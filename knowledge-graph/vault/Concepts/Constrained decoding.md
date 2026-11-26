---
id: "concept:constrained-decoding"
type: concept
name: Constrained decoding
canonical: false
taught_in: 4
community: 56
tags:
  - concept/lesson-term
  - community/56
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/11-machine-translation/docs/en.md
---

# Constrained decoding

**Community:** [[Communities/56 NLLB · Constrained decoding · OOV|56 NLLB · Constrained decoding · OOV]]

> *What people say:* Controlled output

**What it actually means:** Force specific tokens or n-grams to appear / not appear in the output.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]]
- [[Lessons/05-20 Structured Outputs & Constrained Decoding|05/20 Structured Outputs & Constrained Decoding]] — Mask invalid-token logits at every generation step.
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]] — At each token position, mask out tokens that would produce invalid output -- guarantees 100% schema compliance
- [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]] — Decode-time enforcement that masks invalid next-tokens


%% ── my notes ── %%
