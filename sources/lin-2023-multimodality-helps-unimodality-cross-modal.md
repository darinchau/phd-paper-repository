---
title: "Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models"
authors: Zhiqiu Lin, Samuel Yu, Zhiyi Kuang, Deepak Pathak, Deva Ramanan
year: 2023
doi: 10.48550/arXiv.2301.06267
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lin-2023-multimodality-helps-unimodality-cross-modal.pdf"
pdf_filename: lin-2023-multimodality-helps-unimodality-cross-modal.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Treating text and audio as extra few-shot examples for a visual classifier improves unimodal accuracy: with frozen CLIP-style encoders, a linear classifier trained on image plus text (or image plus audio) beats the same classifier trained on images alone, especially in the low-shot regime.

## 1. Document Information

- **Exact title:** *Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models*. [PDF p. 1]
- **Authors:** Zhiqiu Lin, Samuel Yu, Zhiyi Kuang, Deepak Pathak, Deva Ramanan (Carnegie Mellon University); Lin and Yu equal contribution. [PDF p. 1]
- **Source record:** arXiv `2301.06267v5` [cs.CV], 27 August 2024, 22 pages; CVPR 2023. [PDF p. 1]
- **Length and denominator:** 22/22 pages checked; main tables and appendix ablations sampled, with Table 1 as the primary evidence.
- **Extraction method:** `pdftotext -layout`; the cross-modal few-shot table and the audiovisual benchmark description were read directly.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2301.06267`.
- **Category note:** filed under `other` because the contribution is a general cross-modal adaptation method, not a music-domain method or representation.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Cross-modal adaptation:** examples from other modalities are appended to the few-shot training set, turning an n-shot problem into an (n+1)-shot problem. [§1, Fig. 2]
2. **Strong low-shot results** with a simple linear classifier on frozen CLIP features, beating prior prompt-tuning, adapter, and robust-finetuning methods at 1 and 2 shots. [§4, Table 1]
3. **An audiovisual few-shot benchmark**, extending the idea beyond vision–language and improving both image and audio classification. [§4, §5]
4. **Analysis:** cross-modal samples shift decision boundaries and provide complementary cues rather than merely adding data volume. [§4]

## 3. Methodology and Architecture

- **Encoders:** frozen CLIP (image/text) and AudioCLIP (audio) encoders map modalities into a shared space. [§1]
- **Classifier:** linear probing on concatenated cross-modal features; optional partial fine-tuning of the last attention-pooling layer. [§4]
- **Text templates:** class names expanded into sentences with templates following Tip-Adapter. [§4]
- **Benchmarks:** 11 visual datasets (ImageNet, EuroSAT, Cars, etc.) plus a new audiovisual few-shot benchmark. [§4, Table 1]

## 4. Key Results and Benchmarks

- **Low-shot gains:** 1-shot cross-modal linear probing outperforms the 2-shot results of most prior methods; the authors describe this as evidence of complementary cues, not just extra samples. [§4]
- **Audiovisual benchmark:** cross-modal training improves both image and audio classification. [Abstract, §5]
- **Method combinations:** gains persist when combined with CoOp, Tip-Adapter, and WiSE-FT. [§4, Table 2]
- **Interpretation:** the mechanism is *additional evidence about the same concept*, not a new modality tower. It supports the general principle but does not show that an audio tower learns new structure from symbolic data.

## 5. Limitations and Future Work

- **Classification only.** No generation, retrieval at scale, or structured musical output.
- **Requires a shared embedding space** learned from paired multimodal data; the adaptation itself does not create one.
- **Text templates and class names** are part of the method, so language priors can leak.
- **Gains shrink as shots increase**, consistent with the extra modality being complementary rather than strictly more informative.

## 6. Related Work

- CLIP and AudioCLIP: the frozen multimodal encoders used.
- Tip-Adapter, CoOp, WiSE-FT: prior few-shot adaptation methods used as baselines.
- SoundNet and Look, Listen and Learn: earlier cross-modal representation transfer.

## 7. Glossary

- **CLIP:** Contrastive Language–Image Pretraining.
- **CoOp:** Context Optimization (prompt tuning).
- **WiSE-FT:** Weight-Space Ensembling for robust fine-tuning.
