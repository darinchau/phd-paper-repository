---
title: "Emergent Tonal Structure in Learned Chord Embeddings and Its Relation to Tonal Tension"
authors: "Maral Ebrahimzadeh, Gilberto Bernardes, and Sebastian Stober"
year: 2026
doi: 10.48550/arXiv.2609.36460
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf"
pdf_filename: ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper tests whether simple skip-gram chord embeddings can learn interpretable tonal geometry from symbolic chord co-occurrences. Twelve-fold transposition augmentation strengthens circle-of-fifths organization, transposition equivariance, key-centered structure, tonal steering, and tension stability, while the study remains a small, theory-guided triad-level probing baseline.

## 1. Document Information

- **Canonical source:** arXiv `2609.36460v1`; official PDF preserved as `ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40g0oh_t58q.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and scope

**Ebrahimzadeh, Maral; Bernardes, Gilberto; Stober, Sebastian.** “Emergent Tonal Structure in Learned Chord Embeddings and Its Relation to Tonal Tension.” **arXiv:2609.36460v1 [cs.SD], 29 September 2026**. The paper is identified as appearing in the *Proceedings of the 27th International Society for Music Information Retrieval Conference*, Abu Dhabi, 2026. CC BY 4.0. Authors are affiliated with Otto von Guericke University Magdeburg and INESC TEC, University of Porto.

Code: `https://github.com/MaraalE/chord-tonality` (PDF p. 1, footnote 1).

I inspected all **8 PDF pages**, the supplied extracted text, all tables, Figures 1–3, and Equations 1–3. There is **no appendix or separate supplementary section**; pages 7–8 contain the AI-use statement and references.

---

### Central contribution

#### Authors’ claim

The paper tests whether simple skip-gram chord embeddings, trained only from symbolic chord co-occurrences, develop:

1. Circle-of-fifths geometry.
2. Transposition-equivariant structure.
3. Key-centered regions.
4. Interpretable movement between tonal regions.
5. Tension-related quantities corresponding to TIV-based measures and human tension profiles.

The authors report that **12-fold transposition augmentation generally improves stability, tonal coherence, and interpretability**.

#### Interpretation

This is primarily a **post-hoc interpretability and probing study**, not a model with an explicitly designed tonal latent space. The embeddings are ordinary 64-dimensional skip-gram vectors; tonal structure is demonstrated through external geometric tests, key templates, and tension probes.

---

### 1. Data and representation

### Corpora

**BPS-FH**  
- Expert Roman-numeral annotations for the first movements of Beethoven’s 32 piano sonatas.
- Chord roots and qualities derived using an adapted released chord-symbol translation implementation.
- Primary dataset.

**Isophonics**  
- Beatles catalogue chord annotations.
- Only the chord-label layer is used.
- Secondary dataset.

PDF p. 2, §3.1.

### Tokenization and preprocessing

The supported labels are reduced to a vocabulary of **24 root–quality tokens**:

```text
root_quality
C_M
A_m
```

The vocabulary contains all 12 pitch-class roots in major and minor quality.

Processing:

- Major, minor, and dominant-family labels—including sevenths and selected extensions—are mapped to their corresponding major or minor triads.
- Unsupported labels delimit sequences.
- Consecutive duplicate chords are compressed.
- Sequences shorter than three tokens are removed.
- The original corpora retain 9,542 chord events for BPS-FH and 13,470 for Isophonics before the later sequence processing.
- Each corpus is augmented with all 12 pitch-class transpositions.
- Augmentation balances root distributions within each quality.

The representation **does not retain sevenths, inversions, voicing, bass motion, rhythmic salience, or non-chord tones**.

#### Table 1: original corpora

| Dataset | Sequences | Min length | Max length | Vocabulary | Valid-event coverage |
|---|---:|---:|---:|---:|---:|
| BPS-FH | 604 | 3 | 290 | 24 | 89.1% |
| Isophonics | 515 | 3 | 128 | 24 | 94.9% |

PDF p. 2, Table 1.

---

### 2. Skip-gram training

The model is implemented with **gensim** and predicts surrounding chord tokens from a center token.

