---
id: "lesson:05/08"
type: lesson
ref: 05/08
phase: 5
num: 8
title: CNNs and RNNs for Text
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 8
code_files: 1
concepts: 6
prereqs: 3
aliases:
  - 05/08
  - 05-08
tags:
  - phase/05
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text"
---

# 05/08 CNNs and RNNs for Text

> Convolutions learn n-grams. Recurrences remember. Both are superseded by attention. Both still matter on constrained hardware.

**Phase:** [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text) · code: main.py · quiz: 8 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 · 11 (PyTorch Intro), Phase 5 · 03 (Word Embeddings), Phase 4 · 02 (Convolutions from Scratch)`

- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — PyTorch Intro
- [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]] — Convolutions from Scratch
- [[Lessons/05-03 Word Embeddings — Word2Vec from Scratch|05/03 Word Embeddings — Word2Vec from Scratch]] — Word Embeddings

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]]
- depth 3: [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-04 Activation Functions|03/04 Activation Functions]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/03-08 Weight Initialization and Training Stability|03/08 Weight Initialization and Training Stability]], [[Lessons/03-09 Learning Rate Schedules and Warmup|03/09 Learning Rate Schedules and Warmup]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]]

## Builds on this

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]]
- [[Lessons/06-03 Audio Classification — From k-NN on MFCCs to AST and BEATs|06/03 Audio Classification — From k-NN on MFCCs to AST and BEATs]]
- [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]]

## Concepts taught

- TextCNN `lesson term` — Stack of 1D convolutions over word embeddings with global max-pool. Kim (2014).
- RNN `lesson term` — Hidden state updated at each time step: h_t = f(W x_t + U h{t-1}).
- LSTM `lesson term` — Adds input / forget / output gates + a cell state. Trains stably through long sequences.
- GRU `lesson term` — Two gates instead of three. Similar accuracy, fewer parameters.
- [[Concepts/Bidirectional|Bidirectional]] `lesson term` — Forward + backward RNN concatenated. Every token sees both sides of its context.
- [[Concepts/Vanishing gradient|Vanishing gradient]] `lesson term` — Repeated multiplication by <1 weights in plain RNNs makes early-step gradients effectively zero.

## Ships

- [[Artifacts/05-08 text-encoder-picker|text-encoder-picker]] `prompt` — Pick a text encoder architecture for a given constraint set.

## Further reading

- Kim, Y. (2014). Convolutional Neural Networks for Sentence Classification ([link](https://arxiv.org/abs/1408.5882)) — the TextCNN paper. Eight pages. Readable.
- [[Resources/Hochreiter, S. and Schmidhuber, J. (1997). Long Short-Term Memory|Hochreiter, S. and Schmidhuber, J. (1997). Long Short-Term Memory]] ([link](https://www.bioinf.jku.at/publications/older/2604.pdf)) — the LSTM paper. Unexpectedly lucid. ·  also cited by 1 other lesson
- Olah, C. (2015). Understanding LSTM Networks ([link](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)) — the diagrams that made LSTMs accessible to everyone.


%% ── my notes ── %%
