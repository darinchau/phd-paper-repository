---
title: "Exploring Inherent Properties of the Monophonic Melody of Songs"
authors: "Zehao Wang, Shicheng Zhang, and Xiaoou Chen"
year: 2020
doi: 10.48550/arXiv.2003.09287
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2020-exploring-inherent-properties-of-the.pdf"
pdf_filename: wang-2020-exploring-inherent-properties-of-the.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. computationally tractable, 2. semantically meaningful, 3. related to human perception/composition, 4. interpretable, and 5. useful for controlling generation or evaluation.

## 1. Document Information

- **Canonical source:** arXiv `2003.09287v1`; official PDF preserved as `wang-2020-exploring-inherent-properties-of-the.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41ns1t_b3k5.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliographic identity

- **Title:** *Exploring Inherent Properties of the Monophonic Melody of Songs*
- **Authors:** **Zehao Wang**, **Shicheng Zhang**, and **Xiaoou Chen**
- **Affiliations:** Peking University; University of Illinois at Urbana-Champaign; Peking University.
- **arXiv:** 2003.09287v1, [cs.SD], 20 March 2020.
- **PDF length:** 8 pages; no appendix. Page 8 begins the references.

### 1. Problem and scope

#### Author claims

The paper argues that symbolic-music research lacks features that are simultaneously:

1. computationally tractable,
2. semantically meaningful,
3. related to human perception/composition,
4. interpretable, and
5. useful for controlling generation or evaluation.

They contrast abstract mathematical music theories, which they regard as difficult to compute, with low-level MIDI statistics that they regard as rigid and weakly connected to perception (**p.1–3, §§1–2.3**).

The precise scope is deliberately narrow:

- monophonic melody;
- note pitch and duration;
- MIDI/sheet-music-like symbolic representation;
- no audio;
- no harmony–melody relationship;
- no lyrics;
- no bar/meter representation (**p.2–4, §3**).

The authors claim that their features are broadly genre-independent and applicable across tonal, atonal, and different-temperament settings (**abstract, pp.1–2, §5**). This is an author claim, not strongly demonstrated experimentally.

### 2. Proposed representation and features

A note is represented as:

\[
N=(P,d)
\]

where \(P\) is relative pitch and \(d\) is relative duration. A rest has duration only. A melody is:

\[
M=K_1K_2\ldots K_n
\]

where each \(K_i\) is a note or rest (**p.3, §3**).

#### Melodic Center of Gravity (MCG)

For a rest-free melody:

\[
MCG_M=\frac{\sum_i d_iP_i}{\sum_i d_i}
\]

This is intended to describe sentence-wise melodic height while weighting pitches by duration (**p.4, §3.1**).

The simpler duration-independent mean pitch is given as:

\[
MG_M=\frac{\sum_i P_i}{n}
\]

but the authors argue that it loses temporal information. For rests, they recommend adding the rest duration to the preceding note (**p.4, §3.1**).

#### Local and Global Melody Dynamic

The paper defines a pitch-duration “moment”:

\[
pm(N)=dP
\]

(**p.5, §3.2.1**).

For adjacent notes, local melody dynamic is:

\[
LMD_\Phi(N_1,N_2)
=
|pm(\hat N_1)-pm(\hat N_2)|
\]

where \(\Phi\) transforms the pair into \(\hat N_1,\hat N_2\). The transformation is designed around five perceptual assumptions:

- symmetry;
- decay as durations increase;
- convexity in time;
- pitch-translation invariance;
- monotonicity with respect to pitch interval (**p.5, §3.2.1**).

Their concrete transformation is:

\[
\hat N_1=
\left(
\max(0,P_1-P_2),
\frac{d_1}{d_1+d_2}e^{1/d_1+1/d_2}
\right)
\]

\[
\hat N_2=
\left(
\max(0,P_2-P_1),
\frac{d_2}{d_1+d_2}e^{1/d_1+1/d_2}
\right).
\]

For a complete melody, the local values form an LMDS:

\[
\Delta_\Phi M=
(LMD_\Phi(N_1,N_2),\ldots,LMD_\Phi(N_{n-1},N_n)).
\]

Global melody dynamic is any selected norm:

\[
GMD_\Phi(M)=\|\Delta_\Phi M\|
\]

and normalized GMD is:

\[
nGMD_\Phi(M)=
\frac{\|\Delta_\Phi M\|}{|M|-1}.
\]

The authors associate:

- \(L_\infty\)-GMD with irregularity;
- \(L_1\)-GMD with time-dependent dynamic (**p.5, §3.2.1**).

They also give an alternative cosine-based formulation treating pitch and duration as orthogonal coordinates. The paper calls the cosine itself “Alternative Local Melody Dynamic,” although mathematically it is a similarity unless transformed, e.g. \(1-\cos\) (**p.5, §3.2.1**).

#### Melody Dynamic Range

\[
DR(M)=
\max_{P\in P(M)}P-
\min_{P'\in P(M)}P'
\]

This measures pitch span, interpreted as related to vocal range, tension, and expression (**p.6, §3.2.2**).

#### Rhythm Dynamic

The paper starts from nPVI:

\[
nPVI=
\frac{100}{n-1}
\sum_{i=1}^{n-1}
\left|
\frac{d_i-d_{i+1}}{(d_i+d_{i+1})/2}
\right|.
\]

It then defines a first normalized pairwise-variation sequence and applies the same operation again. The second-order sequence is:

\[
\Delta^{(2)}R(M)=\Delta^{(1)}\Delta^{(1)}R(M).
\]

Rhythm Dynamic is:

\[
RD(M)=\|\Delta^{(2)}R(M)\|
\]

and normalized Rhythm Dynamic is:

\[
nRD(M)=\frac{RD(M)}{|M|-2}.
\]

The motivation is that two melodies with different grooves may have different nPVI but similar higher-order rhythmic structure (**p.6, §3.2.3**).

### 3. Figures and examples

All figures are examples or visualizations rather than benchmark experiments.

- **Figure 1, p.3:** “I Will Wait for You” by Michel Legrand. Shows motif transformations, verse/chorus/recapitulation structure, and sentence-wise MCG, GMD, and RD.
- **Figure 2, p.4:** Demonstrates why duration-weighted MCG differs from ordinary mean pitch.
- **Figure 3, p.4:** Bass line from John Williams’s “Shark Theme” compared with a single-pitch rhythm pattern.
- **Figure 4, p.4:** Paired examples intended to illustrate local melody dynamic.
- **Figure 5, p.6:** First measure has nPVI 0; second has nPVI 66.66. The authors report both have RD 0, while their melody-dynamic values are 42.64 and 182.57.
- **Figure 6, p.7:** “Autumn Leaves,” with MCG, normalized \(L_\infty\)-GMD, and RD plots.
- **Figure 7, p.7:** “Fly Me to the Moon,” with the same feature plots.
- **Figure 8, p.7:** Part of Justin Bieber’s “Love Yourself,” with the same feature plots.

The authors interpret the “I Will Wait for You” visualization as showing greater GMD and MCG in the chorus despite relatively low RD (**pp.6–7, §3.3**).

### 4. Experiments and results

#### Human unit-selection experiment

The experiment used:

- 10 participants:
  - 2 professionals,
  - 3 enthusiasts,
  - 5 ordinary listeners;
- 10 songs from the real-world dataset;
- nine combinations of pitch and duration units;
- visualizations containing MCG, GMD, and RD (**p.7, §4.1**).

The table reports:

| Pitch unit | Duration unit | Score |
|---:|---:|---:|
| 0.5 | 0.5 | 3 |
| 0.5 | 1 | 5 |
| 0.5 | 2 | 4 |
| 1 | 0.5 | 7 |
| **1** | **1** | **56** |
| 1 | 2 | 8 |
| 2 | 0.5 | 2 |
| 2 | 1 | 3 |
| 2 | 2 | 2 |

Units are semitones and quarter-lengths. The authors conclude that **(1,1)** best matches human perception (**p.7, Table 1, §4.1**).

#### Important reproducibility issue

The reported scores sum to **90**, whereas 10 participants × 10 songs would suggest 100 selections if one selection was made per participant/song. The paper does not explain this discrepancy.

No confidence intervals, statistical tests, participant-level results, song-level results, or inter-rater agreement are reported.

#### Dataset experiment

The paper names two sources:

1. the **Hooktheorytab/lead-sheet dataset**;
2. a **C-pop dataset created by the authors**.

It says selected data, code, and useful data were available in a GitHub repository (**p.7, §4.2**). However, it reports no dataset sizes, selection criteria, preprocessing details, train/test split, or quantitative extraction results.

### 5. Limitations

#### Explicitly acknowledged by the authors

The paper states that it does **not** provide criteria for deciding whether a melody is “good” or “bad”; it proposes interpretable descriptors instead (**p.7, §5**).

#### Methodological limitations

- Very narrow monophonic scope.
- Harmony, lyrics, meter, bar position, instrumentation, and polyphonic interaction are excluded.
- MCG handles rests using an ad hoc “add rest duration to the previous note” rule.
- Results depend on pitch and duration units.
- Sentence segmentation is assumed but not operationally specified.
- The \(pm=dP\) model is a simple heuristic, not perceptually validated as a general law.
- The claimed style/genre independence of RD is asserted, not established through a dedicated experiment.
- No comparison with learned representations, jSymbolic features, nPVI baselines, or human-rating predictors.
- No automatic generation, evaluation, mashup, or repair system is actually implemented.
- The claim of applicability to atonal music is not tested with a reported atonal dataset.
- The “10 participants/10 songs” experiment is small and has the score-total inconsistency noted above.

### 6. Artifact status

#### Paper-reported status

The paper claims that “all the experimental data” and “all the code and useful data” are in:

- `https://github.com/wayne391/lead-sheet-dataset`
- `https://github.com/water45wzh/exploring_melody`

