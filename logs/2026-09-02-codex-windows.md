# 2026-09-02 — Paper Ingestions

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

## AutoMashUpper Journal Article Ingestion

### Scope and Denominator

- Requested artifacts: **1**.
- Exact PDFs located and inspected: **1/1**.
- Physical PDF pages read: **12/12**; printed article pages 1726–1737.
- Papers admitted with canonical PDF, source digest, domain page, and synthesis links: **1/1**.
- Figure-only evidence crops rendered and visually checked: **8/8**.

### Source and Verification

- Supplied file: `AutoMashUpper_Automatic_Creation_of_Multi-Song_Music_Mashups.pdf`.
- Canonical file: `papers/davies-2014-automashupper-automatic-creation-of-multi.pdf`.
- SHA-256: `37da41dbe01bbd015900dc68e170ba87ba2120d929446dee7fdb0153323d619b` for both files.
- Citra inspection reports 12 digital-text pages and no OCR requirement. Rendered pages were used to recover equations, p-values, correlations, legends, and graph directions lost by text extraction.
- The PDF metadata embeds IEEE article ID `6876193` and DOI `10.1109/TASLP.2014.2347135`. The citation was cross-checked against the author-hosted version-of-record PDF and AIST publication list because IEEE Xplore presented a JavaScript verification screen.

### Classification and Knowledge-Layer Changes

Primary category: `retrieval-and-recombination`.

AutoMashUpper performs phrase-local retrieval and source-preserving transformation of existing recordings. Its principal contribution is transform-aware Mashability: it searches candidate passages under explicit tempo and key changes. The source, score components, and required edits are reconstructable from the specified algorithm, but the paper does not show a complete surfaced or persistent trace.

- Added the complete source digest and concise domain page.
- Added reciprocal links with [[overviews/automated-music-mashup-systems]].
- Extended [[concepts/auditable-creative-editing-pipelines]] with formula-level score and transformation traces.
- Extended [[questions/when-do-interpretable-music-editing-traces-become-faithful-explanations]] with the distinction between explaining a formula and explaining musical success.
- Linked the Davies paper directly to the later Wu dissertation and identified the AutoMashUpper lineage behind its Mashability baseline.

### Claim Delta and Supersede Check

- **Strengthens:** explicit transform-aware retrieval can make source identity, candidate location, score decomposition, and required edits reconstructable in principle within a mixed-initiative workflow; this paper does not demonstrate a complete user-visible or persistent provenance log.
- **Narrows:** the fixed score is evidence for surfacing a promising candidate, not a solved or calibrated definition of listener preference. Highest-ranked examples beat the middle condition, but middle does not beat bottom; overall score–enjoyment correlation is `r = .49`.
- **Narrows:** segmentation superiority is confined to precise narrow-tolerance boundary localization on regular RWC pop; other systems lead at wider tolerances.
- **Extends the historical map:** Davies 2014 is now the explicit handcrafted anchor, while Wu 2026 is the learned ranking/rearrangement/restoration extension.
- No existing claim is contradicted or replaced, so there is no `supersede` entry.

### Evidence Boundaries Preserved

- The paper evaluates phrase sections rather than complete automatic multi-song mashups.
- The central interactive workflow receives no usability, agency, or creative-outcome study.
- Default weights and thresholds come from informal testing; no listening ablation isolates score components.
- The 15-participant study reports no effect sizes, confidence intervals, participant/item model, power analysis, or reproducible corpus description.
- Chroma, kick/snare patterns, and three spectral bands omit vocal interaction, bass conflict, harmonic function, voice leading, cadence, transformation artifacts, transitions, and whole-song form.
- The post-hoc vocal-overlap split is exploratory because subset sizes and subgroup significance are not reported.

### Visual Evidence

The manifest at `wiki/retrieval-and-recombination/assets/davies-2014-automashupper-automatic-creation-of-multi/crop-evidence.json` records the source checksum, physical and printed page numbers, normalized crop boxes, evidence roles, and deterministic output paths for Figures 1, 3, 4, 6, 7, 8, 9, and 10. The crops contain diagrams, plots, or the software interface only; prose and equations are summarized in the digest.

