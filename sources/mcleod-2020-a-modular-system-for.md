---
title: "A Modular System for Harmonic Structure Analysis of Music"
authors: Andrew McLeod and Martin Rohrmeier
year: 2020
doi: null
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/mcleod-2020-a-modular-system-for.pdf"
pdf_filename: mcleod-2020-a-modular-system-for.pdf
source_collection: DMRN+15 workshop proceedings
source_format: pdf
extracted_date: 2026-10-11
---

## One-line Summary

McLeod and Rohrmeier propose a modular harmonic-analysis system that separates chord-boundary detection, chord classification, chord sequencing, key-boundary detection, key sequencing, and initial-chord prediction so each musical dependency can be inspected or retrained independently.

## 1. Document Information

- **Venue:** DMRN+15: Digital Music Research Network One-Day Workshop 2020, Queen Mary University of London, 15 December 2020; two-page workshop paper.
- **Authors and affiliation:** Andrew McLeod and Martin Rohrmeier, Digital and Cognitive Musicology Lab, EPFL, Switzerland.
- **Primary contribution/category:** interpretable, modular symbolic harmonic analysis with explicit chord and local-key structure; categorized under `theory-and-constraints`.
- **Input scope:** the architecture is designed to accept scores, MIDI, or audio spectrogram frames, but the reported experiments use musical scores only.
- **Evidence boundary:** the supplied PDF reports the architecture and a compact evaluation table. It does not provide a public implementation, a complete dataset specification, confidence intervals, or component ablations.

## 2. Key Contributions

1. **Granularity-aligned decomposition:** instead of assigning a single label sequence directly from frames, the system models frames/notes, chord boundaries, chord identities, chord sequences, local-key boundaries, and local-key sequences with separate modules.
2. **Theory-rich output vocabulary:** roots and tonics use 35 spellings from double-flat to double-sharp; chords cover major, minor, augmented, and diminished triads or seventh chords with inversions, for 1,540 chord forms, while keys cover 70 major/minor tonic combinations.
3. **Adaptable pipeline:** module boundaries allow independent retraining and replacement, supporting future MIDI/audio adaptation and human-in-the-loop annotation.

## 3. Methodology and Architecture

The **Chord Transition Model (CTM)** predicts whether each input vector starts a new chord. The **Chord Classification Model (CCM)** consumes the vectors assigned to one chord and predicts a distribution over the full chord vocabulary. The **Chord Sequence Model** predicts the next chord from a sequence of chords represented relative to the current key.

The **Key Transition Model** predicts local-key boundaries from relative chords. The **Key Sequence Model** predicts the next local key from the preceding local-key chord sequence plus the first chord of the new section. The **Initial Chord Model** predicts the first relative chord given the key. The paper describes most components as simple single-layer LSTMs with softmax outputs, with dependencies passed from lower- to higher-level modules.

The design makes an analytical object visible at each level, but the modules are still learned black boxes. Modularity therefore exposes interfaces and error locations; it does not by itself provide a faithful explanation of an individual label.

## 4. Key Results and Benchmarks

The authors train and evaluate on a private annotated score collection from several composers, including the Annotated Beethoven Corpus. Values are average proportions of each piece with the correct label:

| Chord Root+Triad | Chord +7ths | Chord +Inversion | Key Tonic | Key Mode | Full |
|---:|---:|---:|---:|---:|---:|
| 0.47 | 0.32 | 0.26 | 0.45 | 0.34 | 0.15 |

The results are described as promising for a first, simple modular implementation. The `Full` score is substantially lower than the individual dimensions, indicating that jointly satisfying the detailed chord and key attributes is difficult. The paper does not report uncertainty, work-disjoint splits, per-composer results, or comparisons against an integrated baseline.

## 5. Limitations and Future Work

- The evaluation uses private data and only musical scores, so the advertised MIDI/audio portability is not demonstrated.
- The paper does not isolate the contribution of each module, quantify error propagation, or compare modular and monolithic systems under a matched protocol.
- A large chord/key vocabulary creates a demanding exact-label task; the table does not explain whether partial credit or spelling ambiguity affects the scores.
- Sequential decoding can propagate boundary or classification errors upward. The authors suggest scheduled sampling to improve robustness.
- Planned extensions include retraining only the CTM and CCM for MIDI/audio inputs and using the modular search process for human annotation, where a person can force selected labels.

## 6. Related Work

The paper positions itself against frame-sequence harmonic analysis, citing Harmony Transformer and other neural harmonic-analysis systems, and uses the Annotated Beethoven Corpus as a data source. Those cited works are not separately ingested here.

- [[concepts/music-domain-inductive-biases]] — separates a musically structured architecture from an explicit verifier or faithful explanation.
- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — later symbolic interpretability work that adds probing and intervention evidence rather than relying on modularity alone.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — tests recoverability of named music-theory labels from frozen representations; it addresses a different evidence question.

## 7. Glossary

- **Harmonic structure analysis:** assigning chord and local-key information to musical input.
- **Chord transition:** a boundary decision locating the start of a new chord.
- **Relative chord:** a chord represented relative to the current key tonic.
- **Local key:** a key region attached to a span of the piece rather than necessarily the global key.
- **Modular system:** a pipeline of components with defined inputs and outputs that can be replaced or retrained separately.
