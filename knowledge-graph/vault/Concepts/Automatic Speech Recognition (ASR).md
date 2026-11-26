---
id: "concept:automatic-speech-recognition-asr"
type: concept
name: Automatic Speech Recognition (ASR)
canonical: true
category: Multimodal systems
taught_in: 3
community: 23
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/23
source: ai-engineering-from-scratch/glossary/terms.md
---

# Automatic Speech Recognition (ASR)

**Community:** [[Communities/23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph|23 Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph]]

**What it actually means:** The task and system pipeline that maps a speech signal to a transcription, often with optional token or segment timing and confidence information.

**Why it matters:** Speech interfaces depend on more than language modeling. Acoustic variation, segmentation, decoding, vocabulary, and domain conditions all affect the final transcript.

**In practice:** Evaluate word or character errors by language, speaker, noise, and domain, retain timestamps when downstream grounding needs them, and test the exact audio preprocessing used in production.

**Common confusion:** ASR transcribes what was said. Determining who spoke requires diarization or speaker recognition, while translation and intent understanding are separate tasks.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Audio Token|Audio Token]]
- [[Concepts/Encoder|Encoder]]
- [[Concepts/Multimodal Model|Multimodal Model]]
- [[Concepts/Tokenization|Tokenization]]

## Taught in

- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]
- [[Lessons/15-18 Llama Guard and Input-Output Classification|15/18 Llama Guard and Input/Output Classification]] `alias` — Fraction of attacks that bypass the classifier
- [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]] `alias` — Primary metric; must be reported with query budget and judge identity

## Sources

- [[Resources/Connectionist Temporal Classification|Connectionist Temporal Classification]] ([link](https://www.cs.toronto.edu/~graves/icml_2006.pdf))


%% ── my notes ── %%
