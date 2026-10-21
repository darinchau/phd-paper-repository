---
title: "Transcription as Supervision"
tags: [transcription, supervision, weak-labels, audio-to-symbolic, data-curation, label-noise, rendered-audio]
---

# Transcription as Supervision

"Transcription as supervision" is the practice of training a symbolic model on note events produced by an automatic music transcription (AMT) system rather than on human-authored scores or aligned performance MIDI. It is the mechanism behind the largest symbolic corpora: Aria-MIDI, GiantMIDI-Piano, ATEPP, PiJAMA, and the multi-track corpus in SymPAC. The important consequence is that the training label is a **learned function of audio**, not a neutral copy of the score. The model learns the transcriber's note vocabulary, timing conventions, instrument mapping, and errors along with the music.

## The Label Chain

For a recording `a`, the corpus supplies `T(a) = {(pitch, onset, offset, velocity, instrument)}`. Training minimises a loss against `T(a)`, not against the unknown score `s` or the true performance `y`. Three objects are therefore distinct:

| Object | What it contains | Typical loss |
|---|---|---|
| Score `s` | Metre, spelling, voices, notation, repeats | Not recoverable from audio alone |
| Performance `y` | Exact timing, dynamics, pedal, timbre | Partially recoverable, instrument-dependent |
| Transcription `T(a)` | Quantised or performance-time notes chosen by the AMT model | The actual training target |

The gap `T(a) − y` is systematic, not random: missed low-velocity notes, octave errors, merged or split chords, smeared offsets, omitted pedal, and instrument confusion. The gap `y − s` is a second loss: performance timing is not metrical position, and audio does not reveal pitch spelling, voice assignment, or notation.

## Evidence Across the Corpus

- **Piano works at scale.** Aria-MIDI (1.19M files, ~100k hours) uses Aria-AMT; 800,973 files remain after work-level deduplication. Aria then trains a 650M model on 60,473 hours and reports strong probes and listening-test parity with human continuations. This is the strongest positive evidence that transcription-as-supervision is sufficient for solo piano.
- **Multi-track works in-house.** SymPAC runs transcription, beat tracking, chords, sections, and tagging over ~1M tracks and trains an 86M generator; it beats FIGARO/MMT in a 12-rater MOS test. The public MSD arm is weaker than the in-house arm, and the corpus is unreleased.
- **Multi-instrument is the bottleneck.** YourMT3+ reaches 84.6 Multi F1 on synthetic Slakh but below 10% F1 for non-main instruments on real RWC-Pop. A corpus built by transcribing commercial mixtures would inherit that failure.
- **Transcription is not the same as symbolic data quality.** Note F1 is measured against reference notes; a generator or embedding model may be more sensitive to timing conventions, velocity quantisation, or repeated errors than to average F1.

## Failure Modes to Measure

1. **Label noise correlation.** Errors cluster by instrument, register, density, and recording quality; they are not independent noise.
2. **Distribution shift.** A transcriber trained on MAESTRO-like piano generalises poorly to other genres, room acoustics, and mixtures.
3. **Quantisation mismatch.** Some pipelines output performance-time milliseconds (Aria), others a beat grid (SymPAC), others 10 ms frames; mixing them changes what a model can learn.
4. **Missing score-level information.** Metre, voicing, spelling, slurs, dynamics, and form are absent or inferred; a model trained only on `T(a)` cannot learn notation-level constraints unless they are added.
5. **Leakage and duplication.** Repeated performances of the same work inflate apparent scale; work-level deduplication is necessary but metadata-dependent.

## Design Implications

- Report the transcriber, its version, its training distribution, and its measured error profile — not only the corpus size.
- Evaluate downstream models on clean, human-authored symbolic test sets as well as transcribed ones, so corpus and label effects are separable.
- Prefer paired rendered audio/MIDI when the scientific question is about audio–symbolic correspondence, because rendering gives an exact pairing and removes the transcriber from the causal chain.
- Treat transcription confidence or agreement across transcribers as a weighting signal; hard labels discard it.

## Related Pages

- [[overviews/audio-symbolic-transfer]] — the four routes from audio to symbolic data and their evidence.
- [[concepts/audio-symbolic-modality-gap]] — why the two modalities are hard to align even with paired data.
- [[data-and-representation/bradshaw-2025-aria-midi-a-dataset-of]] — the largest piano transcription corpus.
- [[data-and-representation/chang-2024-yourmt3-multi-instrument-music-transcription]] — the multi-instrument quality ceiling.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — a generation system trained only on MIR outputs.
- [[retrieval-and-recombination/bang-2025-pianobind-a-multimodal-joint]] — PIAST MIDI is also AMT output.
