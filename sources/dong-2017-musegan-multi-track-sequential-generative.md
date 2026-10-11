---
title: "MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment"
authors: "Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang, and Yi-Hsuan Yang"
year: 2017
doi: 10.48550/arXiv.1709.06298
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/dong-2017-musegan-multi-track-sequential-generative.pdf"
pdf_filename: dong-2017-musegan-multi-track-sequential-generative.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

They report that the systems can generate coherent four-bar phrases from scratch and can generate four additional tracks conditioned on one human-provided track.

## 1. Document Information

- **Canonical source:** arXiv `1709.06298v2`; official PDF preserved as `dong-2017-musegan-multi-track-sequential-generative.pdf`.
- **Full-paper evidence:** delegate digest `del_mv415ez7_l9fj.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### MuseGAN digest

**Paper:** Dong et al., “MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment,” arXiv:1709.06298v2, 24 Nov 2017.  
**Materials inspected:** full 13-page PDF and extracted text at `/tmp/paper-digest/1709.06298v2.{pdf,txt}`. No files were modified.

### 1. Core contribution

**Author claim — Abstract, Introduction, PDF pp. 1–2:** MuseGAN is a WGAN-GP-based framework for generating short, multi-track, polyphonic symbolic music. It models:

- five tracks: bass, drums, guitar, piano, strings;
- local musical structure at the bar level;
- temporal structure across four-bar phrases;
- inter-track dependencies;
- track-conditional generation for accompaniment.

The authors present three alternative models for inter-track dependency:

1. **Jamming model**
2. **Composer model**
3. **Hybrid model**

They report that the systems can generate coherent four-bar phrases from scratch and can generate four additional tracks conditioned on one human-provided track.

**Interpretation:** The major conceptual contribution is not long-form composition, but factorizing multi-track generation into:

```text
time-independent track/style variables
+ time-dependent shared/private variables
+ bar-level convolutional generators
```

This factorization remains relevant to structured symbolic generation, although the representation and evaluation are now substantially outdated.

---

### 2. Data and representation

#### Piano-roll representation

**Proposed Model → Data Representation, PDF p. 2**

An `M`-track bar is represented as:

```text
x ∈ {0,1}^{R × S × M}
```

where:

- `R = 96` time steps per bar;
- `S = 84` retained pitches after filtering;
- `M = 5` tracks.

A four-bar phrase therefore has shape:

```text
4 × 96 × 84 × 5
```

The representation is binary. For non-drum tracks, a one-step rest is inserted between notes to distinguish successive notes of the same pitch from a sustained note. Notes shorter than two time steps are dropped. Drums encode onsets only.

Generation uses `tanh` outputs thresholded at zero. During rendering, outputs are additionally quantized to sixteenth notes.

**Limitation:** This discards or weakly represents velocity, expressive timing, articulation, pedal, instrument identity, and exact duration. The one-step-rest convention also makes note identity partly dependent on preprocessing assumptions.

#### Dataset

**Implementation → Dataset/Data Preprocessing, PDF pp. 4–5**

Starting sources:

- Lakh MIDI Dataset: **176,581 unique MIDI files**;
- LPD: reported as **173,997 unique multi-track piano-rolls**;
- LPD-matched: **45,129 MIDIs** matched to the Million Song Dataset.

Preprocessing:

1. Merge sparse/similar instrument tracks into five families:
   - bass
   - drums
   - guitar
   - piano
   - strings
2. Restrict to files with high matching confidence, Rock metadata, and 4/4 meter.
3. Segment using structural-boundary detection; use four bars as the phrase length.
4. Discard pitches below C1 or above C8.

After preprocessing:

- LPD-5-matched: **30,887 multi-track piano-rolls**;
- training phrases: **50,266 four-bar phrases**.

The authors explicitly acknowledge that merging tracks introduces noise, but report that it worked better than retaining empty tracks.

**Author limitation — PDF p. 4:** Because there is no reliable melody/accompaniment labeling in the source MIDI, the authors cannot divide tracks into melody, rhythm, and drum roles as some prior work did.

**Interpretation:** The data pipeline strongly narrows the task to quantized, four-bar, Rock-like accompaniment patterns. Results should not be generalized to arbitrary genres, meters, orchestration, or long-range song structure.

---

### 3. The three models

#### 3.1 Jamming model

**Modeling the Multi-track Interdependency, PDF p. 3; Figure 3(a)**

- One generator per track.
- One private random vector `z_i` per track.
- One discriminator per track.
- Tracks are generated independently.

The design models musicians improvising separately.

**Expected advantage:** Good track-specific statistics.  
**Expected weakness:** Weak cross-track harmonic coordination.

#### 3.2 Composer model

**PDF p. 3; Figure 3(b)**

- One generator produces all tracks jointly.
- One shared random vector `z`.
- One discriminator evaluates the complete multi-track object.

The shared latent is described as analogous to a composer’s global intention.

**Expected advantage:** Stronger inter-track coordination.  
**Expected weakness:** Less flexibility; all tracks share the same architecture and generation pathway.

#### 3.3 Hybrid model

**PDF p. 3; Figure 3(c)**

Each track generator receives:

- a shared inter-track vector `z`;
- a private intra-track vector `z_i`.

There is one discriminator evaluating all tracks collectively.

The paper uses:

```text
(K_temp, K_bar) = (1,1) for jamming
                 (1,5) for composer
                 (5,1) for hybrid
