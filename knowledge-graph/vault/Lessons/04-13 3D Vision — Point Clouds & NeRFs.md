---
id: "lesson:04/13"
type: lesson
ref: 04/13
phase: 4
num: 13
title: "3D Vision — Point Clouds & NeRFs"
lesson_type: learn+build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 5
code_files: 1
concepts: 8
prereqs: 2
community: 78
libraries:
  - torch
aliases:
  - 04/13
  - 04-13
tags:
  - phase/04
  - type/learn+build
  - community/78
source: ai-engineering-from-scratch/phases/04-computer-vision/13-3d-vision-nerf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/13-3d-vision-nerf"
---

# 04/13 3D Vision — Point Clouds & NeRFs

> 3D vision comes in two flavours. Point clouds are the sensor's raw output. NeRFs are the learned volumetric field. Both answer "what is where in space."

**Phase:** [[Phases/04 Computer Vision|Phase 4: Computer Vision]] · **Type:** Learn + Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/04-computer-vision/13-3d-vision-nerf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/04-computer-vision/13-3d-vision-nerf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/04-computer-vision/13-3d-vision-nerf) · code: main.py · quiz: 5 questions  
**Community:** [[Communities/78 3D Gaussian splatting · NeRF|78 3D Gaussian splatting · NeRF]] · **Libraries:** [[Libraries/torch (python)|torch]]  

## Prerequisites

Stated upstream: `Phase 4 Lesson 03 (CNNs), Phase 1 Lesson 12 (Tensor Operations)`

- [[Lessons/01-12 Tensor Operations|01/12 Tensor Operations]] — Tensor Operations
- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — CNNs

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]], [[Lessons/04-01 Image Fundamentals — Pixels, Channels, Color Spaces|04/01 Image Fundamentals — Pixels, Channels, Color Spaces]], [[Lessons/04-02 Convolutions from Scratch|04/02 Convolutions from Scratch]]
- depth 3: [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]

## Builds on this

- [[Lessons/04-16 Build a Complete Vision Pipeline — Capstone|04/16 Build a Complete Vision Pipeline — Capstone]]
- [[Lessons/04-22 3D Gaussian Splatting from Scratch|04/22 3D Gaussian Splatting from Scratch]]

## Concepts taught

- Point cloud `lesson term` — Unordered set of (x, y, z) + optional features per point
- PointNet `lesson term` — Shared MLP per point + symmetric (max) pool; permutation-invariant by construction
- [[Concepts/NeRF|NeRF]] `lesson term` — Network mapping (x, y, z, dir) to (density, colour); rendered by ray casting
- [[Concepts/Positional encoding|Positional encoding]] `lesson term` — Encode each coordinate into sin/cos at multiple frequencies to overcome MLP low-frequency bias
- Volumetric rendering `lesson term` — Composite samples along a ray into a single pixel using transmittance and alpha
- Instant-NGP `lesson term` — Replaces NeRF's coordinate MLP with a multi-resolution hash grid; 100-1000x faster
- [[Concepts/3D Gaussian splatting|3D Gaussian splatting]] `lesson term` — Scene = collection of 3D Gaussians; renders in real time, trains in minutes
- SDF `lesson term` — Function returning signed distance to the nearest surface; another implicit representation

## Ships

- [[Artifacts/04-13 prompt-3d-task-router|prompt-3d-task-router]] `prompt` — Route to the right 3D representation (point cloud, mesh, voxel, NeRF, Gaussian splat) based on task and input
- [[Artifacts/04-13 skill-point-cloud-loader|skill-point-cloud-loader]] `skill` — Write a PyTorch Dataset for .ply / .pcd / .xyz files with correct normalisation, centring, and point sampling

## Further reading

- PointNet (Qi et al., 2017) ([link](https://arxiv.org/abs/1612.00593)) — the permutation-invariant classifier
- [[Resources/NeRF (Mildenhall et al., 2020)|NeRF (Mildenhall et al., 2020)]] ([link](https://arxiv.org/abs/2003.08934)) — the paper that made 3D reconstruction from photos a neural-net problem ·  also cited by 1 other lesson
- Instant-NGP (Müller et al., 2022) ([link](https://arxiv.org/abs/2201.05989)) — hash grids, 1000x speedup
- [[Resources/3D Gaussian Splatting (Kerbl et al., 2023)|3D Gaussian Splatting (Kerbl et al., 2023)]] ([link](https://arxiv.org/abs/2308.04079)) — the architecture that replaced NeRFs in production ·  also cited by 1 other lesson


%% ── my notes ── %%
