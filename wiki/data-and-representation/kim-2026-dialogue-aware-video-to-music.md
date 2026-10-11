---
title: "Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections"
authors: "Haven Kim, Zachary Novack, Julian McAuley, and Hao-Wen Dong"
year: 2026
doi: 10.48550/arXiv.2608.11576
category: data-and-representation
source: kim-2026-dialogue-aware-video-to-music.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kim-2026-dialogue-aware-video-to-music.pdf"
pdf_filename: kim-2026-dialogue-aware-video-to-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. **OSSL-v2**, a durable, self-hosted film/video–music dataset. 2. A lightweight, frame-aligned dialogue adapter for existing video-to-music models. 3. Benchmarking of VidMuse, GVMGen, and Diff-V2M on common data.

## Key Contributions

Evidence-grounded digest

### Bibliography and scope

- **Haven Kim, Zachary Novack, Julian McAuley, and Hao-Wen Dong**, “**Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections**,” arXiv:**2608.11576v1**, cs.SD, **12 August 2026**. Affiliations: UC San Diego and University of Michigan.
- Seven-page paper; no appendix or supplementary experiments.
- Main contributions claimed by the authors:
  1. **OSSL-v2**, a durable, self-hosted film/video–music dataset.
  2. A lightweight, frame-aligned dialogue adapter for existing video-to-music models.
  3. Benchmarking of VidMuse, GVMGen, and Diff-V2M on common data.

Key cited systems:
- VidMuse [9], Tian et al., 2025.
- GVMGen [12], Zuo et al., arXiv:2501.09972, 2025.
- Diff-V2M [16], Ji et al., AAAI 2026.
- Prior OSSL [21], Kim et al., arXiv:2506.12573, 2025.

### Page and section anchors

| Location | Evidence |
|---|---|
| p.1, Abstract/§1 | Motivation, dataset scale, dialogue hypothesis, main claims |
| p.2, Fig. 1/Table 1/§2–§3 | Dialogue–music correlation, dataset comparison, OSSL-v2 construction |
| p.3, Fig. 2/§3–§5 | Filtering pipeline and dialogue adapter architecture |
| p.4, §5–§6 | Training protocol, splits, metrics, evaluation design |
| p.5, Table 2/§6–§9 | Complete results, conclusion, acknowledgements |
| pp.5–7, §9 | Bibliography |

### OSSL-v2 construction

#### Dataset facts

**Authors report** (p.1–3):

- **1,886 public-domain films**, downloaded from YouTube.
- **34,343 clips**, totaling **246.4 hours**.
- Mean clip duration: **28.6 seconds**.
- Dataset is hosted rather than distributed

The complete evidence-grounded digest is in [`sources/kim-2026-dialogue-aware-video-to-music.md`](../../sources/kim-2026-dialogue-aware-video-to-music.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
