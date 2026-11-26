---
id: "concept:byte-pair-encoding-bpe"
type: concept
name: Byte Pair Encoding (BPE)
canonical: true
category: "Data & representations"
taught_in: 3
tags:
  - concept/glossary
  - category/data-and-representations
source: ai-engineering-from-scratch/glossary/terms.md
---

# Byte Pair Encoding (BPE)

**What it actually means:** A subword-tokenization method that repeatedly merges frequent adjacent units to construct a fixed vocabulary from training text.

**Why it matters:** It balances vocabulary size with the ability to represent rare or unseen words as smaller units.

**In practice:** Train the tokenizer only on approved corpus splits, version its merge rules with the model, and inspect how it segments code, multilingual text, and whitespace.

**Common confusion:** BPE is one tokenizer family, not a universal description of how every model creates tokens.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Embedding|Embedding]]
- [[Concepts/Token|Token]]
- [[Concepts/Tokenization|Tokenization]]
- [[Concepts/Vocabulary|Vocabulary]]

## Taught in

- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]] `alias` — Iterative merging of most-frequent adjacent pairs until vocabulary hits target size.
- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]] `alias` — Greedy merge of most-frequent character pairs until target vocab size hit.
- [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] `alias` — Byte Pair Encoding -- iteratively merge the most frequent adjacent pair of tokens until the target vocabulary size is reached

## Sources

- [[Resources/Neural Machine Translation of Rare Words with Subword Units|Neural Machine Translation of Rare Words with Subword Units]] ([link](https://arxiv.org/abs/1508.07909))


%% ── my notes ── %%
