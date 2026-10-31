---
title: "Generating Chord Progression from Melody with Flexible Harmonic Rhythm and Controllable Harmonic Density"
authors: Shangda Wu, Yue Yang, Zhaowen Wang, Xiaobing Li, Maosong Sun
year: 2023
doi: 10.48550/arXiv.2112.11122
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wu-2023-generating-chord-progression-from-melody.pdf"
pdf_filename: wu-2023-generating-chord-progression-from-melody.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

AutoHarmonizer predicts one chord per sixteenth-note frame from a melody plus explicit beat and key sequences, so chord changes are not tied to bars, and a single gamma parameter changes how often the chord changes — giving direct, training-free control over harmonic density in a way earlier bar-level harmonisers could not.

## 1. Document Information

- **Canonical citation:** Shangda Wu, Yue Yang, Zhaowen Wang, Xiaobing Li, and Maosong Sun, “Generating Chord Progression from Melody with Flexible Harmonic Rhythm and Controllable Harmonic Density,” arXiv:2112.11122v3 [cs.SD], December 2023, 12 PDF pages in journal submission format. The arXiv comment states “accepted by EURASIP JASMP” (EURASIP Journal on Audio, Speech, and Music Processing); the PDF carries no published journal header, so venue status rests on that arXiv metadata.
- **Affiliations:** Department of Music AI and Information Technology, Central Conservatory of Music, Beijing; Department of Computer Science and Technology, Tsinghua University. The first three authors share equal contribution. [PDF p. 1]
- **DOI:** `10.48550/arXiv.2112.11122` (arXiv DOI; no publisher DOI in the read text).
- **Artifacts:** dataset, source code, model weights and generated samples at `https://github.com/sander-wood/autoharmonizer`. [PDF p. 11]
- **Canonical integrity:** SHA-256 `8c66db6e0090197dab222d82bf35af3ea4d6d86e229d86a3fe0403ac8966c051`.
- **Rights boundary:** arXiv preprint; terms follow the arXiv licence, not restated here. Local research evidence only.
- **Primary category:** `generation-and-planning`. The contribution is a controllable chord generator; the evaluation metrics are its supporting apparatus.
- **Evidence levels:** Table 1 was re-read from the rendered page. Two errors in the earlier batch digest are corrected here: the gamma direction is inverted (higher Γ gives *more* chord changes, not sparser harmony), and a listening study *is* reported (83 subjects), contrary to the digest's claim that all evaluation was symbolic.

## 2. Key Contributions

### Frame-level chords instead of bar-level chords

Chords are predicted for every sixteenth-note frame rather than one per bar or half-bar, which is what makes a *flexible harmonic rhythm* representable at all. Prior neural harmonisers could only produce chord changes at fixed metric positions. [PDF pp. 1–2, 4]

### Explicit beat and key inputs

A four-dimensional beat-strength vector (non-beat, weak, medium, strong) and a fifteen-value key encoding (−7…+7 sharps/flats) are fed to a separate meta-information encoder, so the model is not restricted to 4/4 and C major as the transformer baselines are. [PDF pp. 4–5]

### Gamma sampling for harmonic density

The previously generated chord is treated as an attribute token, and its probability is rescaled before sampling: p_A^out = p_A^{tan(πΓ/2)}, with the remaining mass redistributed over non-attribute chords. Γ = 0.5 leaves the distribution unchanged; Γ > 0.5 lowers the chance of repeating the previous chord, so chords change more often and harmonic density rises; Γ < 0.5 makes the progression sparser. No retraining is needed. [PDF p. 4, eq. 1]

### A reusable metric suite for harmonic rhythm

Beyond frame accuracy, the paper uses chord coverage, chord-histogram entropy, chord tonal distance, chord-tone-to-non-chord-tone ratio, pitch consonance, melody–chord tonal distance, and three new harmonic-rhythm metrics: harmonic-rhythm coverage, harmonic-rhythm histogram entropy, and chord beat strength. [PDF pp. 5–6]