Configuration:

- Context window: **5**
- Negative samples: **5**
- `min_count=1`
- No subsampling
- Embedding dimension: **64**
- Single-threaded training
- Fixed random seeds
- Two random initializations per setting
- Reported metrics are generally averaged over the two seeds

Two settings:

- **AUGMENTED:** 12-fold transposed corpus, trained for **50 epochs**
- **ORIGINAL:** non-augmented corpus, trained for **600 epochs**

The epoch counts are selected to approximately match total training-pair exposure.

PDF p. 2, §3.2.

#### Important methodological qualification

The authors explicitly acknowledge that equivariance is partly built into the augmented data: every sequence occurs under all 12 pitch-class shifts. Therefore, the results demonstrate that the skip-gram solution preserves and organizes this symmetry, but they do not establish that the symmetry was learned independently of augmentation.

---

### 3. Geometric tonal structure

### Circle of fifths

The authors use classical multidimensional scaling (MDS) to inspect the 24-chord spaces.

Measures:

1. **Cyclic ordering error:** agreement between the learned angular ordering and canonical circle-of-fifths ordering, allowing rotation and reversal.
2. **Template correlation:** Spearman correlation between learned pairwise distances and an idealized circle-of-fifths distance template.
3. **Fifth R@2:** fraction of chords whose two same-quality fifth-related neighbors appear among their two nearest neighbors.

#### Table 2: circle-of-fifths results

Values are **major / minor**.

| Dataset | Model | Cyclic error ↓ | Template correlation ↑ | Fifth R@2 ↑ |
|---|---|---:|---:|---:|
| BPS-FH | AUG | 0.000 / 0.000 | 0.868 / 0.958 | 1.000 / 1.000 |
| BPS-FH | ORIG | 0.007 / 0.007 | 0.736 / 0.793 | 0.979 / 0.771 |
| Isophonics | AUG | 0.000 / 0.000 | 0.914 / 0.780 | 1.000 / 0.958 |
| Isophonics | ORIG | 0.000 / 0.111 | 0.769 / 0.594 | 0.729 / 0.750 |

PDF p. 3, §4.1, Table 2.

#### Authors’ conclusion

Augmented embeddings show clearer and more regular circle-of-fifths organization. Non-augmented models still retain tonal organization, but particularly the minor region is less regular.

#### Figure 1

Figure 1 shows MDS projections of representative augmented and non-augmented 24-chord spaces. The augmented plot visibly arranges major and minor chords into more systematic fifth-related regions. The caption does not specify the exact dataset or random seed for the representative plots.

PDF p. 4, Figure 1.

---

### 4. Transposition equivariance

The authors transpose the chord vocabulary by \(k\) semitones and compare the resulting configuration with the original.

Measures:

- **Procrustes alignment error:** global structural mismatch after alignment; lower is better.
- **Jaccard overlap:** overlap of transposed top-8 nearest-neighbor sets; higher is better.

Results are averaged over the **11 non-identity shifts**.

#### Table 3: transposition equivariance

| Dataset | Model | Procrustes ↓ | Jaccard ↑ |
|---|---|---:|---:|
| BPS-FH | AUG | 0.074 | 0.875 |
| BPS-FH | ORIG | 0.464 | 0.609 |
| Isophonics | AUG | 0.180 | 0.792 |
| Isophonics | ORIG | 0.622 | 0.480 |

PDF p. 3, §4.2, Table 3.

#### Interpretation

Augmentation improves both global alignment and local neighbor consistency. The original embeddings retain some local transposition structure, but global alignment is much weaker.

The test is not a strict group-representation test: Procrustes alignment is performed after the fact, and the paper does not learn a fixed representation \(\rho(k)\) of pitch-class transposition.

---

### 5. Emergent key structure

The authors construct a centroid for each key by averaging embeddings of a key-specific chord set.

For C major:

\[
\{C_M,D_m,E_m,F_M,G_M,A_m\}.
\]

For A minor, they use a functional set with a major dominant:

\[
\{A_m,C_M,D_m,E_M,F_M,G_M\}.
\]

