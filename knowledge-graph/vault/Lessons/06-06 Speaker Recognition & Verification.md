---
id: "lesson:06/06"
type: lesson
ref: 06/06
phase: 6
num: 6
title: "Speaker Recognition & Verification"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 58
aliases:
  - 06/06
  - 06-06
tags:
  - phase/06
  - type/build
  - community/58
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/06-speaker-recognition-verification/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/06-speaker-recognition-verification"
---

# 06/06 Speaker Recognition & Verification

> ASR asks "what did they say?" Speaker recognition asks "who said it?" The math looks the same — embeddings plus cosine — but every production decision hinges on a single EER number.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/06-speaker-recognition-verification/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/06-speaker-recognition-verification) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/06-speaker-recognition-verification) · code: main.py  
**Community:** [[Communities/58 DER · EER · WER|58 DER · EER · WER]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 02 (Spectrograms & Mel), Phase 5 · 22 (Embedding Models)`

- [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]] — Embedding Models
- [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]] — Spectrograms & Mel

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]], [[Lessons/05-14 Information Retrieval and Search|05/14 Information Retrieval and Search]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-04 GloVe, FastText, and Subword Embeddings|05/04 GloVe, FastText, and Subword Embeddings]]

## Builds on this

- [[Lessons/06-08 Voice Cloning & Voice Conversion|06/08 Voice Cloning & Voice Conversion]]
- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]]
- [[Lessons/06-16 Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify|06/16 Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify]]
- [[Lessons/06-17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards|06/17 Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards]]

## Concepts taught

- [[Concepts/EER|EER]] `lesson term` — Threshold where False Accept = False Reject.
- [[Concepts/Verification|Verification]] `lesson term` — "Is this Alice?"
- Identification `lesson term` — "Who is speaking?"
- Open-set `lesson term` — Test set can contain unenrolled speakers.
- Enrollment `lesson term` — Computing a speaker's reference embedding.
- AAM-softmax `lesson term` — Softmax with additive angular margin; forces cluster separation.
- PLDA `lesson term` — Probabilistic LDA; likelihood-ratio scoring on top of embeddings.
- [[Concepts/DER|DER]] `lesson term` — Diarization Error Rate — miss + false alarm + confusion.

## Ships

- [[Artifacts/06-06 speaker-verifier|speaker-verifier]] `skill` — Design a speaker verification or diarization pipeline with model choice, enrollment protocol, and threshold tuning.

## Further reading

- Desplanques et al. (2020). ECAPA-TDNN ([link](https://arxiv.org/abs/2005.07143)) — dominant architecture 2020–2026.
- Chen et al. (2022). WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing ([link](https://arxiv.org/abs/2110.13900)) — SSL backbone for SV and diarization.
- Snyder et al. (2018). X-Vectors: Robust DNN Embeddings for Speaker Recognition ([link](https://www.danielpovey.com/files/2018_icassp_xvectors.pdf)) — the classic deep-embedding paper.
- [[Resources/Bredin et al. (2023). pyannote.audio 3.1|Bredin et al. (2023). pyannote.audio 3.1]] ([link](https://github.com/pyannote/pyannote-audio)) — production diarization + embedding stack. ·  also cited by 1 other lesson
- VoxCeleb leaderboard (updated 2026) ([link](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/)) — current EER standings across models.


%% ── my notes ── %%
