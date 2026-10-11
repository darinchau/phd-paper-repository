---
title: "Exploring Inherent Properties of the Monophonic Melody of Songs"
authors: "Zehao Wang, Shicheng Zhang, and Xiaoou Chen"
year: 2020
doi: 10.48550/arXiv.2003.09287
category: data-and-representation
source: wang-2020-exploring-inherent-properties-of-the.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2020-exploring-inherent-properties-of-the.pdf"
pdf_filename: wang-2020-exploring-inherent-properties-of-the.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

1. computationally tractable, 2. semantically meaningful, 3. related to human perception/composition, 4. interpretable, and 5. useful for controlling generation or evaluation.

## Key Contributions

Evidence-grounded digest

### Bibliographic identity

- **Title:** *Exploring Inherent Properties of the Monophonic Melody of Songs*
- **Authors:** **Zehao Wang**, **Shicheng Zhang**, and **Xiaoou Chen**
- **Affiliations:** Peking University; University of Illinois at Urbana-Champaign; Peking University.
- **arXiv:** 2003.09287v1, [cs.SD], 20 March 2020.
- **PDF length:** 8 pages; no appendix. Page 8 begins the references.

### 1. Problem and scope

#### Author claims

The paper argues that symbolic-music research lacks features that are simultaneously:

1. computationally tractable,
2. semantically meaningful,
3. related to human perception/composition,
4. interpretable, and
5. useful for controlling generation or evaluation.

They contrast abstract mathematical music theories, which they regard as difficult to compute, with low-level MIDI statistics that they regard as rigid and weakly connected to perception (**p.1–3, §§1–2.3**).

The precise scope is deliberately narrow:

- monophonic melody;
- note pitch and duration;
- MIDI/sheet-music-like symbolic representation;
- no audio;
- no harmony–melody relationship;
- no lyrics;
- no bar/meter representation (**p.2–4, §3**).

The authors claim that their features are broadly genre-independent and applicable across tonal, atonal, and different-temperament settings (**abstract, pp.1–2, §5**). This is an author claim, not strongly demonstrated experimentally.

### 2. Proposed representation and features

A note is represented as:

\[
N=(P,d)
\]

where \(P\) is relative pitch and \(d\) is relative duration. A rest has duration on

The complete evidence-grounded digest is in [`sources/wang-2020-exploring-inherent-properties-of-the.md`](../../sources/wang-2020-exploring-inherent-properties-of-the.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
