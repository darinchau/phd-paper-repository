# 2026-09-06 — SynTheory Artifact Review

**Final outcome:** ingestion completed after the user explicitly instructed continuation with the discrepancies recorded. The initial hold below is retained as chronological provenance, not the current admission decision.

## Scope and Outcome

- Requested root-level arXiv PDFs: **1** (`2410.00872v1.pdf`).
- PDFs identified and full text read: **1/1**, covering **8/8** physical pages.
- Papers admitted: **0/1**. Ingestion paused under the AGENTS.md artifact-discrepancy rule; no placeholder source/wiki page was created.
- Paper-linked public artifacts inspected: **3/3** landing pages (implementation, dataset, project website), plus the implementation at commit `4f222359e750ec55425c12809c1a0358b74fce49`. Dataset audio, full model inference, and published experiment reruns remain unchecked.

## Findings and Durable Record

[SynTheory artifact review and ingestion hold](../agenda/paper-audits/wei-2024-syntheory-artifact-review.md) records the exact PDF hash, page evidence, commit-pinned code links, validation-dependent normalization, tempo split overlap, missing test-scoring path, and the requirements for resuming.

Citra returned full text through `rust-read-pdf-v1`, with spacing/column-layout corruption. Poppler/MiKTeX layout text and a visual check of Table 2 supplemented extraction. The Poppler tools emitted log-permission errors despite writing usable artifacts; these calls are not counted as clean successes. Temporary extraction, render, clone, and verification files were kept outside the repository.

Executed a standard-library AST control-flow check on the actual released `eval_logits` function with explicit test doubles; confirmed that an unfitted scaler fits validation features. Separately reproduced the tempo row cuts and confirmed shared training/holdout BPM values of 74 and 186. Neither check is an end-to-end reproduction or a measurement of published-score bias.

## Synthesis and Claim Delta

Read the existing symbolic-model overview, music-domain inductive-bias concept, and auditable-editing concept before assessing admission. Their distinction between named structure and faithful explanation is relevant, but **claim delta: unchanged**, because the paper is held. No supersede entry or synthesis link to an unadmitted paper is added. Existing five-paper coverage remains the catalog denominator.

## Repository Verification

Regenerated the catalog and log guide. The synthesis-orphan audit passed at **0/5**, and `git diff --check` passed. Full record validation found ten pre-existing `pdf_path` values outside this checkout's `papers/` directory (all five source/wiki pairs); these records were not changed. The new report and log links were checked separately and passed.

## Continued Ingestion with Explicit Caveats

The user instructed: "Please continue of the ingestion. Record the discrepancy since it might affect the validity of the result". This task-specific authorization supersedes the initial artifact-rule hold for this paper; AGENTS.md was not changed.

- Admission completed: **1/1** requested paper, with an exact copied canonical PDF, complete source digest, and explainability-and-auditability paper page. The stem was generated programmatically from author/year/title tokens; source and copy SHA-256 values match. Original input preserved.
- All **8/8** pages were read during the initial review. Figure 1, Figure 2, and Table 2 were rendered and visually checked (**3/3**); reproducible crop coordinates and PDF hash are recorded beside the paper page's assets. Final crop rendering completed successfully with local renderer-log access.
- Discrepancies are recorded in the source and wiki results/limitations, including validation-dependent normalization, overlapping tempo boundaries, the missing independent test-scoring path, progression timing, and sweep-direction metadata. Published scores remain attributed to the authors; no effect size or ranking change is invented.
- Added `concepts/music-theory-probing` and updated the body of `concepts/music-domain-inductive-biases`. Both link reciprocally to the paper.
- **Claim delta: strengthens** the methodological distinction between explicitly designed musical structure and empirically probed information accessibility. **Narrows** interpretation of strong probe scores to protocol-dependent recoverability, with unresolved implementation validity concerns. No prior paper's empirical claim is contradicted or replaced, so no `supersede` entry is required.
- The operational report now records the resolved admission decision and the outstanding evidence needed to strengthen result claims. Temporary clone/extraction files remain outside the repository; no model experiments were run.

### Final Verification

Catalog regenerated to **6 PDFs / 6 sources / 6 paper pages**, with **6/6** synthesis-connected papers. Orphan audit passed at **0/6**. Targeted validation passed for the new source/wiki schemas, canonical path, source association, all new report/catalog/wiki links, all crop manifests and PNGs, both reciprocal synthesis connections, and exact input/canonical-PDF hash equality. All three final crops were visually inspected. `git diff --check` passed. The previously identified ten old-record PDF-path errors remain outside this ingestion's edits; the whole repository is not claimed to pass full record validation.
