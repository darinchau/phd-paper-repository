---
title: "A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis"
authors: "Tina Raissi, Nhan Phan, Chenxiao Wang, and Mikko Kurimo"
year: 2026
doi: 10.48550/arXiv.2609.30075
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/raissi-2026-a-native-reference-phone-class.pdf"
pdf_filename: raissi-2026-a-native-reference-phone-class.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper addresses interpretable automatic assessment of second-language pronunciation. Existing systems often output holistic proficiency scores without identifying acoustic-phonetic causes. The proposed method estimates pronunciation deviation without:

## 1. Document Information

- **Canonical source:** arXiv `2609.30075v1`; official PDF preserved as `raissi-2026-a-native-reference-phone-class.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41ns1u_lw8s.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper identification

- **Title:** *A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis*
- **Authors:** Tina Raissi, Nhan Phan, Chenxiao Wang, Mikko Kurimo
- **Affiliation:** Department of Information and Communications Engineering, Aalto University, Espoo, Finland
- **Version:** arXiv:2609.30075v1, 24 September 2026
- **PDF length:** 5 pages. Pages 1–4 contain the paper; page 5 is references. There are **six tables, no figures, and no appendices**.

### 1. Problem and contribution

**Author claim — Abstract, p. 1; §§1–2, pp. 1–2:**  
The paper addresses interpretable automatic assessment of second-language pronunciation. Existing systems often output holistic proficiency scores without identifying acoustic-phonetic causes. The proposed method estimates pronunciation deviation without:

- human pronunciation labels,
- read-aloud prompts,
- matched native/L2 recordings of the same text.

It does, however, require phone transcripts and phone-level segmentation through forced alignment.

**Core contribution:** construct a native-reference geometric space from self-supervised speech representations, then compare each learner’s context-dependent phone-class coordinates against native coordinates.

### 2. Method

#### Native reference geometry

**§2, p. 2:**

1. Extract frame-level representations \(H^\ell \in \mathbb{R}^{T \times D}\) from a self-supervised speech encoder.
2. Define context-dependent phone classes:
   - diphones: center phone plus left context;
   - triphones: center phone plus left and right context.
3. For each phone class \(p\), compute a centroid:

\[
\mu(p)=\frac{1}{|T_p|}\sum_{t\in T_p}h_t .
\]

4. Stack native centroids into \(M_{\text{nat}}\), subtract the global native mean, and compute rank-\(K\) SVD:

\[
\bar M_{\text{nat}}\approx U\Sigma V^\top.
\]

5. Use \(V\) as the native-reference basis and \(C_{\text{nat}}=U\Sigma\) as native phone-class coordinates.
6. For learner utterance \(r\):

\[
C^{r}_{L2}=(M^{r}_{L2}-\mathbf{1}\bar\mu_{\text{nat}}^\top)V.
\]

7. Compare only phone classes shared by native and learner speech:

\[
P_r^\star=P_{\text{nat}}\cap P^r_{L2}.
\]

8. Compute Euclidean, cosine, or diagonal Mahalanobis distance for each shared class and aggregate those distances at utterance level.

Two centroid strategies are tested:

- **center-unit averaging:** frames of the central phone only;
- **full-unit averaging:** frames from the full context-dependent unit.

The authors explicitly state that they do not train a predictor from distances to proficiency scores; they test whether raw distances correlate monotonically with human ratings (§2.2, p. 2).

### 3. Data and experimental protocol

**§3.1, p. 2:**

#### Native-reference corpora

Four hours from each:

- **TIMIT:** 630 speakers; ground-truth phone segmentation.
- **LBS-4h:** 4-hour LibriSpeech subset; 630 sampled speakers.
- **UME-ERJ native:** 20 speakers; controlled read sentences.

#### L2 evaluation data

- **Speak and Improve Corpus 2025 (S&I):** Train and Dev partitions; spontaneous English L2 speech.
- **UME-ERJ learner subset:** read English sentences by Japanese learners, evaluated for pronunciation.

S&I scores are averaged over four proficiency-evaluation tasks. UME-ERJ scores use the paper’s sentence-level aggregation procedure.

#### Models and alignment

- WavLM Base+:
  - layer 6 for S&I;
  - layer 12 for UME-ERJ.
- ARPAbet phones, stressed phones merged: 39 phones plus silence.
- Non-TIMIT alignments use a Conformer-based factored HMM trained on the Loquacious subset.
- Lhotse is used for data preparation; RASR for forced alignment.
- Best configuration:
  - rank 32;
  - S&I: triphones with full-unit averaging;
  - UME-ERJ: diphones with center-unit averaging.

**Methodological caution — §3.1, p. 2:**  
The paper says configuration choices were selected using S&I Train and the UME-ERJ learner set, then reports final results on S&I Dev and UME-ERJ learner data. Unless an unreported split exists, UME-ERJ learner data appear to be used both for selection and final evaluation.

### 4. Results

#### Baselines

**Tables 1–2, p. 3:**

Non-acoustic controls correlate substantially with S&I proficiency:

- word count: \(\rho=0.55\) Train, \(0.57\) Dev;
- speaking rate: \(0.54\), \(0.52\);
- matched diphone coverage: \(0.60\), \(0.62\);
- matched triphone coverage: \(0.60\), \(0.62\).

Alignment-derived silence ratio is even stronger:

- \(\rho=-0.60\) S&I Train;
- \(\rho=-0.57\) S&I Dev.

A raw encoder DTW baseline reaches \(\rho=-0.50\) on UME-ERJ but requires matched native and learner recordings of the same text, so it is unsuitable for spontaneous S&I speech.

#### Boundary robustness

**Table 3, p. 3:**

For triphone/full-unit averaging, cosine-distance correlation changes from:

- \(-0.56\) at 0 ms perturbation;
- \(-0.51\) at 60 ms;
- \(-0.34\) at 120 ms.

Triphones and full-unit averaging are more robust than diphones and center-unit averaging.

#### Native corpus and distance metric

**Table 4, p. 3:**

Best correlations:

- S&I Train with LBS-4h and cosine distance: \(\rho=-0.56\).
- UME-ERJ learner with LBS-4h and diagonal Mahalanobis distance: \(\rho=-0.28\).

The direction is consistently negative across TIMIT, LBS-4h, and UME-ERJ native references, although UME-ERJ native is not evaluated as the UME-ERJ test reference in this table.

#### SVD versus full and random projections

**Table 5, p. 4:**

For S&I Train:

- Euclidean: full \(-0.50\), random \(-0.46\), SVD \(-0.52\);
- Mahalanobis: full \(-0.44\), random \(-0.46\), SVD \(-0.51\);
- cosine: full \(-0.58\), random \(-0.53\), SVD \(-0.56\).

For UME-ERJ:

- Euclidean: full \(-0.28\), random \(-0.26\), SVD \(-0.27\);
- Mahalanobis: full \(-0.29\), random \(-0.26\), SVD \(-0.28\);
- cosine: full \(-0.19\), random \(-0.11\), SVD \(-0.13\).

The authors report reducing computation from 2,520 seconds to 8 seconds, approximately a **315× speedup** (§3.4, p. 4).

#### Final evaluation

**Table 6; §3.5, p. 4:**

| Evaluation | Pearson \(r\) | Raw Spearman \(\rho\) | Partial \(\rho\) | 95% CI for raw \(\rho\) |
|---|---:|---:|---:|---:|
| S&I Dev | −0.53 | −0.53 | −0.19 | [−0.56, −0.49] |
| UME-ERJ learner | −0.37 | −0.34 | −0.27 | [−0.37, −0.31] |

The partial correlations control for matched phone-class coverage and silence ratio. The authors interpret the remaining negative associations as evidence that the geometry captures information beyond those factors.

They also report that:

- replacing self-supervised features with MFCCs substantially weakens correlations;
- using a single TIMIT dialect group has only a minor effect;
- all reported final correlations have bootstrap confidence intervals below zero.

### 5. Limitations

**Author-stated — §3.6, p. 4:**

1. S&I ratings are holistic. Pronunciation, fluency, and phone coverage are confounded.
2. UME-ERJ is pronunciation-specific but consists of short read sentences, producing few phone observations and potentially unstable centroids.
3. UME-ERJ average pairwise human-human Spearman correlation is only approximately \(0.50\).
4. Self-supervised representations may encode speaker identity, accent, recording conditions, and other non-phonetic factors.
5. The method still requires phone-level forced alignment and ASR transcripts.

**Additional assessment:**

- The method demonstrates correlation, not causal pronunciation diagnosis.
- SVD dimensions are not inherently human-interpretable phonetic attributes.
- There are no qualitative examples showing which phone classes or coordinates explain an individual score.
- The paper gives no utterance/speaker counts in the reported experiments.
- The apparent UME-ERJ configuration-selection/evaluation overlap weakens the claim of fully held-out generalization.

### 6. Artifact status

**Paper claim — §3.1, p. 2; reference [32], p. 5:**  
Source code is provided at:

<https://github.com/aalto-speech/native-L2-coordinate-geometry>

**Artifact audit beyond the PDF:** the repository is public and contains source modules and five example notebooks for feature extraction, phone averaging, native-reference construction, distance calculation, and evaluation.

However, the repository README states that:

- notebooks are examples, not turnkey reproduction scripts;
- paths, corpus/split names, alignments, model layers, and outputs require adaptation;
- audio, complete Lhotse manifests, feature matrices, and most intermediate pickles are absent;
- UME-ERJ data are not included and require consortium access;
- no software license is listed in the repository metadata.

**Conclusion:** code is available, but the artifact is not a self-contained reproduction package.

### 7. Relevance to explainable generative music

#### Direct relevance

**Interpretation:** The paper is not about music generation, symbolic music, mashups, or repair. Its direct technical object is continuous speech representation and pronunciation assessment.

Its useful transferable pattern is:

> construct a reference distribution from trusted source material, map a new realization into the same coordinate system, compare matched context-dependent units, and expose deviations as evidence.

#### Source-preserving mashups

A music analogue could use a source track as the reference corpus:

- event classes: note pitch interval, duration, metrical position, chord context, voice/instrument, local rhythmic context;
- source centroids: embeddings of intact source events or phrases;
- mashup coordinates: embeddings of corresponding events in the generated/remixed output;
- deviations: per-event distance from the source-reference geometry.

This could distinguish:

- acceptable stylistic transformation;
- source identity loss;
- accidental melodic or rhythmic distortion;
- violations of instrument/voice roles.

Unlike the paper’s native reference, a music system should preserve explicit source provenance rather than treating the reference as a generic population average.

#### Repair

For repair, use the geometry as an anomaly/evidence model:

1. identify a suspicious event or phrase;
2. compare it with source-conditioned context classes;
3. rank candidate repairs by minimizing reference-space deviation;
4. enforce hard musical constraints such as meter, harmony, voice leading, and note-range limits;
5. return a per-event explanation: changed note, context class, reference coordinate deviation, and constraint satisfied.

#### Explainability caveat

The paper’s SVD coordinates provide compact evidence but not semantic explanations. For music, SVD axes should be supplemented with probes or controlled interventions mapping axes to interpretable attributes such as pitch contour, syncopation, harmonic tension, density, or timbral role.

### 8. Concrete research ideas

1. **Source-reference event geometry:** build SVD codebooks from intact symbolic tracks and measure source preservation in generated mashups.
2. **Geometry-guided repair:** optimize candidate note edits using reference distance plus symbolic constraints; compare against rule-based and language-model repair.
3. **Alignment robustness benchmark:** perturb beat/bar or note alignments, analogous to Table 3’s boundary shifts, and measure degradation.
4. **Coverage-aware evaluation:** report matched-event coverage, silence/rest density, instrumentation coverage, and partial correlations rather than relying only on global similarity.
5. **Interpretable coordinate probes:** learn sparse mappings from reference axes to musical attributes and test whether explanations remain stable across composers and genres.
6. **Human-grounded evaluation:** collect ratings for source identity, musicality, repair correctness, and explanation usefulness; report inter-rater agreement as the paper does for UME-ERJ.
7. **Artifact-first benchmark:** release source MIDI, corrupted MIDI, alignments, reference codebooks, per-event distances, and deterministic evaluation scripts—not merely notebooks and model code.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `other`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
