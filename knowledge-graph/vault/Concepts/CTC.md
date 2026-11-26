---
id: "concept:ctc"
type: concept
name: CTC
canonical: false
taught_in: 3
community: 5
tags:
  - concept/lesson-term
  - community/05
source: ai-engineering-from-scratch/phases/04-computer-vision/19-ocr-document-understanding/docs/en.md
---

# CTC

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* "Alignment-free loss"

**What it actually means:** Loss that trains a sequence model without per-timestep labels; marginalises over alignments

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-19 OCR & Document Understanding|04/19 OCR & Document Understanding]]
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]] — Marginal over all frame-to-token alignments; non-AR.
- [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]] — Classic ASR loss for alignment-free training; Whisper does NOT use it.


%% ── my notes ── %%
