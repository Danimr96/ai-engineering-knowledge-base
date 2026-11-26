# Glossary

## A

### Adam (Optimizer)
- **Category:** Math & training
- **What people say:** The default optimizer.
- **What it actually means:** Adaptive moment estimation.
- **Related terms:** Softmax
- **Sources:** [Adam paper](https://arxiv.org/abs/1412.6980)

### Attention
- **Category:** Models & inference
- **What it actually means:** A weighted average of values keyed by similarity.
- **Learn it:** [Self-Attention](../phases/07-transformers/02-self-attention/)
- **Related terms:** Self-Attention, KV Cache, Softmax

### Automatic Speech Recognition (ASR)
- **Category:** Multimodal systems
- **What it actually means:** Audio to text.
- **Related terms:** Attention

## K

### KV Cache
- **Category:** Models & inference
- **What it actually means:** Cached keys and values for decoding.
- **Aliases:** KV-cache, key-value cache
- **Related terms:** Attention

## S

### Self-Attention
- **Category:** Models & inference
- **What it actually means:** Attention where queries, keys and values come from the same sequence.
- **Common confusion:** Not the same as cross-attention.
- **Learn it:** [Self-Attention](../phases/07-transformers/02-self-attention/)
- **Related terms:** Attention

### Softmax
- **Category:** Math & training
- **What it actually means:** Exponentiate and normalise.
- **Related terms:** Attention, Adam (Optimizer)
