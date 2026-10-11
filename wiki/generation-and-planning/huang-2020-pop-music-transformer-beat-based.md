---
title: "Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions"
authors: "Yu-Siang Huang and Yi-Hsuan Yang"
year: 2020
doi: 10.48550/arXiv.2002.00212
category: generation-and-planning
source: huang-2020-pop-music-transformer-beat-based.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/huang-2020-pop-music-transformer-beat-based.pdf"
pdf_filename: huang-2020-pop-music-transformer-beat-based.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The authors argue that Transformer music generation benefits substantially from a better **symbolic event representation**, not only from architectural innovation.

## Key Contributions

Central contribution

The authors argue that Transformer music generation benefits substantially from a better **symbolic event representation**, not only from architectural innovation.

Their representation, **REMI** (“revamped MIDI-derived events”), makes the following explicit:

1. bar boundaries;
2. quantized positions within each bar;
3. note duration;
4. local tempo;
5. chord labels.

The claimed result is better rhythmic regularity and subjective preference over a Transformer-XL adaptation of Music Transformer.

This is an author claim; the empirical evidence is specifically for **expressive solo Pop piano**, not general music generation.

---

### Representation and timing

#### Conventional MIDI-like representation

The baseline follows the event representation of Oore et al. [30] and Music Transformer [23]:

| Musical property | Event |
|---|---|
| Pitch onset | `Note-On`, pitch 0–127 |
| Pitch offset | `Note-Off`, pitch 0–127 |
| Relative timing | `Time-Shift`, 10–1000 ms |
| Dynamics | `Note Velocity`, quantized to 32 levels |

`Time-Shift` expresses the relative time gap between successive events. The authors argue that timing mistakes accumulate during autoregressive inference, even though teacher forcing can hide such problems during training.

Evidence: PDF pp. 1, 3–4; `.txt:56-93, 182-216`.

#### REMI representation

REMI replaces or augments these events as follows:

| REMI event | Specification |
|---|---|
| `Bar` | Starts a new bar |
| `Position` | One of 16 positions within a bar |
| `Note Velocity` | 32 quantized levels |
| `Note-On` | MIDI pitch 0–127 |

The complete evidence-grounded digest is in [`sources/huang-2020-pop-music-transformer-beat-based.md`](../../sources/huang-2020-pop-music-transformer-beat-based.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
