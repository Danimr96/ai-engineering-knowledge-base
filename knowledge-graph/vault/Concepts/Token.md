---
id: "concept:token"
type: concept
name: Token
canonical: true
category: "Data & representations"
taught_in: 5
community: 5
tags:
  - concept/glossary
  - category/data-and-representations
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Token

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* A word-sized piece of model input or output.

**What it actually means:** An integer identifier produced by a model-specific tokenizer from text, bytes, images, audio, or another input representation. A token can be a whole word, part of a word, punctuation, whitespace, a byte sequence, or a special control symbol.

**Common confusion:** Character-to-token ratios vary by language, content, and tokenizer, so count with the target model's tokenizer or provider tools.

**Category:** [[Categories/Data & representations|Data & representations]]

## Related concepts

- [[Concepts/Audio Token|Audio Token]]
- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Byte Pair Encoding (BPE)|Byte Pair Encoding (BPE)]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Early Fusion|Early Fusion]]
- [[Concepts/Image Token|Image Token]]
- [[Concepts/Logits|Logits]]
- [[Concepts/Modality|Modality]]
- [[Concepts/Patch Embedding|Patch Embedding]]
- [[Concepts/Perplexity|Perplexity]]
- [[Concepts/Stop Sequence|Stop Sequence]]
- [[Concepts/Temperature|Temperature]]
- [[Concepts/Token Budget|Token Budget]]
- [[Concepts/Tokenization|Tokenization]]
- [[Concepts/Vocabulary|Vocabulary]]

## Taught in

- [[Lessons/00-04 APIs & Keys|00/04 APIs & Keys]] — A billing unit: input and output tokens are counted and charged separately
- [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]] — Whatever unit the model consumes. Can be word, subword, character, or byte.
- [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]] `normalized` — Number of training tokens seen; determines how well the parameters get used.
- [[Lessons/08-11 Audio Generation|08/11 Audio Generation]] — Discrete index into a codebook; 1024 or 2048 typical.
- [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] — A unit in the model's vocabulary -- could be a character, subword, word, or multi-word chunk


%% ── my notes ── %%
