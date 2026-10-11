---
title: "CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation"
authors: "Jinting Wang, Chenxing Li, Dong Yu, and Li Liu"
year: 2026
doi: 10.48550/arXiv.2609.13118
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2026-cma-ot-hierarchical-expert-supervision.pdf"
pdf_filename: wang-2026-cma-ot-hierarchical-expert-supervision.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper’s central claim is that sparse dance cues cannot adequately supervise dense musical structure. CMA-OT therefore uses a pretrained hierarchical audio expert as an auxiliary training teacher for the dance-to-music generator.

## 1. Document Information

- **Canonical source:** arXiv `2609.13118v1`; official PDF preserved as `wang-2026-cma-ot-hierarchical-expert-supervision.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40xsw4_7uyr.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest: CMA-OT

### 1. Bibliography and scope

- **Title:** *CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation*
- **Authors:** Jinting Wang, Chenxing Li, Dong Yu, Li Liu
- **Affiliations:** HKUST(GZ); Tencent
- **Version:** arXiv:2609.13118v1, `[cs.AI]`, **11 September 2026**
- **Length:** 12-page preprint, including references and appendix
- **Demo:** https://beria-moon.github.io/CMA-OT/
- **Corresponding author:** Li Liu, `avrillliu@hkust-gz.edu.cn`
- Key cited foundations include REPA [3], Jukebox [33], Fused Gromov–Wasserstein OT [16], flow matching [39], AIST++ [40], DiffRhythm [42], and CKNNA [52]. Full bibliography: **pp. 9–10**.

The paper’s central claim is that sparse dance cues cannot adequately supervise dense musical structure. CMA-OT therefore uses a pretrained hierarchical audio expert as an auxiliary training teacher for the dance-to-music generator.

---

### 2. Page and section map

| Pages | Content |
|---|---|
| 1–2 | Abstract, introduction, motivation, contributions |
| 2–3 | Related work |
| 3–4 | Multi-scale music expert and FGW preliminaries |
| 4–6 | CMA-OT architecture, curriculum, scale-aware OT, flow matching |
| 6–8 | Datasets, implementation, metrics, comparisons, ablations, user study |
| 8 | Conclusion |
| 9–10 | References |
| 10–12 | Appendix: expert details, curriculum equations, representation analysis |

Figures: **Figs. 1–9** on pp. 1, 3, 4, 7, 8, 11, and 12.  
Tables: **Tables I–IV** on pp. 5, 7, and 8.

---

### 3. Architecture

#### Generator and dance conditioning

**Paper, Sec. IV-A, p. 4; Fig. 2, p. 3**

1. A dance video is processed by:
   - pretrained **I3D** encoder for global visual/style features \(z_v\);
   - pose/rhythm encoder operating on 2-D skeletons for temporal rhythm features \(z_r\).

2. These features condition a conditional flow-matching music generator using a **Diffusion Transformer / DiT**.

3. The generator:
   - uses 12 LLaMA decoder layers;
   - hidden dimension 764;
   - 12 self-attention heads;
   - produces 64-dimensional audio-VAE latents at 21.5 Hz.

4. Internal DiT representations are selected at three depths:
   - shallow layer \(h_{\text{bot}}\);
   - middle layer \(h_{\text{mid}}\);
   - deep layer \(h_{\text{top}}\).

5. Each is passed through a two-layer GELU MLP projection head:

\[
\tilde h_k=\phi_k(h_k),\qquad k\in\{\text{top},\text{mid},\text{bot}\}.
\]

The paper applies representation supervision at the **final denoising step**, where it assumes DiT features most closely approximate clean music representations (**Sec. IV-B, p. 5**).

#### Audio latent representation

Training clips are 5 seconds, resampled to 44.1 kHz. A pretrained DiffRhythm VAE uses downsampling factor \(f=2048\), producing 64-dimensional latent representations at 21.5 Hz (**Sec. V-B, p. 6**).

The paper describes conditional flow matching as:

\[
\frac{dZ_t}{dt}=v_\theta(Z_t,t\mid z_v,z_r)
\]

\[
\mathcal L_{\mathrm{CFM}}
=
\mathbb E_{t,Z_0,Z_1}
\left[
\left\|
v_\theta(Z_t,t\mid z_v,z_r)-(Z_1-Z_0)
\right\|^2
\right].
\]

The total loss is:

\[
\mathcal L_{\mathrm{total}}
=
\mathcal L_{\mathrm{CFM}}+\mathcal L_{\mathrm{CMA}}.
\]

**Notation issue:** the prose calls \(Z_0\) the music latent, but Eq. (8) states \(Z_0\sim p_0\) is Gaussian prior and \(Z_1\sim p_1\) is the music-latent distribution. Standard flow-matching notation supports the equation, suggesting the prose contains a likely reversal (**Sec. IV-D, p. 5**).

---

### 4. Music expert representations

#### Expert model

**Paper, Sec. III-A, p. 3; Appendix, p. 10**

The teacher is the **Jukebox 1B Lyrics VQ-VAE**, using only its encoder:

- three discrete code levels;
- 64-dimensional embeddings per level;
- codebook size 2048;
- audio resampled to 44.1 kHz and converted to mono;
- hop fractions reported as \([0.125, 0.5, 0.5]\);
- code indices are converted back to continuous codebook embeddings.

The paper interprets the levels as:

| Expert level | Claimed musical content | Generator layer |
|---|---|---|
| Top | global style and genre | DiT layer 10 |
| Middle | melodic and harmonic phrases | DiT layer 6 |
| Bottom | rhythmic texture and timbre | DiT layer 2 |

The layer mapping is selected using CKNNA similarity analysis over 1,000 AIST++ training examples (**Appendix F–H, pp. 11–12; Fig. 8**).

**Important interpretation:** these are hierarchical **audio embeddings**, not explicit symbolic representations. The semantic labels “style,” “harmony,” “melody,” “rhythm,” and “timbre” are author interpretations of the VQ-VAE levels, not independently supervised symbolic factors.

---

### 5. Curriculum-guided supervision

#### Multi-scale loss

For each level:

\[
\mathcal L_{\mathrm{align}}^{(k)}
=
\operatorname{Align}(\tilde h_k,z_k).
\]

The curriculum loss is:

\[
\mathcal L_{\mathrm{CMA}}
=
\sum_{k\in\{\mathrm{top},\mathrm{mid},\mathrm{bot}\}}
\lambda_k\mathcal L_{\mathrm{align}}^{(k)}.
\]

**Paper, Sec. IV-B, pp. 4–5; Fig. 3, p. 4**

Training is coarse-to-fine:

1. **Phase 1:** top-level/global alignment dominates during the first 30 epochs.
2. **Phase 2:** middle-level alignment increases from epochs 30–100 while top-level weight decreases.
3. **Phase 3:** bottom-level alignment activates after epoch 100.

The cosine schedule ultimately uses approximately:

- \(\lambda_{\text{top}}\): 1.0 → 0.4 → 0.2
- \(\lambda_{\text{mid}}\): 0 → 0.6 → 0.3
- \(\lambda_{\text{bot}}\): 0 → 0 → 0.5

The appendix gives the exact transition function:

\[
\lambda_t
=
\lambda_{\mathrm{end}}
+\frac12(\lambda_{\mathrm{start}}-\lambda_{\mathrm{end}})
\left[
1+\cos\left(\pi\frac{t-t_s}{t_e-t_s}\right)
\right].
\]

#### Why curriculum is used

**Author claim:** simultaneously activating all scales causes conflicting gradients and unstable optimization. Coarse-to-fine supervision reduces interference and improves convergence.

**Interpretation:** this is a form of teacher forcing over representation abstraction: the generator is first encouraged to establish broad musical organization before being pressured to match local temporal detail.

---

### 6. Scale-aware FGW alignment

#### Standard FGW

For source sequence \(X=\{x_i\}\), target sequence \(Y=\{y_k\}\), relation matrices \(C^X,C^Y\), and transport plan \(P\):

\[
D_{\mathrm{FGW}}(X,Y)
=
\min_{P\in\Pi(a,b)}
\sum_{i,k}
\left[
(1-\alpha)c(x_i,y_k)
+
\alpha\sum_{j,l}
L(C^X_{i,j},C^Y_{k,l})P_{j,l}
\right]P_{i,k}.
\]

Here:

- \(c\): feature-level discrepancy;
- \(L\): pairwise structural discrepancy;
- \(\alpha\in[0,1]\): semantic-versus-structural balance.

#### Scale-aware objective

At scale \(k\):

\[
\mathcal L_{\mathrm{align}}^{(k)}
=
\min_{P^{(k)}\in\Pi(a,b)}
\sum_{i,p}
\left[
(1-\alpha_k)c(\tilde h_{k,i},z_{k,p})
+
\alpha_k
\sum_{j,q}
P^{(k)}_{j,q}
L(C^{\tilde h_k}_{i,j},C^{z_k}_{p,q})
\right]P^{(k)}_{i,p}.
\]

The paper uses:

- cosine distance for \(c\);
- MSE for \(L\);
- \(\epsilon=10^{-6}\).

The adaptive balance is based on expected semantic and structural costs:

\[
m_k=\mathbb E_{P^{(k)}}[c(\tilde h_k,z_k)],
\qquad
n_k=\mathbb E_{P^{(k)}}[L(C^{\tilde h_k},C^{z_k})],
\]

\[
\alpha_k
=
\sigma\left(
\log\frac{n_k}{m_k+\epsilon}
\right).
\]

**Author claim:** FGW handles temporal-length mismatch and preserves both feature semantics and within-sequence structure better than pointwise cosine matching.

**Interpretation:** the transport plan \(P^{(k)}\) could become an explainable alignment object, but the paper does not expose or evaluate transport plans as explanations.

---

### 7. Data, training, and evaluation

#### Datasets

**Sec. V-A, p. 6**

- **AIST++:** 1,020 dance videos, 10 dance genres, professional studio recordings.
- **TikTok:** 445 dance videos covering 85 songs.
- Standard prior-work splits and protocols are used.
- Each training example is a 5-second music clip.

#### Training

**Sec. V-B, p. 6**

- Adam, \(\beta_1=0.9,\beta_2=0.95\)
- Learning rate \(10^{-4}\)
- Batch size 4
- 200 epochs
- DWpose with default hyperparameters
- 32-step Euler ODE sampler at inference
- classifier-free guidance scale 4
- No expert computation at inference

The paper does not report seed, hardware, wall-clock time, parameter count, confidence intervals, or statistical significance tests.

#### Metrics

**Sec. V-C, p. 6**

- Rhythm: BCS, BHS, their standard deviations CSD/HSD, and F1.
- Audio quality:
  - \(FAD_p\): PANNs features;
  - \(FAD_c\): CLAP features.
- Audiobox aesthetics:
  - CE: content enjoyment;
  - CU: content usefulness;
  - PC: production complexity;
  - PQ: production quality.
- User study:
  - OVL: overall perceptual quality;
  - REL: dance relevance;
  - 5-point Likert scale.

---

### 8. Main results

#### Table I — AIST++ and TikTok, p. 5

Columns are BCS, CSD, BHS, HSD, F1, CE, CU, PC, PQ, \(FAD_p\), \(FAD_c\).

##### AIST++

| Method | BCS | CSD | BHS | HSD | F1 | CE | CU | PC | PQ | FADp | FADc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D2M-GAN | 89.09 | 14.05 | 88.95 | 22.23 | 88.84 | 4.76 | 6.65 | 5.13 | 6.33 | 49.49 | 1.27 |
| CDCD | 92.18 | 14.66 | 89.50 | 21.16 | 88.95 | 6.69 | 6.76 | 5.31 | 6.30 | 47.95 | 1.25 |
| LORIS | 92.13 | 7.94 | 91.71 | 9.69 | 92.05 | 6.41 | 6.80 | 6.23 | 6.74 | 33.64 | 0.68 |
| Textual-Inv | 93.21 | 11.74 | 84.97 | 17.15 | 86.75 | 6.73 | 7.26 | 6.56 | 7.10 | 28.70 | 0.52 |
| MotionComposer | 95.84 | 7.89 | 95.09 | 16.09 | 96.45 | 6.87 | 7.46 | 6.49 | 7.33 | 27.52 | 0.49 |
| **CMA-OT** | **99.14** | **7.07** | **99.12** | **7.56** | **99.12** | **6.93** | **7.49** | **6.71** | **7.44** | **12.50** | **0.26** |

##### TikTok

| Method | BCS | CSD | BHS | HSD | F1 | CE | CU | PC | PQ | FADp | FADc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| D2M-GAN | 82.55 | 28.03 | 87.07 | 24.62 | 84.22 | 4.49 | 5.61 | 5.24 | 5.84 | 52.68 | 1.48 |
| CDCD | 84.46 | 25.95 | 87.95 | 23.27 | 86.45 | 5.12 | 5.91 | 5.32 | 5.94 | 49.55 | 1.36 |
| LORIS | 88.02 | 24.14 | 85.25 | 18.72 | 87.43 | 5.64 | 6.81 | 6.13 | 6.52 | 45.18 | 0.94 |
| Textual-Inv | 90.16 | 27.41 | 82.08 | 21.62 | 85.43 | 6.21 | 7.10 | 6.06 | 7.28 | 29.64 | 0.78 |
| MotionComposer | 89.09 | 17.95 | 90.02 | 17.35 | 89.50 | 6.19 | 7.15 | 6.41 | 7.24 | 30.61 | 0.81 |
| **CMA-OT** | **92.88** | **13.42** | **92.05** | **16.27** | **92.41** | **6.31** | **7.19** | **6.67** | **7.36** | **27.53** | **0.38** |

**Author claim:** CMA-OT is best on every displayed metric in both datasets.

---

### 9. Ablations

#### Table II — Component ablation on AIST++, p. 7

| Variant | BCS | CSD | BHS | HSD | F1 | CE | CU | PC | PQ | FADp | FADc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 97.19 | 9.54 | 97.42 | 9.31 | 97.27 | 6.04 | 6.71 | 6.54 | 6.92 | 21.12 | .42 |
| Base + CLAP-OT | 97.94 | 8.76 | 97.84 | 11.09 | 97.90 | 6.14 | 6.75 | 6.51 | 6.83 | 20.42 | .39 |
| Base + MERT-OT | 98.12 | 8.17 | 98.23 | 12.29 | 98.18 | 6.33 | 7.12 | 6.62 | 7.13 | 19.76 | .37 |
| Base + Top-OT | 97.93 | 8.19 | 97.76 | 9.22 | 97.83 | 6.32 | 6.78 | 6.57 | 7.10 | 19.91 | .38 |
| Base + Middle-OT | 98.26 | 8.03 | 98.47 | 9.06 | 98.39 | 6.46 | 7.18 | 6.65 | 7.15 | 18.92 | .35 |
| Base + Bottom-OT | 98.65 | 7.81 | 98.72 | 8.89 | 98.67 | 6.61 | 7.24 | 6.67 | 7.21 | 15.69 | .32 |
| Base + MA-OT | 97.77 | 8.09 | 97.70 | 12.05 | 97.73 | 6.05 | 6.68 | 6.57 | 6.84 | 20.64 | .39 |
| Base + CMA | 98.68 | 7.83 | 98.79 | 8.72 | 98.71 | 6.73 | 7.26 | 6.69 | 7.24 | 13.36 | .29 |
| Base + CMA-OT* | 99.03 | 7.31 | 99.04 | 7.92 | 99.03 | 6.81 | 7.33 | 6.69 | 7.42 | 12.84 | .27 |
| **Base + CMA-OT** | **99.14** | **7.07** | **99.12** | **7.56** | **99.12** | **6.93** | **7.49** | **6.71** | **7.44** | **12.50** | **.26** |

**Author interpretation:**

- CLAP and MERT provide only marginal gains.
- Bottom-level supervision is strongest among single-scale variants.
- Multi-scale alignment without curriculum, MA-OT, degrades performance.
- Curriculum plus cosine alignment improves substantially.
- Replacing cosine with FGW improves alignment and FAD.
- Adaptive scale weighting gives an additional improvement.

**Numerical inconsistency:** the text says “Base + CMA” reduces \(FAD_p\) by 40.81% relative to Base. The displayed values imply:
- Base → Base+CMA: \(21.12\to13.36\), a **36.74%** reduction.
- Base → full CMA-OT: \(21.12\to12.50\), a **40.81%** reduction.

The paper also says it evaluates “eight variants,” although Table II displays more than eight experimental conditions.

#### Table III — Curriculum strategy, p. 8

| Strategy | BCS | F1 | CE | FADp |
|---|---:|---:|---:|---:|
| Fixed weights | 99.05 | 99.02 | 6.78 | 13.01 |
| Hard switch | 99.07 | 99.04 | 6.82 | 12.79 |
| Linear schedule | 99.12 | 99.09 | 6.86 | 12.57 |
| **Cosine schedule** | **99.14** | **99.12** | **6.93** | **12.50** |

#### Table IV — Alignment method, p. 8

| Alignment | BCS | F1 | CE | FADp |
|---|---:|---:|---:|---:|
| Linear + cosine | 98.83 | 98.79 | 6.68 | 13.69 |
| Time-Conv + cosine | 99.03 | 98.91 | 6.73 | 13.36 |
| Standard OT | 99.05 | 98.97 | 6.75 | 13.05 |
| **Scale-FGW** | **99.14** | **99.12** | **6.93** | **12.50** |

---

### 10. Figures

- **Fig. 1, p. 1:** contrasts conventional final-output supervision with CMA-OT’s hierarchical expert supervision.
- **Fig. 2, p. 3:** full pipeline: video/pose conditioning, DiT layers, Jukebox levels, curriculum, FGW, and flow-matching loss.
- **Fig. 3, p. 4:** cosine curriculum weights over 200 epochs.
- **Fig. 4, p. 7:** spectrogram comparison; authors claim better rhythm and tonal coherence.
- **Fig. 5, p. 7:** FAD versus training epoch; authors claim faster convergence. It is not a wall-clock efficiency measurement.
- **Fig. 6, p. 8:** 40-person subjective study; CMA-OT has the highest OVL and REL bars.
- **Fig. 7, p. 11:** fixed, hard-switch, linear, and cosine curriculum schedules.
- **Fig. 8, p. 12:** CKNNA heatmap between DiT layers and Jukebox levels. Reported mapping: bottom→layer 2, middle→layer 6, top→layer 10.
- **Fig. 9, p. 12:** t-SNE distributions. Authors claim CMA-OT’s generated-music distribution is closer to ground-truth music than the baseline.

---

### 11. Limitations and artifact status

#### Explicit paper limitations

The paper has **no dedicated limitations section**. It does not report:

- cross-dataset generalization beyond AIST++ and TikTok;
- long-form generation;
- cross-composer or held-out-song transfer;
- statistical significance;
- compute cost or wall-clock training;
- released checkpoints;
- detailed OT solver, regularization, marginal, or transport-plan settings.

#### Substantive limitations

1. **Audio rather than symbolic supervision:** Jukebox embeddings do not directly expose notes, chords, voices, instrument identities, bar structure, or repair operations.
2. **Interpretability is asserted rather than demonstrated:** the three levels are described musically, but no probing or intervention establishes that each level cleanly disentangles its claimed factor.
3. **Evaluation is mostly proxy-based:** FAD, Audiobox scores, rhythm metrics, t-SNE, and a small AIST++ user study do not directly measure harmonic correctness, structural form, voice leading, or editability.
4. **Narrow data regime:** only 5-second clips and relatively small paired datasets are used.
5. **Teacher is training-only:** expert representations improve learning but are unavailable as an explicit controllable interface at inference.
6. **Potential computational cost:** multi-scale FGW can be expensive for long sequences; complexity and approximation details are not given.

#### Public artifacts

The paper lists a demo page. The linked page currently exposes:

- a public GitHub code link;
- demo videos;
- training and inference scripts;
- configuration files;
- feature-extraction tools;
- reproducibility documentation.

The associated code repository’s documentation reports:

- Apache-2.0 source license;
- Python 3.11.6 / PyTorch 2.6.0+cu124 environment;
- Jukebox feature extraction;
- inference with dance-only conditions;
- no redistributed datasets or external weights.

However, its reproducibility documentation explicitly says evaluator implementations are omitted pending metric auditing. Its asset lock marks release as blocked until:

- an exact Jukebox checkpoint is pinned;
- an authorized TorchScript inference decoder is pinned.

Thus, the public code/demo is useful, but the available artifact does not yet establish exact reproduction of the paper’s reported results.

---

### 12. Relevance to auxiliary music-expert supervision

#### Strong relevance

CMA-OT provides a directly reusable design pattern:

1. freeze a pretrained music expert;
2. extract hierarchical representations;
3. map generator hidden states into the expert space;
4. align them with a structure-aware loss;
5. apply supervision coarse-to-fine;
6. remove the expert at inference.

For symbolic music, the same design could replace Jukebox with a symbolic expert whose representations are explicitly grounded in:

- form and phrase structure;
- harmony and tonality;
- melody and voice leading;
- beat/meter/rhythm;
- instrumentation and texture.

#### Important distinction

CMA-OT is **not yet an interpretable symbolic-music method**. Its hierarchy is inferred from an audio VQ-VAE, and the output is audio latent generation. Its contribution is the supervision mechanism, not symbolic representation or transparent editing.

---

### 13. Concrete research ideas for symbolic mashup and repair

1. **Symbolic CMA-OT**
   - Use a frozen MIDI/event transformer or multi-expert symbolic encoder.
   - Define explicit levels: form → phrase → chord/melody → beat/note.
   - Align generator layers with these levels using FGW.

2. **Theory-grounded structural costs**
   - Construct relation matrices from bar distance, metrical position, chord-root distance, voice-leading distance, melodic contour, and instrument-family similarity.
   - Make \(C^Z\) interpretable rather than relying only on learned embedding geometry.

3. **Mashup alignment**
   - Use the transport plan \(P^{(k)}\) to align vocal melody, accompaniment, and target form.
   - Expose bar- and beat-level correspondences as an explanation of why material was combined.

4. **Repair-specific supervision**
   - Corrupt symbolic sequences through deletion, substitution, timing shifts, or instrumentation removal.
   - Apply expert supervision only to corrupted spans while enforcing identity on untouched material.
   - Train from global form/harmony first, then local note repair.

5. **Interpretable expert probes**
   - Test whether top/middle/bottom representations predict explicit labels such as key, chord, phrase boundary, beat position, density, and instrument family.
   - Use interventions: perturb one expert level and measure only the corresponding musical factor.

6. **Unbalanced OT for symbolic edits**
   - Standard FGW assumes transport between sequences; symbolic repair often needs insertion/deletion.
   - Unbalanced or partial OT would better model missing notes, extra notes, and phrase-length differences.

7. **Human-facing explanations**
   - Report selected expert level, transport correspondences, \(\alpha_k\), and changed bars/voices.
   - Evaluate explanation faithfulness by checking whether masking the cited evidence changes the repair.

8. **Better evaluation**
   - Add exact repair accuracy, chord/key consistency, voice-leading violations, rhythmic-grid compliance, untouched-region preservation, form consistency, and expert/human preference tests.

**Bottom line:** CMA-OT is highly relevant as an auxiliary-supervision architecture for interpretable symbolic music, but a symbolic adaptation must replace opaque audio-level supervision with explicit, probeable musical structures and expose OT correspondences as part of the explanation.

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
