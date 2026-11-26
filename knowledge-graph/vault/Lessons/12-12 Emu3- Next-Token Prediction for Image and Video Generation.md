---
id: "lesson:12/12"
type: lesson
ref: 12/12
phase: 12
num: 12
title: "Emu3: Next-Token Prediction for Image and Video Generation"
lesson_type: learn
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 6
prereqs: 1
aliases:
  - 12/12
  - 12-12
tags:
  - phase/12
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/12-multimodal-ai/12-emu3-next-token-for-generation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/12-emu3-next-token-for-generation"
---

# 12/12 Emu3: Next-Token Prediction for Image and Video Generation

> BAAI's Emu3 (Wang et al., September 2024) is the 2024 result that should have ended the diffusion-versus-autoregressive debate. A single Llama-style decoder-only transformer, trained only on the next-token-prediction objective, across a unified vocabulary of text + VQ image tokens + 3D VQ video tokens, beats SDXL on image generation and LLaVA-1.6 on perception. No CLIP loss. No diffusion schedule. Classifier-free guidance is used at inference for quality, but the core training objective is next-token prediction with teacher forcing. Published in Nature. This lesson reads the Emu3 thesis — why a better tokenizer plus scale is all you need — and contrasts with diffusion approaches.

**Phase:** [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] · **Type:** Learn · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/12-multimodal-ai/12-emu3-next-token-for-generation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/12-multimodal-ai/12-emu3-next-token-for-generation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/12-multimodal-ai/12-emu3-next-token-for-generation) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 12 · 11 (Chameleon)`

- [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]] — Chameleon

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]]
- depth 3: [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Concepts taught

- [[Concepts/Next-token prediction|Next-token prediction]] `lesson term` — Standard autoregressive loss: predict token[i+1] given token[0..i]; works for every modality when tokenized
- IBQ tokenizer `lesson term` — A class of VQ-VAE with larger codebooks (32768+) and better reconstruction than Chameleon's
- 3D VQ `lesson term` — Codebook indexed by (time, row, col); one token covers a 4x4x4 pixel cube
- [[Concepts/Classifier-free guidance|Classifier-free guidance]] `lesson term` — Mix conditional and unconditional logits with weight gamma; boosts image quality at inference
- Unified vocabulary `lesson term` — Text + image + video all draw from the same integer space; model predicts whichever modality comes next
- MJHQ-30K `lesson term` — Midjourney-quality benchmark with 30k prompts; Emu3 reports FID here

## Ships

- [[Artifacts/12-12 token-gen-cost-analyzer|token-gen-cost-analyzer]] `skill` — Compute token counts, inference latency, and quality ceiling for Emu3-style next-token generation and pick between Emu3-family and diffusion.

## Further reading

- Sun et al. — Emu: Generative Pretraining in Multimodality (arXiv:2307.05222) ([link](https://arxiv.org/abs/2307.05222))
- Yu et al. — MAGVIT-v2 (arXiv:2310.05737) ([link](https://arxiv.org/abs/2310.05737))
- [[Resources/Liu et al. — LWM (arXiv-2402.08268)|Liu et al. — LWM (arXiv:2402.08268)]] ([link](https://arxiv.org/abs/2402.08268)) ·  also cited by 1 other lesson
- [[Resources/Tian et al., 2024 — -Visual Autoregressive Modeling- Scalable Image Generation via Next-Scale Prediction|Tian et al., 2024 — "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction]] ([link](https://arxiv.org/abs/2404.02905)) ·  also cited by 1 other lesson
- Wang et al. — Emu3: Next-Token Prediction is All You Need (arXiv:2409.18869) ([link](https://arxiv.org/abs/2409.18869))


%% ── my notes ── %%
