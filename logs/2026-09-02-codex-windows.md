# 2026-09-02 — Xinyang Wu Dissertation Ingestion

## Scope and Denominator

- Requested artifacts: **1**.
- Exact PDFs located and inspected: **1/1**.
- Papers admitted with canonical PDF, source digest, domain page, and synthesis links: **1/1**.
- Thesis chapters reviewed: **5/5**, plus front matter, abstract, contents, figure/table lists, conclusions, and publication list.
- Physical PDF pages: **109**. The methodological and argumentative body is PDF pp. 15–98; PDF pp. 99–109 are the bibliography.
- Figure-only evidence crops created and visually checked: **12/12**.

## Source and Extraction

- Supplied file: `XinyangWU_thesis_library.pdf`.
- Canonical file: `papers/wu-2026-an-automated-pop-song-mashup.pdf`.
- SHA-256: `771daaeeec623de9af1b10dab64816119b8553b5a7d90b7688938ce692723501` for both files.
- Citra inspection reports 109 digital-text pages, no OCR requirement, an outline, and page labels.
- Citra was used for canonical inspection and PDF evidence routing. Local `pdftotext` supplied a page-broken working extraction because a rich Citra read returned an impractically large geometry payload. Rendered PDF pages, not extraction alone, were used to verify tables, figures, formulas, and numerical claims.
- No web search or publisher HTML was used.

## Classification

Primary category: `retrieval-and-recombination`.

The thesis uses source separation, selection, alignment, structural rearrangement, and mix restoration to preserve and recombine real recordings. Learned generation and evaluation are substantial secondary contributions, but classifying the work primarily as generation would obscure its editing-based methodological center.

## Knowledge-Layer Changes

- Added the complete source digest and concise domain page.
- Created [[overviews/automated-music-mashup-systems]] because the library had no system-level mashup anchor.
- Created [[concepts/auditable-creative-editing-pipelines]] to distinguish visible workflow state from faithful semantic explanation.
- Created [[questions/when-do-interpretable-music-editing-traces-become-faithful-explanations]] because the paper exposes useful traces without validating explanation faithfulness or human utility.
- Added bidirectional links between the paper and all three synthesis pages.

## Claim Delta and Supersede Check

This is the first admitted paper, so no prior knowledge-base claim is contradicted or replaced and there is no `supersede` entry.

The paper establishes the library’s initial claim that a hybrid editing pipeline can expose provenance and intervention points while retaining learned components. The digest narrows the author’s “interpretable” and “transparent” language to **structural auditability**: the thesis does not evaluate semantic explanation faithfulness, causal completeness of learned traces, or user-facing explanation utility.

## Evidence Boundaries Preserved

- The local-warping contribution has no direct timing benchmark, global-only ablation, or warp-artifact study.
- Context-held-out ranking reuses the same ten-song pool and is not external song generalization.
- Same-song unshuffling accuracy is not cross-song mashup quality.
- Chapter 3 uses “significantly” without reporting inferential statistics.
- Chapter 4 tests out-of-domain song content under the same synthetic, invertible EQ/level corruption family and has no human listening test.
- Chapter 5’s agent, full-length, spatial, confidence-triggered, and mixed-initiative systems are proposals.

## Internal Questions

The digest records rather than reconciles these issues:

1. `1,800` versus `1,335` versus `1,096` ranking comparisons, and `ρ = 0.71` versus `0.738/0.74`.
2. Four-bar figure versus eight-bar experiment prose.
3. An impossible every-second-beat conversion from 0.5-second beats to 2.0-second downbeats.
4. Multi-scale train/validation gaps that do not match the stated 4–6 points.
5. No statistical test behind Chapter 3’s significance language.
6. `150/all` MUSDB18-HQ songs versus 149 in Table 4.2.
7. Ambiguous “all out-of-domain” wording for ten internal-validation clips.
8. Approximately 5 dB condition value in Figure 4.8 versus 6.67 dB pooled and 5.46–7.70 dB by condition.

## Artifact and Publication Hold

The authorization page permits HKUST to lend and reproduce the thesis for scholarly research, but third-party public Git redistribution is not clearly granted. The PDF is stored locally as the canonical source. No child or parent branch was pushed. Publication must remain blocked until repository visibility and PDF redistribution policy are decided.

## Visual Evidence

The manifest at `wiki/retrieval-and-recombination/assets/wu-2026-an-automated-pop-song-mashup/crop-evidence.json` records the source hash, physical and printed page numbers, normalized crop boxes, evidence roles, and output paths. Crops contain diagrams, charts, heatmaps, spectrograms, and control curves only; large prose blocks and tables were transcribed into notes instead of captured as images.

## Gaps

- No LaTeX source was supplied.
- No exact PDFs for the five listed thesis-related publications were supplied, so they were not ingested as separate papers.
- Corpus licensing and third-party PDF redistribution remain unresolved.
