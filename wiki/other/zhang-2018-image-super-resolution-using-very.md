---
title: "Image Super-Resolution Using Very Deep Residual Channel Attention Networks"
authors: "Yulun Zhang, Kunpeng Li, Kai Li, Lichen Wang, Bineng Zhong, and Yun Fu"
year: 2018
doi: 10.48550/arXiv.1807.02758
category: other
source: zhang-2018-image-super-resolution-using-very.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhang-2018-image-super-resolution-using-very.pdf"
pdf_filename: zhang-2018-image-super-resolution-using-very.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

Single-image super-resolution: reconstruct a high-resolution image from a low-resolution counterpart, an ill-posed inverse problem with multiple plausible solutions (Sections 1, 4.1).

## Key Contributions

Evidence-grounded digest

**Paper:** Zhang et al., *Image Super-Resolution Using Very Deep Residual Channel Attention Networks* (arXiv:1807.02758v2, 16-page PDF, 2018).

#### Problem

Single-image super-resolution: reconstruct a high-resolution image from a low-resolution counterpart, an ill-posed inverse problem with multiple plausible solutions (Sections 1, 4.1).

#### Method

RCAN combines:

- **Residual-in-residual (RIR):** 10 residual groups, each containing 20 residual channel-attention blocks; long and short skip connections bypass low-frequency information and ease optimization of a network with over 400 convolutional layers (Sections 3.1–3.2).
- **Channel attention (CA):** global-average-pools each channel, applies a bottleneck ReLU transformation and sigmoid gate, then adaptively rescales channels (Section 3.3; Eqs. 10–12).
- **RCAB:** two convolutions plus channel attention inside a residual block (Section 3.4; Eqs. 13–14).
- **Training:** L1 loss, Adam, 800 DIV2K training images, 48×48 LR patches, PyTorch, Titan Xp GPU (Section 4.1).
- **Evaluation:** PSNR/SSIM on the luminance channel under bicubic (BI) and blur-downscale (BD) degradation; also an ImageNet object-recognition preprocessing test (Sections 4.1, 4.5).

#### Results reported by the authors

- **Ablation:** on Set5 ×2 after 50,000 iterations, PSNR rises from **37.45 dB** without RIR/CA to **37.90 dB** with both; both long/short skip connections and CA contribute (Table 1, Section 4.2).
- **BI degradation:** RCAN+ (self-ensemble) is best in the reported comparisons for every dataset and scale in Table

The complete evidence-grounded digest is in [`sources/zhang-2018-image-super-resolution-using-very.md`](../../sources/zhang-2018-image-super-resolution-using-very.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
