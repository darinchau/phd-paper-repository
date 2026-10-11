---
title: "TrueMuse: A Benchmark for Data Attribution in Text-to-Music Models"
authors: "Jiawei Yu and Jian Liu"
year: 2026
doi: 10.48550/arXiv.2610.00835
category: explainability-and-auditability
source: yu-2026-truemuse-a-benchmark-for-data.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2026-truemuse-a-benchmark-for-data.pdf"
pdf_filename: yu-2026-truemuse-a-benchmark-for-data.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

It constructs attribute-specific text-to-music models by fine-tuning existing diffusion generators on known source clips. It then evaluates black-box retrieval methods that attempt to recover those source clips from generated audio.

## Key Contributions

What the paper actually contributes

This is primarily a **controlled benchmark**, not a new end-to-end source-attribution model.

It constructs attribute-specific text-to-music models by fine-tuning existing diffusion generators on known source clips. It then evaluates black-box retrieval methods that attempt to recover those source clips from generated audio.

The learned “mapper” is a linear projection on top of frozen audio embeddings; it is an enhanced baseline, not the central generative model.

---

### Benchmark construction

#### Core procedure

Pages 3–4, §3.1, Figure 1, Equations (1)–(2):

1. Start with a pretrained text-to-music diffusion model.
2. Select a small source set \(D_c\) for musical attribute \(c\).
3. Fine-tune only the denoising U-Net using an association prompt such as:

   > “a recording of [V] musician”

   where `[V]` is a rare identifier such as `sks`.
4. Generate new audio using contextual and style prompts containing the identifier.
5. Treat \(D_c\) as the known attribution target.

The authors describe inclusion in fine-tuning as controlled ground truth. Strictly, this is **known training-set provenance**, not proof that every source clip causally influenced every generated output.

#### Four attribution sets

Table 1 and §§3.1.1–3.1.4, pp.4–5:

| Set | Attributes | Source construction | Clips/attribute |
|---|---:|---|---:|
| Melody-Centric | 50 | Short FMA clips with identifiable pitch contours | 1 |
| Instrument-Centric | 25 | YouTube clips dominated by an instrument | 3 or 6 |
| Musician-Centric | 50 | Different tracks by the same FMA artis

The complete evidence-grounded digest is in [`sources/yu-2026-truemuse-a-benchmark-for-data.md`](../../sources/yu-2026-truemuse-a-benchmark-for-data.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
