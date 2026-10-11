---
title: "Automatic Analysis and Influence of Hierarchical Structure on Melody, Rhythm and Harmony in Popular Music"
authors: "Shuqi Dai, Huan Zhang, and Roger B. Dannenberg"
year: 2020
doi: 10.48550/arXiv.2010.07518
category: theory-and-constraints
source: dai-2020-automatic-analysis-and-influence-of.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/dai-2020-automatic-analysis-and-influence-of.pdf"
pdf_filename: dai-2020-automatic-analysis-and-influence-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. **Low-level repeated phrases**, using similarity in chords, rhythm onsets, and melody. 2. **Higher-level sections**, inferred from the arrangement of detected phrases and separator-like non-melodic material. 3. Statistical relationships between hierarchical position and **harmony, melody, and rhythm**.

## Key Contributions

Core contribution

The paper presents a symbolic-MIDI method for detecting:

1. **Low-level repeated phrases**, using similarity in chords, rhythm onsets, and melody.
2. **Higher-level sections**, inferred from the arrangement of detected phrases and separator-like non-melodic material.
3. Statistical relationships between hierarchical position and **harmony, melody, and rhythm**.

The authors argue that hierarchy is not merely repetition at different time scales: phrase and section positions have measurably different musical behavior (Abstract; §§1, 5, 7).

**Interpretation:** This is primarily an analysis and controllability resource, not a generation model. It provides structural annotations and conditional musical statistics that could be used by a generator, mashup system, or repair system.

---

### 2. Corpus and preprocessing

#### Corpus

- **909 Chinese popular-song MIDI transcriptions** derived manually from audio (§3.2, PDF p. 4).
- Key and chord labels from audio were combined with automatically derived MIDI labels.
- Differences were resolved with heuristics.
- MIDI files contain a melody track, simplifying melody extraction.
- Melodies were quantized to sixteenth notes.
- The corpus spans approximately **seven decades** of music (§5, PDF p. 7).

The paper cites the Pop909 work by Wang et al. (2020), and says the dataset, annotations, and experimental results were released at:

`https://github.com/Dsqvival/hierarchical-structure-analysis` (§7, PDF p. 8).

#### Important caveat

The paper does **not** clearly report:

- a train/test split,
- the number of human ann

The complete evidence-grounded digest is in [`sources/dai-2020-automatic-analysis-and-influence-of.md`](../../sources/dai-2020-automatic-analysis-and-influence-of.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
