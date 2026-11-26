---
id: "lesson:04/22"
type: lesson
ref: 04/22
phase: 4
num: 22
title: 3D Gaussian Splatting from Scratch
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 3
libraries:
  - numpy
  - torch
aliases:
  - 04/22
  - 04-22
tags:
  - phase/04
  - type/build
source: ai-engineering-from-scratch/phases/04-computer-vision/22-3d-gaussian-splatting/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/22-3d-gaussian-splatting"
---

# 04/22 3D Gaussian Splatting from Scratch

> A scene is a cloud of millions of 3D Gaussians. Each one has a position, orientation, scale, opacity, and a colour that depends on viewing direction. Rasterise them, backprop through the rasterisation, done.

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/22-3d-gaussian-splatting/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/22-3d-gaussian-splatting) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/22-3d-gaussian-splatting) · code: main.py · quiz: 5 questions  
**Libraries:** [[Libraries/numpy (python)|numpy]], [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 13 (3D Vision & NeRF), Phase 1 Lesson 12 (Tensor Operations), Phase 4 Lesson 10 (Diffusion basics optional)`

- [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]] — Tensor Operations
- [[Lessons/04-10 Image Generation — Diffusion Models|04/10 Image Generation — Diffusion Models]] — Diffusion basics optional
- [[Lessons/04-13 3D Vision — Point Clouds & NeRFs|04/13 3D Vision — Point Clouds & NeRFs]] — 3D Vision & NeRF

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]], [[Lessons/04-07 Semantic Segmentation — U-Net|04/07 Semantic Segmentation — U-Net]]
- depth 3: [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]], [[Lessons/04-04 Image Classification|04/04 Image Classification]]

## Concepts taught

- 3DGS `lesson term` — Explicit scene representation as millions of 3D Gaussians with per-Gaussian position, rotation, scale, opacity, SH colour
- Covariance `lesson term` — Sigma = R S S^T R^T; orientation and anisotropic scale of one Gaussian
- Alpha compositing `lesson term` — Same equation as NeRF's volumetric render, now over an explicit sparse set
- [[Concepts/Densification|Densification]] `lesson term` — Adaptive addition of new Gaussians where reconstruction is under-fit
- Pruning `lesson term` — Remove Gaussians that have collapsed to near-zero opacity during training
- Spherical harmonics `lesson term` — Fourier basis on the sphere; stores colour as a function of viewing direction
- Splatfacto `lesson term` — The easiest path to training 3DGS in 2026
- KHR_gaussian_splatting `lesson term` — Khronos 2026 extension that makes 3DGS portable across viewers and engines

## Ships

- [[Artifacts/04-22 prompt-3dgs-capture-planner|prompt-3dgs-capture-planner]] `prompt` — Plan a photo capture session for 3DGS reconstruction given scene type and hardware
- [[Artifacts/04-22 skill-3dgs-export-router|skill-3dgs-export-router]] `skill` — Pick the right 3DGS export format (.ply / .splat / glTF KHR_gaussian_splatting / USD) given the downstream viewer or engine

## Further reading

- nerfstudio Splatfacto ([link](https://docs.nerf.studio/nerfology/methods/splat.html)) — reference training recipe
- Khronos KHR_gaussian_splatting extension ([link](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_gaussian_splatting/README.md)) — the 2026 portable format
- gsplat (Meta/nerfstudio) ([link](https://github.com/nerfstudio-project/gsplat)) — production-quality CUDA rasteriser
- OpenUSD 26.03 release notes ([link](https://openusd.org/release/)) — `UsdVolParticleField3DGaussianSplat` schema
- 3D Gaussian Splatting for Real-Time Radiance Field Rendering (Kerbl et al., SIGGRAPH 2023) ([link](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)) — the original paper
- THE FUTURE 3D State of Gaussian Splatting 2026 ([link](https://www.thefuture3d.com/blog-0/2026/4/4/state-of-gaussian-splatting-2026)) — industry overview


%% ── my notes ── %%
