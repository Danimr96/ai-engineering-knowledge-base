---
id: "concept:temperature"
type: concept
name: Temperature
canonical: true
category: "Models & inference"
taught_in: 8
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Temperature

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* A creativity setting.

**What it actually means:** A decoding parameter that rescales logits before a probability distribution is formed. Higher positive values usually flatten the distribution; lower positive values sharpen it.

**Why it matters:** Temperature changes sampling behavior, not the model's knowledge or factuality.

**Common confusion:** A zero setting is often implemented as greedy decoding, but exact behavior and determinism depend on the provider, sampler, seed support, and serving system.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/Hyperparameter|Hyperparameter]]
- [[Concepts/Logits|Logits]]
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]]
- [[Concepts/Softmax|Softmax]]
- [[Concepts/Token|Token]]
- [[Concepts/Top-k Sampling|Top-k Sampling]]

## Taught in

- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]] — Divides logits by T before softmax. T<1 sharpens (more confident), T>1 flattens (more diverse)
- [[Lessons/01-22 Stochastic Processes|01/22 Stochastic Processes]] — Parameter controlling the tradeoff between exploration and exploitation
- [[Lessons/03-05 Loss Functions|03/05 Loss Functions]] — A scalar divisor on logits/similarities that controls how peaked the resulting distribution is; lower = sharper
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — Divide logits by T; T→0 = greedy, T→∞ = uniform.
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — A scaling factor on the logit distribution before softmax -- higher values flatten the distribution (more random), lower values sharpen it (more deterministic)
- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]] — Scalar that scales logits before softmax/sigmoid; controls sharpness of the distribution
- [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]] — Divide logits by T before softmax; T less than 1 sharpens, T equal to 1 keeps the natural distribution, T greater than 1 flattens
- [[Lessons/19-62 Vision-Language Pretraining|19/62 Vision-Language Pretraining]] — Scalar that controls how peaked the contrastive softmax is


%% ── my notes ── %%
