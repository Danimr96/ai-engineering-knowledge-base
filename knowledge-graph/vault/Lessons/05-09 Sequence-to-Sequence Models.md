---
id: "lesson:05/09"
type: lesson
ref: 05/09
phase: 5
num: 9
title: Sequence-to-Sequence Models
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 2
community: 12
aliases:
  - 05/09
  - 05-09
tags:
  - phase/05
  - type/build
  - community/12
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence"
---

# 05/09 Sequence-to-Sequence Models

> Two RNNs pretending to be a translator. The bottleneck they hit is the reason attention exists.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence) · code: main.py · quiz: 8 questions  
**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 08 (CNNs + RNNs for Text), Phase 3 · 11 (PyTorch Intro)`

- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — PyTorch Intro
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]] — CNNs + RNNs for Text

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]

## Builds on this

- [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]
- [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]]
- [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]]

## Concepts taught

- [[Concepts/Encoder|Encoder]] `glossary` — Reads source. Produces per-step hidden states and a final context vector.
- [[Concepts/Decoder|Decoder]] `glossary` — Initialized from context vector. Generates target tokens one at a time.
- Context vector `lesson term` — Final encoder hidden state. Fixed size. The bottleneck attention solves.
- [[Concepts/Teacher forcing|Teacher forcing]] `lesson term` — Feed the ground-truth previous token at training time. Stabilizes learning.
- Exposure bias `lesson term` — Model trained on true tokens never practiced recovering from its own mistakes.
- [[Concepts/Beam search|Beam search]] `lesson term` — Keep top-k partial sequences alive at each step instead of committing greedily.

## Ships

- [[Artifacts/05-09 seq2seq-design|seq2seq-design]] `prompt` — Design a sequence-to-sequence pipeline for a given task.

## Further reading

- Cho et al. (2014). Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation ([link](https://arxiv.org/abs/1406.1078)) — introduced the GRU and the encoder-decoder framing.
- [[Resources/Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate|Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate]] ([link](https://arxiv.org/abs/1409.0473)) — the attention paper. Read immediately after this lesson. ·  also cited by 2 other lessons
- Sutskever, Vinyals, Le (2014). Sequence to Sequence Learning with Neural Networks ([link](https://arxiv.org/abs/1409.3215)) — the original seq2seq paper. Four pages.
- PyTorch NLP from Scratch tutorial ([link](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)) — buildable seq2seq + attention code.


%% ── my notes ── %%
