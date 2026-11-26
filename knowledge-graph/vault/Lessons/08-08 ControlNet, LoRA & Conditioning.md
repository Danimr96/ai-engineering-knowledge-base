---
id: "lesson:08/08"
type: lesson
ref: 08/08
phase: 8
num: 8
title: "ControlNet, LoRA & Conditioning"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 68
aliases:
  - 08/08
  - 08-08
tags:
  - phase/08
  - type/build
  - community/68
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/08-controlnet-lora-conditioning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/08-controlnet-lora-conditioning"
---

# 08/08 ControlNet, LoRA & Conditioning

> Text alone is a clumsy control signal. ControlNet lets you clone a pretrained diffusion model and steer it with a depth map, pose skeleton, scribble, or edge image. LoRA lets you fine-tune a 2B-parameter model by training 10 million parameters. Together they turned Stable Diffusion from a toy into the 2026 image pipeline that ships at every agency.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/08-controlnet-lora-conditioning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/08-controlnet-lora-conditioning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/08-controlnet-lora-conditioning) · code: main.py  
**Community:** [[Communities/68 CFG · ControlNet|68 CFG · ControlNet]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 07 (Latent Diffusion), Phase 10 (LLMs from Scratch — for LoRA foundation)`

- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]] — Latent Diffusion
- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from Scratch — for LoRA foundation ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]], [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Builds on this

- [[Lessons/08-09 Inpainting, Outpainting & Image Editing|08/09 Inpainting, Outpainting & Image Editing]]

## Concepts taught

- [[Concepts/ControlNet|ControlNet]] `lesson term` — Cloned encoder + zero-conv skips; reads a conditioning image.
- Zero convolution `lesson term` — 1×1 conv initialized to zero; ControlNet starts as no-op.
- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]] (as *LoRA*) `glossary` — W + B @ A, r << d; 100x fewer params than a full fine-tune.
- rank r `lesson term` — LoRA compression; 4-16 typical, 64+ for heavy personalization.
- IP-Adapter `lesson term` — Small image-conditioning adapter via CLIP-image tokens.
- DreamBooth `lesson term` — Train the full model on ~30 images of a subject.
- Textual Inversion `lesson term` — Learn a new word embedding only; legacy, mostly replaced.

## Ships

- [[Artifacts/08-08 sd-toolkit-composer|sd-toolkit-composer]] `skill` — Compose ControlNets, LoRAs, and IP-Adapters on top of an SD / Flux base for a given set of inputs.

## Further reading

- [[Resources/LoRA paper|LoRA paper]] ([link](https://arxiv.org/abs/2106.09685)) — LoRA (originally for LLMs; ports to diffusion). ·  also cited by 1 other lesson
- Ruiz et al. (2023). DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation ([link](https://arxiv.org/abs/2208.12242)) — DreamBooth.
- Zhang, Rao, Agrawala (2023). Adding Conditional Control to Text-to-Image Diffusion Models ([link](https://arxiv.org/abs/2302.05543)) — ControlNet.
- Mou et al. (2023). T2I-Adapter: Learning Adapters to Dig Out More Controllable Ability ([link](https://arxiv.org/abs/2302.08453)) — lighter alternative to ControlNet.
- Ye et al. (2023). IP-Adapter: Text Compatible Image Prompt Adapter ([link](https://arxiv.org/abs/2308.06721)) — IP-Adapter.
- HuggingFace Diffusers — ControlNet / LoRA / IP-Adapter docs ([link](https://huggingface.co/docs/diffusers/training/controlnet)) — reference pipelines.


%% ── my notes ── %%
