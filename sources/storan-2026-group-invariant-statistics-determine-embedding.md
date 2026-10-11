---
title: "Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky"
authors: "Liam Storan, Andreas Tolias, and Nina Miolane"
year: 2026
doi: 10.48550/arXiv.2610.00647
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/storan-2026-group-invariant-statistics-determine-embedding.pdf"
pdf_filename: storan-2026-group-invariant-statistics-determine-embedding.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The authors provide code at `https://github.com/liamstoran01/group_invariant_statistics.git` (p.31, Appendix H).

## 1. Document Information

- **Canonical source:** arXiv `2610.00647v1`; official PDF preserved as `storan-2026-group-invariant-statistics-determine-embedding.pdf`.
- **Full-paper evidence:** delegate digest `del_mv4099iy_2n3q.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and scope

**Paper:** Liam Storan, Andreas Tolias, and Nina Miolane, *Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky*, arXiv:2610.00647v1 [cs.LG], 30 September 2026. The PDF is marked **“Preprint. Under review.”**

The authors provide code at `https://github.com/liamstoran01/group_invariant_statistics.git` (p.31, Appendix H).

I reviewed the extracted text and the PDF’s 31 pages, including the main figures, Tables 1–3, and Appendices A–I.

---

### 2. Central thesis

**Author claim:** If a word family’s co-occurrence statistics are invariant, or approximately invariant, under a group \(G\), then the leading eigenspaces of its co-occurrence matrix—and therefore the geometry of quadratic word embeddings—are formed from matrix coefficients of \(G\)’s irreducible representations (irreps).

This generalizes the known result that translation-invariant statistics on a cyclic latent space produce Fourier embeddings.

The paper demonstrates:

- \(Z_{12}\) symmetry → Fourier circles for months.
- \(D_{12}\) transposition/inversion symmetry → interleaved dihedral circles for major/minor chords.
- \(SO(3)/SO(2)\) symmetry → spherical-harmonic blocks for celestial objects.

**Interpretation:** The paper’s strongest conceptual contribution is moving from “embeddings happen to form recognizable manifolds” to a testable pipeline:

\[
\text{statistical symmetry}
\rightarrow
\text{group Fourier/operator spectrum}
\rightarrow
\text{embedding geometry}.
\]

---

### 3. Theory and assumptions

#### 3.1 From co-occurrences to embeddings

The normalized co-occurrence matrix is

\[
M_{xy}
=
\frac{1}{2}
\frac{P_{xy}-P_xP_y}{P_{xy}+P_xP_y}
\tag{1, p.4; Eq.5, p.11}
\]

and the centered matrix is

\[
\widetilde M=PMP,\qquad
P=I-\frac{1}{n}\mathbf 1\mathbf 1^\top.
\]

Following Karkada et al. (2025), positive eigenpairs of \(\widetilde M\) determine the leading PCA scores of word2vec-style embeddings:

\[
W_x \text{ projected onto leading PCs}
\approx
\big(\sqrt{\lambda_i}\,v_i(x)\big)_i.
\]

Centering removes the constant/trivial representation (Appendix B.2, pp.13–14).

#### 3.2 Statistical invariance assumption

The core assumption is

\[
M_{g\cdot x,g\cdot y}=M_{x,y}
\qquad
(g\in G,\;x,y\in L).
\tag{2, p.4; Definition A.3, p.12}
\]

For a free and transitive action—a \(G\)-**torsor**—identifying words with group elements gives

\[
M_{g,h}=C(g^{-1}h),
\tag{8, p.12}
\]

where \(C:G\to\mathbb R\) is a symmetric kernel satisfying \(C(g^{-1})=C(g)\).

For a transitive but non-free action, words correspond to a homogeneous space \(G/K\), and the kernel must be **bi-\(K\)-invariant** (Appendix D, pp.20–22).

#### 3.3 Finite-group theorem

Theorem 4.1 (p.4; formal Theorem B.3, pp.13–14) states that for each irrep \(\rho\), the Fourier coefficient

\[
C(\rho)=\sum_{g\in G}C(g)\rho(g)
\tag{10, p.13}
\]

has eigenvectors \(u_\rho^{(s)}\) and eigenvalues \(\lambda_\rho^{(s)}\). The corresponding eigenfunctions are