### Rights and Gaps

- The IEEE footer permits personal use and academic text/data mining but requires permission for republication or redistribution. The canonical PDF is retained locally and must not be pushed until repository visibility and rights are resolved.
- No author- or AIST-hosted source-code release was located. A public third-party repository says it is merely based on the paper and is not treated as official implementation evidence.
- The historical example-video URL now redirects to an unavailable host.
- The supplied root PDF remains unchanged because the paper-library contract prohibits moving or deleting user files; a conflicting unregistered local helper note suggested removal after copying.

## Three arXiv Paper Ingestions: NotaGen, Moonbeam, and HRM

### Scope and Denominator

- Requested artifacts: **3** root-level PDFs.
- One independent paper agent was assigned to each PDF.
- Exact PDFs located, copied, and inspected: **3/3**.
- Physical PDF pages read: **56/56** — NotaGen **12/12**, Moonbeam **20/20**, and HRM **24/24**.
- Papers admitted with canonical PDF, complete source digest, concise domain page, and reciprocal synthesis links: **3/3**.
- Claim-bearing figure, algorithm, and table crops rendered and visually checked: **22/22** — NotaGen **7**, Moonbeam **8**, and HRM **7**.
- No extraction failures, empty pages, OCR requirements, or unchecked papers.

### Source and Extraction

All three supplied files were arXiv PDFs with digital text. Citra was not available in the active tool set, so full-document Poppler/MiKTeX `pdftotext -layout` extraction was combined with rendered-page inspection. Equations, signs, table values, plot directions, diagrams, and paper-internal visual discrepancies were checked against the rendered PDFs rather than inferred from extraction alone. No web search, publisher HTML, code repository, checkpoint, demo, or external dataset artifact was used.

| Supplied PDF | Canonical paper | Pages | SHA-256 |
|---|---|---:|---|
| `2502.18008v5.pdf` | `papers/wang-2025-notagen-advancing-musicality-in-symbolic.pdf` | 12 | `b10f17fd4e0a5914f50a491b5c7a473d8cf6c755691521e8573197f4e6bf1431` |
| `2505.15559v1.pdf` | `papers/guo-2025-moonbeam-a-midi-foundation-model.pdf` | 20 | `88d90533b1da810eba59dd0009d4e702e5ec7ba0a4ea7d86326389e488d93592` |
| `2506.21734v3.pdf` | `papers/wang-2025-hierarchical-reasoning-model.pdf` | 24 | `81b05b03ebd92748b1bc0e59d4b6e0d8271e1e56b84d1d589a03430db79b6e25` |

Each canonical file is byte-for-byte identical to its supplied root PDF. The supplied files remain unchanged because the authoritative paper-library contract prohibits moving or deleting user files.

### Classification

All three papers use `generation-and-planning` as the primary category, for different reasons:

- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] contributes a hierarchical ABC generator plus pretraining, classical fine-tuning, and learned-evaluator preference optimization.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] contributes a pretrained autoregressive MIDI architecture, downstream generation/infilling adaptation, and classification adaptation; representation and data are substantial secondary contributions.
- [[generation-and-planning/wang-2025-hierarchical-reasoning-model]] contributes a recurrent latent-planning architecture and adaptive computation. It is not a music paper, an explainability method, or a theory-constraint system; its music relevance is explicitly treated as a transfer hypothesis.

### Knowledge-Layer Changes

- Added three canonical PDFs, three complete source digests, and three concise domain pages.
- Created [[overviews/symbolic-music-foundation-models]] to compare NotaGen and Moonbeam across symbolic medium, context, pretraining, adaptation, evaluation, provenance, and auditability without treating their metrics as directly comparable.
- Created [[concepts/music-domain-inductive-biases]] to distinguish music-shaped representations and attention geometry from explicit constraints and faithful explanations.
- Created [[concepts/hierarchical-latent-reasoning]] to document HRM's slow/fast recurrence and the evidence required before transferring it to long-form symbolic music.
- Added reciprocal paper-to-synthesis and synthesis-to-paper links. All five paper pages in the repository now have at least one overview or concept connection.

### NotaGen Evidence and Boundaries

