---
title: "SymPAC: Scalable Symbolic Music Generation With Prompts And Constraints"
authors: "Haonan Chen, Jordan B. L. Smith, Janne Spijkervet, Ju-Chiang Wang, Pei Zou, Bochen Li, Qiuqiang Kong, and Xingjian Du"
year: 2024
doi: 10.48550/arXiv.2409.03055
source: chen-2024-sympac-scalable-symbolic-music.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2024-sympac-scalable-symbolic-music.pdf"
pdf_filename: chen-2024-sympac-scalable-symbolic-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [symbolic-generation, transcription, multi-track, control, fsm, remi-plus, scalability, bytedance]
---

# SymPAC: Scalable Symbolic Music Generation With Prompts And Constraints

## Summary

SymPAC is the clearest existence proof that a multi-track symbolic generator can be trained only on auto-transcribed audio. It runs beat tracking, chord detection, section detection, multi-track transcription, and tagging over ~1M in-house tracks (plus MSD and Lakh as public arms), encodes the results in REMI+ with a separate prompt-bar section, and constrains decoding with a finite-state machine. An 86M Llama-style model scales with data on six of seven KLD classes, adheres to chord inputs 87% of the time, and beats FIGARO and MMT on a 12-participant MOS test. The limits are as important as the result: 1/16-bar quantization, 12 triads only, an unreleased corpus, and no separation of transcription error from model error.

## Key Contributions

- First demonstration of symbolic generation trained solely on MIR-extracted audio events, with scale evidence rather than a single dataset.
- Prompt bars: all controls precede the music, and the model can fill in missing controls.
- FSM-constrained sampling that enforces encoding grammar and user constraints exactly, instead of soft conditioning.
- A public-data arm (MSD/Lakh) that is weaker but reproducible, alongside the unreleased 1M-track arm.

## Methodology and Architecture

Pipeline: audio → beat tracking, chord detection, section detection, multi-track transcription, tagging → REMI+ tokens. A song bar contains meta (bar/genre/section/bpm), chords (position/chord), per-instrument tracks (position/duration/pitch), and drums. Prompt bars contain only controls; the sequence is prompt bars, `end_of_prompt`, song bars, `end_of_song`. Model: 12-layer, 12-head, 768-dim Llama decoder (~86M parameters), 10,240-token windows. At inference an FSM restricts each sampling step to tokens allowed by the grammar and the requested chord/section/track values. Training uses no augmentation or filtering. Corpora are used separately: IHD (~1M full songs), MSD (1M previews), LMD (170K MIDI).

## Results

| Claim | Measurement | Anchor |
|---|---|---|
| Scale helps | IHD-100 best KLD in 6/7 classes; IHD-1% worst in 6/7 | Table 2, p. 4 |
| Chord control | 87.2% (IHD-100), 87.6% (MSD), 74.0% (IHD-1%) | Table 4, p. 5 |
| Structure control | HR3F 0.60, PWF 0.50, Sf 0.50 | Table 5, p. 5 |
| MOS overall | 3.60 IHD / 3.25 LMD / 3.07 MSD / 2.74 FIGARO / 2.16 MMT | Table 3, p. 5 |
| Non-monotone structure KLD | 0.220 at 10% vs 0.348 at 100% | Table 2, p. 4 |

The MOS study has 12 raters and 10 samples per model; no confidence intervals are reported. Control adherence is not musical quality: the FSM guarantees that requested tokens appear, not that the result is coherent or non-repetitive. The in-house corpus is the source of the strongest numbers and is not available for inspection.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the multi-track, control-oriented instance of the hard-transcription route.
- [[concepts/transcription-as-supervision]] — every training target is a MIR model output, so beat/chord/transcription errors define the distribution.
- [[data-and-representation/bradshaw-2025-aria-midi-a-dataset-of]] — the piano-only, much larger parallel corpus.
- [[data-and-representation/chang-2024-yourmt3-multi-instrument-music-transcription]] — the transcription stack whose quality bounds this approach.
- [[generation-and-planning/zhu-2025-efficient-fine-grained-guidance-for]] — a different way to enforce harmonic constraints, at sampling time in diffusion.
- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] — score-text generation with a different control surface.
