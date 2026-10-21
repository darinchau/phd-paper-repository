# 2026-10-21 — Audio–symbolic transfer batch (10 arXiv papers)

**TL;DR:** Ten papers on turning audio into symbolic music, aligning the two modalities, and rendering symbols back to audio were read and ingested; together they show piano-scale transcription works, multi-instrument transcription does not yet, and nobody has measured which musical information actually transfers — so that measurement is the recommended new line.

## Scope and completion

User supplied a list of ten arXiv links and asked for two things: digest the papers, and recommend a feasible new research line (owner likes "getting past piano" and "what actually transfers"). All ten were downloaded, read in full (main text, tables, figures; references skimmed), digested into the paper repository, and connected to two new concept pages and one new overview.

| # | Paper | arXiv | Pages | Category |
|---|---|---|---:|---|
| 1 | Aria-MIDI | 2504.15071 | 17 | data-and-representation |
| 2 | Scaling Self-Supervised Representation Learning for Symbolic Piano Performance (Aria) | 2506.23869 | 9 | data-and-representation |
| 3 | CLaMP 3 | 2502.10362 | 21 | retrieval-and-recombination |
| 4 | PianoBind | 2509.04215 | 8 | retrieval-and-recombination |
| 5 | Descriptor-Injected Cross-Modal Learning | 2604.10283 | 26 | retrieval-and-recombination |
| 6 | Systematic Analysis of Music Representations from BERT | 2306.04628 | 7 | explainability-and-auditability |
| 7 | SymPAC | 2409.03055 | 12 | generation-and-planning |
| 8 | Efficient Fine-Grained Guidance (FGG) | 2410.08435 | 25 | generation-and-planning |
| 9 | YourMT3+ | 2407.04822 | 15 | data-and-representation |
| 10 | Multi-instrument Music Synthesis with Spectrogram Diffusion | 2206.05408 | 12 | generation-and-planning |

Two links did not match the commentary that accompanied the list: `2306.04628` is the MusicBERT representation-analysis paper, not a transcription paper, and `2410.08435` is FGG (diffusion control), not a CLaMP follow-up. Both were digested as the actual papers.

## Records

- Canonical PDFs in `papers/` with stems listed below; SHA-256 prefixes:
  - `bradshaw-2025-aria-midi-a-dataset-of.pdf` — `ffa245d64b233ac2`
  - `bradshaw-2025-scaling-self-supervised-representation.pdf` — `92bf1578c39c4414`
  - `wu-2025-clamp-3-universal-music.pdf` — `a4dfe1dbce914b0d`
  - `fernandez-mendez-2026-descriptor-injected-cross-modal-learning.pdf` — `087404b3f2c4ad1a`
  - `bang-2025-pianobind-a-multimodal-joint.pdf` — `d0c6fea3f1e59683`
  - `han-2023-systematic-analysis-of-music.pdf` — `846c46ba7bceea0e`
  - `chen-2024-sympac-scalable-symbolic-music.pdf` — `6bf4c08a47ab97e7`
  - `zhu-2025-efficient-fine-grained-guidance-for.pdf` — `a706905424ddf6c4`
  - `chang-2024-yourmt3-multi-instrument-music-transcription.pdf` — `3deb043b284186b9`
  - `hawthorne-2022-multi-instrument-music-synthesis-with.pdf` — `f30b5595735cab14`
- Ten `sources/` records and ten `wiki/<category>/` pages, each with page/section anchors.
- New synthesis: `wiki/overviews/audio-symbolic-transfer.md` (four routes, evidence map, factor decomposition, feasibility ranking), `wiki/concepts/transcription-as-supervision.md`, `wiki/concepts/audio-symbolic-modality-gap.md`.
- Reciprocal links added from every new paper page to the overview and at least one concept; the overview links back to all ten.

## Category decisions

- **Aria-MIDI, Aria, YourMT3+ → `data-and-representation`.** Primary contribution is a corpus, a representation-learning recipe, and a transcription/data-production model respectively, not a generator.
- **CLaMP 3, PianoBind, descriptor injection → `retrieval-and-recombination`.** Cross-modal retrieval/alignment is the task; the embeddings are the method.
- **MusicBERT analysis → `explainability-and-auditability`.** Its contribution is a probing/audit methodology, not a new representation.
- **SymPAC, FGG, spectrogram diffusion → `generation-and-planning`.** Control and synthesis are generative contributions.

## What the batch establishes

1. **Piano-scale transcription-as-supervision works.** Aria-MIDI supplies ~100k hours; Aria trains on ~60k hours and reports SOTA piano probes and listening-test parity with human continuations. This is the strongest positive result in the batch.
2. **Multi-track transcription-as-supervision works in-house but not publicly.** SymPAC's 1M-track corpus and MOS win are real, but the corpus is unreleased; YourMT3+ reaches 84.6 Multi F1 on synthetic Slakh and below 10% F1 for non-main instruments on real RWC-Pop.
3. **Text-bridged audio–symbolic alignment is coarse.** CLaMP 3's emergent audio↔symbolic MRR is 0.03–0.06 versus 0.0075 random and 0.31–0.53 for symbolic↔symbolic. PianoBind and descriptor injection improve retrieval, but none yields note-level correspondence.
4. **Descriptors can force alignment, at a robustness cost.** The A4 audio descriptor raises MAESTRO retrieval by 8.8 points and is causally necessary (zeroing it costs 75–78 points), but velocity/octave perturbation drops S below 18%.
5. **Probing methodology exists but has not been applied to the transfer question.** MusicBERT's seven probes show objective- and layer-dependent information; Aria's probes are coarse metadata tasks. No paper compares matched corpora (score vs performance vs transcribed) on the same factor suite.
6. **The inverse direction is bounded by the audio representation.** Spectrogram diffusion matches the inverter's transcription-F1 ceiling (0.36) but not raw audio (0.63).

## Synthesis gaps noted

- No paper in the batch isolates **expressive performance** vs **instrumentation/timbre** vs **compositional structure** vs **recording/style** as separate transferable factors. This is the gap the recommended line targets.
- No public multi-instrument corpus with exact MIDI/audio pairing was evaluated at scale in these papers; Slakh is the obvious public option but is rendered, not recorded.
- No note-level audio–symbolic benchmark exists in the batch; CLaMP 3/PianoBind/descriptor injection all evaluate global or segment retrieval.
- Score-level information (metre, spelling, voices, notation) is absent from every audio-derived corpus here; this is a structural limit of the route, not an engineering detail.

## Validation

- `validate_paper_records.py`: 85 source records, 85 paper pages, 14 synthesis pages, crop evidence — 0 errors.
- `audit_synthesis_orphans.py`: 0/85 orphans.
- `build_indexes.py --date 2026-10-21`: `index.md` and four category indexes regenerated.
- No page claims a result that was not in the read text; all quantitative claims carry a table/figure/section anchor.

## Acronyms

- **AMT:** Automatic Music Transcription.
- **CLaMP:** Contrastive Language–Music Pretraining.
- **FGG:** Fine-Grained Guidance.
- **MIR:** Music Information Retrieval.
- **MIDI:** Musical Instrument Digital Interface.
- **MOS:** Mean Opinion Score.
- **MRR:** Mean Reciprocal Rank.
- **MT3:** Multi-Task Multitrack Music Transcription.
- **SSL:** Self-Supervised Learning.
