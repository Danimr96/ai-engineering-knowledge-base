---
id: "concept:logits"
type: concept
name: Logits
canonical: true
category: "Models & inference"
taught_in: 4
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Logits

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** The model's unnormalized numeric scores for candidate outcomes before a normalization function or decoding rule converts them into selections.

**Why it matters:** Temperature, softmax, top-k, and top-p operate on or derive from logits, so logits connect model computation to generated tokens.

**In practice:** Inspect logits or log probabilities when the API exposes them, apply masks before sampling, and avoid interpreting raw magnitude as calibrated confidence.

**Common confusion:** Logits are not probabilities and are not comparable across unrelated positions, models, or tasks without a defined transformation.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Calibration|Calibration]]
- [[Concepts/Cross-Entropy|Cross-Entropy]]
- [[Concepts/Knowledge Distillation|Knowledge Distillation]]
- [[Concepts/Softmax|Softmax]]
- [[Concepts/Temperature|Temperature]]
- [[Concepts/Token|Token]]
- [[Concepts/Top-k Sampling|Top-k Sampling]]

## Taught in

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — Unnormalized scores before softmax. Named after the logistic function
- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] `alias` — The unnormalized output of the final layer before applying softmax or sigmoid
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — The pre-softmax vector of C numbers per image; cross-entropy expects these, not softmaxed values
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — Raw output of the LM head before softmax; sampling happens on these.

## Sources

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762))


%% ── my notes ── %%
