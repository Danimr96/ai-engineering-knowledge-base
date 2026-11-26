---
id: "concept:tokenization"
type: concept
name: Tokenization
canonical: true
category: "Data & representations"
taught_in: 0
tags:
  - concept/glossary
  - category/data-and-representations
source: ai-engineering-from-scratch/glossary/terms.md
---

# Tokenization

**What it actually means:** Converting an input representation into the ordered token identifiers a specific model or tokenizer accepts.

**Why it matters:** Tokenization determines sequence length, vocabulary boundaries, cost accounting, truncation behavior, and how text or code is represented before embedding.

**In practice:** Use the exact tokenizer for the target model, version it with artifacts, and test multilingual text, code, whitespace, and special tokens.

**Common confusion:** Tokenization is not always word splitting, and two models can assign different token counts and IDs to the same input.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]]
- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Token|Token]]
- [[Concepts/Vocabulary|Vocabulary]]

## Sources

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909))


%% ── my notes ── %%
