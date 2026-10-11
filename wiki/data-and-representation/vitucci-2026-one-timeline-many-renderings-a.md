---
title: "One Timeline, Many Renderings: A Wolfram Language Paclet for Heterogeneous Musical Output"
authors: "Francesco Vitucci, Michele Lorusso, and Francesco Scagliola"
year: 2026
doi: 10.48550/arXiv.2608.24683
category: data-and-representation
source: vitucci-2026-one-timeline-many-renderings-a.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/vitucci-2026-one-timeline-many-renderings-a.pdf"
pdf_filename: vitucci-2026-one-timeline-many-renderings-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

I inspected all five PDF pages, the extracted text, Figures 1–2, and the references. **There are no tables, appendices, or quantitative result tables.**

## Key Contributions

Paper identification

**Full title:** *One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output*  
**Authors:** Francesco Vitucci, Michele Lorusso, and Francesco Scagliola  
**Affiliation:** Conservatorio di Musica “N. Piccinni” di Bari  
**Version:** arXiv:2608.24683v1, 25 August 2026; 5-page PDF, classified `[cs.CL]`.

I inspected all five PDF pages, the extracted text, Figures 1–2, and the references. **There are no tables, appendices, or quantitative result tables.**

### Executive digest

The paper presents **Temporal System**, an unreleased Wolfram Language paclet for representing one algorithmic-composition timeline once and compiling it into several synchronized outputs:

- Csound score/orchestra artifacts;
- beta MusicXML 4.0 notation;
- OSC event schedules;
- Csound-based rehearsal click tracks.

Its central design is an **immutable typed event store using exact rational beat positions**. Conversion to seconds, samples, milliseconds, or frequency is deferred to individual renderers.

The contribution is primarily an **authoring and rendering architecture**, not a music-generation model, symbolic transformation algorithm, or source-preserving recomposition method.

---

### 1. Problem and motivation

#### Author claims — PDF p. 1, §1 Introduction

The paper identifies a practical problem in mixed computer-music workflows: the same composition may require a Csound score, notation, real-time control, and rehearsal click, but separately authored outputs can drift when tempo, meter, or structure changes.

The proposed solution is to make

The complete evidence-grounded digest is in [`sources/vitucci-2026-one-timeline-many-renderings-a.md`](../../sources/vitucci-2026-one-timeline-many-renderings-a.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