## 3. Methodology and Architecture

- **Representation per sixteenth-note frame.** Melody: 128-dimensional one-hot (rest + 127 MIDI pitches excluding pitch 0). Beat: 4 dimensions. Key: 15 values. Chord: 1,462 dimensions (rest + 1,461 chord symbols observed in the corpus). [PDF p. 4]
- **Network.** Two Bi-LSTM encoders — melody, and concatenated beat+key — each with two stacked blocks of a 256-unit Bi-LSTM and a 128-unit time-distributed layer; their final hidden states are concatenated; a three-layer Bi-LSTM decoder emits 1,462 logits autoregressively, frame by frame. Dropout 0.2, batch 512, early stopping with patience 20. [PDF p. 4]
- **Data.** Wikifonia lead sheets: 6,675 compositions, reduced to 5,204 after removing sheets with no chord symbols or no chord change within four bars; 90/10 train/validation split, giving 515 validation tunes. [PDF p. 5]
- **Baselines.** CGSM (Bi-LSTM, 24 triads per bar), STHarm and VTHarm (two chords per bar, applicable only to 4/4). Only 311 of the 515 validation tunes are in 4/4, which the authors state makes the comparison not fully matched. [PDF p. 5]
- **Listening study.** A human-versus-machine discrimination test with 83 subjects in three groups (33 music majors and students; 25 non-music majors with harmony knowledge; 25 listeners with no harmony training), on 20 randomly drawn validation tunes, each in seven versions. [PDF p. 9]

## 4. Key Results and Benchmarks

Table 1, 515 validation tunes [PDF p. 6]:

| System | Accuracy | CC | CHE | CTD | CTnCTR | PCS | MCTD | HRC | HRHE | CBS |
|---|---|---|---|---|---|---|---|---|---|---|
| Ground truth | 1.0000 | 12.0603 | 2.0582 | 1.0653 | 0.8476 | 0.4975 | 1.1525 | 5.7626 | 1.1877 | 2.6024 |
| AH-0.5 | 0.3087 | 5.0914 | 1.3477 | 1.1864 | 0.9054 | 0.5590 | 1.1252 | 5.9027 | 1.3965 | 2.8904 |
| AH-0.6 | 0.3142 | 5.7101 | 1.4353 | 1.1769 | 0.9030 | 0.5723 | 1.1076 | 5.9397 | 1.3494 | 2.8668 |
| AH-0.7 | 0.3111 | 6.4163 | 1.5227 | 1.1584 | 0.8979 | 0.5775 | 1.1011 | 6.0233 | 1.2901 | 2.8310 |
| AH-0.8 | 0.3088 | 7.3152 | 1.6267 | 1.1289 | 0.8916 | 0.5773 | 1.1016 | 6.1031 | 1.2451 | 2.7758 |
| AH-0.9 | 0.2890 | 8.6420 | 1.7555 | 1.0911 | 0.8797 | 0.5712 | 1.1038 | 6.1770 | 1.1910 | 2.6572 |
| CGSM | 0.2822 | 5.9883 | 1.3619 | 0.7814 | 0.9077 | 0.6224 | 1.0901 | 1.2354 | 0.0459 | 2.9892 |
| STHarm | 0.0885 | 9.8051 | 1.5723 | 0.6331 | 0.6184 | 0.2604 | 1.3285 | 1.0000 | 0.0000 | 2.5000 |
| VTHarm | 0.0928 | 13.5588 | 2.2083 | 0.8367 | 0.6063 | 0.2686 | 1.3364 | 1.0000 | 0.0000 | 2.5000 |