```

in the architecture table.

**Expected advantage:** Shared information coordinates tracks while private inputs preserve track-specific variation. It also permits different architectures per track.

**Author result:** The hybrid model is generally preferred by professional listeners for both from-scratch and conditional generation, and by non-professionals for from-scratch generation.

---

### 4. Temporal models

#### From-scratch generation

**Modeling the Temporal Structure, PDF p. 3; Figure 4(a); Equation (3)**

A temporal generator `G_temp` maps a random vector to a sequence of latent vectors:

```text
z → {z^(t)}_{t=1}^T
```

A bar generator `G_bar` then converts each latent vector into one bar:

```text
G(z) = {G_bar(G_temp(z)^(t))}_{t=1}^T
```

The temporal generator is intended to encode phrase-level evolution, while the bar generator handles within-bar patterns.

#### Track-conditional generation

**PDF pp. 3–4; Figure 4(b); Equation (4)**

Given a human-provided sequence for one track, the model generates the remaining tracks bar by bar.

An encoder `E` maps the condition track into a low-dimensional inter-track representation:

```text
y^(t) → E(y^(t))
```

The conditional bar generator receives the condition and time-dependent noise.

In the main experiments, the **piano track** is used as the condition and the other four tracks are generated. Appendix Figure 13 instead demonstrates conditioning on the strings track.

**Important limitation:** This is accompaniment generation, not source-preserving editing. The condition is retained as an input/reference, but the paper does not formulate arbitrary-track preservation, masked inpainting, note-level repair, or identity constraints.

---

### 5. Architecture and training

**Appendix B, PDF p. 9; Table 4**

- `G_temp`: two 1-D transposed-convolution layers along the inter-bar time axis.
- `G_bar`: five 1-D transposed-convolution layers along intra-bar time, followed by two layers along pitch.
- `D`: five 1-D convolutional layers plus fully connected layers.
- `E`: reverse-style convolutional encoder with skip connections.
- Encoder filters are constrained to 16 to compress inter-track information.
- Total random-vector dimensionality: **128**.
- Optimizer: Adam.
- Learning rate: **0.001**.
- `β1 = 0.5`, `β2 = 0.9`.
- Generator, and encoder when applicable, updated once for every five discriminator updates.
- Batch normalization applied to generators.
- Training time: **under 24 hours per model on a Tesla K40m**.

The adversarial objective is WGAN-GP, motivated by improved stability and reduced mode collapse relative to the original GAN objective.

**Author-reported failure:** The ablated composer model without batch normalization “barely learns anything” and is used as a reference baseline.

---

### 6. Metrics

**Objective Metrics for Evaluation, PDF p. 5**

#### Intra-track metrics

- **EB — Empty Bars:** percentage of empty bars.
- **UPC — Used Pitch Classes:** number of distinct pitch classes per bar, from 0 to 12.
- **QN — Qualified Notes:** percentage of notes at least three time steps long; intended to detect excessive fragmentation.
- **DP — Drum Pattern:** percentage of drum notes belonging to common 8- or 16-beat Rock patterns.

#### Inter-track metric

- **TD — Tonal Distance:** tonal distance between two tracks. Larger values imply weaker harmonic relation.

The authors compare generated statistics with training-data statistics. These are distributional proxies, not direct measures of musical quality, source preservation, structural similarity, or repair correctness.

---

### 7. Objective results

**Objective Evaluation, Tables 1–2, PDF p. 6**

The authors generate **20,000 bars per model**.

#### Table 1: intra-track metrics

Columns are:

```text
EB: bass, drums, guitar, piano, strings
UPC: bass, guitar, piano, strings
QN: bass, guitar, piano, strings
DP: drums
```

Training data:

```text
EB   8.06, 8.06, 19.4, 24.8, 10.1
UPC  1.71, 3.08, 3.28, 3.38
QN   90.0, 81.9, 88.4, 89.6
DP   88.6
```

From scratch:

```text
Jamming:
EB   6.59, 2.33, 18.3, 22.6, 6.10
UPC  1.53, 3.69, 4.13, 4.09
QN   71.5, 56.6, 62.2, 63.1
DP   93.2