Distances of in-key chords are calculated leave-one-out to avoid evaluating a chord against a centroid containing itself.

Measures:

- **LOO gap:** mean out-of-key distance minus mean in-key distance.
- **AUC:** \(P(d_{\mathrm{in}} < d_{\mathrm{out}})\).

#### Table 4: key-centered structure

Values are **major / minor**.

| Dataset | Model | LOO gap ↑ | AUC ↑ |
|---|---|---:|---:|
| BPS-FH | AUG | 0.363 / 0.313 | 0.931 / 0.891 |
| BPS-FH | ORIG | 0.281 / 0.239 | 0.891 / 0.849 |
| Isophonics | AUG | 0.369 / 0.268 | 0.946 / 0.857 |
| Isophonics | ORIG | 0.269 / 0.197 | 0.922 / 0.825 |

PDF p. 3, §4.3, Table 4.

#### Controls

The authors report that:

- Random and label-permuted embeddings fail to recover key structure, with AUC near or below chance.
- Global sequence shuffling reduces key discrimination to approximately **AUC 0.46 / 0.58** and increases Procrustes error to **0.84**, compared with approximately **0.07** for the augmented model.
- Within-sequence shuffling preserves circle-of-fifths ordering and much key separation, with AUC approximately **0.92**, but increases Procrustes error to approximately **0.17**.

#### Authors’ interpretation

Broad tonal structure depends more on **sequence-level co-occurrence statistics** than on exact chord order.

#### Critical qualification

Key centroids are not purely emergent: the evaluation uses hand-specified diatonic and functional chord collections. Thus, the result demonstrates that the learned geometry supports these externally defined tonal categories; it does not show that the model independently discovered the exact key labels without theory-guided evaluation.

---

### 6. Tonal-region steering

The authors define a direction from a source-key centroid to a target-key centroid and apply it to **source-only chords**, meaning chords belonging to the source key but not the target key.

Metrics at steering strength \(\alpha=2.0\):

- **Continuous preference change \(\Delta\):** post-steering minus pre-steering change in  
  \(d(x,\mathrm{target})-d(x,\mathrm{source})\). More negative is better.
- **Target hit:** nearest chord after steering belongs to the target-key set.
- **Source escape:** steered chord leaves the source-key set.

#### Table 5: steering results

| Dataset | Model | Preference change ↓ | Target hit ↑ | Source escape ↑ |
|---|---|---:|---:|---:|
| BPS-FH | AUG | −0.921 | 0.630 | 0.685 |
| BPS-FH | ORIG | −0.724 | 0.377 | 0.410 |
| Isophonics | AUG | −0.840 | 0.639 | 0.667 |
| Isophonics | ORIG | −0.678 | 0.295 | 0.305 |

PDF p. 4, §4.4, Table 5.

#### Interpretation for symbolic systems

This is evidence for **interpretable tonal directions**, but not yet evidence of usable chord generation or musical editing. The paper does not decode steered vectors into complete symbolic sequences or evaluate resulting music.

---

### 7. Embedding-based tension measures

### Key-relative tension

For chord embedding \(c_t\), key centroid \(\mu_K\), and leave-one-out centroid \(\mu_K^{\mathrm{LOO}}(t)\), the authors estimate a prefix-conditioned key distribution:

\[
p_t(K)
=
\operatorname{softmax}_K
\left(
\frac{
\cos(\bar c_{1:\min(t,8)},\mu_K)
}{0.25}
\right).
\]

The prefix is capped at the first eight chords. The key-relative tension is:

\[
T_{\mathrm{key}}(t)
=
\sum_K p_t(K)
d(c_t,\mu_K^{\mathrm{LOO}}(t)).
\tag{1}
\]

Here \(d\) is cosine distance.

For this tension analysis, minor keys use a **natural-minor triadic collection**, unlike the functional dominant-major collection used in the earlier key-structure experiment.

### Contextual tension

The short-range contextual term is:

\[
T_{\mathrm{ctx}}(t)
=
d(c_t,\bar c_{t-W:t-1}),
\qquad W=3,
\tag{2}
\]

