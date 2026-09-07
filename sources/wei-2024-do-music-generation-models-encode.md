---
title: "Do Music Generation Models Encode Music Theory?"
authors: Megan Wei, Michael Freeman, Chris Donahue, and Chen Sun
year: 2024
doi: 10.48550/arXiv.2410.00872
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-paper-digestion/phd-paper-repository/papers/wei-2024-do-music-generation-models-encode.pdf"
pdf_filename: wei-2024-do-music-generation-models-encode.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-09-06
---

## One-line Summary

SynTheory uses synthetic, concept-controlled music clips to probe music-theory information in frozen Jukebox and MusicGen representations; reported decoding performance is high, but released evaluation-code discrepancies may affect the validity of the numerical results, and probing does not establish causal musical reasoning.

## 1. Document Information

- **Version and venue:** supplied arXiv `2410.00872v1`, eight physical pages; page 1 identifies ISMIR 2024. The DOI above identifies the arXiv record, not a separately verified proceedings DOI. Wei and Freeman share first authorship; affiliations are Brown University and Carnegie Mellon University.
- **Rights stated in the PDF:** CC BY 4.0 on page 1. This notice concerns the paper; it does not independently settle all dataset/soundfont rights.
- **Reading evidence:** all eight pages read through Citra `rust-read-pdf-v1`, supplemented with layout text because Citra collapsed spacing and interleaved columns. Figure 1, Figure 2, and Table 2 were rendered and visually inspected. No LaTeX source accompanied the supplied PDF.
- **Primary contribution/category:** internal-representation probing and interpretation of music-theory encoding, supported by a synthetic benchmark. Categorized under explainability and auditability; the paper does not introduce a theory-constrained generator or demonstrate faithful explanations. Dataset construction is a secondary contribution.
- **Author-linked artifacts:** [code](https://github.com/brown-palm/syntheory), [dataset](https://huggingface.co/datasets/meganwei/syntheory), and [project/examples website](https://brown-palm.github.io/music-theory/). Code inspected at `4f222359e750ec55425c12809c1a0358b74fce49`. Dataset and website pages were inspected; audio was not downloaded or listened to. The code and dataset card identify MIT licensing.
- **Evidence boundary:** paper-reported scores, inspected implementation behavior, and repository interpretations are distinguished below. No embedding extraction, probe training, or reproduction of Table 2 was performed. The exact code revision used for the published experiments is not established.

## 2. Key Contributions

1. **SynTheory:** a programmatically generated MIDI/audio benchmark isolating seven elementary Western music-theory tasks, with balanced combinations of labels and nuisance factors. Synthetic construction reduces annotation/alignment demands and permits controlled variation. It does not prove that all acoustic shortcuts are removed. [PDF pp. 2–4]
2. **Representation comparison:** probes compare frozen audio-codec and decoder-LM features with mel spectra, MFCCs, chroma, and their aggregation. [PDF pp. 4–6]
3. **Layer and size analysis:** the authors report strong Jukebox performance and stronger MusicGen Small probing than Medium/Large, with substantial layer dependence. This concerns accessibility of information under this probing protocol, not a general ordering of music-generation ability. [PDF pp. 5–6]
4. **Reusable experimental direction:** simple isolated concepts can be decoded well even from handcrafted features, motivating harder compositional and entangled-concept benchmarks. The authors propose future language-side probing and concept control; they do not demonstrate such interventions here. [PDF p. 6]

## 3. Methodology and Architecture

### Concept-controlled stimuli

Tonal datasets use 92 selected MIDI instrument programs rendered through `TimGM6mb.sf2`; exclusions target sound effects, pitch-unstable articulation, and programs labeled polyphonic. Rhythmic datasets use five metronome-like timbral settings. Instruments are balanced across tonal labels, but this is not an instrument-disjoint generalization split. Tonal examples generally fix tempo at 120 BPM. [PDF p. 3]

| Dataset | Construction and prediction target | Reported configurations |
|---|---|---:|
| Tempo | Integer 50–210 BPM, 4/4, five click settings, five random offsets; regress BPM | 4,025 |
| Time signatures | 2/2, 2/4, 3/4, 3/8, 4/4, 6/8, 9/8, 12/8 at 120 BPM; three reverb levels, five click settings, ten offsets; classify eight meters | 1,200 |
| Notes | 12 pitch classes × nine octaves × 92 instruments; predict pitch class, not octave | 9,936 |
| Intervals | 12 roots × 12 interval distances × 92 instruments × simultaneous/ascending/descending playback; predict interval | 39,744 |
| Scales | Seven diatonic modes × 12 roots × 92 instruments × ascending/descending; predict mode | 15,456 |
| Chords | 12 roots × four triad qualities × 92 instruments × three inversions; predict quality | 13,248 |
| Chord progressions | 19 four-chord templates × 12 key roots × 92 instruments; predict template | 20,976 |

Table 1 totals **104,585 configurations** (repository arithmetic). Notes include 88 silent extreme-register configurations; the paper distinguishes 9,848 non-silent note samples from 9,936 configurations. This distinction must survive any dataset-size or evaluation-denominator claim. [PDF p. 3, Table 1 and footnote]

The intervals span minor second through perfect octave; “unison” in the playback description means simultaneous presentation, not a zero-semitone target class. Ascending/descending pairs repeat four times; simultaneous intervals repeat eight times. Scales use Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, and Locrian. Triads are major, minor, diminished, or augmented. [PDF p. 4]

The progressions comprise ten major-mode and nine natural-minor templates. Examples are I–IV–V–I, I–V–vi–IV, and i–iv–v–i. Classification is among predefined templates; it is not open-ended harmonic-function analysis. The PDF describes quarter-note chord playback, while the inspected generator uses two beats per chord at 120 BPM; see the discrepancy section. [PDF p. 4]

### Feature extraction

Inputs are trimmed to four seconds and converted to mono. Jukebox features are extracted through Jukemirlib from 72 decoder layers, with time-mean pooling to 4,800 features per layer. The PDF describes temporal downsampling with a Librosa FFT method. MusicGen audio is resampled to 32 kHz; its pre-quantization EnCodec representation has shape 128 × 200 and becomes 128-dimensional after time pooling. MusicGen decoder states are reported as 24 × 200 × 1,024 for Small, 48 × 200 × 1,536 for Medium, and 48 × 200 × 2,048 for Large; each layer is pooled over time. One layer is selected per model and concept. [PDF p. 5]

The study focuses on audio representations and says it does not pass text through the text encoder. The released MusicGen extractor actually passes an empty-string text condition through the processor and model; this is not a substantive musical prompt, but it should not be equated with verified removal of the text-conditioning route. [PDF p. 5; code: `embeddings/models.py`, `extract_musicgen_decoder_lm_emb`]

For each handcrafted feature matrix, concatenate temporal means and standard deviations of the original features and first- and second-order differences. Aggregate handcrafted features concatenate the mel, MFCC, and chroma descriptors. A temporally pooled descriptor need not preserve explicit event order, even if it predicts a progression label. [PDF p. 5; final sentence is repository inference]

### Probes and selection

Each concept has its own probe. Six tasks use cross-entropy classification and accuracy; tempo uses MSE regression and R². Classification uses a nominal 70/15/15 train/validation/test partition; released code randomly splits rows, with no instrument-, root-, or soundfont-disjoint guarantee. Tempo is intended to train on the middle 70% of BPM values and evaluate on the extremes. [PDF p. 4]

Codec/handcrafted probes search normalization on/off, linear versus one 512-unit hidden layer with ReLU, batch size 64/256, learning rate 1e-5/1e-4/1e-3, dropout 0.25/0.5/0.75, and L2 off/1e-4/1e-3. Decoder probes fix normalization on, a 512-unit hidden layer, batch size 64, learning rate 1e-3, dropout 0.5, and no L2, then select the layer. Adam is used. Thus the headline decoder results are not demonstrations of linear separability, and comparison budgets differ between feature families. [PDF pp. 4–5]

## 4. Key Results and Benchmarks

**All values below are paper-reported, not independently reproduced. The implementation discrepancies in Section 5 may affect their validity.** Table 2 describes validation-based hyperparameter selection and per-concept layer selection; the released runner does not establish a separate test-scoring path.

| Representation | Notes | Intervals | Scales | Chords | Progressions | Tempo R² | Meter | Mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jukebox LM | .951 | .995 | .978 | .997 | .971 | .993 | 1.000 | .984 |
| MusicGen Small LM | .897 | .995 | .949 | .990 | .942 | .969 | .911 | .950 |
| MusicGen Medium LM | .851 | .983 | .863 | .989 | .870 | .956 | .883 | .914 |
| MusicGen Large LM | .866 | .972 | .905 | .989 | .901 | .965 | .905 | .929 |
| MusicGen codec | .729 | .965 | .383 | .879 | .330 | .947 | .677 | .701 |
| Mel spectrogram | .712 | .995 | .897 | .988 | .723 | .785 | .827 | .847 |
| MFCC | .467 | .822 | .370 | .863 | .872 | .923 | .688 | .715 |
| Chroma | .954 | .820 | .989 | .994 | .869 | .847 | .672 | .878 |
| Aggregate handcrafted | .941 | .997 | .972 | .992 | .868 | .947 | .833 | .936 |

[PDF p. 6, Table 2; visually verified transcription]

The mean combines accuracy and R² and is not a pooled success rate. Jukebox has the highest reported mean, but handcrafted aggregate leads interval accuracy, and chroma leads notes and modes. MusicGen Small's mean exceeds Medium and Large; handcrafted aggregate lies between Small and Large. The codec is weaker on scales and progressions, but that comparison also changes feature dimension and temporal context, so the table alone does not isolate training-objective effects.

Figure 2 plots mean probing metrics against **percentage through decoder layers**, not an equal absolute layer count. The visually checked curves show a marked early trough for Medium/Large, later recovery, and final-layer declines; Small is comparatively stable and Jukebox remains high through much of its later depth. These are cross-concept averages, not proof that every concept peaks at the same layer. [PDF p. 5]

The authors suggest that isolated notes may be less common in training music and that smaller models may encode concepts more efficiently. These are hypotheses, not controlled explanations established by the experiments. No uncertainty intervals, repeated-seed score distributions, listening study, or causal intervention result accompanies the headline table. [PDF p. 6]

## 5. Limitations and Future Work

### Discrepancies that may affect result validity

Inspection concerns commit `4f222359e750ec55425c12809c1a0358b74fce49`. Its connection to the original result-producing runs is unknown; the findings do not prove that published numbers are wrong or quantify their bias.

1. **Validation-dependent normalization:** the training loop creates an unfitted scaler and evaluates validation at step zero. `eval_logits` catches `NotFittedError` and fits that scaler on validation features; training then updates the same scaler. This exposes validation feature statistics to preprocessing, without demonstrating label leakage into gradients. The actual function's control flow was checked with explicit test doubles, not full numerical training. [Code: `probe/probes.py` lines 341–377, 429, 450–455; [pinned source](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L340)]
2. **Tempo split is not strictly value-disjoint:** cuts at row indices 603 and 3,421 in 4,025 sorted rows split groups of 25 samples/BPM. Training and combined holdout share 74 and 186 BPM. A standard-library reproduction confirmed these boundaries. Most extreme BPMs remain unseen; the flaw is bounded but contradicts a strictly unseen-value interpretation. [PDF p. 4; [split implementation](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L192)]
3. **Independent test scoring is not demonstrated by the release:** `start()` loads data, trains, and returns; internal evaluation and metric persistence use validation. This is a reproducibility gap, not proof that no external test evaluation occurred. Table 2 already mentions validation-based selection. [Code: [runner](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/main.py), [saved metrics](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L578)]
4. **Stimulus timing:** the released progression generator uses two beats per chord, rather than the PDF's quarter-note description. Published audio was not measured to identify which implementation it follows. [PDF p. 4; [generator](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/dataset/synthetic/chord_progressions.py#L75)]
5. **Sweep direction metadata:** grid sweeps say `minimize` for accuracy/R², while training maximizes its early-stopping score. This does not by itself establish wrong selection in the final table. [Code: [sweep definitions](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probe_config.py#L34)]

A defensible verification would map results to code/run versions, fit and freeze preprocessing on training data only, split tempo by unique BPM, select layers/probes on validation, and score once on independent test data. Report per-task changes and uncertainty rather than assuming these issues either explain or leave unchanged the model ranking.

### Scientific scope

- **Decodability is not causality:** a separately trained MLP can recover information that the generator does not use as a reason for any particular output. There are no activation interventions, concept erasures, causal mediation tests, or explanation-utility studies.
- **Synthetic isolation is not ecological validity:** single-soundfont, controlled clips are not polyphonic classical works with expressive timing, ambiguous harmony, voice leading, or long-form dependencies. The benchmark tests elementary categories, not complete Western theory or other musical traditions.
- **Shortcut control is incomplete:** balanced instrument combinations help, but random row splits do not show transfer to unseen instruments, soundfonts, keys, or musical contexts. Predefined progression recognition need not require abstract harmonic-function reasoning.
- **Probe capacity and feature dimensions differ:** successful nonlinear classification is neither proof of linearly accessible concepts nor a controlled model-size scaling result. Unequal feature dimensions and per-layer selection complicate comparisons.
- **Authored next steps:** harder entangled/compositional concepts and language-side probing for better control. **Repository extension:** add nuisance-disjoint evaluation, causal interventions during generation, and musician tasks measuring diagnosis/repair, separately from musical quality. [PDF p. 6; extension is repository inference]

## 6. Related Work

The paper's background contrasts high-level audio-representation probes with its elementary concept benchmark and discusses language-model probing as motivation. Those cited background papers are not separately ingested here; this digest does not adopt them as independently read evidence. [PDF pp. 1–2, 7–8]

- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] supplies explicit MIDI attribute structure; SynTheory instead tests whether named concepts can be recovered from audio-model states. This is a repository comparison, not a comparison reported by Wei et al.
- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] uses score hierarchy and a learned preference evaluator; high evaluator scores and high concept-probe scores answer different questions and neither establishes causal explanations.
- [[concepts/music-theory-probing]] defines the recoverability claim, protocol, and evidence boundaries.
- [[concepts/music-domain-inductive-biases]] separates musical structure, inductive bias, constraints, and faithful explanation.

## 7. Glossary

- **Probe:** a supervised predictor trained on fixed representations to measure accessible target information.
- **Pitch class:** pitch modulo octave; the note task predicts one of twelve classes.
- **Mode:** a scale's interval pattern relative to its root; here one of seven diatonic modes.
- **Chord quality:** major, minor, diminished, or augmented triad structure, distinct from root and inversion.
- **Mean pooling:** averaging representations over time; it compresses temporal information rather than explicitly decoding a sequence of musical events.
- **R²:** regression fit relative to a constant-mean reference; it is not classification accuracy.
- **Value-disjoint split:** no target BPM value appears in both training and holdout, even when each value has multiple rendered examples.
- **Feature-distribution leakage:** held-out feature statistics influence fitted preprocessing; distinct from direct exposure of held-out target labels to training.
- **Causal faithfulness:** an explanation identifies factors that actually influence the model's decision, rather than merely correlate with a decodable label.
