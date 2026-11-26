---
id: "concept:audio-token"
type: concept
name: Audio Token
canonical: true
category: Multimodal systems
taught_in: 1
community: 18
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Audio Token

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** A discrete identifier produced by an audio codec or tokenizer for a short segment or feature of an audio signal, sometimes across several codebooks.

**Why it matters:** Discrete audio representations let sequence models process, predict, store, or generate sound using token-oriented architectures.

**In practice:** Version the codec with the model, preserve sample-rate and codebook metadata, measure reconstruction quality, and distinguish semantic audio tokens from waveform-compression tokens.

**Common confusion:** An audio token is not a fixed duration, phoneme, or word. Its meaning and time span depend on the tokenizer and codebook design.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Multimodal Model|Multimodal Model]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/06-13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split|06/13 Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split]]

## Sources

- [[Resources/SoundStream|SoundStream]] ([link](https://arxiv.org/abs/2107.03312))


%% ── my notes ── %%