where the reference is the centroid of the previous three chord embeddings.

### Combined measure

\[
T_{\mathrm{comb}}(t)
=
T_{\mathrm{key}}(t)+\beta T_{\mathrm{ctx}}(t),
\qquad \beta=0.5.
\tag{3}
\]

PDF pp. 4–5, §5.1.

---

### 8. Transposition stability of tension curves

The authors use a model-independent subset of sequences containing at least six chords. Each sequence is transposed by \(k=0,\ldots,11\), and the resulting tension curves are compared using relative \(\ell_2\) error and correlation. Table values average over non-identity shifts \(k=1,\ldots,11\).

#### Table 6: transposition stability

| Dataset | Model | \(T_{\mathrm{key}}\) rel. \(\ell_2\) / corr. | \(T_{\mathrm{ctx}}\) rel. \(\ell_2\) / corr. | \(T_{\mathrm{comb}}\) rel. \(\ell_2\) / corr. |
|---|---|---:|---:|---:|
| BPS-FH | AUG | 0.063 / 0.883 | 0.074 / 0.995 | 0.065 / 0.976 |
| BPS-FH | ORIG | 0.173 / 0.321 | 0.246 / 0.925 | 0.180 / 0.770 |
| Isophonics | AUG | 0.144 / 0.804 | 0.200 / 0.968 | 0.155 / 0.914 |
| Isophonics | ORIG | 0.246 / 0.305 | 0.391 / 0.861 | 0.267 / 0.696 |

PDF p. 5, §5.1, Table 6.

#### Authors’ interpretation

- Augmentation mainly strengthens **global key-relative organization**.
- Short-range contextual structure remains relatively robust without augmentation.
- \(T_{\mathrm{ctx}}\) has particularly high curve-shape correlation on BPS-FH even in the original model.

---

### 9. Correspondence with TIV-based quantities

The paper compares embedding-derived quantities with matched components from the **12-dimensional Fourier-based Tonal Interval Vector (TIV)** representation.

Comparisons:

- \(T_{\mathrm{ctx}}\) vs. a TIV contextual phase-distance measure.
- \(T_{\mathrm{key}}\) vs. a TIV key-relative phase-distance measure.
- Both representations use the same hard key estimate  
  \(\hat K^t=\arg\max_K p_t(K)\).
- Values are length-weighted means of per-sequence correlations.

#### Table 7: TIV correspondence

| Dataset | Model | Context Pearson / Spearman | Key-relative Pearson / Spearman |
|---|---|---:|---:|
| BPS-FH | AUG | 0.733 / 0.701 | 0.624 / 0.698 |
| BPS-FH | ORIG | 0.707 / 0.687 | 0.513 / 0.511 |
| Isophonics | AUG | 0.637 / 0.628 | 0.526 / 0.592 |
| Isophonics | ORIG | 0.617 / 0.599 | 0.422 / 0.440 |

PDF p. 5, §5.2, Table 7.

#### Authors’ conclusion

The learned spaces capture local harmonic relationships compatible with TIV-based measures. Augmentation has its clearest advantage for the **key-relative** component; contextual correlations are comparatively similar between augmented and original models.

---

### 10. Relation to human tension ratings

The paper uses the same **12 short chord progressions** and mean human tension ratings reported by Navarro-Cáceres et al. [7].

Important details:

- Uses one representative augmented model, **seed 1**, rather than an ensemble.
- Combines:
  - learned contextual chord distance,
  - learned key-relative distance,
  - repetition,
  - a local resolution term based on decreases in key-relative distance and repetition.
- Quantities are z-normalized.
- Components are linearly combined.
- A first-order memory process smooths the result.
- Output is mapped to the unit interval.

All-12 fitted weights:

| Component | Weight |
|---|---:|
| Key-relative \(w_{\mathrm{key}}\) | 0.491 |
| Resolution \(w_{\mathrm{res}}\) | 0.343 |
| Repetition \(w_{\mathrm{rep}}\) | 0.108 |
| Contextual distance \(w_{\mathrm{ctx}}\) | 0.057 |

The measure is therefore driven mostly by **key-relative fit and hand-designed local resolution**, not by contextual embedding distance alone.

