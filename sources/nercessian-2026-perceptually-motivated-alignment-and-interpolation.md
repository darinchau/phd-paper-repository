---
title: "Perceptually Motivated Alignment and Interpolation of Pitch-Aligned Time-Frequency Representations"
authors: "Shahan Nercessian, Jeff Sontag, and Alejandro Koretzky"
year: 2026
doi: 10.48550/arXiv.2609.31971
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/nercessian-2026-perceptually-motivated-alignment-and-interpolation.pdf"
pdf_filename: nercessian-2026-perceptually-motivated-alignment-and-interpolation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I inspected all eight PDF pages, equations, figures, algorithms, tables, and the experiments described in the extracted text. The paper refers to additional figures and audio demonstrations at `https://tiv-ext.netlify.app`.

## 1. Document Information

- **Canonical source:** arXiv `2609.31971v1`; official PDF preserved as `nercessian-2026-perceptually-motivated-alignment-and-interpolation.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40l1xa_5pfn.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliographic record

- **Shahan Nercessian, Jeff Sontag, Alejandro Koretzky**, “**Perceptually Motivated Alignment and Interpolation of Pitch-Aligned Time-Frequency Representations**,” Splice, New York.
- **arXiv:2609.31971v1 [eess.AS], 25 September 2026**.
- Published in the proceedings of the **29th International Conference on Digital Audio Effects (DAFx26)**, Cambridge, 1–4 September 2026.
- Eight-page paper, printed pages **DAFx.1–DAFx.8**, CC BY 4.0.
- The paper’s central prior works are Bernardes et al.’s TIV representation [5], TIV.lib [6], Henderson and Solomon’s audio OT [9], Levy’s Circle of Fourths/Fifths [10], Hungarian assignment [14], QAP [15], and Hoyer sparsity [23].

I inspected all eight PDF pages, equations, figures, algorithms, tables, and the experiments described in the extracted text. The paper refers to additional figures and audio demonstrations at `https://tiv-ext.netlify.app`.

---

### 1. Core contribution

The authors propose a signal-processing toolkit for manipulating pitch-aligned time-frequency representations (PTFRs), including:

1. An invertible extension of the tonal interval vector (TIV).
2. Perceptually weighted alignment through pitch-axis permutations.
3. Optimal-transport interpolation on the Circle of Fourths/Fifths.
4. A low-dimensional geometric representation intended to separate:
   - root,
   - scale density,
   - scale color.

Their stated goal is structured manipulation of both audio-derived and symbolic pitch representations without requiring explicit key detection (Abstract; DAFx.1, §1).

**Interpretation:** This is best understood as a harmonic/pitch-structure layer, not a complete mashup-alignment system. It does not solve beat synchronization, phrase alignment, source separation, timbral matching, or expressive timing.

---

### 2. TIV and the perceptual representation

#### Original TIV

For chroma \(c\in\mathbb{R}^{N}\), normally \(N=12\), the paper defines:

\[
T(c)[k]
=
w_\ast[k]\sum_{n=0}^{N-1}\bar c[n]
\exp\left(-j\frac{2\pi kn}{N}\right),
\qquad 1\leq k\leq 6,
\]

with

\[
\bar c[n]=
\frac{c[n]}{\sum_{n=0}^{N-1}c[n]}.
\]

This normalization makes the representation amplitude-invariant (DAFx.2, §2, Eqs. 1–2).

The weights are:

- **Symbolic:**  
  \[
  w_{\text{symbolic}}=[2,11,17,16,19,7].
  \]
- **Audio:**  
  \[
  w_{\text{audio}}=[3,8,11.5,15,14.5,7.5].
  \]

The authors state that these weights derive from empirical dyad-consonance ratings. They claim that Euclidean distance in TIV space better corresponds to perceived consonance than Euclidean distance in chroma space.

#### Invertible real Fourier basis

The original TIV discards the DC component and represents complex Fourier values in a reduced form. The authors construct:

- \(F_{\text{complex}}\in\mathbb{C}^{(N/2+1)\times N}\),
- \(F_{\text{real}}\in\mathbb{R}^{(N+2)\times N}\), stacking real and imaginary parts.

They remove the two imaginary rows that are identically zero at DC and Nyquist, then move the DC row to the final position, producing a square full-rank matrix:

\[
F\in\mathbb{R}^{N\times N}.
\]

Figure 1 (DAFx.2) visually compares the original real basis, the basis implicit in the prior TIV equation, and the proposed invertible basis.