\[
\phi_{\rho,a,s}(g)
=
\sqrt{\frac{d_\rho}{|G|}}
[\rho(g)u_\rho^{(s)}]_a.
\tag{11, p.13}
\]

Thus the embedding coordinates are selected, scaled matrix coefficients of irreps, up to orthogonal transformation and realification.

Important qualifications:

- Only positive eigenvalues contribute to the embedding construction.
- The corpus determines which irreps and columns are large.
- If embedding dimension is too small, weaker irrep components are truncated.
- Base-point choice changes no structural conclusions (Lemma B.4, pp.14–15).
- Approximate rather than exact invariance produces approximate harmonic geometry.

If \(C\) is a class function, Schur’s lemma makes \(C(\rho)\) a scalar multiple of the identity, yielding multiplicity \(d_\rho^2\) (Proposition B.5, pp.15–16).

#### 3.4 Compact groups and homogeneous spaces

For compact groups, sums become Haar integrals and the finite Fourier basis becomes the Peter–Weyl basis (Theorem C.5, pp.18–20).

For \(G/K\), Theorem D.1 (pp.20–21) restricts irreps to their \(K\)-fixed subspaces. For the sphere,

\[
S^2=SO(3)/SO(2),
\]

the relevant functions are real spherical harmonics \(Y_{\ell m}\), with dimension \(2\ell+1\). The eigenvalue for degree \(\ell\) is

\[
c_\ell
=
\frac12\int_{-1}^{1} C(t)P_\ell(t)\,dt,
\tag{p.22}
\]

where \(P_\ell\) is a Legendre polynomial.

**Author limitation:** The theorem directly concerns word embeddings, not arbitrary transformer residual activations. The sky experiment therefore treats activation Gram matrices as an empirical proxy and tests whether the same structure is present (pp.7–9).

---

### 4. Experiments

### 4.1 Cyclic case: months and the “Pringle”

**Location:** Section 5, pp.5–6; Figure 2 on p.5; Appendix E, pp.23–24.

#### Setup

- Corpus: text8, 17,005,207 tokens.
- Twelve months.
- Co-occurrence window: \(B=16\), triangular weighting \(f(d)=B+1-d\).
- “May” disambiguation retains 3,129 of 19,115 occurrences.
- Month counts after filtering: approximately 2,771–3,650 each.

For \(Z_{12}\), irreps are Fourier modes

\[
e^{2\pi i km/12}.
\]

After realification, conjugate pairs produce cosine/sine planes:

\[
\left(
\cos \frac{2\pi km}{12},
\sin \frac{2\pi km}{12}
\right).
\]

#### Results

- Average kernel predicts raw month co-occurrences with \(R^2=0.87\) (Figure 2B, p.5).
- Leading empirical modes have Fourier purities:
  - \(0.99,0.86\) for \(k=1\),
  - \(0.92,0.88\) for \(k=2\).
- Leading PCs:
  - \(k=1\) eigenvalues approximately \(2.17,1.59\),
  - \(k=2\) eigenvalues approximately \(0.88,0.76\).
- The first four empirical PCs match theory with:
  - mean per-month cosine \(0.96\),
  - median \(0.97\),
  - label-shuffle null mean \(0.35\), 95th percentile \(0.53\).
- Correctly treating “May” improves cosine prediction from \(0.90\) to \(0.96\) (Appendix E, p.23).
- The first circular plane advances roughly 31° per month; the second roughly 66° per month.
- The familiar “Pringle” is described as a sinusoidal component superimposed on a circular base.

**Author claim:** The geometry is explained by approximate \(Z_{12}\)-invariance rather than merely observed visually.

---

### 4.2 Dihedral case: Bach chords and \(T/I\)

**Location:** Section 6, pp.6–7; Figure 3, p.6; Appendices B.6 and F, pp.17 and 23–27.

#### Group and prediction

The 24 major/minor triads form a torsor for

\[
T/I \cong D_{12},
\]

where \(T\) is transposition and \(I\) is inversion. In the paper’s convention, \(D_{12}\) has order 24:

\[
D_{12}\cong Z_{12}\rtimes Z_2.
\]

There are four one-dimensional irreps and five two-dimensional irreps \(E_1,\ldots,E_5\).

For major chord \(T_m\) and minor chord \(I_m\),