#### Table 8: human-profile agreement

| Evaluation | Pearson \(r\) | Spearman \(\rho\) | RMSE |
|---|---:|---:|---:|
| All-12 fit | 0.473 | 0.531 | 0.189 |
| Leave-one-progression-out | 0.406 | 0.456 | 0.199 |

The model reaches \(r\geq 0.6\) on **7 of 12 progressions** under both all-12 fitting and leave-one-out evaluation.

PDF p. 6, §5.3, Table 8.

### Figures 2 and 3

- **Progression A:** all models broadly reproduce the human rise-and-fall profile.
- **Progression B:** the embedding-based measure closely follows the participant curve.
- **Progression C:** the embedding model misses a pronounced human change, which the authors associate with information absent from chord labels, especially inversion.

Figure 2 compares the proposed model with TIV, Lerdahl, MorpheuS, and participant ratings. Figure 3 displays score representations for the three examples.

#### Authors’ limitation

The result is diagnostic rather than a complete perceptual tension model. Human judgments may depend on:

- Inversion
- Realized bass motion
- Voicing
- Rhythmic salience
- Non-chord tones

---

### 11. Limitations

### Explicitly stated by the authors

1. **Very restricted vocabulary:** only major/minor triads.
2. **No inversion, voicing, bass, rhythm, or non-chord-tone information.**
3. **Only 12 human-rated progressions.**
4. Human tension results are moderate and diagnostic, not a full perceptual model.
5. Future work should use larger heterogeneous corpora such as ChoCo.
6. Future work should expand beyond triads and incorporate contextualized or note-level information.

PDF pp. 6–7, §5.3 and §6.

### Additional methodological qualifications

These are interpretations rather than explicit author claims:

- The 12-fold augmentation makes transposition symmetry part of the training distribution, so the strength of the equivariance result should not be interpreted as entirely spontaneous discovery.
- Key centroids and chord collections are theory-defined evaluation constructs.
- The human measure includes two hand-designed terms and fitted smoothing, so the reported human correlation is not a pure test of the embedding geometry.
- The study uses only two random seeds and does not report confidence intervals or statistical significance tests.
- The embeddings are evaluated on the same small symbolic domains from which they are learned; the paper does not establish robust out-of-corpus generalization.
- The steering experiment operates in continuous embedding space and does not demonstrate valid discrete chord decoding, sequence generation, mashup, or repair.

---

### 12. Connection to group-equivariant representations

The natural symmetry is the cyclic pitch-class transposition group:

\[
C_{12}=\mathbb{Z}_{12}.
\]

A chord token can be represented as:

\[
x=(r,q),
\]

where \(r\in\mathbb{Z}_{12}\) is the root and \(q\in\{\mathrm{major},\mathrm{minor}\}\). Transposition by \(k\) acts as:

\[
g_k(r,q)=(r+k \bmod 12,q).
\]

An explicitly equivariant embedding would aim for:

\[
E(g_kx)\approx \rho(k)E(x),
\]

where \(\rho\) is a known or learned representation of \(C_{12}\).

The paper instead:

- Augments all sequences under \(C_{12}\).
- Learns unconstrained skip-gram vectors.
- Measures approximate equivariance after training using Procrustes alignment and neighborhood overlap.

Thus, the paper provides a useful **empirical baseline for emergent equivariance**, but not an architectural group-equivariant model.

A further nuance is that the circle of fifths and chromatic transposition are related but not identical coordinate choices. The circle-of-fifths generator corresponds to adding seven semitones rather than one, while the transposition group remains cyclic over the 12 pitch classes.

---

### 13. Relevance to explicit symbolic latent spaces

### Direct relevance

The paper supports using a symbolic chord latent space with interpretable probes:

- Circle-of-fifths neighborhoods.
- Key-centroid distances.
- In-key versus out-of-key discrimination.
- Transposition-stable tension curves.
- TIV correspondence.
- Key-to-key steering directions.

These can serve as evaluation criteria for an explicit latent space rather than relying only on reconstruction or prediction loss.

### Important distinction

