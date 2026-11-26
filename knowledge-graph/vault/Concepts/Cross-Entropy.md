---
id: "concept:cross-entropy"
type: concept
name: Cross-Entropy
canonical: true
category: "Math & training"
taught_in: 4
community: 5
tags:
  - concept/glossary
  - category/math-and-training
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Cross-Entropy

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* The classification loss.

**What it actually means:** A loss based on the negative log probability assigned to the target outcome. In next-token training, it penalizes the model when it assigns low probability to the observed next token.

**Common confusion:** Perplexity is the exponentiated average cross-entropy only when the averaging and logarithm base are defined consistently.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Logits|Logits]]
- [[Concepts/Loss Function|Loss Function]]
- [[Concepts/Perplexity|Perplexity]]
- [[Concepts/Softmax|Softmax]]

## Taught in

- [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]] — -sum(p_true log(p_predicted)). Measures how different two distributions are. Lower is better
- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — Average surprise when using model distribution Q to encode events from true distribution P.
- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]] — Measures divergence between predicted probability distribution and true distribution using -log(p)
- [[Lessons/04-04 Image Classification|04/04 Image Classification]] — Negative log-probability of the correct class; combines log-softmax and NLL in one stable op


%% ── my notes ── %%