\[
E_h(T_m)=R(2\pi hm/12),
\]

\[
E_h(I_m)=R(2\pi hm/12)F,
\qquad
F=\operatorname{diag}(1,-1).
\]

Each active \(E_h\) predicts two interleaved twelve-point circles:

\[
T_m:
\left(
\cos(2\pi hm/12+\theta),
\sin(2\pi hm/12+\theta)
\right),
\]

\[
I_m:
\left(
\cos(2\pi hm/12-\theta),
\sin(2\pi hm/12-\theta)
\right),
\]

with equal radius and a corpus-determined phase.

#### Data

- 371 Bach chorales from music21.
- 24,374 chord tokens.
- 92 sonority types; 24 major/minor triads comprise 78% of tokens.
- Three-token flat window.
- Additive smoothing \(\alpha=0.5\).

#### Invariance results

Projection of \(M\) onto \(T/I\)-invariant matrices explains

\[
R^2=0.822
\]

of entrywise matrix variance.

Transposition-only \(Z_{12}\) explains \(R^2=0.830\), only slightly more despite having fewer restrictions.

A chord-relabeling null gives \(p=5\times 10^{-4}\); none of 2,000 random relabelings approaches the observed \(T/I\) score (Section 6, p.7; Appendix F, p.24).

Other hypotheses perform worse:

- \(Z_{24}\): \(R^2=0.699\)
- \(P_{LR}\): \(0.442\)
- \(Z_{12}\times Z_{12}\): \(0.440\)
- latent \(Z_{12}\): \(0.632\)
- \(T/I\) conjugacy classes: \(0.435\)

#### Embedding results

- Leading plane is dominated by \(E_5\) with isotypic energy \(0.958\).
- Chance level for a two-dimensional irrep plane is \(4/24=0.167\).
- Top three Bach planes are dominated by:
  - \(E_5\): \(0.958\)
  - \(E_2\): \(0.873\)
  - \(E_3\): \(0.662\)
- Theory-to-empirical per-chord cosine:
  - first plane: \(0.98\), median \(0.99\);
  - first three planes: \(0.98,0.94,0.80\);
  - six-dimensional aggregate: \(0.95\), median \(0.96\).
- The leading \(E_5\) plane is the **circle of fifths**.

**Author claim:** The circle of fifths is not merely a property of music-theoretic notation; it can emerge because Bach chord co-occurrence statistics approximately respect \(T/I\).

#### ChordBERT replication

ChordBERT is a 4.71M-parameter masked symbolic-music model.

- Layer 3 residual activations were averaged by triad across all chorales.
- The first two PCs have high \(E_5\) isotypic energy.
- The same dihedral structure appears.
- Theory-to-ChordBERT per-chord cosine:
  - \(0.91\), median \(0.95\).
- Chord-label permutation null:
  - mean \(0.29\),
  - 95th percentile \(0.48\).

#### Data efficiency and robustness

Using ten train/test splits:

- RAW unconstrained statistics perform best by a small margin.
- \(T/I\) performs almost as well with only 19 effective parameters.
- At 12 training chorales, \(T/I\) reaches held-out cosine \(0.892\), best among tested models.
- RAW needs approximately 50 chorales—over four times as much data—to match it.
- Window-size experiments preserve rotation angles and isotypic energy; weaker third-plane values vary more.
- Eigenvalues drift substantially with window size, showing that symmetry structure is more stable than corpus-specific scale.

**Interpretation:** The most useful conclusion for symbolic music is not that all chord embeddings must be dihedral, but that a measurable \(T/I\) symmetry can provide a strong low-data inductive bias.

---

### 5. Continuous case: celestial objects

**Location:** Section 7, pp.7–9; Figures 4–5, pp.8–9; Tables 2–3, pp.29–30; Appendix G, pp.27–31.

#### LLM activation analysis

Data from Berdnikov & Liokumovich:

- 188 stars and constellations.
- 25 proximity-style prompts.
- Top 16 PCA activation coordinates per layer.
- Mistral Large 2, layer 72 of 89 selected for best linear decoding of true celestial positions.

The authors use the centered activation Gram matrix as a proxy for \(M\).

For Mistral Large 2:

- zonality \(R^2=0.490\);
- linear position-decoding \(R^2=0.905\);
- degree-1 top-three canonical subspace overlap \(0.91\);
- degree ordering approximately:
  \[
  1,1,1,2,2,2,2,2,3,\ldots
  \]
