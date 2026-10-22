---
title: "Characterizing and Overcoming the Greedy Nature of Learning in Multi-modal Deep Neural Networks"
authors: Nan Wu, Stanisław Jastrzębski, Kyunghyun Cho, Krzysztof J. Geras
year: 2022
doi: 10.48550/arXiv.2202.05306
source: wu-2022-characterizing-and-overcoming-the-greedy.md
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wu-2022-characterizing-and-overcoming-the-greedy.pdf"
pdf_filename: wu-2022-characterizing-and-overcoming-the-greedy.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [multimodal, optimization, modality-imbalance, generalization]
---

## Summary

Multimodal networks are greedy: they tend to learn from whichever modality improves fastest and under-fit the rest. Wu et al. quantify this with the conditional utilisation rate — the accuracy gain from adding one modality to another — and find severe imbalances (0.63 for depth given RGB versus 0.01 for RGB given depth in one gesture model). They propose a training-time proxy and a balancing algorithm that improves generalisation on three datasets.

## Key Contributions

- The conditional utilisation rate as a diagnostic for which modality a trained model actually uses. [§4, Def. 4.1]
- Evidence that multimodal models can be worse than their best unimodal branch. [§1, §4]
- A conditional-learning-speed proxy that can be measured during training. [§5]
- A balancing intervention with generalisation gains on Colored MNIST, ModelNet40, and NVGesture. [§6, Table 1]

## Methodology and Architecture

Train the full two-branch model plus unimodal ablations; compare test accuracy with and without each modality. Because this is expensive, use per-modality learning speed as an online proxy and reweight the branches to keep their speeds comparable.

## Results

- Imbalance appears across tasks and architectures; `u(depth|RGB) = 0.63` and `u(RGB|depth) = 0.01` in the hand-gesture example. [§1]
- Balancing improves generalisation on all three datasets. [§6, Table 1]
- A multimodal model can underperform the best unimodal model when one branch dominates. [§1]

The lesson for audio→symbolic distillation is that a null result must be checked against an instrument-only or shuffled control: the student may simply have ignored the audio teacher.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — why cross-modal gains are conditional and how to test for them.
- [[other/huang-2021-what-makes-multi-modal-learning-better]] — the population-risk counterpart.
- [[other/garcia-2018-modality-distillation-with-multiple-stream]] — a distillation design that explicitly connects the privileged stream to the target stream.
