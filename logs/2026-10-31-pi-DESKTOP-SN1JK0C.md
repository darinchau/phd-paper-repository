# 2026-10-31 — Seven arXiv-batch digests ingested from the local batch

**TL;DR:** Seven papers that had only local digests in the parent repository's `papers/<slug>/DIGEST.md` were ingested into the paper repository, which fixes the eight “unknown paper” citation errors those cards produced on the registry dashboard.

## Why this ingest happened

The parent repository's 18-paper arXiv batch (2026-10-25 to 2026-10-28) was digested into `phd-research/papers/<slug>/DIGEST.md` rather than into this repository. Four registry cards cited those local digest paths in their `papers:` field, and the dashboard validates that field against `wiki/<category>/<slug>.md`, so it reported eight unknown-paper problems (one paper is cited by two cards). The registry convention requires wiki digest paths, so the correct repair was to ingest the cited papers here rather than to drop the citations.

## Work

- Added seven canonical PDFs to `papers/`, named `{first-author}-{year}-{five-title-tokens}.pdf`.
- Added seven `sources/` records with the standard eight headings and page anchors, and seven `wiki/<category>/` pages.
- Categories: `explainability-and-auditability` (DA-LRT, Harmonic Representations), `generation-and-planning` (Sori, AutoHarmonizer, Hung timbre transfer), `data-and-representation` (MSVAE), `interaction-and-evaluation` (MusICA-MetaBench).
- Synthesis: added a dated subsection to `wiki/overviews/2026-symbolic-music-literature-map.md`, plus reciprocal paragraphs and links in `wiki/concepts/music-theory-probing.md`, `wiki/concepts/audio-symbolic-modality-gap.md`, `wiki/concepts/work-identity-versus-performance-variation.md`, `wiki/concepts/auditable-creative-editing-pipelines.md`, and `wiki/concepts/music-domain-inductive-biases.md`.
- Regenerated `index.md`, the category indexes, and `logs/README.md`.

| Paper | arXiv | PDF pages | Category |
|---|---|---:|---|
| Audio Cross Verification Using Dual Alignment Likelihood Ratio Test | 2607.18190v1 | 6 | explainability-and-auditability |
| Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills | 2607.06015v1 | 9 | interaction-and-evaluation |
| Harmonic Representations in Symbolic Music Transformers are Localized and Controllable | 2610.15957v1 | 9 | explainability-and-auditability |
| Sori: Streamable and Controllable Model for Non-musical Audio to Symbolic Music Transformation | 2610.15474v1 | 5 | generation-and-planning |
| Generating Chord Progression from Melody with Flexible Harmonic Rhythm and Controllable Harmonic Density | 2112.11122v3 | 12 | generation-and-planning |
| MSVAE: Rethinking Musical Semantics in Continuous Latent Spaces | 2610.17187v1 | 13 | data-and-representation |
| Musical Composition Style Transfer via Disentangled Timbre Representations | 1905.13567v1 | 7 | generation-and-planning |

## Corrections to the local batch digests

Re-reading the PDFs while writing these records found five errors in the earlier local digests. The new records follow the PDFs.

1. **Harmonic Representations:** the earlier digest swapped the unsteered and relative-steering Fréchet Music Distance values. Table 1 gives 80.27 unsteered, 85.42 relative-minor and 106.65 parallel-minor.
2. **Harmonic Representations:** mode steering uses α = 0.25 and works best applied only at the last bar positions; the digest did not state the strength.
3. **Musica-MetaBench:** the per-modality percentages 31/75/35 belong to ChoralSynth (Table 4), not ChoraleBricks; and the size calibration is 750 items for 3 points and 1,500 for 2 points, not “780 for 1–2%”.
4. **AutoHarmonizer:** the gamma direction was inverted. Higher Γ makes the model *less* likely to repeat the previous chord, so harmonic density rises; the digest said higher Γ favours repetition. The digest also claimed there was no listening study, but the paper reports an 83-participant human-versus-machine discrimination test.
5. **Hung et al. 2019:** the digest swapped the Gururani et al. and DuoED rows of Table 1 (their averages are 0.817 and 0.815), and listed 0.721/0.790/0.865/0.810/0.912/0.815 under Gururani rather than under DuoED.

## Validation

- `validate_paper_records.py`: all seven new source records and all seven new wiki pages pass. Three pre-existing errors remain, all in the YuE2 page and its source record, where a `## 8. 2026-10-30 re-check addendum` and an `## Implications (2026-10-30 re-check)` heading are not in the allowed heading sets, and the wiki page links to an `agent-notes/` path outside this repository. They predate this ingest and were left untouched.
- `audit_synthesis_orphans.py`: 0 orphans of 106 paper pages.
- `build_indexes.py`: `index.md` and the seven category indexes regenerated for 2026-10-31.

## Acronyms

- **AMT:** Automatic Music Transcription.
- **ASR:** Automatic Speech Recognition.
- **ATTM:** Academic Text-To-Music challenge protocol.
- **CFG:** Classifier-Free Guidance.
- **DAT:** Domain-Adversarial Training.
- **FMD:** Fréchet Music Distance.
- **LLM / MLLM:** (Multimodal) Large Language Model.
- **MIDI:** Musical Instrument Digital Interface.
- **MSVAE:** Music Semantic Variational Autoencoder.
- **PDF:** Portable Document Format.
- **TL;DR:** Too Long; Didn't Read.