- degree-1 alignment:
  - per-object cosine \(0.92\),
  - median \(0.97\),
  - permutation null mean \(0.12\), 95th percentile \(0.17\).
- Degree-2 alignment:
  - cosine \(0.73\),
  - median \(0.82\),
  - null mean \(0.17\), 95th percentile \(0.21\).

#### Cross-model results

Table 2, p.29:

| Model | \(R^2_{\text{zonal}}\) | \(R^2_{\text{dec}}\) | Top-3 harmonic overlap |
|---|---:|---:|---:|
| Qwen3-235B | .581 | .928 | .94 |
| Mistral-Large-123B | .490 | .905 | .91 |
| GLM-4.5-Air | .484 | .904 | .91 |
| Qwen3-32B | .440 | .865 | .87 |
| Llama-3.3-70B | .395 | .898 | .91 |
| Mixtral-8x22B | .238 | .836 | .84 |
| GPT-OSS-120B | .072 | .634 | .64 |

Five of seven models show clear harmonic ordering; Mixtral is borderline and GPT-OSS is the outlier.

#### Independent book corpus

From 24 public-domain astronomy books totaling 1.6M words, four “star-guide” books were selected:

- 131k total tokens.
- 39 sufficiently counted objects.
- Kernel correlation with the Mistral activation kernel: \(0.95\).
- Degree-1 cosine:
  - \(0.55\),
  - median \(0.68\),
  - permutation null mean \(0.22\), 95th percentile \(0.32\).
- Degree-2 cosine:
  - \(0.39\),
  - median \(0.44\),
  - null mean \(0.27\), 95th percentile \(0.35\).

Text8, despite being approximately 130 times larger, gives only \(D=0.01\), \(p=0.48\), because it contains many non-astronomical uses of terms such as “algol,” “peacock,” and “mimosa.”

#### Synthetic sample-size experiment

The authors fit a zonal kernel to the books, convert it back to expected co-occurrence rates, and generate off-diagonal counts from Poisson distributions at corpus multipliers

\[
0.25,0.5,1,2,4,8,16,32,128.
\]

They run 1,000 simulations per multiplier.

Results:

- The observed book cosine \(0.55\) lies at the 93rd percentile of matched \(m=1\) simulations.
- At \(m=1\), the 5–95% band is \([0.27,0.56]\).
- The synthetic curve reaches the LLM’s \(0.92\) performance at roughly \(32\)–\(64\times\) the book corpus’s pair-count volume.

**Author interpretation:** The weaker book harmonic structure is consistent with sample-size limitations rather than a different underlying geometry.

---

### 6. Figures and tables

- **Figure 1, p.2:** visual summary: month circle, dihedral chord prism, celestial sphere.
- **Figure 2, p.5:** month eigenvalue pairs, \(Z_{12}\)-invariant kernel, empirical/theoretical circles.
- **Figure 3, p.6:** Bach and ChordBERT dihedral chord geometry.
- **Figure 4, pp.8–9:** LLM Gram-matrix zonality, harmonic degree purity, and book/LLM degree-1 alignment.
- **Figure 5, p.9:** synthetic corpus-size simulation.
- **Figure 6, p.24:** Bach isotypic energy; \(E_5,E_2,E_3\) dominate the first three planes.
- **Figure 7, p.24:** ChordBERT layer-3 irrep content.
- **Figure 8, p.26:** held-out prediction and data efficiency across eight music hypotheses.
- **Figure 9, p.26:** window-size sensitivity.
- **Table 1, p.27:** eight music symmetry hypotheses, including \(T/I\), \(Z_{12}\), \(Z_{24}\), \(P_{LR}\), \(Z_{12}\times Z_{12}\), latent \(Z_{12}\), conjugacy-class \(T/I\), and RAW.
- **Table 2, p.29:** seven-model celestial harmonic comparison.
- **Table 3, p.30:** astronomy-book selection; the four selected star guides have \(D=0.22\)–\(0.45\), while text8 has \(D=0.01\).

---

### 7. Limitations

**Explicit author limitations, pp.9 and 31:**