Composer:
EB   0.01, 28.9, 1.34, 0.02, 0.01
UPC  2.51, 4.20, 4.89, 5.19
QN   49.5, 47.4, 49.9, 52.5
DP   75.3

Hybrid:
EB   2.14, 29.7, 11.7, 17.8, 6.04
UPC  2.35, 4.76, 5.45, 5.24
QN   44.6, 43.2, 45.5, 52.0
DP   71.3
```

Conditional generation:

```text
Jamming:
EB   4.60, 3.47, 13.3, –, 3.44
UPC  2.05, 3.79, –, 4.23
QN   73.9, 58.8, –, 62.3
DP   91.6

Composer:
EB   0.65, 20.7, 1.97, –, 1.49
UPC  2.51, 4.57, –, 5.10
QN   53.5, 48.4, –, 59.0
DP   84.5

Hybrid:
EB   2.09, 4.53, 10.3, –, 4.05
UPC  2.86, 4.43, –, 4.32
QN   43.3, 55.6, –, 67.1
DP   71.8
```

#### Authors’ interpretation

- Jamming performs best on many intra-track metrics because each generator specializes in one track.
- Composer and hybrid produce lower tonal distances than jamming, indicating stronger cross-track harmonic relations.
- Generated music uses more pitch classes and has substantially fewer qualified notes than the training data.
- The authors attribute fragmentation partly to thresholding continuous `tanh` outputs into binary piano-rolls.
- Composer and hybrid have problematic empty-drum-bar rates: **28.9%** and **29.7%** respectively in from-scratch generation.

#### Table 2: tonal distance

Training data:

```text
B-G 1.57   B-S 1.58   B-P 1.51
G-S 1.10   G-P 1.02   S-P 1.04
```

Training data after random track pairing:

```text
1.59, 1.59, 1.56, 1.14, 1.12, 1.13
```

From-scratch:

```text
Jamming   1.56, 1.60, 1.54, 1.05, 0.99, 1.05
Composer  1.37, 1.36, 1.30, 0.95, 0.98, 0.91
Hybrid    1.34, 1.35, 1.32, 0.85, 0.85, 0.83
```

Conditional:

```text
Jamming   1.51, 1.53, 1.50, 1.04, 0.95, 1.00
Composer  1.41, 1.36, 1.40, 0.96, 1.01, 0.95
Hybrid    1.39, 1.36, 1.38, 0.96, 0.94, 0.95
```

**Interpretation:** The lower TD values for composer/hybrid show that shared latent information can impose cross-track harmonic coupling. However, lower TD than the data is not automatically better: it may indicate over-smoothed or overly correlated generation.

---

### 8. Figures and qualitative evidence

- **Figure 1, p. 1:** hierarchical structure of music, motivating bar- and phrase-level modeling.
- **Figure 2, p. 2:** five-track piano-roll representation.
- **Figure 3, p. 3:** jamming, composer, and hybrid architectures.
- **Figure 4, p. 3:** from-scratch and track-conditional temporal models.
- **Figure 5, p. 4:** complete MuseGAN system, combining shared/private static and temporal random vectors.
- **Figure 6, p. 5:** dataset preparation and cleansing pipeline.
- **Figure 7, p. 6:** composer and hybrid examples from scratch.
- **Figure 8, p. 7:** training evolution from noise to recognizable pitch ranges, bass clusters, and longer chord-like notes.
- **Figure 9, p. 7:** discriminator loss, UPC, and QN during training.
- **Figure 10, p. 10:** training-data examples.
- **Figures 11–12, pp. 11–12:** composer and hybrid generated piano-rolls, before and after binarization.
- **Figure 13, p. 13:** composer model conditioned on a strings track.

**Author observations from Figure 7, p. 6:**

- tracks often share a scale;
- some samples contain chord-like intervals;
- bass is often low-pitched and mostly monophonic;
- drums often show 8- or 16-beat patterns;
- guitar, piano, and strings tend to play chords with overlapping pitches.

**Interpretation:** These are recognizable genre-level regularities, not evidence of reliable arrangement, long-range form, or intentional harmonic planning.

---

### 9. User study

**User Study, Table 3, PDF p. 7**

- **144 listeners** recruited online through the authors’ social circles.
- **44** classified as “pro users.”
- Each listener heard nine clips in random order.
- Each clip contained three generated four-bar phrases.
- Ratings used a five-point Likert scale:
  - harmonious;
  - rhythmic;
  - musically structured;
  - coherent;
  - overall rating.

Table 3 reports mean ratings in the order:

```text
H, R, MS, C, OR
```

#### From scratch

```text
Non-professional
Jamming   2.83, 3.29, 2.88, 2.84, 2.88
Composer  3.12, 3.36, 2.95, 3.13, 3.12
Hybrid    3.15, 3.33, 3.09, 3.30, 3.16

