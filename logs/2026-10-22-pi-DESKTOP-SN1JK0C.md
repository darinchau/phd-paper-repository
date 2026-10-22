# 2026-10-22 — AGT 1 novelty check and cross-modal digests

**TL;DR:** Ingested twelve cross-modal transfer and music papers, creating a new synthesis overview and establishing that the narrow audio→symbolic perceptual claim is open while the broad claim is not.

## Work

- Added 12 canonical PDFs to `papers/` and 12 source records + 12 wiki pages.
- Categories: 3 in `data-and-representation`, 4 in `generation-and-planning`, 5 in `other` (general cross-modal methods; category note on each page).
- New overview: `wiki/overviews/cross-modal-supervision-transfer.md`.
- Updated `wiki/overviews/audio-symbolic-transfer.md` with a section on cross-modal evidence outside the original ten-paper batch and links to the new pages.
- Regenerated `index.md`, the category indexes, and `logs/README.md`.

## Novelty verdict (AGT 1)

- **Narrow claim open:** no prior audio→symbolic distillation of a perceptual property (blend/clash/masking) with a validated teacher and note-level attribution checked by re-rendering edits.
- **Broad claim not open:** the general literature predicts gains only where the second modality carries information the first lacks; MIDI already encodes structure, so structure gains should be null.
- Closest prior art: MIDI-REPA (symbolic→audio), SMART (audio reward on symbolic output), cross-modal bootstrapping (audio style with a frozen symbolic backbone), modality hallucination/distillation (privileged-modality template), greedy multimodal learning (utilisation controls).

## Validation

- `validate_paper_records.py`: 97 source records, 97 paper pages, 15 synthesis pages, 0 errors.
- `audit_synthesis_orphans.py`: 0/97 orphans.

## Gaps and next steps

- Feasibility checks (ASAP↔MAESTRO overlap, licences, Aria-AMT/MERT runnability, renderer) handed off as **AGT 1b**.
- Perceptual orchestration ground-truth papers identified but not ingested (Sandell 1995; Kendall & Carterette 1993; Lembke et al. 2017; McAdams et al. 2022; Carpentier et al. 2010).
- Citation-graph crawl from MIDI-REPA, SMART, and CLaMP 3 is required before submission.