#### Current availability check

- `wayne391/lead-sheet-dataset` is currently reachable. Its README describes TheoryTab-derived lead sheets, MIDI and source downloads, and code for conversion. It reports 18,843 successfully parsed sections from 18,986 sections, but this is repository metadata, not necessarily the subset used in this paper.
- `water45wzh/exploring_melody` currently returns **404 / repository not found**. Therefore, the paper’s claimed companion code and C-pop experimental data are not presently verifiable from that URL.
- No supplementary appendix or reproducibility package is included in the PDF.

### 7. Relevance to explainable symbolic-music AI

#### Direct relevance

The paper provides a useful vocabulary for explaining symbolic melody at phrase level:

- **MCG:** “this phrase is globally higher/lower.”
- **GMD:** “this phrase contains stronger local pitch-duration changes.”
- **RD:** “this phrase has more/less second-order rhythmic variation.”
- **DR:** “this phrase occupies a wider/narrower pitch range.”

These are more interpretable than latent vectors and potentially more flexible than conditioning a generator on fixed interval strings.

#### Interpretation for mashups

A mashup system could:

1. segment two melodies into phrases;
2. normalize pitch relative to key and duration relative to beat;
3. align their MCG/GMD/RD trajectories;
4. use feature mismatch to select compatible phrase transitions;
5. preserve harmony and arrangement through a separate compatibility model.

