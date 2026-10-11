---
title: "VMAS: Video-to-Music Generation via Semantic Alignment in Web Music Videos"
authors: "Yan-Bo Lin, Yu Tian, Linjie Yang, Gedas Bertasius, and Heng Wang"
year: 2024
doi: 10.48550/arXiv.2409.07450
category: generation-and-planning
source: lin-2024-vmas-video-to-music-generation.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/lin-2024-vmas-video-to-music-generation.pdf"
pdf_filename: lin-2024-vmas-video-to-music-generation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The supplied PDF is the v1 manuscript. The project page identifies the work as a **WACV 2025 Oral** paper and provides qualitative demo videos.

## Key Contributions

Core contribution

**Author claim:** VMAS generates instrumental background music directly from video, avoiding the small, narrow MIDI datasets used by earlier video-to-music systems.

The system combines:

1. A temporally efficient video encoder.
2. An autoregressive EnCodec-token music decoder.
3. A global video–music contrastive objective.
4. A local video-beat alignment objective based on optical flow and onset detection.

The stated goal is simultaneous alignment with:

- **High-level semantics:** genre, style, and overall content.
- **Low-level dynamics:** scene changes, human motion, and other visually salient moments.

**Interpretation:** VMAS is not merely video-conditioned music generation. It explicitly introduces intermediate alignment signals that could be exposed as controls or explanations.

---

### 3. Dataset: DISCO-MV

#### Dataset statistics

**PDF p. 1, Table 1; p. 3, §3**

| Dataset | Videos | Mean within-video frame similarity |
|---|---:|---:|
| SymMV | 1.1K | 0.64 |
| YouTube-8M subset | 110K | 0.66 |
| DISCO-10M | 15.3M | 0.91 |
| **DISCO-MV** | **2.2M** | **0.61** |

The paper describes DISCO-MV as **2.28M video–music samples spanning approximately 47,000 hours**. It also combines 81K video–music samples from YouTube-8M.

Evaluation splits were manually selected for strong video–music correspondence:

- Validation: **1,120 videos**
- Test: **1,086 videos**

#### Construction

**PDF p. 3, §3**

1. Start from DISCO-10M, built from YouTube videos matched to Spotify artist metadata.
2. Remove visually static or repetitive videos using pairwise frame simil

The complete evidence-grounded digest is in [`sources/lin-2024-vmas-video-to-music-generation.md`](../../sources/lin-2024-vmas-video-to-music-generation.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
