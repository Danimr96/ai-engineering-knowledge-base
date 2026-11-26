---
id: "concept:vocabulary"
type: concept
name: Vocabulary
canonical: true
category: "Data & representations"
taught_in: 0
tags:
  - concept/glossary
  - category/data-and-representations
source: ai-engineering-from-scratch/glossary/terms.md
---

# Vocabulary

**What it actually means:** The finite mapping between token identifiers and the units a tokenizer can emit, including ordinary, byte-level, and special control tokens.

**Why it matters:** Vocabulary design affects sequence length, multilingual coverage, code representation, embedding size, and compatibility between tokenizers and model weights.

**In practice:** Version the vocabulary and special-token assignments with the model, test encode-decode round trips, and never substitute a tokenizer with merely similar token names.

**Common confusion:** A model vocabulary is not a dictionary of human words; many entries are fragments, bytes, whitespace patterns, or control symbols.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Token|Token]]
- [[Concepts/Tokenization|Tokenization]]

## Sources

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909))


%% ── my notes ── %%
