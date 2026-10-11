---
title: "A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation"
authors: "Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang"
year: 2026
doi: 10.48550/arXiv.2605.07489
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/he-2026-a-decomposed-retrieval-edit-rerank.pdf"
pdf_filename: he-2026-a-decomposed-retrieval-edit-rerank.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. **Retrieval**: find stylistically plausible melody–chord examples. 2. **Editing**: project each retrieved chord progression into a music-theoretically feasible space. 3. **Reranking**: select among feasible candidates using a soft trade-off between retrieval similarity and editing cost.

## 1. Document Information

- **Canonical source:** arXiv `2605.07489v1`; official PDF preserved as `he-2026-a-decomposed-retrieval-edit-rerank.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zsu6b_0w2k.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

**Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang.** “A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation.” *International Conference on Multimedia Retrieval (ICMR ’26)*, Amsterdam, June 16–19, 2026, 5 pages. DOI: `10.1145/3805622.3810672`; ACM ISBN `979-8-4007-2617-0/2026/06`.

- arXiv version: **2605.07489v1 [cs.SD]**, submitted **8 May 2026**.
- Authors: NetEase Cloud Music except Dichucheng Li, listed as Individual Researcher.
- Inspected the complete supplied PDF and extracted text: pages 1–5, Figures 1–5, Tables 1–2, all equations, conclusion, and references.

### 2. Paper’s central claim

The paper decomposes symbolic melody harmonization into:

1. **Retrieval**: find stylistically plausible melody–chord examples.
2. **Editing**: project each retrieved chord progression into a music-theoretically feasible space.
3. **Reranking**: select among feasible candidates using a soft trade-off between retrieval similarity and editing cost.

**Author claim:** This separation improves the diversity–feasibility trade-off, interpretability, and controllability relative to monolithic chord-generation systems (Abstract; pp. 1–2, §2).

**Interpretation:** The main contribution is architectural and procedural rather than a new generative model. The system turns chord generation into candidate-conditioned symbolic decision-making.

---

### 3. Method and algorithms

#### 3.1 Retrieval

**Memory construction** (p. 2, §2.1; Fig. 2, p. 3):

- Training melodies are clipped into structurally meaningful segments.
- A Transformer melody encoder maps each segment into a shared embedding space.
- Positive pairs are melody segments with similar chord progressions; negative pairs have dissimilar progressions.
- Figure 2 shows:
  - Transformer hidden size `h = 256`
  - six repeated encoder blocks
  - output embeddings of shape `(1, 256)`
  - positive-pair chord cosine similarity threshold `> 0.8`
- Each stored embedding is associated with its chord progression.

At inference:

- Embed the query melody.
- Retrieve **Top K = 100** nearest melody–chord candidates.
- Similarity: cosine similarity.
- Retrieval backend: **FAISS**.
- Retrieval intentionally prioritizes stylistic plausibility, not correctness.

#### 3.2 Editing / constraint projection

The editor projects a retrieved candidate \(C_r\) into feasible candidate \(C_e\):

\[
C_e = \arg\min_{C_e \in \mathcal{F}} d(C_e,C_r)
\tag{1}
\]

(p. 2, §2.2).

The feasible set \(\mathcal{F} \subset \mathcal{V}\) contains three constraint types:

1. **Tonal alignment / vertical compatibility**  
   Chords must be compatible with the input melody.
2. **Cadential resolution / horizontal structure**  
   Proper initiation and phrase-boundary cadences, explicitly mentioning authentic **V → I** resolution.
3. **Global regularization**  
   Reject harmonically implausible chords while permitting intentional genre-specific dissonance, such as jazz sonorities.

The modification distance is described as a weighted sum of penalties for these constraints, with a style parameter controlling genre-specific complexity.

Implementation:

- The chord vocabulary \(\mathcal{V}\) is defined as **48 categories**.
- Constraints are represented as transition and emission probabilities.
- Equation 1 is solved with the **Viterbi algorithm**.

**Important reproducibility limitation:** The paper does not provide the actual penalty weights, transition/emission tables, style-parameter values, key/tone/transition extraction procedure, or exact chord encoding.

#### 3.3 Reranking

For feasible candidate \(C\), the score is:

\[
S(C)=\lambda S_{\mathrm{ret}}(m,m')
 +(1-\lambda)S_{\mathrm{edit}}(d)
\tag{2}
\]

where \(\lambda\in[0,1]\) controls retrieval relevance versus editing fidelity (p. 2–3, §2.3).

- \(S_{\mathrm{ret}}\): similarity between query melody \(m\) and retrieved melody \(m'\).
- \(S_{\mathrm{edit}}\): score derived from modification cost \(d\):

\[
S_{\mathrm{edit}}(d)=
\frac{2}{1+\exp(\gamma d)}
\tag{3}
\]

where \(\gamma\) is a scaling factor.

- \(\lambda\) is selected by validation-set grid search.
- Final output:

\[
\hat{y}=\arg\max_C S(C)
\]

The paper claims that reranking preserves diversity without overriding feasibility. It also identifies three control interfaces:

- retrieved-candidate-set size \(K\)
- constraint set \(\mathcal{F}\)
- reranking weight \(\lambda\)

**Interpretation:** The resulting explanation can be decomposed into “which example was retrieved,” “which constraints caused edits,” “how much editing occurred,” and “why this feasible candidate beat the others.” However, the paper does not test explanation faithfulness.

---

### 4. Data and evaluation protocol

#### Datasets (p. 3, §3.1)

- **RWC-Pop**: paid pop-song dataset with AIST annotations.
- **Wikitest**: derived from the Wikifonia test split.
- **POP-909**: 909 professionally created pop songs.
- **Nk1k3**: internal dataset containing 1,558 labeled pop songs.

Retrieval training:

- **2,465 songs** from POP-909 and Nk1k3.
- 80/20 training/validation split.
- Songs clipped into **16-bar segments**.

Evaluation:

- **543 songs** from RWC-Pop and Wikitest.
- **4,834 melody clips**.
- Authors state no overlap with training data.

#### Metrics

The paper uses metrics from Yeh et al. [22]:

- Diversity/transition structure: **CHE, CC, CTD**
- Harmonic compatibility/tonal fitness: **PCS, MCTD, CTnCTR**

The paper does not define their formulas; it refers readers to [22].

Subjective evaluation:

- 15 randomly selected test clips.
- Clip lengths: 8–16 bars.
- 30 listeners:
  - 7 professionals
  - 15 musically trained amateurs
  - 8 non-musicians
- Five-point ratings for Harmonicity, Creativity, and Overall preference.

---

### 5. Ablation results

Table 1 reports the following values. The first three columns are printed as \(\Delta\)CHE, \(\Delta\)CC, and \(\Delta\)CTD; PCS, MCTD, and CTnCTR are reported directly.

#### RWC-Pop

| Method | ΔCHE | ΔCC | ΔCTD | PCS | MCTD | CTnCTR |
|---|---:|---:|---:|---:|---:|---:|
| Ground Truth | 1.4131 | 32.5385 | 0.8532 | 0.9978 | .1318 | .4216 |
| RER Frame | +.0579 | -.2418 | -.2083 | 1.4398 | .1280 | .4781 |
| W/o Retrieval | -.5912 | -13.0000 | -.5150 | 1.3888 | .1259 | .4751 |
| W/o Editor | -.4035 | -10.0330 | -.2454 | 1.2917 | .1307 | .4671 |
| W/o Reranking | -.2025 | -6.4506 | -.2358 | 1.3633 | .1292 | .4640 |
| Random | +.6959 | +28.6044 | +.2737 | .6288 | .1367 | .3454 |

#### Wikitest

| Method | ΔCHE | ΔCC | ΔCTD | PCS | MCTD | CTnCTR |
|---|---:|---:|---:|---:|---:|---:|
| Ground Truth | 1.2912 | 19.3926 | .4536 | .9307 | .0887 | .4206 |
| RER Frame | -.0358 | -.5989 | +.1774 | .7601 | .0864 | .3839 |
| W/o Retrieval | -.9402 | -8.5932 | -.3854 | .7554 | .0877 | .3856 |
| W/o Editor | -.6922 | -11.4041 | +.5830 | .7489 | .0887 | .3749 |
| W/o Reranking | -.0385 | -2.0430 | -.2846 | .7496 | .0891 | .3772 |
| Random | +.8813 | +26.4985 | +.5053 | .7122 | .0906 | .3657 |

#### Author interpretation

- Removing retrieval substantially reduces diversity and coverage.
- Removing editing damages melody–chord compatibility and increases unstable transitions.
- Removing reranking has limited feasibility impact but produces a consistent preference-score decline.
- Retrieval and editing have opposing effects on CTD:
  - without retrieval: progressions become conservative;
  - without editing: progressions become excessive or erratic.
- All variants outperform random according to the authors.

---

### 6. Baselines and comparison results

Baselines in Table 2:

- **TransformerLM** [9]
- **Bi-LSTM** [11]
- **HMM** [12]
- Ground truth

#### RWC-Pop

| Method | ΔCHE | ΔCC | ΔCTD | PCS | MCTD | CTnCTR |
|---|---:|---:|---:|---:|---:|---:|
| Ground Truth | 1.4179 | 24.6207 | .8590 | .7896 | .1322 | .4349 |
| RER Frame | -.2048 | -4.9081 | -.2160 | 1.0764 | .1262 | .4824 |
| TransformerLM | -.4440 | -7.3678 | -.3294 | 1.0192 | .1285 | .4181 |
| Bi-LSTM | -.3624 | -8.7619 | -.4310 | .9465 | .1469 | .4814 |
| HMM | -.5041 | -8.3563 | -.2475 | .6527 | .1285 | .4732 |

#### Wikitest

| Method | ΔCHE | ΔCC | ΔCTD | PCS | MCTD | CTnCTR |
|---|---:|---:|---:|---:|---:|---:|
| Ground Truth | 1.2919 | 19.2980 | .4540 | .9218 | .0884 | .4195 |
| RER Frame | -.0372 | -.6189 | +.1777 | .9432 | .0884 | .4835 |
| TransformerLM | -.1423 | -1.4957 | -.0257 | 1.3067 | .0929 | .4622 |
| Bi-LSTM | -.1178 | -2.4072 | -.0484 | .5511 | .0977 | .4624 |
| HMM | -.3163 | -2.6963 | +.3784 | .7226 | .0889 | .3777 |

#### Author’s claims

- HMM provides harmonic stability but overly conservative diversity.
- Bi-LSTM has loose transitions and the highest MCTD on RWC-Pop.
- TransformerLM performs strongly on local relationships but has weaker CHE/CC.
- RER has the best overall balance according to the authors and is closer to ground truth on diversity measures.
- RER “outperforms Transformer-based models without additional GPU cost.”

**Caveat:** Table 2 excludes segments that do not satisfy baseline generation conditions, so its ground-truth rows differ from Table 1. No compute measurements are supplied to substantiate the GPU-cost claim.

---

### 7. Figures and qualitative evidence

- **Figure 1, p. 3:** Pipeline from input melody through memory retrieval, editor, reranker, and final chord output.
- **Figure 2, p. 3:** Six-block, 256-dimensional Transformer melody encoder and contrastive-pair construction.
- **Figure 3, p. 3:** Conceptual candidate progression:
  - retrieved candidates \(C_r\)
  - projection into feasible set \(\mathcal{F}\)
  - final selection using \(S(C)\)
- **Figure 4, p. 4:** Bad case. In **2 evaluation examples**, retrieval returns chord sequences distant from \(\mathcal{F}\); editing makes substantial modifications, yielding a conservative progression.
- **Figure 5, p. 4:** Boxplots for Harmonicity, Creativity, and Overall preference. The paper gives no numerical means or statistical tests. Authors describe RER as the most balanced system, while HMM tends toward rigid correctness and Bi-LSTM/TransformerLM toward randomness.

---

### 8. Limitations and reproducibility

#### Explicitly reported

- Retrieval failures occurred in **2 cases**, approximately **2% of the evaluation**.
- These failures cause heavy editing and conservative outputs.
- Future work: a global controller over retrieval, editing, and reranking to reduce manual tuning.
- Table 2 uses a filtered subset of clips, producing different ground-truth values from the ablation.

#### Additional limitations evident from the paper

- No code, model checkpoint, or complete configuration is supplied in the paper.
- Nk1k3 is internal and unavailable; RWC-Pop is paid.
- Missing:
  - optimizer, batch size, epochs, and random seeds;
  - exact train/validation song lists;
  - encoder input representation;
  - negative-sampling procedure;
  - constraint weights;
  - transition/emission probabilities;
  - style parameter;
  - \(\gamma\) and selected \(\lambda\);
  - exact 48-category vocabulary.
- Evaluation is restricted to pop-style melody harmonization.
- The system retrieves existing progressions and edits chord categories; it does not generate note-level counterpoint, orchestration, voice-leading, or multi-source recomposition.
- Subjective evaluation is small: 15 clips and 30 listeners, with no reported significance tests or confidence intervals.
- The paper calls the pipeline interpretable, but does not evaluate whether its explanations are faithful to actual causal decisions.

---

### 9. Relevance to explainable symbolic mashup and repair

#### Directly useful ideas

1. **Candidate-conditioned generation**  
   Rather than asking one model to invent and validate simultaneously, maintain explicit alternatives and record:
   - retrieved source/example;
   - similarity score;
   - candidate chord progression;
   - constraints violated;
   - edits applied;
   - edit cost;
   - reranking terms.

2. **Minimal symbolic repair**  
   Equation 1 is closely aligned with provenance-preserving repair:

   \[
   \text{choose the feasible repair minimizing weighted modification cost}
   \]

   For mashups, \(d\) could penalize:
   - deleting protected source notes;
   - changing recognizable motifs;
   - changing rhythm or meter;
   - altering bass motion;
   - introducing voice-leading violations;
   - breaking phrase/cadence structure.

3. **Hard constraints versus soft preferences**  
   Put non-negotiable requirements in \(\mathcal{F}\), such as meter, range, protected notes, collision avoidance, and cadence. Put compatibility, novelty, source identity, and stylistic preference into reranking.

4. **Inspectable alternatives**  
   Return the top feasible candidates rather than only \(\hat y\). This supports counterfactual explanations: “If source identity were weighted more heavily, candidate B would win.”

#### Important mismatch

The paper’s retrieval is melody-to-chord retrieval, not two-source mashup retrieval. It has no representation of:

- source A versus source B;
- provenance;
- motif identity;
- alignment uncertainty;
- conflict diagnosis;
- orchestration roles;
- novelty beyond retrieved progressions.

Therefore, its interpretability claim should be transferred to mashups cautiously: the decomposition is promising, but not yet an explanation-faithfulness result.

---

### 10. Concrete research directions

1. **Provenance-aware RER for mashups**  
   Retrieve aligned excerpts and candidate transformations from both sources; attach source labels to every note, phrase, and operation.

2. **Conflict-aware editor**  
   Extend Viterbi or constrained dynamic programming with explicit conflict classes: pitch clash, meter conflict, cadence conflict, range conflict, voice-leading conflict, and texture collision.

3. **Protected-material constraints**  
   Define hard preservation sets for recognizable melody/motif material and use weighted edit costs for everything else.

4. **Multi-objective reranking**  
   Replace a single \(\lambda\) with a Pareto front over:
   - source identity A;
   - source identity B;
   - compatibility;
   - structural coherence;
   - novelty;
   - playability;
   - edit magnitude.

5. **Explanation faithfulness tests**  
   Evaluate whether removing a claimed constraint or changing its weight actually changes the output. Add counterfactual candidate tests and explanation agreement with expert annotations.

6. **Candidate-set diagnostics**  
   Measure retrieval coverage, diversity, source recognizability, and failure probability before editing. The paper’s 2% retrieval-failure case suggests that retrieval distance should be an explicit confidence signal.

7. **Global controller with auditability**  
   Learn \(K\), constraint weights, and reranking weights, but expose them and compare learned decisions against manually specified controls.

8. **Benchmark for repair and recomposition**  
   Include paired sources, annotated conflicts, protected material, minimal-repair targets, provenance labels, and separate evaluation of compatibility, identity, coherence, novelty, playability, and explanation faithfulness.

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
