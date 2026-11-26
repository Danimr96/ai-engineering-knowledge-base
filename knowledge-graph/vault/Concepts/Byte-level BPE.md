---
id: "concept:byte-level-bpe"
type: concept
name: Byte-level BPE
canonical: false
taught_in: 4
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/en.md
---

# Byte-level BPE

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* BPE on raw bytes

**What it actually means:** GPT-2's scheme. Vocabulary starts with 256 bytes, so nothing is ever OOV.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]]
- [[Lessons/05-19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece|05/19 Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece]] — BPE over raw 256 bytes; GPT-2 / Llama use this.
- [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] — BPE operating on raw bytes (0-255) instead of Unicode characters, guaranteeing no unknown tokens for any input
- [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]] — BPE with a base vocabulary of 256 byte values -- handles any input without unknown tokens


%% ── my notes ── %%