- **Control works in the expected direction.** As Γ rises from 0.5 to 0.9, chord coverage rises 5.09 → 8.64 and chord-histogram entropy 1.35 → 1.76, i.e. more distinct chords and more switching; chord tonal distance falls 1.19 → 1.09 toward the ground-truth 1.07. [PDF p. 6, Table 1]
- **Accuracy is modest and decreases with Γ.** Frame accuracy is 0.309–0.314 around Γ = 0.5–0.7 and 0.289 at Γ = 0.9, versus 0.282 for CGSM and below 0.10 for the two bar-level transformer baselines. [PDF p. 6, Table 1]
- **Harmonicity is closer to ground truth than the baselines** on most melody/chord metrics, but the generated progressions are more consonant than real music (higher chord-tone ratio and consonance, lower melody–chord distance). [PDF pp. 6–8]
- **Listening study.** AutoHarmonizer was mistaken for human more often than CGSM and STHarm in all configurations; AH-0.5 was judged most human-like, and half the subjects also misclassified genuine human progressions as machine-generated. Untrained listeners were more likely than musicians to accept fixed-rhythm baselines as human. [PDF p. 9]

## 5. Limitations and Future Work

- **Low absolute accuracy.** About 31% frame-level agreement; the model is not a replacement for a human arranger, and the authors say the evaluation shows room for improvement. [PDF pp. 6, 11]
- **Weak and mismatched baselines.** CGSM, STHarm and VTHarm are older systems, two of them restricted to 4/4, and only 311 of 515 tunes are in 4/4. [PDF p. 5]
- **No dedicated test set.** The listening study and the metrics use tunes drawn from the validation split, because the dataset has no separate test partition. [PDF p. 9]
- **Narrow corpus and vocabulary.** Wikifonia is Western lead-sheet repertoire, and the 1,462-symbol vocabulary is corpus-specific. [PDF p. 5]
- **Dated architecture.** A small Bi-LSTM; no comparison with modern Transformers or diffusion models. [PDF p. 4]
- **Control changes density, not appropriateness.** Γ changes how often the chord changes, not whether the change is structurally well motivated; high Γ can produce chord churn. [PDF pp. 4, 8]
- **Key and beat are inputs, not inferred.** The system assumes they are known. [PDF p. 4]

## 6. Related Work

- **Harmonic theory as an explicit constraint.** Key, beat and a large chord vocabulary are inputs rather than learned latents, which connects to [[concepts/music-domain-inductive-biases]] and to the theory-side analyses in [[theory-and-constraints/mcleod-2020-a-modular-system-for]].
- **Harmonisation and accompaniment in this repository.** [[theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned]] studies what tonal structure models learn; AutoHarmonizer instead fixes the vocabulary and controls density.
- **Interpretable control versus explanation.** The Γ dial is an interpretable control in the sense of [[concepts/auditable-creative-editing-pipelines]], but the model gives no per-frame reason for a chord; the paper's own next step would be to expose the melody-note evidence behind each choice.
- **Symbolic control interfaces for repair.** A frame-level harmoniser can re-harmonise a passage rather than replace a whole bar, which is the granularity a local repair tool needs; compare [[concepts/expression-aware-symbolic-representations]].

## 7. Glossary

- **ACC:** frame accuracy of chord labels.
- **AH:** AutoHarmonizer.
- **Bi-LSTM:** Bidirectional Long Short-Term Memory network.
- **CBS:** Chord Beat Strength.
- **CC:** Chord Coverage, the number of distinct chord types.
- **CHE:** Chord Histogram Entropy.
- **CGSM:** Chord Generation from Symbolic Melody (baseline).
- **CTD:** Chord Tonal Distance.
- **CTnCTR:** Chord Tone to non-Chord Tone Ratio.
- **HRC:** Harmonic Rhythm Coverage.
- **HRHE:** Harmonic Rhythm Histogram Entropy.
- **MCTD:** Melody–Chord Tonal Distance.
- **PCS:** Pitch Consonance Score.
- **STHarm / VTHarm:** transformer-based harmonisation baselines.
- **Γ (gamma):** the harmonic-density control strength.