Professional
Jamming   2.89, 3.44, 2.97, 3.01, 3.06
Composer  2.70, 3.29, 2.98, 2.97, 2.86
Hybrid    2.78, 3.34, 2.93, 2.98, 3.01
```

#### Conditional

```text
Non-professional
Jamming   2.31, 3.05, 2.48, 2.49, 2.42
Composer  2.66, 3.13, 2.68, 2.63, 2.73
Hybrid    2.92, 3.25, 2.81, 3.00, 2.93

Professional
Jamming   2.44, 3.32, 2.67, 2.72, 2.69
Composer  2.35, 3.21, 2.59, 2.67, 2.62
Hybrid    2.49, 3.29, 2.71, 2.73, 2.70
```

#### Authors’ conclusion

- Hybrid is preferred by professionals for both scenarios.
- Hybrid is preferred by non-professionals for from-scratch generation.
- Jamming is preferred by non-professionals for conditional generation.
- Composer and hybrid receive higher harmony ratings than jamming for from-scratch generation.

#### Limitations

The paper does not report confidence intervals, statistical significance tests, listener-level random effects, clip-level balancing details, or comparisons against a human-composed baseline. The clips are short and all come from the same narrow preprocessing regime.

---

### 10. Artifacts

**Abstract, Introduction p. 1, footnote, Appendix C**

The authors state that the project website provides:

- source code;
- LPD and metadata;
- conversion utilities;
- rendered audio samples;
- generated piano-roll examples.

URL:

```text
https://salu133445.github.io/musegan/
```

The paper does not provide modern experiment-tracking details such as fixed seeds, formal train/validation/test splits, checkpoint hashes, confidence intervals, or automated artifact versioning.

---

### Relevance to source-preserving symbolic mashups and repair

### Directly useful ideas

1. **Shared/private factorization**  
   The hybrid model is a useful conceptual template for separating:
   - source-preserving information;
   - track-specific variation;
   - shared harmonic/structural information.

2. **Track-conditional completion**  
   Conditioning on one track and generating the others is an early form of accompaniment completion. It can be extended to:
   - bass-conditioned arrangement;
   - drum-conditioned arrangement;
   - vocal-conditioned accompaniment;
   - partial multi-track completion.

3. **Bar-level structured generation**  
   Treating bars as units makes constraints, editing, and evaluation easier than unrestricted event generation.

4. **Cross-track metrics**  
   Tonal distance, empty-bar rate, pitch-class usage, note fragmentation, and drum-pattern statistics are useful diagnostic signals for repair systems.

### What MuseGAN does not solve

**Interpretation grounded in the method and reported experiments:**

- It does not preserve the exact timing, pitch, duration, or expressive characteristics of source tracks beyond the supplied condition.
- It does not perform masked note-level inpainting.
- It does not distinguish source material from generated material.
- It does not optimize edit minimality.
- It does not guarantee that non-edited tracks remain unchanged.
- It has no voice-leading, chord-symbol, key, meter, or phrase-boundary constraints.
- It generates only four-bar phrases from scratch.
- It does not evaluate mashup compatibility across unrelated songs.
- It does not evaluate repair accuracy against known corrupted originals.
- Its binary piano-roll representation is poorly suited to expressive or production-oriented MIDI repair.

For source-preserving mashups, the strongest limitation is that accompaniment generation is **conditional synthesis**, not **constrained completion**.

---

### Concrete modern research ideas

### 1. Source-preserving masked MuseGAN

Replace unconditional generation with a masked completion objective:

```text
input = original multi-track piano-roll + edit mask
output = repaired/completed multi-track piano-roll
loss = reconstruction on locked cells
     + adversarial realism
     + cross-track harmony
     + edit sparsity