NotaGen is a 516M-parameter model with a 20-layer patch decoder and six-layer character decoder. It pretrains on 1.6M internal-use ABC sheets, fine-tunes on 8,948 classical sheets, and applies three rounds of CLaMP-DPO. Interleaved ABC brings simultaneous voices together, `[r:]` labels encode current/remaining bars, and continuation can exceed one context. None of those representation choices receives an isolated long-form ablation. [PDF pp. 2–5]

CLaMP-DPO embeds prompt-matched fine-tuning references, scores generations by cosine similarity to the mean reference embedding, selects the top and bottom 10%, and optimizes the pairs with DPO-Positive. Average CLaMP 2 Score rises monotonically for NotaGen, MuPT, and MET, but this is also the score used to construct preferences. Prompt-label agreement generally improves; MuPT's bar-alignment error simultaneously worsens from `0.824%` to `4.676%`. [PDF pp. 4–7]

The 92-participant study reports more votes for post- than pre-optimization outputs. Against human references, NotaGen obtains `41.7%`, no preference `8.3%`, and ground truth `50.0%`; it is closer than MuPT or MET but does not beat ground truth. The PDF reports no item counts, intervals, effect sizes, participant/item model, or significance tests, so the abstract's “significantly outperforms” language is not statistically established. [PDF pp. 6–7]

The training workflow is procedurally auditable, but the learned cosine score provides no note-, rule-, cadence-, voice-leading-, or form-level rationale. Internal data dominate both pretraining and fine-tuning; reference pieces come from the fine-tuning corpus; provenance, rights, deduplication, held-out work identity, memorization, and independent reward validity remain unresolved.

### Moonbeam Evidence and Boundaries

Moonbeam represents MIDI events as absolute onset, duration, octave, pitch class, instrument, and velocity; continuous Fundamental Music Embeddings handle scalar fields, Multidimensional Relative Attention assigns head groups to attribute differences, and a GRU predicts the six next-event fields sequentially. Small has 309M parameters; Medium has 839M and uses 19 listed datasets totaling 81.58K hours and 18.06B attribute tokens. [PDF pp. 3–7, 14–17]

The full Small model reaches perplexity `2.423`, versus `2.512` for standard attention and `2.512` for the all-attribute rotation variant. Medium leads accuracy and macro-F1 on three of four classification datasets. These single-run comparisons do not isolate model scale from corpus breadth, and the whole-module ablation does not show that each named MRA dimension is used causally. PiJAMA appears in pretraining while PiJAMA30 is downstream without a documented exclusion/deduplication boundary. [PDF pp. 7–9, 14]

In conditional generation, the REMI-like baseline is better on objective pitch, velocity, and timing control, while Moonbeam receives higher ratings from 20 experts for chord fit, metadata fit, coherence, and enjoyment. The generation checkpoint scale, equal-budget decoding comparison, `±` statistic, and Wilcoxon analysis unit are not stated. The claimed infilling capability is architectural; no dedicated infilling benchmark appears. [PDF pp. 6–9, 18–20]

Moonbeam strengthens architectural and provenance auditability through named event fields, head-group mappings, conditioning paths, and a dataset-license table. It does not provide causal head interventions, note-level traces, explicit theory rules, or explanation-utility evidence. “Freely available” corpus data include research-only and non-commercial licenses, while several license cells are blank.

### HRM Evidence and Boundaries

HRM is a 27M-parameter direct-prediction model with a slow high-level recurrent Transformer module and a fast low-level module. It differentiates only through the latest local updates, applies detached final-target supervision to repeated segments, and uses a Q-head for adaptive halting. The PDF does not compare the one-step gradient with full BPTT or exact implicit differentiation and reports no measured memory, latency, FLOPs, seeds, intervals, or most benchmark hyperparameters. [PDF pp. 3–10]

Under the paper's protocols, HRM reports `40.3%` ARC-AGI-1, `5.0%` ARC-AGI-2, `55.0%` Sudoku-Extreme, and `74.5%` Maze-Hard from roughly 1,000 examples. The near-perfect Sudoku curves use Sudoku-Extreme-Full with 3,831,994 training examples, not the 1,000-example subset. ARC solves 1,000 augmented variants per input before voting over two inverse-transformed predictions, so leaderboard comparisons are not compute matched. [PDF pp. 1–3, 10–12]

