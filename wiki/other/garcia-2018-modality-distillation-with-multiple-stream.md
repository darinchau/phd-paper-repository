---
title: "Modality Distillation with Multiple Stream Networks for Action Recognition"
authors: Nuno C. Garcia, Pietro Morerio, Vittorio Murino
year: 2018
doi: 10.48550/arXiv.1806.07110
source: garcia-2018-modality-distillation-with-multiple-stream.md
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/garcia-2018-modality-distillation-with-multiple-stream.pdf"
pdf_filename: garcia-2018-modality-distillation-with-multiple-stream.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [modality-distillation, privileged-information, action-recognition, cross-modal]
---

## Summary

Garcia et al. train an RGB action-recognition model with depth as privileged information and deploy it with RGB only. A hallucination network learns to imitate depth features from RGB, connected multiplicatively to the RGB stream, and is trained with soft labels, hard labels, and feature-map distance. The RGB-only model at test time beats RGB-only training and reports state-of-the-art NTU RGB+D results for that setting.

## Key Contributions

- Generalised distillation for the missing-modality setting: extra modality at training, single modality at test. [§1]
- A hallucination network with multiplicative cross-stream connections, not just feature regression. [§3]
- A combined soft-label, hard-label, and feature-distance objective. [§3]
- Robustness analysis with noisy depth at training time. [§4, Table 3]

## Methodology and Architecture

Three streams: RGB, depth (teacher), and a hallucination stream that takes RGB and predicts depth-like features. The classifier consumes the RGB and hallucinated features; at inference the depth stream is removed entirely.

## Results

- State-of-the-art RGB-only action classification on NTU RGB+D at the time of publication. [Table 2]
- Moderate depth noise at training degrades performance gracefully rather than collapsing it. [Table 3]
- The transfer works because depth and RGB are spatially aligned; the paper does not test a pairing where the privileged modality is only loosely coupled.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — the privileged-modality pattern and its assumptions.
- [[other/hoffman-2016-learning-with-side-information-through]] — the earlier hallucination architecture.
- [[other/wu-2022-characterizing-and-overcoming-the-greedy]] — the risk that the student ignores the privileged stream.
