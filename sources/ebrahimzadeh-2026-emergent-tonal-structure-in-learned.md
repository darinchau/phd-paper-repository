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

The paper tests whether a very simple **skip-gram embedding of chord tokens** can learn interpretable tonal geometry without explicit music-theoretic supervision. It compares:

## 1. Document Information

- **Canonical source:** arXiv `2609.36460v1`; official PDF preserved as `ebrahimzadeh-2026-emergent-tonal-structure-in-learned.pdf`.
- **Full-paper evidence:** delegate digest `del_mv42kok5_kdou.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Paper:** Maral Ebrahimzadeh, Gilberto Bernardes, Sebastian Stober, “Emergent Tonal Structure in Learned Chord Embeddings and Its Relation to Tonal Tension,” arXiv:2609.36460v1, ISMIR 2026.  
**Source inspected:** PDF and extracted text; all 8 pages, figures, and tables were reviewed.

### Central contribution

The paper tests whether a very simple **skip-gram embedding of chord tokens** can learn interpretable tonal geometry without explicit music-theoretic supervision. It compares:

- **AUG:** all 12 pitch-class transpositions of each corpus sequence.
- **ORIG:** the original, non-augmented sequences.

The augmented embeddings generally recover stronger circle-of-fifths structure, transposition equivariance, key-centered organization, interpretable key-to-key steering, and more stable tension-related quantities.

Code: **https://github.com/MaraalE/chord-tonality** (p. 1, footnote 1).

---

### Page-by-page evidence map

- **p. 1:** Abstract, motivation, introduction, related work, code link.
- **p. 2:** Related work; datasets; corpus preprocessing; Table 1; skip-gram setup.
- **p. 3:** Circle-of-fifths analysis; Figure 1; Tables 2–3; transposition equivariance; start of key analysis.
- **p. 4:** Table 4 key structure; controls; tonal-region steering; Table 5; start of tension analysis.
- **p. 5:** Tension definitions, Eqs. 1–3; Table 6; TIV comparison setup.
- **p. 6:** Table 7 TIV correspondence; human-tension experiment setup.
- **p. 7:** Figure 2, Figure 3, Table 8; limitations; conclusion and future work.
- **p. 8:** AI usage statement and references.

---

### Data and preprocessing

### Corpora (§3.1, p. 2)

1. **BPS-FH**
   - Expert Roman-numeral annotations for the first movements of Beethoven’s 32 piano sonatas.
   - Chord roots and qualities derived using an adapted released chord-symbol translation implementation.

2. **Isophonics**
   - Beatles chord annotations.
   - Only the chord-label layer was used.

Chord labels were reduced to a **24-token vocabulary**: 12 roots × major/minor quality. Major, minor, dominant-family labels, sevenths, and selected extensions were mapped to their corresponding major/minor triads. Unsupported labels marked sequence boundaries.

Important information was discarded:

- sevenths and inversions,
- voicing,
- bass realization,
- non-chord tones.

After filtering and triad reduction:

- BPS-FH: **9,542** major/minor chord events retained.
- Isophonics: **13,470** retained events.

Consecutive duplicate chords were compressed, sequences shorter than three tokens were removed, and AUG applied all 12 pitch-class transpositions while balancing root distributions within each quality.

#### Table 1: Original corpus statistics (§3.1, p. 2)

| Dataset | Sequences | Min length | Max length | Vocabulary | Valid-event coverage |
|---|---:|---:|---:|---:|---:|
| BPS-FH | 604 | 3 | 290 | 24 | 89.1% |
| Isophonics | 515 | 3 | 128 | 24 | 94.9% |

### Skip-gram configuration (§3.2, p. 2)

- Implemented with **gensim**.
- Token format: `root_quality`, e.g. `C_M`, `A_m`.
- Context window: **5**.
- Negative samples: **5**.
- `min_count=1`.
- No subsampling.
- Embedding dimension: **64**.
- Single-threaded training.
- Fixed random seeds.
- Two random initializations per setting; reported metrics are generally averaged over both seeds.
- AUG: **50 epochs** on the 12-fold transposed corpus.
- ORIG: **600 epochs** on the original corpus, approximately matching total training-pair exposure.

The model predicts surrounding chord tokens from a center chord, so all learned structure is distributional rather than explicitly labeled as tonal.

---

### Tonal geometry results

### Circle of fifths (§4.1, Figure 1, Table 2, p. 3)

The authors use classical MDS to visualize the 24-chord spaces. Figure 1 shows that AUG produces more systematically aligned major and minor regions, while ORIG remains tonal but is less regular, particularly for minor chords.

Metrics:

- **Cyclic ordering error:** deviation from canonical circle-of-fifths order, allowing rotation and reversal.
- **Template ρ:** Spearman correlation between learned pairwise distances and an ideal circle-of-fifths distance template.
- **Fifth R@2:** whether the two fifth-related neighbors occur among the two nearest neighbors within the same quality.

#### Table 2: Circle-of-fifths structure

Values are major/minor.

| Dataset | Model | Cyclic error ↓ | Template ρ ↑ | Fifth R@2 ↑ |
|---|---|---:|---:|---:|
| BPS-FH | AUG | 0.000 / 0.000 | 0.868 / 0.958 | 1.000 / 1.000 |
| BPS-FH | ORIG | 0.007 / 0.007 | 0.736 / 0.793 | 0.979 / 0.771 |
| Isophonics | AUG | 0.000 / 0.000 | 0.914 / 0.780 | 1.000 / 0.958 |
| Isophonics | ORIG | 0.000 / 0.111 | 0.769 / 0.594 | 0.729 / 0.750 |

**Interpretation:** tonal proximity, especially fifth-related proximity, emerges from chord co-occurrence alone. Augmentation makes it more precise and consistent.

### Transposition equivariance (§4.2, Table 3, p. 3)

The authors compare each learned space with its pitch-class-transposed counterpart over the **11 non-identity shifts**.

- **Procrustes error:** global geometric alignment; lower is better.
- **Jaccard:** overlap between transposed top-8 nearest-neighbor sets; higher is better.

| Dataset | Model | Procrustes ↓ | Jaccard ↑ |
|---|---|---:|---:|
| BPS-FH | AUG | 0.074 | 0.875 |
| BPS-FH | ORIG | 0.464 | 0.609 |
| Isophonics | AUG | 0.180 | 0.792 |
| Isophonics | ORIG | 0.622 | 0.480 |

The authors explicitly caution that AUG’s advantage is partly built into the data because every sequence is transposed through all 12 pitch classes. ORIG nevertheless retains some local transposition consistency despite weak global alignment.

### Emergent key structure (§4.3, Table 4, p. 3–4)

Each key is represented by the mean embedding of its associated chord set. For example, C major uses:

`C_M, D_m, E_m, F_M, G_M, A_m`

For minor keys, the functional set uses a major dominant; A minor is:

`A_m, C_M, D_m, E_M, F_M, G_M`

The authors compute:

- **LOO gap:** `mean(d_out) − mean(d_in)`.
- **AUC:** probability that an in-key chord is closer to its key centroid than an out-of-key chord.

| Dataset | Model | LOO gap major/minor | AUC major/minor |
|---|---|---:|---:|
| BPS-FH | AUG | 0.363 / 0.313 | 0.931 / 0.891 |
| BPS-FH | ORIG | 0.281 / 0.239 | 0.891 / 0.849 |
| Isophonics | AUG | 0.369 / 0.268 | 0.946 / 0.857 |
| Isophonics | ORIG | 0.269 / 0.197 | 0.922 / 0.825 |

AUG improves both separation and consistency, especially for minor keys.

#### Controls

- Random and label-permuted embeddings fail to recover key structure, with AUC near or below chance (approximately 0.5).
- Global sequence shuffling gives AUC **0.46/0.58** and Procrustes error **0.84**, compared with approximately **0.07** for AUG.
- Within-sequence shuffling preserves circle-of-fifths ordering and most key separation (AUC approximately **0.92**) but increases Procrustes error to **0.17** from **0.07**.

This suggests that broad tonal geometry depends more on sequence-level co-occurrence than exact chord order.

### Tonal-region steering (§4.4, Table 5, p. 4)

A steering vector is constructed from a source-key centroid to a target-key centroid and applied to chords belonging to the source key but not the target key.

Metrics:

- **Continuous preference change Δ:** post-steering minus pre-steering change in  
  `d(x,target) − d(x,source)`. More negative is better.
- **Target hit:** fraction whose nearest chord after steering belongs to the target-key set.
- **Source escape:** fraction leaving the source-key set.

At steering strength **α = 2.0**:

| Dataset | Model | Δ ↓ | Target hit ↑ | Source escape ↑ |
|---|---|---:|---:|---:|
| BPS-FH | AUG | −0.921 | 0.630 | 0.685 |
| BPS-FH | ORIG | −0.724 | 0.377 | 0.410 |
| Isophonics | AUG | −0.840 | 0.639 | 0.667 |
| Isophonics | ORIG | −0.678 | 0.295 | 0.305 |

This is evidence that the embedding geometry supports an interpretable, directional notion of tonal-region movement.

---

### Relation to tonal tension

### Embedding-based measures (§5.1, Eqs. 1–3, p. 4–5)

For chord embedding \(c_t\), key centroid \(\mu_K\), and leave-one-out centroid \(\mu_K^{LOO}(t)\):

\[
p_t(K)=\operatorname{softmax}_K
\left(
\frac{\cos(\bar c_{1:\min(t,8)},\mu_K)}{0.25}
\right)
\]

The first eight chords provide the prefix context.

#### Key-relative tension

\[
T_{\text{key}}(t)=
\sum_K p_t(K)d(c_t,\mu_K^{LOO}(t))
\]

This is low when the current chord fits the inferred tonal context and high when it is distant from likely key regions.

#### Contextual chord tension

\[
T_{\text{ctx}}(t)=d(c_t,\bar c_{t-W:t-1}), \quad W=3
\]

This measures displacement from the centroid of the previous three chord embeddings.

#### Combined measure

\[
T_{\text{comb}}(t)=T_{\text{key}}(t)+\beta T_{\text{ctx}}(t),
\quad \beta=0.5
\]

Transposition stability was evaluated on sequences with at least six chords, averaging over shifts \(k=1,\ldots,11\).

#### Table 6: Transposition stability

Lower relative \(\ell_2\) error and higher correlation are better.

| Dataset | Model | \(T_\text{key}\) rel. \(\ell_2\) / corr. | \(T_\text{ctx}\) rel. \(\ell_2\) / corr. | \(T_\text{comb}\) rel. \(\ell_2\) / corr. |
|---|---|---:|---:|---:|
| BPS-FH | AUG | 0.063 / 0.883 | 0.074 / 0.995 | 0.065 / 0.976 |
| BPS-FH | ORIG | 0.173 / 0.321 | 0.246 / 0.925 | 0.180 / 0.770 |
| Isophonics | AUG | 0.144 / 0.804 | 0.200 / 0.968 | 0.155 / 0.914 |
| Isophonics | ORIG | 0.246 / 0.305 | 0.391 / 0.861 | 0.267 / 0.696 |

**Main result:** augmentation primarily improves global key-relative stability. Short-range contextual tension remains comparatively robust even without augmentation.

### Correspondence with TIV quantities (§5.2, Table 7, p. 5–6)

The learned quantities are compared with matched components derived from the **12-dimensional Fourier-based Tonal Interval Vector (TIV)** representation.

| Dataset | Model | Context Pearson / Spearman | Key-relative Pearson / Spearman |
|---|---|---:|---:|
| BPS-FH | AUG | 0.733 / 0.701 | 0.624 / 0.698 |
| BPS-FH | ORIG | 0.707 / 0.687 | 0.513 / 0.511 |
| Isophonics | AUG | 0.637 / 0.628 | 0.526 / 0.592 |
| Isophonics | ORIG | 0.617 / 0.599 | 0.422 / 0.440 |

The contextual term corresponds moderately well to the TIV contextual quantity in both settings. Augmentation provides its clearest gain for the key-relative component.

### Human tension ratings (§5.3, Figure 2, Figure 3, Table 8, p. 6–7)

The authors use one representative AUG model, **seed 1**, and combine:

- embedding-based contextual chord distance,
- embedding-based key-relative distance,
- repetition,
- a simple local-resolution term based on decreases in key-relative distance and repetition.

The terms are z-normalized, linearly combined, smoothed with a first-order memory process, and mapped to \([0,1]\).

Fitted weights:

- key-relative: **0.491**
- resolution: **0.343**
- repetition: **0.108**
- contextual distance: **0.057**

#### Table 8: Human-rating correspondence

| Evaluation | Pearson \(r\) | Spearman \(\rho\) | RMSE |
|---|---:|---:|---:|
| All-12 fit | 0.473 | 0.531 | 0.189 |
| Leave-one-progression-out | 0.406 | 0.456 | 0.199 |

The model reaches \(r \geq 0.6\) on **7 of 12 progressions** in both the all-12 fit and LOOCV conditions.

Figure 2 compares the proposed model with TIV, Lerdahl, MorpheuS, and participant ratings:

- **Progression A:** most models recover the broad rise-and-fall profile.
- **Progression B:** the embedding model closely follows participants.
- **Progression C:** the embedding model misses a pronounced human-rated change.

Figure 3 contains the corresponding score representations for the three progressions.

---

### Limitations

The authors explicitly frame the tension experiment as **diagnostic rather than a complete perceptual model**.

Key limitations:

1. **Chord-label abstraction**
   - No inversions, bass motion, voicing, rhythmic salience, or non-chord tones.
   - These factors likely explain failures such as Progression C.

2. **Small and culturally narrow corpora**
   - Beethoven first movements and Beatles annotations are both Western tonal repertoires.
   - Cross-genre and cross-cultural validity is untested.

3. **Tiny vocabulary**
   - Only 24 major/minor triad tokens.
   - No explicit seventh-chord or inversion representation.

4. **Augmentation confound**
   - Transposition equivariance is partly guaranteed by including every transposition during training.
   - AUG and ORIG also use different epoch counts to match approximate pair exposure.

5. **Limited statistical replication**
   - Most reported metrics average only two seeds.
   - Human-tension analysis uses one representative augmented model.

6. **No full generative evaluation**
   - The paper demonstrates interpretable geometry and probes, but does not test whether the embedding improves composition, mashup, repair, or next-chord generation.

Future work proposed by the authors includes larger heterogeneous corpora such as **ChoCo**, expanded chord vocabularies, and contextualized or note-level information (p. 7).

---

### Relevance to explainable symbolic music AI

### Composition

The embedding provides interpretable control variables:

- distance to candidate key centroids,
- contextual displacement from recent chords,
- estimated key distribution \(p_t(K)\),
- direction from one tonal region to another.

A symbolic generator could expose these as controls such as “increase tonal stability,” “move toward D major,” or “create a controlled tension peak,” while preserving a traceable explanation in terms of embedding distances.

### Mashup and harmonic alignment

The steering experiment is directly relevant to mashup:

1. Infer the source and target tonal regions.
2. Compute a centroid-to-centroid steering direction.
3. Rank candidate chord substitutions by movement toward the target region.
4. Penalize excessive contextual distance or voice-leading cost.
5. Report each substitution as an interpretable change in source-key distance, target-key distance, and local tension.

The paper’s AUG results suggest that transposition-robust embeddings would be preferable for key-changing or cross-song mashup systems.

### Symbolic repair

The measures can support anomaly detection:

- high \(T_{\text{key}}\): chord poorly aligned with the inferred tonal context;
- high \(T_{\text{ctx}}\): abrupt local harmonic displacement;
- high combined tension: candidate repair location.

Repairs could be generated by replacing a suspicious chord with candidates that minimize a weighted objective over:

- key-relative distance,
- contextual distance,
- voice-leading distance,
- rhythmic or metrical constraints.

The paper also warns that chord embeddings alone are insufficient for repairs involving inversion, bass, or voicing.

---

### Concrete research directions

1. **Tonal-control module for a symbolic Transformer**  
   Condition generation on \(p_t(K)\), \(T_{\text{key}}\), \(T_{\text{ctx}}\), and centroid-steering vectors. Evaluate whether explanations remain faithful under interventions.

2. **Explainable mashup boundary optimization**  
   Optimize transition chords between two songs using centroid steering plus voice-leading and meter constraints. Compare AUG embeddings against fixed TIV, circle-of-fifths, and learned non-augmented baselines.

3. **Tension-aware repair benchmark**  
   Corrupt chord sequences and measure whether high embedding tension identifies the corruption. Evaluate repair accuracy and human-perceived improvement.

4. **Separate learned equivariance from augmentation leakage**  
   Train on selected transpositions and test on held-out pitch-class shifts. Compare data augmentation with explicit equivariant architectures or relative pitch representations.

5. **Hierarchical note/chord embeddings**  
   Preserve the paper’s interpretable chord-level space while adding inversion, bass, voicing, rhythm, and non-chord-tone channels.

6. **Human-calibrated tension models**  
   Fit the dynamic tension measure on larger, held-out progression collections and test cross-composer and cross-genre generalization rather than fitting only 12 progressions.

7. **Faithfulness tests for explanations**  
   Intervene on a chord’s embedding, key centroid, or contextual window and verify that predicted tension and generated repairs change in the direction claimed by the explanation.

**Bottom line:** the paper provides strong evidence that simple distributional chord embeddings can become useful, partially interpretable tonal spaces. Its most actionable contribution for explainable symbolic AI is the combination of **key-centroid geometry, transposition-stable distances, and directional tonal steering**—but reliable composition, mashup, and repair systems will need to augment this chord-level representation with note-level and temporal information.

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
