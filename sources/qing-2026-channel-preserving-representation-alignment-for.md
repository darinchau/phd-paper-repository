---
title: "Channel-Preserving Representation Alignment for EEG-to-Music Reconstruction"
authors: "Jiaxin Qing, Junwei Lu, and Lexin Li"
year: 2026
doi: 10.48550/arXiv.2606.04040
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/qing-2026-channel-preserving-representation-alignment-for.pdf"
pdf_filename: qing-2026-channel-preserving-representation-alignment-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I used `pdftotext -layout` on the supplied PDF/text and visually inspected all 22 rendered PDF pages, including Figures 1–3 and Tables 1–8. No files were edited.

## 1. Document Information

- **Canonical source:** arXiv `2606.04040v2`; official PDF preserved as `qing-2026-channel-preserving-representation-alignment-for.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zdkcf_xx3h.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

I used `pdftotext -layout` on the supplied PDF/text and visually inspected all 22 rendered PDF pages, including Figures 1–3 and Tables 1–8. No files were edited.

### Bibliography and version

- **Qing, Jiaxin; Lu, Junwei; Li, Lexin.** “Channel-Preserving Representation Alignment for EEG-to-Music Reconstruction.”
- **arXiv:2606.04040v2 [cs.SD]**, dated **26 September 2026**.
- Manuscript status: **Preprint**; no venue publication is stated.
- PDF: 22 pages: main paper pp. 1–10, references pp. 11–13, appendices pp. 14–22.

### Problem and contribution

The paper addresses reconstruction of naturalistic music from EEG recorded while subjects listen to music. Its central claim is that EEG information is distributed across electrodes:

- compressing electrodes can reduce estimation variance but discard music-relevant spatial information;
- preserving electrode identity increases representational capacity and estimation cost;
- channel dropout should therefore impose prediction consistency without destroying electrode identity.

The proposed **channel-preserving representation alignment** has three components:

1. **Per-electrode tokenization:** each electrode is separately partitioned into 50-sample temporal patches, preserving spatial identity before transformer aggregation.
2. **Multi-view self-distillation:** DINO-style teacher/student training uses two global temporal crops and eight local crops. The student receives 0.6 channel dropout; the teacher does not.
3. **Masked EEG–music alignment:** synchronized EEG/music crops are aligned with frozen CLAP using symmetric contrastive cross-entropy. EEG channel dropout is 0.2.

The aligned EEG representation is mapped through a ridge adapter into CLAP space and used to condition frozen AudioLDM.

**Anchors:** Abstract and §1, PDF pp. 1–2; pipeline Figure 1, p. 3; reconstruction Figure 2, p. 4.

### Method details

#### EEG encoder

- 125 EEG channels.
- Sampling rate after preprocessing/downsampling: 125 Hz.
- 50-sample temporal patches.
- 512-dimensional embeddings.
- 16 attention heads and 8 transformer layers.
- Eight-second SSL windows: 1,000 samples with stride 800.
- Alignment windows: one second, 125 samples.
- Alignment head:
  - 1-D convolution, 512 input/output channels, kernel 3, stride 1, no padding;
  - mean pooling;
  - 512→512 linear layer, GELU;
  - second 512→512 linear layer;
  - layer normalization.

**Anchors:** §3.1–§3.2, PDF pp. 3–4; implementation Tables 6–7, p. 21.

#### Self-distillation

- Two global crops: default fractions `[0.5, 0.9]`.
- Eight local crops: `[0.1, 0.5]`.
- Global crops are resized to 1,000 samples; local crops to 500.
- Student channel dropout: 0.6.
- Teacher channel dropout: 0.
- Student/teacher temperatures: 0.1/0.04.
- Teacher-logit center momentum: 0.9.
- Projection MLP: `512 → 2048 → 2048 → 256`, then normalized and mapped to 512 logits.
- Teacher is updated by cosine-scheduled EMA.

#### Paired alignment and reconstruction

- EEG and music receive synchronized random resized crops.
- Gaussian noise is applied; alignment noise level is 0.05.
- 0.2 of EEG channels are dropped after positional embedding.
- Frozen CLAP supplies audio targets.
- Ridge adapter regularization: **λ = 0.1**.
- Frozen AudioLDM uses 100 diffusion sampling steps.

### Theory

#### 1. Information retention versus estimation cost

The paper analyzes a simplified Gaussian regression setting:

\[
H\sim\mathcal N(0,I_p), \qquad V=W H+\epsilon,
\]

with noise energy \(\mathbb E\|\epsilon\|^2=\sigma^2\). It compares OLS using all \(p\) coordinates with OLS using a rank-\(r\) compressed representation.

**Proposition 4.1** gives:

\[
R_{\text{full}}
=\sigma^2\frac{n-1}{n-p-1},
\qquad
R_A
=(\sigma^2+b_A)\frac{n-1}{n-r-1},
\]

where \(b_A\) is the task-relevant energy discarded by compression.

Preservation is better exactly when:

\[
b_A>\frac{\sigma^2(p-r)}{n-p-1}.
\]

**Paper’s claim:** preservation is useful when discarded task information exceeds the additional finite-sample estimation cost.

**Interpretation:** this supports the architectural motivation, but it is not a performance guarantee for the actual transformer. The theorem assumes whitened Gaussian features, independent samples, fixed linear compression, zero-intercept OLS, and an unconstrained target.

**Anchors:** §4.1, PDF p. 5; proof and interpretation, Appendix A.1, pp. 14–15.

#### 2. Channel masking as consistency regularization

For masked logits \(S_{M,O}\), the expected symmetric contrastive loss decomposes as:

\[
\mathbb E L(S_{M,O})
=
L(\bar S)+\frac{1}{2B}\sum_v J_v,
\]

where \(\bar S=\mathbb E[S_{M,O}]\) and each \(J_v\) is a KL divergence between the softmax of the mean logits and the softmax under a particular mask/order.

**Paper’s claim:** channel dropout is not merely ordinary augmentation; in expectation it adds a prediction-consistency penalty.

For fixed-count electrode subsets, **Theorem 4.2** decomposes centered-logit variability into:

- first-order electrode sensitivity;
- residual nonlinear interactions and ordering effects.

If \(V\) denotes this total centered-logit variance, the row penalty satisfies:

\[
J\leq V/4.
\]

Under a nonsaturation condition in which softmax probabilities remain at least \(\mu>0\), the paper also gives:

\[
J\geq \mu V/2.
\]

The lower bound can be weak at low temperature or highly saturated logits.

**Anchors:** §4.2, PDF p. 5; proof and local Fisher discussion, Appendix A.2–A.3, pp. 15–16.

#### 3. From variability to retrieval errors

For a candidate set whose paired item is top-ranked by the mean predictor, the paper defines a candidate-separation cost \(c_y(p)\). It derives:

\[
\Pr(\text{masked ranking error})
\leq
\min\{1,J/c_y(p)\}
\leq
\min\{1,V/(4c_y(p))\}.
\]

The interpretation is that masking variability is more damaging when candidate separation is small.

A separate margin bound connects continuous prediction error to retrieval error:

\[
\Pr(\text{error})
\leq
\Pr(\Gamma<2\gamma_0)
+
\frac{2\mathbb E\|\hat V-V\|^2}{\gamma_0}.
\]

**Important qualification:** Appendix A.4 explicitly notes that comparing these upper bounds does not establish an ordering of actual retrieval errors. The bounds also require assumptions about correct mean prediction, candidate margins, and—in one version—drift from the full-channel predictor.

**Anchors:** §4.3, PDF p. 6; Appendix A.4, pp. 16–17.

### Dataset and evaluation protocol

#### Data

- **NMED-T:** 20 subjects, 10 Western pop songs.
- **NMED-H:** 48 subjects, 4 Hindi songs; original and reversed stimuli used.
- Total: **29.4 hours, 68 subjects**.
- 125 channels after benchmark preprocessing.
- Preprocessing: 0.3–50 Hz filtering, artifact removal, per-channel normalization; then downsampling to 125 Hz.

#### Split

- Non-overlapping one-second EEG/music pairs.
- Random 95%/5% train/test assignment.
- Test segments come from the same subjects and song collections as training.
- Temporally adjacent segments can fall into different partitions.
- No temporal purge gap exists.

Reference SSL is **transductive**: eight-second SSL windows use all EEG, including EEG later assigned to the downstream test split. A training-only control excludes any SSL window sharing even one raw sample with a test segment.

**Anchors:** §5.1, PDF p. 6; Appendix B.2, p. 18; Table 5, p. 18.

### Metrics and baselines

#### Metrics

- SSIM and PSNR on mel spectrograms.
- CLAP cosine similarity between generated and target audio.
- 10-class genre-label agreement using a frozen Wav2Vec2 classifier trained on GTZAN.
- 50-way identification among sampled paired test examples.
- 14-way identification using candidates from 14 distinct songs.
- Ten candidate-set samplings per evaluation.

Identification is separated into:

- **pre-generation EEG/CLAP alignment retrieval** for encoder methods;
- **post-generation audio retrieval** for EEG2Mel, Postolache et al., and the audio reconstruction reference.

#### Table 1: pooled NMED-T/H

Values are shown as `SSIM, PSNR, CLAP, genre agreement, 50-way, 14-way`.

| Method | SSIM | PSNR | CLAP | Genre | 50-way | 14-way |
|---|---:|---:|---:|---:|---:|---:|
| Linear EEG reference | .491 | 14.32 | .576 | .126 ± .067 | .018 ± .057 | .067 ± .057 |
| LaBraM | .422 | 14.21 | .657 | .162 ± .056 | .380 ± .057 | .681 ± .051 |
| EEGPT | .378 | 14.34 | .625 | .141 ± .065 | .326 ± .069 | .643 ± .068 |
| CBraMod | .418 | 14.42 | .641 | .169 ± .059 | .402 ± .058 | .690 ± .064 |
| **Ours** | **.488** | **14.41** | **.683** | **.203 ± .055** | **.487 ± .067** | **.692 ± .062** |
| Audio reconstruction reference | .416 | 13.26 | .752 | .276 ± .060 | .598 ± .069 | .775 ± .061 |
| EEG2Mel | **.762** | **24.37** | .588 | .132 ± .051 | .259 ± .050 | .478 ± .062 |
| Postolache et al. 2025 | .469 | 14.52 | .672 | .187 ± .052 | .392 ± .060 | .688 ± .061 |

**Paper’s interpretation:** the method is strongest on CLAP similarity, genre agreement, and pre-generation alignment.

**Important qualification:** EEG2Mel substantially wins SSIM and PSNR, meaning the proposed method does not dominate local spectrogram fidelity.

**Anchor:** Table 1 and §5.3, PDF pp. 7–8.

#### Table 2: matched encoder comparison

The one-second comparison uses identical NMED training EEG, 40,000 SSL steps, the same downstream alignment head, and matched fine-tuning policy.

| Encoder | 50-way | 14-way | CLAP |
|---|---:|---:|---:|
| CBraMod | .388 ± .048 | .680 ± .042 | .635 ± .050 |
| **Ours** | **.485 ± .055** | **.690 ± .052** | **.683 ± .062** |
| CSBrain, NMED-adapted | .392 ± .046 | .689 ± .049 | .640 ± .051 |

Absolute improvement over matched CBraMod:

- 50-way: **+.097**
- 14-way: **+.010**
- CLAP: **+.048**

This is the source of the abstract’s “0.388 to 0.485” and “0.635 to 0.683” claims. It should not be confused with Table 1’s released-checkpoint CBraMod result of .402.

**Anchor:** Table 2 and matched-pretraining discussion, PDF p. 8; Appendix C.1, p. 22.

### Ablations

Table 3 uses the reference protocol and reports identification before generation.

| Variant | 50-way | 14-way |
|---|---:|---:|
| Full model | **.487 ± .053** | **.692 ± .067** |
| Five-channel block tokenization | .141 ± .064 | .406 ± .062 |
| No multi-view pretraining | .050 ± .067 | .155 ± .066 |
| No SSL or alignment channel dropout | .411 ± .067 | .598 ± .054 |
| Linear head, encoder fixed | .092 ± .065 | .191 ± .061 |
| Linear head, encoder fine-tuned | .422 ± .051 | .612 ± .063 |
| Temporal head, encoder fixed during alignment | .179 ± .062 | .425 ± .063 |

**Paper’s claims:**

- Per-electrode tokens strongly outperform the tested five-electrode block representation.
- Multi-view pretraining produces the largest ablation effect.
- Removing dropout from both SSL and alignment hurts performance.
- Joint encoder/head adaptation is important.

**Interpretation:** the ablations establish that the complete recipe works better than the tested alternatives, but they do not isolate every component independently. For example, “no SSL or alignment dropout” removes two mechanisms simultaneously.

**Anchor:** Table 3 and §5.4, PDF p. 8.

#### Augmentation sensitivity

| SSL student dropout | 50-way | 14-way |
|---:|---:|---:|
| .1 | .477 ± .020 | .689 ± .023 |
| .2 | .480 ± .045 | .688 ± .049 |
| .3 | .485 ± .062 | .691 ± .051 |
| .6 default | .487 ± .053 | .692 ± .067 |

Crop sweep:

- Short crops `[G .4–.8, L .1–.4]`: .477 / .681
- Default `[G .5–.9, L .1–.5]`: .487 / .692
- Long `[G .6–1.0, L .2–.6]`: .485 / .691

The tested settings are relatively stable.

**Anchor:** Table 4 and §5.4, PDF pp. 8–9; Appendix C.2, p. 22.

### Training-only control and reproducibility

Excluding downstream test EEG from SSL pretraining gives:

| SSL EEG | 50-way | 14-way | CLAP |
|---|---:|---:|---:|
| All EEG | .487 ± .067 | .692 ± .062 | .683 |
| Training-only EEG | .485 ± .050 | .690 ± .055 | .683 |

The paper reports that training-only SSL has nearly identical mean performance. However:

- reference standard deviations are across ten candidate samplings;
- training-only standard deviations are across three training seeds;
- these are not directly comparable sources of variation.

Reproducibility strengths:

- detailed architecture and hyperparameters;
- fixed hyperparameters without validation/test-based selection;
- baseline implementation details;
- hardware and approximate compute reported: NVIDIA RTX 6000 Ada, approximately 20 GPU-hours for reference pretraining and alignment.

Reproducibility weaknesses:

- the paper does not provide a proposed-method code or checkpoint link;
- the only explicit public code link is the AudioLDM repository;
- reference results appear to use one trained model, with variability primarily from candidate sampling;
- subject-, song-, and temporally independent replication is absent;
- exact training seeds and several lower-level implementation choices for the proposed model are not fully documented.

**Anchors:** Appendices B.4–B.7, PDF pp. 19–21.

### Attention analysis

Figure 3 visualizes final-layer CLS-to-channel attention:

- averaged across temporal patches, heads, and windows;
- subject-level maps z-scored across electrodes;
- averaged across subjects.

The paper reports peaks around lateral posterior temporal and temporo-occipital electrodes, sometimes left-lateralized. NMED-H and NMED-T attention maps cluster separately; many between-dataset dissimilarities exceed 0.20, while within-NMED-T distances are approximately 0.05–0.15.

**Author’s interpretation:** these patterns may relate to temporal structure, beat, or musical affect.

**More cautious interpretation:** the strong NMED-H/NMED-T separation is also compatible with dataset, language, stimulus, subject, or recording confounds. Attention allocation is not a causal explanation; leave-one-channel-out or counterfactual perturbation tests would be needed.

**Anchor:** Figure 3 and §5.5, PDF p. 9; computation details Appendix C.3, p. 22.

### Limitations

The authors explicitly acknowledge:

- random segment splits from observed subjects and songs;
- no subject-held-out transfer;
- no song-held-out transfer;
- no temporally blocked evaluation;
- need for larger paired datasets;
- possible gains from stronger EEG-to-audio adapters and music encoders.

Additional limitations evident from the protocol:

1. **Potential temporal leakage:** adjacent segments can cross train/test boundaries.
2. **Song memorization risk:** the same songs occur in train and test.
3. **Transductive reference SSL:** test EEG is used in unsupervised pretraining, although the training-only control reduces concern about its average effect.
4. **Indirect audio evaluation:** CLAP and genre agreement measure semantic/style correspondence, not faithful note-level reconstruction.
5. **No human listening test.**
6. **No symbolic representation:** outputs are generated audio, not MIDI, note events, chord sequences, or editable arrangements.
7. **Theory-to-model gap:** the theory analyzes OLS and fixed masked logits, whereas the empirical system is a nonlinear transformer trained jointly with augmentation and a frozen generative stack.
8. **Interpretability gap:** Figure 3 is attention visualization, not validated causal explanation.

### Relevance to explainable symbolic music AI

#### Direct relevance: limited

This paper is **not directly a symbolic-music paper**. It does not address:

- MIDI or event-token modeling;
- symbolic composition;
- instrument/voice separation;
- mashup construction;
- note-level repair;
- harmonic or rhythmic constraints;
- user-facing explanations;
- causal attribution of musical decisions.

Its output is generated audio conditioned on EEG and CLAP embeddings.

#### Useful transferable ideas

1. **Track-preserving symbolic representations**

   Treat instrument, voice, stem, or symbolic track identity analogously to EEG electrode identity. Tokenize each track separately before cross-track aggregation rather than immediately pooling all events.

   Possible architecture:

   - per-track note/time tokens;
   - track embeddings preserving instrument/voice identity;
   - cross-track transformer aggregation;
   - explicit track-level attribution scores.

2. **Mask-consistent mashup modeling**

   Apply structured dropout to tracks, stems, or voices while retaining their identities. Train the model to produce stable musical predictions under missing or partially observed tracks.

   This could support:

   - mashups with incomplete stems;
   - arrangement completion;
   - robust accompaniment generation;
   - explanation of which tracks materially influence a prediction.

3. **Repair as masked conditional reconstruction**

   Replace EEG channel masks with corrupted symbolic events:

   - missing notes;
   - wrong pitches;
   - timing perturbations;
   - removed voices;
   - inconsistent chord tones.

   Use consistency across corruption masks and report uncertainty when candidate repairs have low separation margins.

4. **Information-retention criterion for symbolic compression**

   The paper’s threshold suggests a practical experiment: compare pooled versus track-preserving tokenizations while measuring both:

   - task information lost by compression;
   - estimation/sample complexity.

   For symbolic repair, this could quantify when compressing a full arrangement into harmonic summaries harms voice-leading or ornament recovery.

5. **Explanation stability under perturbation**

   Adapt the masking theorem empirically:

   - compute attribution or influence under multiple track/event masks;
   - measure variance across masks;
   - distinguish first-order track influence from interaction effects;
   - report explanations only when attribution is stable.

   This is more defensible than treating a single attention map as an explanation.

6. **Margin-aware repair confidence**

   The ranking analysis suggests confidence should depend not only on the top repair probability but also on the separation from alternatives. For example:

   - top candidate: F♯4;
   - second candidate: G4;
   - low margin means ambiguous repair;
   - high margin supports a stronger explanation.

7. **Evaluation transfer**

   For symbolic music AI, use stricter splits than this paper:

   - composer-held-out;
   - piece-held-out;
   - style-held-out;
   - temporally blocked segments;
   - arrangement/instrumentation-held-out.

   Metrics should include note precision/recall, onset and duration accuracy, chord consistency, voice-leading violations, structural repetition, repair edit distance, and human judgments of musical plausibility.

### Bottom line

**Author-supported conclusion:** under matched NMED pretraining and alignment conditions, the proposed channel-preserving EEG representation improves 50-way identification and CLAP similarity over CBraMod, with strong ablation evidence for per-electrode tokenization, self-distillation, channel dropout, and joint adaptation.

**My assessment:** the strongest contribution is the design principle—preserve identity while regularizing predictions under partial observation—not the claim of faithful music reconstruction. The empirical advantage is clearest in CLAP-space semantic alignment and retrieval, while EEG2Mel is much better on local spectrogram metrics. For explainable symbolic music AI, the paper is best treated as a source of ideas for track-preserving representations, structured masking, stability-based explanations, and margin-aware uncertainty—not as a directly applicable symbolic composition, mashup, or repair method.

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
