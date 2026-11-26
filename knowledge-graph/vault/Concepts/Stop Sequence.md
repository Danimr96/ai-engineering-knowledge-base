---
id: "concept:stop-sequence"
type: concept
name: Stop Sequence
canonical: true
category: "Models & inference"
taught_in: 0
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Stop Sequence

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** An application-specified token or text pattern that causes generation to stop when the decoding system encounters it.

**Why it matters:** Stop sequences bound output protocols and multi-part generation without waiting for the model to decide semantically that it is finished.

**In practice:** Choose unambiguous delimiters, test tokenization and partial streaming matches, and still enforce output length and schema validation.

**Common confusion:** A stop sequence is a mechanical decoding condition, not proof that the answer is complete or that an agent goal is satisfied.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/Structured Output|Structured Output]]
- [[Concepts/Termination Condition|Termination Condition]]
- [[Concepts/Token|Token]]

## Sources

- Transformers text-generation documentation ([link](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation))


%% ── my notes ── %%
