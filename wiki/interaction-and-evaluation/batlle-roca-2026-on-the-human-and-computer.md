---
title: "On the Human and Computer Alignment of Attribute-Based Music Matches"
authors: "Roser Batlle-Roca, Woosung Choi, Joan Serrà, Fabio Morreale, Wei-Hsiang Liao, Xavier Serra, Emilia Gómez, Yuki Mitsufuji"
year: 2026
doi: 10.48550/arXiv.2609.00987
category: interaction-and-evaluation
source: batlle-roca-2026-on-the-human-and-computer.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/batlle-roca-2026-on-the-human-and-computer.pdf"
pdf_filename: batlle-roca-2026-on-the-human-and-computer.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-14
tags: []
---
## Summary

"**On the Human and Computer Alignment of Attribute-Based Music Matches**." arXiv:2609.00987v1 [cs.SD], **1 September 2026**, 15 pages. MTG-UPF, Sony AI, EC Joint Research Centre.

## Key Contributions

Bottom line

**Author claim:** shifting from global to attribute-level judgments (melody, harmony, rhythm, voice, timbre) yields substantial expert agreement on music matches — melody >85% agreement, κ ≈ 0.60 — and the MiRA similarity metrics show only partial, attribute-specific alignment with those judgments (CoverID → melody/harmony; CLAP/DEfNet → rhythm/timbre/voice; KL/PaSST blind to melody/harmony), supporting multi-metric replication assessment. The MATCHA dataset (300 triplets, 1,105 annotations, 83 experts) is released as the perceptual benchmark.

**My assessment:** the valuable part for this programme is the evidence that attribute decomposition makes similarity judgments consensual — the perceptual counterpart of explainable, per-attribute replication reporting — plus a reusable benchmark with a known failure mode (their Stable Audio Open generations were too artifact-laden to support perceptual matching, so the AI-generated alignment evidence rests on 30 uncontrolled media cases). Everything is audio-side; no symbolic metric is tested, which leaves symbolic replication detection unbenchmarked.

The complete evidence-grounded digest is in [`sources/batlle-roca-2026-on-the-human-and-computer.md`](../../sources/batlle-roca-2026-on-the-human-and-computer.md).

## Methodology and Architecture

Read the linked source digest for the triplet forced-choice design, the four stimulus sections (SMP plagiarism, Discogs-VI versions, Stable Audio Open with DDIM-inversion/prompt-controlled similarity, media-documented Suno cases), participant screening, and the Kendall's τ alignment protocol against MiRA's four metrics.

## Results

The linked source digest preserves the paper-reported agreement and alignment numbers, the approximate Figure 1/Figure 2 reads with their evidence caveat, and the dataset distribution terms; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor; the overview places this paper in the evaluation and human-interaction cluster beside the attribution and plagiarism-detection work.
- [[explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism]] — machine-side counterpart: embedding-shift plagiarism detection whose scalar-distance critique MATCHA grounds perceptually; neither covers symbolic detection.
- [[explainability-and-auditability/yu-2026-truemuse-a-benchmark-for-data]] — attribution benchmark without the human-perception axis that MATCHA contributes.
