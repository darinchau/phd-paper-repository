---
title: "CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion"
authors: "Zixiang Zhao, Haowen Bai, Jiangshe Zhang, Yulun Zhang, Shuang Xu, Zudi Lin, Radu Timofte, and Luc Van Gool"
year: 2023
doi: 10.48550/arXiv.2211.14461
category: other
source: zhao-2023-cddfuse-correlation-driven-dual-branch.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhao-2023-cddfuse-correlation-driven-dual-branch.pdf"
pdf_filename: zhao-2023-cddfuse-correlation-driven-dual-branch.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

Multi-modality image fusion combines complementary infrared/visible or medical images while preserving modality-shared structure and modality-specific detail. The authors identify three problems with prior CNN/autoencoder approaches: poor controllability/interpretability, limited local receptive fields, and loss of high-frequency information during forward propagation (`...txt:63–78`).

## Key Contributions

CDDFuse digest

**Source inspected:** full `/tmp/paper-digest/2211.14461v2.pdf` and extracted text through its references (`/tmp/paper-digest/2211.14461v2.txt`, pp. 1–11). No files modified.

#### Problem

Multi-modality image fusion combines complementary infrared/visible or medical images while preserving modality-shared structure and modality-specific detail. The authors identify three problems with prior CNN/autoencoder approaches: poor controllability/interpretability, limited local receptive fields, and loss of high-frequency information during forward propagation (`...txt:63–78`).

#### Method

CDDFuse uses:

- A shared Restormer-based shallow feature encoder.
- A **dual branch**:
  - Lite Transformer (LT) branch for low-frequency, global/long-range “base” features.
  - Invertible Neural Network (INN) branch for high-frequency, local “detail” features (`...txt:178–235`).
- A correlation-driven decomposition loss: base features from the two modalities are encouraged to correlate, while detail features are encouraged to decorrelate (`...txt:277–300`).
- Separate LT/INN fusion layers followed by a Restormer decoder.
- Two-stage training: first reconstruct each source image; then fuse decomposed features (`...txt:239–276`).

The authors’ central assumption is that low-frequency information is modality-shared, whereas high-frequency information is modality-specific (`...txt:80–99`). Their “interpretability” claim is therefore architectural/constraint-based, not a demonstrated human-understandable explanation mechanism.

#### Results claimed by the authors

On infrared-vis

The complete evidence-grounded digest is in [`sources/zhao-2023-cddfuse-correlation-driven-dual-branch.md`](../../sources/zhao-2023-cddfuse-correlation-driven-dual-branch.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