The weighting matrix is:

\[
W=\operatorname{diag}(\text{frequency weights plus a free DC weight}),
\qquad
T=WF.
\]

The free DC parameter is denoted \(\kappa\) in the paper:

- \(\kappa=0\): recovers the original DC-invariant TIV behavior.
- \(\kappa=1\): retains the DC component and makes the generalized transform invertible when applied directly to \(c\).

The paper distinguishes the invertibility of \(F\) from that of the perceptually weighted \(T\): with \(\kappa=0\), \(F\) is invertible but the original TIV remains non-invertible; with \(\kappa=1\), the generalized transform supports inverse filtering (DAFx.2, §3.1).

#### Perceptually smoothed PTFR

The proposed feature extractor is:

\[
A(c)=c'=F^{T}T^{T}c
=F^{T}WFc.
\tag{3}
\]

For unit weights and \(\kappa=1\), it recovers the input. Otherwise, it acts as a fixed, perceptually motivated spectral filter along the pitch axis.

Important caveat from the authors: \(c'\) is **not guaranteed to remain non-negative**, even when \(c\) is non-negative (DAFx.4, §3.4).

#### Normalization and higher dimensions

The paper optionally:

- normalizes the rows of \(F\) to be orthonormal;
- rescales the non-DC weights so that their sum is \(N/2-1\);
- extends the construction to \(N=12o\), where \(o\) is the number of octaves represented.

For higher-dimensional representations, the canonical 12-dimensional weight vector is linearly interpolated. Figure 3 compares:

- a 96-dimensional zero-padded chroma vector;
- a 96-dimensional octave-replicated vector;
- their corresponding TIV representations.

The replicated representation produces zeros at non-original frequencies because of periodicity; zero-padding produces sinc-like spectral convolution (DAFx.3, §3.3).

For an 88-key piano representation, the paper pads to the nearest \(12o\)-dimensional representation, applies the transform, then truncates. Figure 4 shows the original and perceptually smoothed 88-dimensional PTFR (DAFx.4).

#### Temperley-profile finding

Using inverse filtering, Figure 2 reconstructs Shaath and Temperley pitch-class profiles from TIV.lib. The authors report an unexpected emphasis on D in the recovered C-major Temperley profile and suggest that this may explain degraded internal key-detection performance of those profiles.

This is an implementation/representation diagnostic, not a new empirical validation of key detection.

---

### 3. Permutation alignment

#### Exact optimization problem

Given non-negative PTFRs \(x,y\), the authors search over permutation matrices \(P\):

\[
\min_{P\in\mathcal{P}_N}J(P),
\]

\[
J(P)=\|TPx-Ty\|_2^2.
\tag{4–5}
\]

The permutation acts on the **musical pitch axis**, while the objective is measured in TIV space (DAFx.4, §4).

Expanding the objective gives:

\[
J(P)
=
(Px)^TT^TT(Px)
-2(Px)^TT^TTy
+y^TT^TTy.
\tag{6}
\]

Because non-uniform perceptual weights make \(T^TT\) non-diagonal, the quadratic term depends on \(P\). The authors therefore identify the exact problem as a **quadratic assignment problem (QAP)**, which is NP-hard.

When \(W=I\), the quadratic term becomes constant and the problem reduces to a linear assignment problem (LAP).

#### Approximated LAP objective

With an orthogonal \(F\) and \(\kappa=0\), the paper writes:

\[
J(P)
=
\|A(Px)-A(y)\|_2^2.
\tag{7}
\]

It then approximates this using:

\[
J_{\text{LAP}}(P)
=
\|Px-y\|_2^2
=
-2(Px)^Ty+\|x\|_2^2+\|y\|_2^2.
\tag{8}
\]

#### Alignment variants

The paper evaluates four types of alignment:

1. **Argmax circular shift**  
   Aligns the maximum component of \(x\) to the maximum component of \(y\), treating the dominant pitch as a root.

2. **Cross-correlation circular shift**  
   Finds the best circular shift using cross-correlation, but applies it to perceptually smoothed PTFRs rather than raw chroma.

3. **Argsort permutation**  
   For vector inputs, the rearrangement inequality implies that sorting the components in the same order minimizes the LAP objective.

4. **Hungarian assignment**  
   For time-varying matrices \(X,Y\in\mathbb{R}^{N\times M}\), the cost matrix is:

   \[
   C_{ij}=-2X'_jY'_i,
   \tag{11}
   \]

   and the Hungarian algorithm solves the LAP.

The authors then use a greedy **2-opt refinement**: try row swaps, evaluate the true QAP objective, and keep improving swaps until no single swap lowers the loss (DAFx.5, §4.3).

**Interpretation:** The method avoids explicit key estimation by matching pitch distributions directly. However, the argmax method still embeds an implicit root assumption, and unrestricted permutations can produce pitch remappings that are mathematically optimal but musically difficult to realize as a single global transposition.

---

### 4. Optimal-transport interpolation

The interpolation problem assumes \(L_1\)-normalized PTFRs \(\bar x,\bar y\), treating them as probability distributions.

#### Linear OT

A greedy monotone rearrangement algorithm constructs a transport plan \(\pi^\ast\), moving mass from source pitch bin \(i\) to target pitch bin \(j\). Interpolation places transported mass along the path between \(i\) and \(j\), conceptually at:

\[
(1-t)i+t j,
\qquad t\in[0,1].
\]

This produces an “earth-moving” transition rather than simply fading one pitch set out while fading another in. Algorithm 1 gives the greedy one-dimensional OT construction (DAFx.5, §5.1).

#### Circle of Fourths/Fifths

For chroma, the authors replace chromatic adjacency with adjacency on the Circle of Fourths/Fifths.

The permutation is:

\[
c_{\mathrm{cof}}
=
c[0,7,2,9,4,11,6,1,8,3,10,5].
\]

The inverse is \(H^T\). Because the circle is periodic, the endpoint classes C and B are connected.

For every source-target pair, the circular algorithm computes clockwise and counter-clockwise distances:

\[
\Delta_{\rightarrow}=(j-i)\bmod N,
\qquad
\Delta_{\leftarrow}=(i-j)\bmod N.
\]

It transports mass through the shorter direction and splits fractional movement between neighboring bins when necessary (Algorithm 2, DAFx.6).

The authors claim that this better reflects harmonic proximity and produces transitions consistent with musical voice-leading principles. That claim is supported in the paper by one illustrative C-major/C-minor example, not by a broad perceptual experiment.

---

### 5. Geometric scale representation

The model is intended to represent chroma on a cylindrical three-dimensional space:

- \(r\): scale density;
- \(\theta\): root location on the Circle of Fourths/Fifths;
- \(z\): learned scale color.

#### Deterministic coordinates

The density coordinate \(r\) is based on the Hoyer sparsity metric, scaled so that:

- a single active pitch maps to \(1/12\);
- a uniform chromatic scale maps to \(1\).

The root coordinate \(\theta\) is the angular distance from C to the argmax-defined root on the Circle of Fourths/Fifths.

The model rotates each chroma vector by \(-\theta\), so the network sees root-normalized inputs.

#### Learned architecture

The architecture in Figure 6 is:

1. \(L_1\)-normalize chroma.
2. Compute \(r,\theta\).
3. Rotate by \(-\theta\).
4. Apply the TIV transform with DC preservation, \(\kappa=1\).
5. \(L_2\)-normalize.
6. Encode to \(z\).
7. Concatenate \(z\) with \(r\).
8. Decode a reconstructed normalized TIV.
9. Invert the TIV.
10. Rotate back by \(\theta\).
11. Apply final \(L_1\) normalization.

Both encoder and decoder contain three linear layers, hidden dimension 2, and LeakyReLU activations.

#### Scale experiment

Training uses:

- 106 internally constructed scale profiles;
- tetrachord, pentatonic, hexatonic, heptatonic, octatonic, chromatic, and single-note profiles;
- Krumhansl-Schmuckler and Temperley weights, with non-scale tones set to zero;
- 20,000 Adam steps;
- learning rate \(10^{-3}\);
- the full training set as every batch.

Figure 7 shows:

- a 3D cylindrical encoding;
- a planar \(\theta=0\) view.

The authors observe Locrian-like and Lydian-like profiles at opposite ends of \(z\), interpreting \(z\) as dark-to-bright scale color and \(r\) as density. They also report smooth aural transitions when varying \(z\) while holding \(r\) fixed on the demo website.

**Interpretation:** This is an interpretable latent coordinate system, but the paper does not establish that the factorization is identifiable, perceptually calibrated, or generalizes beyond the hand-constructed training set.

---

### 6. Experimental results

#### 6.1 Alignment

The main musical example uses:

- \(X\): synthetic I–IV–V–I chromagram sequence in D major with perturbations.
- \(Y\): standard minor cantus-firmus sequence `1–5–4–3–2–1–3–2–1` in C minor.

A second experiment uses **1,024 randomly generated chromagram pairs**.

The evaluation reports the original TIV distance from Eq. 1, deliberately avoiding evaluation solely in the authors’ new representation.

| Method | PCP/vector musical | PCP/vector random | Sequence musical | Sequence random |
|---|---:|---:|---:|---:|
| None | 23.354 | 7.308 | 130.450 | 26.344 |
| Argmax | 13.206 | 6.534 | 104.226 | 24.174 |
| Cross-correlation | 13.206 | 5.055 | 104.226 | 20.277 |
| Argsort | 5.361 | 3.086 | 100.266 | 15.964 |
| Argsort + 2-opt | **4.350** | **2.276** | 107.568 | 14.509 |
| Hungarian | 7.622 | 3.183 | 90.537 | 14.889 |
| Hungarian + 2-opt | 7.891 | 2.559 | **89.847** | **13.012** |

**Author-supported conclusions:**

- Argsort is strongest for the vector/PCP LAP case.
- Hungarian is strongest for the time-varying matrix LAP case.
- 2-opt improves the best sequence result from 90.537 to 89.847 and the random sequence result from 14.889 to 13.012.

**Important nuance:** 2-opt does not improve every initialization in every column: the musical sequence score for argsort worsens from 100.266 to 107.568. Thus the table supports selective improvement, not uniformly monotonic superiority across methods.

#### 6.2 Interpolation

The interpolation example is between:

\[
\bar x=[1/3,0,0,0,1/3,0,0,1/3,0,0,0,0]
\]

(C major) and

\[
\bar y=[1/3,0,0,1/3,0,0,0,1/3,0,0,0,0]
\]

(C minor).

Table 2 reports:

| \(t\) | Linear fade / linear OT | Circular OT on CoF |
|---:|---|---|
| 0 | C major: [C,E,G] | C major: [C,E,G] |
| 1/3 | Cadd♯9: [C,D♯,E,G] | Fadd9: [C,F,G,A] |
| 1/2 | Cadd♯9: [C,D♯,E,G] | Gm9/C: [C,D,F,G,A,B♭] |
| 2/3 | Cadd♯9: [C,D♯,E,G] | Gm/C: [C,D,G,B♭] |
| 1 | C minor: [C,E♭,G] | C minor: [C,E♭,G] |

The authors state that the midpoint is a Wasserstein barycenter and produces a “colorless” hexatonic collection, neither major nor minor. In this example, the baselines largely fade or locally alter E toward D♯/E♭, whereas circular OT travels through harmonically named intermediate sonorities.

#### 6.3 Geometric model

There are no quantitative reconstruction, generalization, or perceptual scores. Evidence consists of the plotted embedding and the authors’ report of smooth audio transitions on the external demo.

---

### 7. Limitations and unsupported claims

#### Explicitly acknowledged by the authors

- The perceptual feature extractor can produce negative values, conflicting with OT’s non-negativity requirement.
- Integrating the extractor directly into circular OT remains future work.
- Alternative alignment objectives such as cosine or \(L_1\) distance remain unexplored.
- The scale-color coordinate \(z\) should be regularized or bounded, potentially with a truncated-Gaussian VAE or finite scalar quantization.
- Deeper integration with PTFR-conditioned generative systems is future work (DAFx.8, §8).

#### Additional limitations evident from the experiments

1. **QAP optimization is heuristic.**  
   The exact perceptual objective is NP-hard; 2-opt has no global-optimality guarantee.

2. **The alignment data are synthetic.**  
   The reported musical example and 1,024 random pairs do not establish performance on real songs, stems, expressive recordings, or noisy transcription outputs.

3. **The interpolation result is mainly illustrative.**  
   The C-major/C-minor example is musically suggestive, but there is no listening study, voice-leading benchmark, or comparison with human judgments.

4. **No temporal alignment is addressed.**  
   PTFR columns may be time-varying, but the paper aligns pitch bins, not beats, bars, phrases, or tempo curves.

5. **Root estimation remains fragile.**  
   The geometric model uses \(\arg\max(c)\) as root. Ties, inversions, modal ambiguity, bass-independent harmony, and noisy audio can violate this assumption.

6. **Permutation flexibility may exceed musical realizability.**  
   An arbitrary pitch-bin permutation preserves mass but does not necessarily correspond to a single transposition, a legal voicing transformation, or a coherent instrument-specific mapping.

7. **The geometric factorization is only weakly validated.**  
   It is trained on 106 internally constructed profiles, with no held-out evaluation or test against independent perceptual ratings.

8. **Higher-dimensional behavior is representation-dependent.**  
   Zero-padding and octave replication give different off-grid spectral behavior, so “the” 96-dimensional extension is not unique.

---

### 8. Relevance to audio/symbolic mashup alignment

#### Strongly applicable ideas

1. **Pitch-only alignment before recombination**  
   For symbolic rolls, piano-roll activations, or audio transcription chromagrams, use \(A(c)=F^TWFc\) to obtain a consonance-aware pitch representation, then estimate a permutation \(P\) between stems or phrases.

2. **Separate harmonic alignment from temporal alignment**  
   Use a conventional beat/phrase DTW or bar alignment for time, and apply the paper’s \(P\) or Hungarian assignment only to the pitch axis. This avoids conflating two fundamentally different alignment problems.

3. **Explainable transformations**  
   A transformation can expose:
   - the pitch permutation \(P\);
   - the TIV-distance reduction;
   - the OT transport plan;
   - source/target roots;
   - density \(r\);
   - scale color \(z\).

   These are much easier to explain than an opaque latent-space edit.

4. **Key-aware interpolation**  
   CoF OT provides a candidate transition mechanism for cross-key mashups, harmonic bridges, reharmonization, and controlled transitions between incompatible chord collections.

5. **Audio/symbolic common interface**  
   The same PTFR abstraction can accept:
   - chroma or CQT-derived activations from audio;
   - piano rolls;
   - MIDI-derived pitch activation maps;
   - 88-key transcription representations.

#### Important integration boundary

The paper does **not** provide a complete audio mashup algorithm. It does not address:

- source separation;
- phase coherence;
- onset/beat synchronization;
- instrument or register compatibility;
- vocal formants;
- spectral masking;
- rhythmic conflict;
- crossfade energy normalization.

Its most realistic role is an interpretable harmonic-control module within a larger mashup pipeline.

---

### 9. Concrete research ideas

1. **Real mashup benchmark**  
   Build paired symbolic/audio stem examples with known harmonic transformations. Compare:
   - no alignment;
   - circular transposition;
   - argsort;
   - Hungarian;
   - Hungarian + 2-opt;
   - learned relaxed assignment.

   Evaluate original TIV distance, chord-recognition stability, voice-leading cost, and human preference.

2. **Differentiable QAP solver**  
   Relax \(P\) to a doubly stochastic matrix using Sinkhorn or Gumbel-Sinkhorn, optimize the perceptual QAP objective, then project to a permutation and refine with 2-opt.

3. **Constrained mashup permutations**  
   Restrict \(P\) to musically realizable transformations:
   - global transpositions;
   - octave-preserving mappings;
   - scale-degree substitutions;
   - voice-leading-limited assignments.

   Compare these against unrestricted permutations.

4. **Time-aware CoF OT**  
   Compute OT plans per beat or chord segment, regularized for temporal smoothness. This would allow harmonic transitions without abrupt frame-to-frame pitch remapping.

5. **Positive perceptual OT representation**  
   Keep the raw non-negative PTFR for OT mass, but use TIV/\(A(c)\) only as the cost function. This preserves OT validity while retaining perceptual weighting.

6. **Explainable generator controls**  
   Condition a symbolic or audio generator on \((\theta,r,z)\):
   - \(\theta\): root/key;
   - \(r\): density/complexity;
   - \(z\): tonal color.

   Report transformations as explicit paths in this coordinate system.

7. **Robust root inference**  
   Replace single-frame argmax root selection with a posterior over roots using temporal context, bass information, chord recognition, or Bayesian key profiles.

8. **Perceptual validation**  
   Test whether TIV-space distances and CoF-OT paths correlate with:
   - consonance ratings;
   - perceived harmonic distance;
   - voice-leading judgments;
   - mashup acceptability.

Overall, the paper offers a useful and unusually interpretable harmonic transformation framework. Its strongest immediate research value for mashups is as a **pitch-structure alignment and explanation layer**, provided temporal, timbral, and non-negativity constraints are handled separately.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `retrieval-and-recombination`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