1. The theory applies only when a word family has an identifiable approximate group invariance.
2. Such symmetry is not expected for arbitrary language concepts.
3. Theorems apply to trained word embeddings; applying them to LLM residual streams is empirical extrapolation.
4. Celestial objects are nonuniformly sampled, requiring inverse-density weighting.
5. The astronomy result depends on carefully selected star-guide prose.
6. Finite corpora weaken harmonic recovery.
7. The paper does not establish that all observed neural representations are caused exclusively by corpus statistics.

Additional methodological limitations:

- The Bach experiment analyzes 24 triads, not the full 92-sonority vocabulary.
- The \(T/I\) hypothesis is approximate; transposition-only \(Z_{12}\) has slightly higher in-sample \(R^2\).
- Geometry is identifiable only up to orthogonal transformations, phases, and basis choices within degenerate eigenspaces.
- The paper studies representation geometry, not downstream composition quality, generation fidelity, or human musical judgments.
- The ChordBERT result uses a Gram matrix proxy rather than directly proving that the model learned the exact corpus co-occurrence operator.

---

### 8. Relevance to explicit symbolic/music latent spaces

### Author-supported implications

The Bach result supports using group harmonic coordinates as an interpretable basis for symbolic music:

- transposition corresponds to a predictable rotation;
- inversion corresponds to the reflection \(F\);
- each \(E_h\) plane has a clear harmonic index;
- radius reflects corpus statistics;
- departures from the predicted plane indicate symmetry breaking, style, or contextual information.

### Interpretation for transposition/inversion-equivariant mashups

A music model could represent a chord, motif, or phrase \(x\) by a latent vector \(z_x\) satisfying

\[
E(g\cdot x)\approx \rho(g)E(x),
\qquad g\in T/I.
\]

For mashups, this would enable:

1. **Key/inversion alignment:** estimate a relative \(g\in T/I\) between two pieces and rotate/reflection-transform one latent representation before fusion.
2. **Equivariant cross-attention:** condition attention on group-relative features rather than absolute pitch labels.
3. **Content/style separation:** use invariant quantities—norms, isotypic energies, relative phases—for harmonic function, while retaining equivariant coordinates for transposition.
4. **Counterfactual explanations:** show that a generated phrase changes according to the predicted \(T\) or \(I\) action.
5. **Symmetry-aware retrieval:** retrieve musically equivalent phrases by comparing group orbits rather than raw token sequences.

These are interpretations and proposed applications, not experiments performed in the paper.

---

### 9. Concrete research ideas

1. **Corpus symmetry benchmark:** Compute \(M\), \(T/I\)-projection \(R^2\), irrep energies, and theory-to-embedding cosine across Bach, chorales, lead sheets, pop, jazz, and multi-instrument MIDI.
2. **Equivariant symbolic VAE:** Use \(T/I\)-equivariant encoder/decoder layers with
   \[
   \|E(gx)-\rho(g)E(x)\|^2
   \]
   as a regularizer.
3. **Harmonic latent basis:** Initialize latent coordinates from \(D_{12}\) irreps and measure whether training preserves \(E_5\)-like circle-of-fifths structure.
4. **Equivariant mashup model:** Align two pieces using a learned group element, then perform cross-attention in a shared \(T/I\)-canonical frame.
5. **Explainable repair:** Project corrupted chord embeddings onto the nearest valid irrep geometry; use the residual as an uncertainty or anomaly score.
6. **Symmetry-breaking analysis:** Compare genre, composer, rhythm, meter, and instrumentation by how much they perturb the ideal \(T/I\) kernel.
7. **Beyond \(T/I\):** Test product groups combining pitch transformations with rhythmic cyclic groups, meter actions, instrument permutations, or phrase-position symmetries.
8. **Intervention tests:** Transpose or invert input sequences and verify whether model activations transform by the predicted representation matrices, rather than merely preserving output accuracy.
9. **Human-facing explanations:** Report “this latent change is primarily \(E_5\), corresponding to circle-of-fifths motion,” instead of exposing opaque neuron-level explanations.

**Bottom line:** The paper provides a mathematically principled route from measurable statistical symmetry to explicit, interpretable music latent geometry. Its strongest directly relevant evidence is the Bach result: approximate \(T/I\) invariance, \(E_5\)-dominated embeddings, a recovered circle of fifths, and substantially better low-data prediction than an unconstrained model.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `explainability-and-auditability`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
