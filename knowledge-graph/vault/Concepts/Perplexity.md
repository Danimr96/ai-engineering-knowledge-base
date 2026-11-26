---
id: "concept:perplexity"
type: concept
name: Perplexity
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

# Perplexity

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* How surprised a language model is by a dataset.

**What it actually means:** The exponentiated average negative log-likelihood under a stated tokenization and logarithm convention. Lower values mean the model assigned higher probability to the evaluated sequence.

**Common confusion:** Perplexity is not comparable across different tokenizers or evaluation setups and does not directly measure factuality or usefulness.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Cross-Entropy|Cross-Entropy]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — Exponential of cross-entropy. The effective vocabulary size the model is choosing from at each step.
- [[Lessons/01-10 Dimensionality Reduction|01/10 Dimensionality Reduction]] — Controls the effective number of neighbors each point considers. Low perplexity focuses on very local structure. High perplexity captures broader patterns.
- [[Lessons/05-16 Text Generation Before Transformers — N-gram Language Models|05/16 Text Generation Before Transformers — N-gram Language Models]] — exp(-average log-prob) on held-out data. Lower is better.
- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]] — exp(-avg(log P(token_i given context))) -- lower means the model assigns higher probability to the actual tokens


%% ── my notes ── %%
