---
title: "Why Alzheimer's Speech Screening Fails to Generalize: Bridging the Deployment Gap via Cross-Corpus Evidence Anchoring"
authors: "Zijian Lu et al."
year: 2026
doi: 10.48550/arXiv.2609.31293
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-why-alzheimer-s-speech-screening.pdf"
pdf_filename: al-2026-why-alzheimer-s-speech-screening.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Why Alzheimer’s Speech Screening Fails to Generalize: Bridging the Deploym1ent Gap via Cross-Corpus Evidence Anchoring**” [p. 1]. The embedded PDF metadata spells this as “Deployment.”

## 1. Document Information

- **Canonical source:** arXiv `2609.31293v1`; official PDF preserved as `al-2026-why-alzheimer-s-speech-screening.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41ns1u_b5x0.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper digest

### Bibliographic identity

**PDF title (as printed, including apparent typo):**  
“**Why Alzheimer’s Speech Screening Fails to Generalize: Bridging the Deploym1ent Gap via Cross-Corpus Evidence Anchoring**” [p. 1].  
The embedded PDF metadata spells this as “Deployment.”

**Authors:** Zijian Lu, Sizhe Liu, Yin Zhang, Jixuan Deng, Xinrong Lin, Xinchen Yuan, Chicheng Jin, Yiping Zuo, and Yuanchao Li [p. 1].

Affiliations are Nanjing University of Posts and Telecommunications, Shouyi Technology, University of Science and Technology of China, and University of Cambridge. The paper is dated **25 September 2026**, arXiv:2609.31293v1.

The PDF has **16 pages**, including references; there is **no appendix**.

---

### Executive summary

The paper studies whether Alzheimer’s speech-screening models generalize to unseen corpora, languages, tasks, and recording protocols. Its central finding is that:

1. Most interpretable speech markers are not directionally stable across datasets.
2. High-performing deep representations can fail catastrophically on one unseen corpus.
3. A compact, training-only-selected set of interpretable “evidence anchors” can improve worst-domain robustness when fused with an XLM-R model.
4. Mean performance and worst-domain performance require different fusion weights.

The strongest reported results are:

- XLM-R mean speaker AUC: **0.769**; worst corpus: **0.520** [§5, Table 2, p. 9].
- Balanced anchor/XLM-R fusion: **0.785 mean AUC** [§6.2, pp. 12–13].
- Anchor-heavy fusion: **0.615 worst-domain AUC**, versus **0.520** for XLM-R and **0.504** for GroupDRO [§6.2, pp. 12–13].
- However, the paired bootstrap interval for the weakest-domain improvement is **[−0.004, 0.195]**, so the improvement is not decisively significant at conventional levels [p. 13].

---

### 1. Problem and motivation

#### Author claims

The authors frame deployment as an **external-domain generalization** problem rather than an ordinary random train/test problem. A deployed system may encounter:

- new picture prompts or tasks,
- different languages,
- microphones and recording protocols,
- segmentation policies,
- ASR error profiles,
- different cohorts [§1, pp. 1–2].

They argue that:

- hand-designed markers may reverse direction across domains;
- deep representations may achieve high average performance while failing on a particular unseen corpus;
- worst-case domain performance should therefore be a primary metric [§1, p. 2].

The paper proposes a three-stage framework:

1. audit marker transferability;
2. select compact evidence anchors from source corpora;
3. fuse anchor scores with an XLM-R text score [§1, p. 2].

#### Interpretation

The important conceptual contribution is not a new speech architecture. It is a **methodological separation of predictive strength from evidence transferability**. A feature can be interpretable and predictive within one dataset while being unsafe as a cross-domain explanation.

That distinction is directly relevant to explainable music systems: a model explanation should not be treated as reliable merely because the feature name is musically meaningful.

---

### 2. Data

The paper uses four heterogeneous corpora [§3.1, Table 1, p. 4]:

| Corpus | Language | Task | Samples | Speakers | HC | Risk |
|---|---|---:|---:|---:|---:|---:|
| NCMMSC | Mandarin | Mixed | 246 | 116 | 90 | 156 |
| Pitt Cookie | English | Picture description | 547 | 291 | 241 | 306 |
| TAUKADIAL Mandarin | Mandarin | Connected speech | 507 | 169 | 222 | 285 |
| Mandarin Chou | Mandarin | Picture description | 261 | 87 | 120 | 141 |
| **Total** | — | — | **1,561** | **663** | **673** | **888** |

The binary target collapses Alzheimer’s disease, MCI, and other cognitive-impairment labels into one “risk” class [§3.1, p. 4].

Speaker IDs are corpus-prefixed, and multiple samples from one speaker are averaged before speaker-level AUC computation [p. 4].

#### Interpretation and limitation

The data deliberately combine language, task, corpus, and protocol differences. This is appropriate for stress-testing transfer, but it also makes corpus identity highly confounded with clinical and procedural factors. The paper later confirms strong corpus separability in feature space.

---

### 3. Method

#### Features and models

The interpretable pool contains **70 speech/language features**, with a predefined **24-feature core panel** covering:

- word class,
- temporal fluency,
- discourse structure,
- information content,
- speech quantity,
- lexical diversity,
- alignment quality,
- disfluency,
- repetition [§3.2, pp. 5, 8].

Deep baselines:

- frozen **768-dimensional XLM-R transcript embeddings**;
- frozen **1,024-dimensional wav2vec 2.0 layer-12 embeddings**;
- frozen **1,024-dimensional wav2vec 2.0 layer-24 embeddings** [§3.2, p. 5].

The downstream model is weighted, L2-regularized logistic regression with:

- λ = 1.0;
- L-BFGS-B optimization;
- winsorization at the 1st/99th percentiles;
- median imputation;
- z-score normalization;
- inverse-class-frequency and inverse-speaker-count weighting [§3.2, p. 5].

All preprocessing, feature selection, fitting, and calibration use source corpora only.

#### LOCO evaluation

The core protocol is **Leave-One-Corpus-Out (LOCO)**:

- train on three corpora;
- hold out the fourth as an unseen deployment domain;
- repeat for all four corpora [§3.3, p. 5].

Metrics are:

- macro-averaged speaker AUC;
- worst held-out-corpus speaker AUC [p. 5].

The comparison domain-generalization method is GroupDRO applied to frozen XLM-R features, with:

- source corpus as group;
- 100 exponentiated-gradient iterations;
- η = 0.1;
- λ = 1.0 [§3.3, p. 5].

---

### 4. Evidence-transferability audit

#### Definition

For marker \(m\) and corpus \(c\), the paper computes a within-corpus standardized effect:

\[
d_m^{(c)} =
\frac{\mu_{m,1}^{(c)}-\mu_{m,0}^{(c)}}{\sigma_m^{(c)}}
\]

where positive values indicate greater expression in the risk group [§4.1, p. 6].

A cross-corpus conflict occurs when the marker has both negative and positive effects:

\[
\min_c d_m^{(c)} < 0
\quad\land\quad
\max_c d_m^{(c)} > 0.
\]

#### Findings

The authors report [§4.2, pp. 6–7; Fig. 1]:

- **59/70** markers have cross-dataset direction conflicts.
- **20/24** core markers have cross-dataset conflicts.
- **29/70** markers reverse between task families.
- **7/24** core markers reverse between task families.
- Only **11/70** markers and **4/24** core markers are dataset-stable.

Examples reported as relatively stable:

- pronoun ratio;
- function-word ratio;
- content/function-word ratio;
- timestamp-coverage ratio.

Examples reported as protocol-sensitive:

- silence ratio;
- mean pause duration;
- long pauses per minute;
- character speech rate.

For example, silence ratio decreases in the NCMMSC risk group but increases in the other three corpora [p. 7].

#### Figure 2

Figure 2 groups standardized HC-versus-risk contrasts across all 70 features by:

- timing/pause/rate;
- lexical output;
- POS/function;
- syntax/discourse [§4.3, p. 8].

The visual pattern supports the text claim that lexical and POS features are more directionally aligned, whereas temporal and pause-related features frequently invert.

#### Figure 3

The 24 core indicators are tested individually under LOCO. The best individual marker reaches only **0.658 mean AUC**, and many markers have worst-domain AUC below 0.50 [§4.3, pp. 8–9].

The authors therefore position the indicators as **auditable complementary evidence channels**, not standalone diagnostic rules.

---

### 5. Deep-model results

#### Table 2: frozen representations under LOCO

| Representation | NCMMSC | Pitt | TAUKADIAL | Chou | Mean | Worst | Range |
|---|---:|---:|---:|---:|---:|---:|---:|
| XLM-R text | 0.520 | 0.739 | 0.850 | 0.968 | **0.769** | **0.520** | 0.447 |
| wav2vec 2.0 L12 | 0.462 | 0.502 | 0.835 | 0.955 | 0.688 | 0.462 | 0.493 |
| wav2vec 2.0 L24 | 0.454 | 0.574 | 0.800 | 0.969 | 0.699 | 0.454 | 0.515 |

[§5, Table 2, pp. 9–10]

#### Author interpretation

XLM-R is the strongest standalone representation but collapses to near chance on NCMMSC. The authors conclude that pretrained representations do not inherently solve external domain shift.

#### Interpretation

The large gap between average and worst-corpus AUC is the paper’s clearest empirical argument for reporting worst-domain metrics. The model appears excellent if only the macro-average is considered, but deployment in the NCMMSC-like environment would be unreliable.

---

### 6. Evidence-anchor protocol

#### Anchor selection

Within each LOCO fold, the authors:

1. restrict candidates to the 24 core indicators;
2. rank them by macro-averaged training-corpus AUC;
3. select \(k=4\);
4. fit a weighted L2 logistic regression on those four features [§6.1, pp. 10–11].

The held-out corpus is not used for selection, regularization, or threshold calibration.

#### Table 3

| Selector/configuration | Mean AUC | Worst AUC |
|---|---:|---:|
| P-value top four | 0.506 | 0.363 |
| Random top four | 0.542 | 0.195 |
| Evidence-ranked top four | 0.555 | 0.520 |
| All 24 core | 0.521 | 0.418 |
| All 70 indicators | 0.538 | 0.395 |
| **Source-AUC anchors** | **0.629** | **0.588** |

[§6.1, Table 3, p. 11]

The selected features vary by held-out corpus:

- NCMMSC: mean pause duration, pronoun ratio, top-5 word ratio, character speech rate;
- Pitt Cookie: silence ratio, pronoun ratio, mean pause duration, top-5 word ratio;
- TAUKADIAL: silence ratio, pronoun ratio, character speech rate, content/function ratio;
- Mandarin Chou: silence ratio, pronoun ratio, content/function ratio, adjacent sentence overlap.

Pronoun ratio is the only feature selected in all four folds [§6.1, pp. 11–12; Fig. 4].

#### Fusion

The final score is:

\[
s_\alpha =
\alpha s_{\text{anchor}}
+
(1-\alpha)s_{\text{XLM-R}}.
\]

The authors evaluate:

- \(\alpha=0.50\): balanced fusion;
- \(\alpha=0.75\): anchor-heavy fusion [§6.2, p. 11].

Figure 5 shows a trade-off: balanced fusion favors mean AUC, while heavier anchor weighting favors worst-domain AUC.

---

### 7. Main results

#### Figure 6 / corpus-level results

| Model | NCMMSC | Pitt | TAUKADIAL | Chou |
|---|---:|---:|---:|---:|
| Evidence anchors | 0.63 | 0.59 | 0.60 | 0.70 |
| XLM-R | 0.52 | 0.74 | 0.85 | 0.97 |
| GroupDRO | 0.50 | 0.74 | 0.86 | 0.97 |
| Balanced fusion | 0.59 | 0.72 | 0.87 | 0.96 |
| Anchor-heavy fusion | 0.62 | 0.71 | 0.81 | 0.94 |

[§6.2, Fig. 6, pp. 12–13]

Authors report:

- balanced fusion mean AUC: **0.785**;
- this is **0.019 above GroupDRO**;
- anchor-heavy worst-domain AUC: **0.615**;
- this is **0.111 above GroupDRO** and **0.095 above XLM-R** on the weakest domain [§6.2, pp. 12–13].

The trade-off is real: anchor-heavy fusion improves NCMMSC but reduces performance on already-easy corpora.

#### Bootstrap and stream distinctness

On NCMMSC:

- XLM-R: AUC **0.520**, 95% CI **[0.407, 0.627]**;
- anchor-heavy fusion: AUC **0.615**, 95% CI **[0.509, 0.715]**;
- paired bootstrap CI for the 0.095 improvement: **[−0.004, 0.195]** [p. 13].

The mean absolute Spearman correlation between anchor and XLM-R scores is:

- \(\rho=0.235\);
- reported orthogonality index: **0.765** [p. 13].

The streams therefore provide partly distinct information, although the uncertainty interval weakens the strength of the performance claim.

---

### 8. Controls and artifact checks

#### Table 4

| Control | Mean speaker AUC | 95% CI |
|---|---:|---:|
| Label shuffle | 0.490 | 0.465–0.514 |
| Metadata only | 0.469 | 0.416–0.500 |
| Corpus only | 0.500 | 0.500–0.500 |
| Length only | 0.580 | 0.458–0.694 |
| Corpus identity probe | **0.899** | 0.864–0.934 |

[§6.2, Table 4, p. 13]

#### Author interpretation

The shuffled-label, metadata, and corpus-only controls are near chance. Transcript length has little reliable signal. The corpus identity probe is highly accurate, confirming strong distributional separability and motivating LOCO evaluation.

#### Interpretation

The **0.899 corpus-identity-probe score is simultaneously a strength and a warning**:

- Strength: the paper demonstrates that the domains are genuinely different.
- Warning: domain, task, language, recording conditions, and clinical labels may remain entangled. The method improves robustness under these four corpus shifts, but it does not establish causal clinical invariance.

---

### 9. Limitations

#### Explicit author-stated limitations

The authors state that evaluation is limited to:

- four English/Mandarin corpora;
- one generic domain-generalization baseline;
- a simple fusion architecture;
- fixed deep representations [§7, p. 14].

They also state that future deployment requires evidence auditing and worst-case testing, not merely stronger classifiers or source-loss reweighting [§7, pp. 13–14].

#### Additional limitations evident from the paper

1. **No human or clinical validation.** Results are AUC-only; there is no clinician assessment, prospective deployment, calibration study, or utility analysis.
2. **Heterogeneous target definition.** Alzheimer’s disease, MCI, and other cognitive impairment are collapsed into one risk class.
3. **Small number of domains.** Four held-out corpora provide only four domain-level tests.
4. **Potential selection optimism.** Anchor ranking uses source-corpus AUC, but the paper does not fully specify nested source-domain validation, repeated seeds, or a confidence interval for anchor selection stability.
5. **Fixed pretrained encoders.** Fine-tuned models, newer encoders, and multimodal alternatives are not tested.
6. **No ablation of individual audit components.** The paper does not isolate the effects of the 24-feature restriction, direction audit, \(k=4\), source-AUC ranking, or the fusion normalization choices.
7. **Statistical uncertainty.** The key weakest-domain improvement has a paired bootstrap interval that includes zero.
8. **Artifact shortcuts remain plausible.** The high corpus-identity-probe score shows that the feature space strongly encodes dataset identity.

---

### 10. Artifact and reproducibility status

**What is present:**

- The four corpora are named and referenced.
- TalkBank URLs are provided for Pitt and Mandarin Chou.
- The NCMMSC/AD2021 GitHub URL is referenced [Refs. 29–31, pp. 15–16].
- The paper specifies major preprocessing, model, and evaluation settings.

**What is not present in the PDF/text:**

- no code repository for this study;
- no released checkpoints;
- no feature-extraction scripts;
- no detailed configuration files;
- no random seeds;
- no supplementary appendix;
- no explicit code/data availability statement;
- no complete feature-definition table or implementation specification.

Therefore, the artifact status is **partially reproducible from public dataset references and methodological descriptions, but no author-provided implementation artifact is identifiable in the paper**.

---

### Relevance to explainable generative music

### Direct relevance

Direct relevance is **low**. This is a clinical speech-screening paper, not a music-generation, symbolic-music, mashup, source-separation, or repair paper. It does not evaluate:

- musical structure;
- note-level generation;
- source preservation;
- harmonic compatibility;
- stem identity;
- repair correctness;
- human musical judgments.

### Methodological relevance

Methodological relevance is **high** for explainable generative music systems.

#### 1. Treat explanations as domain-transfer hypotheses

A musically meaningful feature—e.g., key consistency, chord-tone ratio, rhythmic regularity, melodic contour—may be predictive in one dataset but fail under:

- genre shift;
- instrument shift;
- performance-style shift;
- symbolic-vs-audio representation shift;
- quantization or transcription differences;
- producer or recording-domain shift.

The paper’s direction-conflict audit suggests testing whether a feature’s effect is stable across musical domains before presenting it as a reliable explanation.

#### 2. Use worst-domain evaluation

For source-preserving mashups and repair, average metrics can hide failure on:

- unfamiliar genres;
- sparse arrangements;
- live performances;
- non-Western scales;
- noisy MIDI transcription;
- unusual meters;
- out-of-vocabulary instruments.

A LOCO-style evaluation should report both mean and minimum-domain source-preservation scores.

#### 3. Separate interpretable evidence from high-capacity generation

The anchor/XLM-R fusion provides a useful design pattern:

- high-capacity generator proposes an output;
- a compact interpretable evidence model evaluates source or constraint adherence;
- the two scores are fused or used for reranking.

This is more auditable than relying on latent similarity alone.

#### 4. Dynamic anchors are preferable to a universal feature list

The paper does not conclude that every feature is bad. It finds that the useful feature subset changes by deployment domain. For music, a mashup involving vocals and drums may require different anchors from a piano-only repair task.

---

### Concrete research ideas

### A. Musical evidence-transfer audit

Create a 50–100-feature interpretable panel covering:

- beat/onset alignment;
- meter consistency;
- key and mode consistency;
- chord-tone proportion;
- voice-leading distance;
- melodic contour;
- phrase-boundary preservation;
- rhythmic density;
- instrument/timbre identity;
- source-note retention;
- edit sparsity;
- harmonic tension;
- repetition and motif preservation.

For each feature, compute domain-specific effects and flag sign reversals across genre, dataset, task, and representation.

### B. LOCO evaluation for source-preserving mashups

Hold out one:

- dataset;
- genre;
- artist;
- instrument family;
- recording condition;
- symbolic transcription pipeline.

Train on the remaining domains and report:

- source-preservation mean;
- worst-domain score;
- edit sparsity;
- musical quality;
- constraint violations;
- human preference.

### C. Evidence-anchor reranking for generation

Generate multiple mashup or repair candidates with a high-capacity model. Rerank them using a compact anchor model with features such as:

- percentage of source melody retained;
- onset displacement;
- chord compatibility;
- voice-leading violations;
- non-source insertion count;
- phrase-boundary preservation.

Compare:

1. latent-score-only ranking;
2. all-feature ranking;
3. source-domain-selected anchor ranking;
4. anchor-heavy ranking under domain shift.

### D. Source-preserving repair as constrained evidence fusion

Use two explicit streams:

- a generative reconstruction score;
- an interpretable source-preservation score.

Fuse them with a tunable weight analogous to \(\alpha\). Evaluate the mean-quality/worst-preservation trade-off rather than optimizing only average musicality.

### E. Shortcut controls for music

Replicate the paper’s controls with:

- source-ID-only features;
- duration and event-count-only features;
- loudness and recording metadata;
- genre labels;
- shuffled repair masks;
- artist or dataset identity probes.

A high source/dataset identity probe would indicate that explanations may be exploiting corpus artifacts.

### F. Confidence-aware explanations

When an anchor reverses direction across domains, do not present it as a universal explanation. Report:

- feature value;
- training-domain direction;
- conflict rate;
- target-domain uncertainty;
- whether the feature was selected as a stable anchor.

This would make explanations explicitly conditional and provenance-aware.

### G. Statistical validation

Adopt:

- speaker/song-level bootstrap equivalents;
- paired bootstrap comparisons;
- multiple random seeds;
- nested source-domain selection;
- human listening tests;
- confidence intervals for worst-domain improvements.

The paper’s own paired interval, **[−0.004, 0.195]**, illustrates why a numerical improvement should not automatically be described as statistically established.

---

### Page-by-page inspection ledger

- **p. 1:** title, authors, abstract, introduction.
- **p. 2:** deployment-gap motivation, LOCO framework, contributions.
- **p. 3:** related work and interpretability/generalization distinction.
- **p. 4:** four corpora and Table 1.
- **p. 5:** features, frozen encoders, preprocessing, LOCO, GroupDRO.
- **p. 6:** controls, effect-size definition, conflict criterion.
- **p. 7:** Figure 1 and concrete stable/unstable marker examples.
- **p. 8:** Figure 2 and 24-feature evidence-family organization.
- **p. 9:** Figure 3 and Table 2.
- **p. 10:** deep-model interpretation and anchor-selection method.
- **p. 11:** Table 3, Figure 4, anchor compositions, fusion equation.
- **p. 12:** Figure 5 and Figure 6.
- **p. 13:** Table 4, bootstrap analysis, stream correlation, conclusion.
- **p. 14:** explicit limitations, disclosure, references.
- **pp. 15–16:** remaining references only; no appendix or supplementary material.

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