The paper’s latent space is **not explicitly factorized** into:

- pitch-class/root,
- chord quality,
- harmonic function,
- key,
- inversion,
- voicing,
- rhythm,
- phrase context.

Its interpretability is discovered after training and partly supplied by external tonal templates.

For an explainable symbolic model, the strongest lesson is therefore:

> Use this skip-gram space as a transparent baseline and probe suite, then impose the desired symbolic structure explicitly.

---

### 14. Relevance to explainable mashup and repair

### Mashup

Potential use:

1. Infer a source and target tonal region.
2. Compute a centroid direction from source key to target key.
3. Use the direction to propose compatible transpositions or chord substitutions.
4. Preserve transposition-consistent relations through a \(C_{12}\)-equivariant latent layer.
5. Explain each change using:
   - source/target key centroids,
   - circle-of-fifths distance,
   - change in key-relative tension,
   - contextual chord distance.

However, the paper itself does **not** perform mashup generation or audio/symbolic sequence integration. The steering result only establishes a geometric property of the embedding.

### Repair

A repair system could use:

\[
S(c_t)=T_{\mathrm{key}}(t)+\beta T_{\mathrm{ctx}}(t)
\]

as an anomaly or tension score, then rank replacement chords by:

- lower key-relative distance,
- lower contextual distance,
- preserved chord quality/function,
- minimal transposition or edit distance.

An explanation could say:

> “Replace \(X\) with \(Y\): \(Y\) is closer to the inferred key centroid, has a smaller contextual distance to the preceding three chords, and reduces the predicted tension score by \(z\).”

The paper does not validate such repairs; this is a proposed application.

---

### 15. Concrete research ideas

1. **Architectural \(C_{12}\)-equivariant chord encoder**  
   Use a root-indexed representation with fixed cyclic shifts or Fourier/regular-representation blocks. Add an explicit loss:
   \[
   \|E(g_kx)-\rho(k)E(x)\|^2.
   \]
   Compare against augmentation-only skip-gram.

2. **Factorized symbolic latent space**  
   Separate:
   - root/key orbit,
   - chord quality,
   - functional role,
   - inversion/bass,
   - voicing and extension residuals.

3. **Equivariance plus invariance**  
   Use equivariant coordinates for root/key movement and invariant coordinates for relative harmonic function, tension, and repair confidence.

4. **Discrete steering for mashup**  
   Convert continuous centroid steering into a constrained discrete operation: key transposition, substitution, or reharmonization. Evaluate whether the selected symbolic chord sequence actually moves toward the target key while preserving rhythm and phrase structure.

5. **Tension-guided chord repair**  
   Detect high \(T_{\mathrm{key}}\) or \(T_{\mathrm{ctx}}\) events, generate candidate replacements, and optimize:
   \[
   \text{tension reduction}
   +\text{context preservation}
   +\text{minimal edit cost}.
   \]

6. **Extend beyond triads**  
   Represent a chord as root plus structured attributes for seventh, extension, inversion, bass, and voicing. Test whether the root subspace retains the paper’s circle-of-fifths geometry.

7. **Unseen-transposition evaluation**  
   Hold out selected transformations during training instead of exposing all 12 shifts. This would distinguish genuine learned equivariance from symmetry copied directly from augmentation.

8. **Larger and more heterogeneous validation**  
   Replicate on ChoCo and multiple genres, with confidence intervals over seeds, artists, pieces, and corpora.

9. **Explainability interface**  
   For every prediction or repair, expose:
   - nearest chord neighbors,
   - inferred key distribution,
   - key-centroid distances,
   - contextual-distance contribution,
   - transposition-equivalent explanation.

### Bottom line

The strongest evidence is that **simple distributional chord embeddings can organize themselves into highly interpretable tonal geometries**, especially when transposition augmentation is used. The strongest limitation is that the result remains a small, theory-guided, triad-level probing study. For explicit symbolic latent spaces, the paper is most valuable as a **baseline, diagnostic methodology, and source of measurable tonal constraints**, not as a complete architecture for explainable composition, mashup, or repair.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `theory-and-constraints`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