Selected decoded states show path and grid revisions, and trained high-/low-level states differ in participation ratio. These are observational probes. They do not establish causal algorithms, representative traces, faithful explanations, or biological correspondence. HRM contains no music representation, theory rule, provenance mechanism, multiple-valid-output evaluation, or human creative study. [PDF pp. 12–16]

The defensible music implication is tentative: a slow state could own form/harmonic plans while a fast state realizes and repairs notes. That proposal requires explicit musical interfaces, constraints and exceptions, intervention-tested state semantics, matched-compute evaluation, and human prediction/diagnosis/repair evidence before it becomes more than an architectural analogy.

### Internal Discrepancies Preserved

NotaGen:

- The abstract uses “significantly,” but no inferential test is reported.
- Syntax/plagiarism filters are described as optional; only same-instrument stave-grouping exclusion is confirmed experimentally.
- Appendix continuation pages label the prompt list “Table 2 – Continued,” while the final caption is Table 4.
- The MuPT baseline name says `550M`, while the text reports 505M parameters.

Moonbeam:

- Figure 3's legend labels the small bars “Train” and large bars “Test,” opposite the stated 90%/10% split.
- The main ablation uses a 5% Lakh split, while Appendix A mentions a private pretraining test set without routing reported results to it.
- “Without FME” retains onset FME.
- The prose/diagram relationship between MRA and grouped-query attention is ambiguous.
- The Wilcoxon analysis unit and meaning of `±` are unspecified.

HRM:

- The formal high-level recurrence uses prior `z_L`, while prose and pseudocode use the just-updated low-level state.
- A fixed-point parameter tuple omits `theta_H` immediately before differentiating with respect to it.
- ACT defines `M_max`, but the printed target equation uses undefined `N_max`.
- The printed token loss lacks a leading negative sign despite minimization and cross-entropy pseudocode.
- The stability argument names AdamW, while the implementation paragraph names Adam-atan2.
- Figure 8 panel `(c)`/`(d)` references are reversed in body prose relative to the caption.

### Claim Delta and Supersede Check

- **Strengthens:** symbolic pretraining can support substantial generation, control, and understanding tasks in both ABC and MIDI systems.
- **Strengthens:** learned-evaluator post-training can shift evaluator-aligned metrics and observed A/B votes across several symbolic encodings.
- **Strengthens:** semantically factorized event representations and attribute-relative attention are feasible at foundation-model scale.
- **Strengthens:** slow/fast latent recurrence and additional inference compute can improve the paper's exact-grid tasks.
- **Narrows:** semantically named fields, stages, head groups, or decodable states provide architectural/procedural auditability, not automatically a faithful explanation.
- **Narrows:** proxy improvement can coexist with worse symbolic validity or objective control; no one reported scalar establishes musical quality.
- **Unchanged:** none of the three papers establishes explicit common-practice theory compliance, long-form classical form, faithful theory traces, or explanation utility.
- No existing claim is contradicted or replaced, so there is no `supersede` entry.

### Visual Evidence

The three manifests under `wiki/generation-and-planning/assets/{paper-stem}/crop-evidence.json` record canonical checksums, physical pages, normalized boxes, evidence roles, and deterministic outputs. The 22 retained crops cover architectures, representation diagrams, preference-selection algorithms, data tables, ablations, human-result plots, adaptive-compute curves, decoded trajectories, dimensionality analysis, and one visual train/test discrepancy. Crops contain claim-bearing figures/tables rather than large prose blocks.

### Rights and Publication Hold

- Moonbeam's embedded metadata identifies CC BY-SA 4.0.
- NotaGen and HRM do not state a redistribution license in the supplied PDF, so public Git redistribution cannot be inferred from local possession or arXiv origin alone.
- The three canonical PDFs are committed only to the local feature branch. The child and parent branches must not be pushed until visibility and redistribution policy for all PDFs are confirmed.
- No LaTeX source archive accompanied any supplied PDF.