```

Require exact equality on all locked source events.

### 2. Hybrid latent separation

Adapt the hybrid model into explicit latent variables:

```text
z_source       source identity/style
z_structure    harmony, groove, phrase form
z_track_i      instrument-specific realization
z_edit         controlled repair/mashup changes
```

Test whether the model can alter one track while preserving source fingerprints in all others.

### 3. Multi-track conditional diffusion or transformer

Modernize the convolutional GAN with:

- masked diffusion for symbolic inpainting;
- hierarchical Transformer blocks;
- bar/beat/event positional representations;
- cross-track attention;
- explicit conditioning on key, meter, chord, tempo, and section labels.

MuseGAN’s shared/private architecture can serve as an ablation baseline.

### 4. Source-aware mashup compatibility model

Before generation, estimate compatibility between source tracks using:

- key and mode;
- chord progression;
- beat grid and tempo;
- rhythmic density;
- tonal distance;
- register overlap;
- phrase-boundary alignment.

Use these estimates to condition generation and to reject incompatible outputs.

### 5. Repair-specific benchmark

Construct synthetic corruption pairs:

```text
clean MIDI → delete/mask/shift/shorten/corrupt events → corrupted MIDI
```

Evaluate:

- exact event recovery;
- pitch/duration F1;
- timing deviation;
- locked-event preservation;
- edit distance;
- tonal-distance change;
- groove preservation;
- human preference.

This directly addresses a gap in MuseGAN’s evaluation.

### 6. Better preservation metrics

Extend MuseGAN’s metrics with:

- source-event preservation rate;
- unedited-track identity score;
- masked-region recovery F1;
- voice-leading continuity;
- chord-conditioned harmonic consistency;
- phrase-level repetition and contrast;
- instrumentation and register preservation;
- perceptual similarity between original and repaired renderings.

### 7. Human study redesign

Use a within-subject study comparing:

- original;
- corrupted;
- MuseGAN-style generation;
- modern masked completion;
- human repair.

Report confidence intervals and mixed-effects significance tests. Separate judgments of realism, musicality, preservation, repair correctness, and amount of unwanted change.

---

### Bottom line

**Author-supported conclusion:** MuseGAN demonstrates that shared/private latent variables plus temporal convolution can generate short, recognizable, multi-track Rock piano-rolls, and that conditional generation can provide rudimentary accompaniment.

**Interpretive conclusion for this research:** Its most valuable legacy is the explicit decomposition of multi-track generation into shared inter-track structure and private track structure. For source-preserving mashups and repair, MuseGAN should be treated as an architectural and diagnostic baseline—not as a complete preservation method. The necessary next step is masked, source-locked, edit-minimal conditional generation with evaluation centered on preservation and repair correctness rather than only distributional musicality.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `generation-and-planning`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
