---
title: "Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models"
authors: Zhiqiu Lin, Samuel Yu, Zhiyi Kuang, Deepak Pathak, Deva Ramanan
year: 2023
doi: 10.48550/arXiv.2301.06267
source: lin-2023-multimodality-helps-unimodality-cross-modal.md
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lin-2023-multimodality-helps-unimodality-cross-modal.pdf"
pdf_filename: lin-2023-multimodality-helps-unimodality-cross-modal.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [cross-modal, few-shot, clip, transfer]
---

## Summary

Cross-modal adaptation treats examples from other modalities as additional few-shot training examples: a text label becomes an extra shot for a visual classifier, and an audio clip becomes another. Using frozen CLIP/AudioCLIP encoders and a linear classifier, the method beats prior prompt-tuning and adapter baselines at one and two shots, and improves both image and audio classification on a new audiovisual benchmark.

## Key Contributions

- A one-line adaptation strategy: append cross-modal examples to the support set. [§1, Fig. 2]
- SOTA low-shot results with a linear probe on frozen features. [§4, Table 1]
- The first audiovisual few-shot benchmark, to the authors' knowledge. [§4–5]
- Evidence that the gain is complementary information, not just more samples: one-shot cross-modal beats most prior two-shot methods. [§4]

## Methodology and Architecture

Frozen CLIP and AudioCLIP encoders map images, text, and audio into a shared space. A linear classifier is trained on the available image examples plus text/audio examples; class names are expanded with templates. Optional partial fine-tuning of the last pooling layer is tested.

## Results

- 1-shot cross-modal probing outperforms the 2-shot results of most prior methods. [§4]
- Gains persist when combined with CoOp, Tip-Adapter, and WiSE-FT. [§4, Table 2]
- Audiovisual training improves both image and audio classification. [Abstract, §5]

The mechanism requires an already-aligned multimodal space and is demonstrated on classification, not generation or structured musical output.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — when a second modality adds complementary evidence.
- [[data-and-representation/arandjelovic-2017-look-listen-and-learn]] — learning the shared space from scratch instead of using CLIP.
- [[other/huang-2021-what-makes-multi-modal-learning-better]] — the generalisation-theory account of why more modalities can help.