This is a proposed application, not evaluated by the authors.

#### Interpretation for repair

For symbolic repair, compute feature residuals before and after a corruption:

- MCG shift detects contour distortion;
- GMD spikes detect implausible pitch-duration transitions;
- RD changes detect rhythmic irregularity;
- DR detects range expansion or collapse.

A repair optimizer could minimize:

\[
\text{edit cost}
+
\lambda_1|\Delta MCG|
+
\lambda_2|\Delta GMD|
+
\lambda_3|\Delta RD|
\]

while preserving unaffected notes. This would provide an explicit explanation such as: “the repair restores the phrase’s contour and removes an abnormal local dynamic spike.”

### 8. Concrete research directions

1. **Feature-conditioned hierarchical generation:** generate phrase-level MCG/GMD/RD targets first, then realize notes under those targets.
2. **Explainable repair:** use feature residuals to identify suspicious notes and constrained search to repair them.
3. **Mashup compatibility scoring:** compare normalized feature trajectories across candidate melodies before harmonic or rhythmic alignment.
4. **Counterfactual explanations:** show which note-duration changes caused an MCG or GMD change.
5. **Large-scale validation:** test genre, culture, tonality, atonality, meter, and listener expertise with mixed-effects statistical models.
6. **Polyphonic extension:** add voice-specific and ensemble-level MCG/GMD/RD while separately modeling harmony and voice-leading.
7. **Representation audit:** compare these features with nPVI, jSymbolic, learned embeddings, and human judgments rather than assuming superiority.
8. **Robust segmentation:** make phrase boundaries, rests, tempo, meter, and transposition explicit; these are essential for reliable mashup and repair use.

**Overall assessment:** The paper is a promising proposal for interpretable, low-dimensional symbolic-melody descriptors, but it is a feature-definition and visualization paper—not yet a validated explainable generation, mashup, or repair method.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `data-and-representation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
