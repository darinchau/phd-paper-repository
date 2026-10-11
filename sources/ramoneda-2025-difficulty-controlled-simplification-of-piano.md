---
title: "Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education"
authors: "Pedro Ramoneda, Emilia Parada-Cabaleiro, Dasaem Jeong, and Xavier Serra"
year: 2025
doi: 10.48550/arXiv.2511.16228
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/ramoneda-2025-difficulty-controlled-simplification-of-piano.pdf"
pdf_filename: ramoneda-2025-difficulty-controlled-simplification-of-piano.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education**.” **arXiv:2511.16228v2 [cs.SD], 22 November 2025**, 9 pages. No journal or conference venue is specified in the paper. The version/date appear on p. 1. The complete reference list is on pp. 8–9.

## 1. Document Information

- **Canonical source:** arXiv `2511.16228v2`; official PDF preserved as `ramoneda-2025-difficulty-controlled-simplification-of-piano.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zdkce_99rp.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliographic record

**Ramoneda, Pedro; Parada-Cabaleiro, Emilia; Jeong, Dasaem; Serra, Xavier.**  
“**Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education**.” **arXiv:2511.16228v2 [cs.SD], 22 November 2025**, 9 pages. No journal or conference venue is specified in the paper. The version/date appear on p. 1. The complete reference list is on pp. 8–9.

Important cited resources include:

- Mayer et al. (2024), “Practical End-to-End Optical Music Recognition for Pianoform Music” — source of the LMX representation.
- Ramoneda et al. (2024), “Combining piano performance dimensions for score difficulty classification” — source of the difficulty-labeling framework.
- Wu et al. (2025), “CLaMP 3: Universal Music Information Retrieval Across Unaligned Modalities and Unseen Languages” — style/content similarity model.
- XMander (2023), unofficial MuseScore dataset — source of the initial corpus.

### Research question and contribution

The paper asks whether piano-score simplification can be treated as **conditional symbolic-score translation**: given a difficult piano score, generate an easier version while preserving its musical identity, especially melody, harmony, style, readability, and playability.

The authors’ claimed contributions are:

1. A decoder-only transformer for difficulty-aware MusicXML score generation.
2. **PianoPairs**, a synthetic paired dataset of versions of the same piece at different estimated difficulty levels.
3. A mining strategy combining:
   - difficulty estimation with a calibrated Gaussian Naive Bayes classifier; and
   - stylistic similarity using CLaMP-3.
4. Public release of code, models, data, and a demonstration system (pp. 1–3).

**Interpretation:** The principal contribution is not a novel transformer architecture. It is the combination of an open synthetic-pair construction method, explicit MusicXML-oriented representation, and pair mining.

### Synthetic-data construction

#### Initial corpus

The authors pretrained on the **XMander dataset**, derived from MuseScore and downloaded in 2023:

- 80% training / 20% validation split.
- Only piano scores with two staves were retained.
- The training portion contains **136,000 scores** and approximately **450 million tokens**.
- Copyright restrictions are acknowledged (p. 5).

They selected **3,500 pieces from the validation split** as bases for synthetic generation. Using validation pieces as bases helps separate synthetic-pair construction from the pretraining corpus, although the paper does not provide a complete piece-level leakage audit.

#### Variation generation

For each of the 3,500 base pieces, the model generated **128 autoregressive variations**, yielding approximately **448,000 generated variations**.

Each variation was conditioned on:

- a **melody skyline**: the highest active pitch at each time step;
- a **12-dimensional pitch-class profile** representing harmonic context.

The authors describe these variations as sharing the original melody and harmony, but these are conditioning signals rather than hard symbolic constraints. The generated model may therefore alter details of the melody, rhythm, voicing, or harmony.

#### Difficulty labeling

Each generated score was assigned an estimated difficulty using a calibrated **Gaussian Naive Bayes classifier** based on **12 hand-crafted symbolic-score features**. The predicted level is:

\[
\hat{y}=\arg\max_y P(y\mid f)
\]

The classifier uses a nine-level difficulty scale associated with Henle-style grading. The authors retain the maximum posterior probability as confidence and discard the **least-confident 25% of variations** (p. 5).

The paper does not list the 12 features, provide the calibration procedure, or report classifier accuracy/calibration on the generated variations.

#### Style/content mining

For two generated variations of the same original piece, the authors calculate CLaMP-3 embedding cosine similarity. For each original piece and each difficulty level, they retain the **most similar 50% of candidate pairs**.

The resulting random-versus-filtered pool sizes are:

| Difficulty gap | Training pairs | Validation pairs |
|---|---:|---:|
| ≥1 level | **1.1 million** | **231,000** |
| ≥2 levels | **395,000** | **72,000** |

Before filtering, the paper reports **5.3 million pairs with a gap of at least one level** and **2.3 million with a gap of at least two levels** (p. 5).

Average CLaMP distance in the mined pair pool fell from:

- **0.296 to 0.237** for gap 1;
- **0.296 to 0.246** for gap 2.

These figures show that the filtering procedure selects pairs closer in CLaMP embedding space. They do not establish that the pairs are musically or pedagogically better according to independent human judgments.

### Representation and model

#### Linearized MusicXML

The paper uses **Linearized MusicXML (LMX)**, a depth-first traversal of the MusicXML tree that produces a flat token sequence.

It retains tokens for:

- pitch;
- duration;
- dynamics;
- notation and layout information;
- multiple piano parts/staves.

The paper’s example reduces a **1,711-character MusicXML measure to 173 characters and 23 tokens** (p. 4, Fig. 3).

This is important for the authors’ educational use case: unlike MIDI, MusicXML can preserve human-readable notation and engraving-related information.

#### Conditioning

The model prepends a conditioning prefix:

\[
X'=\{C,x_1,\ldots,x_T\}
\]

The prefix may contain:

- symbolic melody tokens from the skyline;
- a continuous harmonic embedding from the pitch-class profile.

The harmonic profile is perturbed with controlled noise:

\[
\tilde p_i=\operatorname{clip}(p_i+\epsilon_i,0,1),
\qquad
\epsilon_i\sim U(-0.2p_i,0.2p_i)
\]

and then renormalized (p. 4).

The loss is masked so that the model receives the conditioning prefix but is not trained merely to copy it. Loss is applied only to the score tokens.

#### Transformer

The reported architecture is:

- decoder-only transformer;
- **30 layers**;
- hidden size **2,048**;
- embedding size **512**;
- vocabulary size **512**;
- **8 attention heads**;
- dropout **0.1**;
- approximately **95 million parameters**;
- RoPE positional embeddings;
- FlashAttention;
- KV cache during inference.

Three models are described:

1. An unconditional pretrained base model.
2. A LoRA-finetuned melody/harmony-conditioned model.
3. A LoRA-finetuned difficulty-adaptation model.

LoRA uses rank **64** and alpha **128** (p. 5).

#### Difficulty adaptation objective

Given a difficult score \(X_{\text{hard}}\) and an easier score \(X_{\text{easy}}\), the training sequence is:

\[
X'=\{x_1,\ldots,x_T,[SEP],y_1,\ldots,y_S\}
\]

where the first part is the difficult input and the second part is the easier target. Loss is applied only to the target segment:

\[
\mathcal L=-\frac{1}{S}\sum_{s=1}^{S}
\log P(y_s\mid x_{1:T}, [SEP], y_{<s})
\]

The prose refers to conditioning on input and lower target difficulty, but the formal specification only clearly defines the `[SEP]` control token. The exact encoding of numeric difficulty levels at inference is not reported.

### Training setup

Reported settings (p. 6):

- context length up to **8,000 tokens**;
- effective batch size **4**;
- learning rate \(6\times10^{-4}\);
- AdamW;
- RTX 2080 Ti GPUs;
- fixed random seed **42**.

The paper does not report training steps, epochs, scheduler, weight decay, checkpoint-selection rule, decoding parameters, or the number of GPUs.

### Evaluation

#### Objective benchmarks

The authors evaluate two benchmarks.

##### Original benchmark

- **52 copyrighted pieces** selected after 2023 to reduce leakage.
- 10 pop, 10 rock, 10 K-pop, 10 Latin, 10 film arrangements, and 2 classical pieces.
- 20 generated variations per piece.
- The authors note that most pieces are below difficulty level 2, limiting difficulty diversity.

##### Extended benchmark

Synthetic pieces generated using melody/harmony conditioning:

- **96 pieces** total;
- level 1: 35;
- level 2: 29;
- level 3: 28;
- level 4: 4;
- 10 generated variations per piece.

The objective labels are:

- easier than the original;
- similar;
- harder.

“Dis.” is mean CLaMP cosine distance between original and generated pieces.

#### Exact objective results

##### Original benchmark — Table 1, p. 6

| Mining | Gap | Easier | Similar | Harder | CLaMP distance |
|---|---:|---:|---:|---:|---:|
| Random | 1 | 68.8% | 24.4% | 6.8% | .309 |
| Filtered | 1 | **71.8%** | 22.4% | **5.8%** | **.283** |
| Random | 2 | 66.6% | 25.0% | 8.5% | .305 |
| Filtered | 2 | **74.4%** | **17.1%** | 8.4% | **.299** |

On this benchmark, filtering improves the proportion of outputs classified as easier and reduces CLaMP distance in both gap settings.

##### Extended benchmark — Table 2, p. 6

| Mining | Gap | Easier | Similar | Harder | CLaMP distance |
|---|---:|---:|---:|---:|---:|
| Random | 1 | **76.8%** | 19.4% | 3.9% | .269 |
| Filtered | 1 | 76.3% | 19.3% | 4.6% | **.252** |
| Random | 2 | 72.1% | 23.2% | 4.7% | .315 |
| Filtered | 2 | **78.4%** | **18.6%** | **3.0%** | .317 |

The filtered gap-2 model gives the highest easier rate, **78.4%**, and the lowest harder rate, **3.0%**.

However, the authors’ statement that filtered mining “outperforms” random mining in all configurations is too strong:

- extended gap 1: filtered is slightly worse on easier rate, **76.3% vs. 76.8%**;
- extended gap 2: filtered has slightly worse CLaMP distance, **.317 vs. .315**.

Thus, the filtered strategy improves the main difficulty-direction measure in three of four settings and improves stylistic-distance measures in three of four settings, not all settings.

Figures 5–6 (pp. 6–7) show genre- and level-wise trends but do not provide exact numerical values in the text. The authors report that harder pieces are generally easier to simplify than simple pieces.

#### Subjective evaluation

Ten expert Spanish pianists participated:

- all had at least a Bachelor of Music in Piano Performance;
- all were active piano teachers;
- mean age: **40.1 years**;
- mean piano experience: **30 years**.

They evaluated six excerpts, comparing random- and filtered-model outputs on:

- easiness;
- coherence/style preservation;
- readability;
- playability;
- overall preference.

They also rated three pedagogical questions on a 1–5 Likert scale.

Exact pairwise results (p. 7, Fig. 7):

| Criterion | Filtered vs. random | Exact two-sided binomial p-value |
|---|---:|---:|
| Easiness | **44 vs. 16** | **0.0004** |
| Readability | **42 vs. 18** | **0.0027** |
| Playability | 36 vs. 24 | 0.1550 |
| Overall preference | 33 vs. 27 | 0.5190 |
| Coherence | approximately equal | not reported |

Mean pedagogical ratings:

- instructional control: **4.20 ± 1.25**;
- pedagogical alignment: **3.90 ± 1.55**;
- personalized instruction: **4.10 ± 1.22**.

The evidence supports a filtered-model advantage for perceived easiness and readability. It does **not** establish a statistically significant playability or overall-preference advantage.

### Author-stated limitations

The authors explicitly acknowledge (p. 7):

1. The method targets arrangements with a clear melody–accompaniment structure and may generalize poorly to highly polyphonic or contrapuntal music.
2. Simplification primarily affects accompaniment; melodic complexity is rarely simplified.
3. Explicit melodic-complexity control is absent.
4. Upward difficulty generation for advanced learners was not explored.
5. Evaluation relies on synthetic pairs because public human-aligned datasets are unavailable.
6. More work is needed to preserve musical character and nuance.

### Additional missing evidence and methodological concerns

These are interpretive assessments rather than claims made by the authors.

#### Proxy-based evaluation

Both central objective measures are proxy-based:

- “easier” is determined by the difficulty estimator;
- stylistic proximity is measured by CLaMP-3.

The synthetic training pairs are also selected using those same types of models. This creates potential metric circularity: the system is trained and filtered according to proxies that are later used to judge it.

There is no independent assessment of:

- actual playing time or error rate;
- hand span;
- jumps;
- voice crossing;
- rhythmic complexity;
- note density;
- student success;
- expert difficulty labels for generated outputs.

#### No human-aligned target score

The model is not evaluated against professionally prepared simplified arrangements of the same pieces. Consequently, the study establishes controlled movement according to its estimators, not equivalence to expert pedagogical adaptation.

#### Weak preservation evidence

Melody and harmony are conditioning signals, not hard constraints. The paper does not report note-level or phrase-level preservation metrics, alignment accuracy, key/harmony deviation, voice-preservation accuracy, or edit locality.

#### Limited human study

The subjective test has only ten experts and six excerpts. It includes no students, practice sessions, performance recordings, learning outcomes, or longitudinal evidence. Pairwise observations are nested within raters and excerpts, but the reported analysis uses an exact binomial test without discussing dependence or inter-rater agreement.

#### Reproducibility gaps

The paper omits:

- the 12 difficulty features;
- classifier training/calibration details;
- CLaMP-3 checkpoint and preprocessing;
- decoding temperature/top-\(p\)/sampling settings;
- training epochs and stopping criteria;
- exact pair split procedure;
- numeric target-difficulty token format;
- MusicXML validation and correction procedure;
- full benchmark identifiers;
- independent baseline results.

### Artifacts and reproducibility

The abstract says the authors “openly release” the code, dataset, and models. A footnote qualifies this as:

> “All data and code will be released upon acceptance.”

The only concrete link in v2 is the demo:

**https://pramoneda.github.io/diff2diff/**

The paper states that PianoPairs is released in MusicXML format, but the supplied manuscript provides no repository URL, model-checkpoint URL, versioned commit, license, checksum, or downloadable dataset link.

Therefore, the reproducibility claim is promising but conditional in the v2 document. The synthetic data may be openly distributable, but the original XMander/MuseScore material is subject to copyright and cannot necessarily be redistributed.

### Relevance to the explainable symbolic music programme

This work is strongly relevant as an **infrastructure and methodology precedent**, but it is not itself a mashup or repair system.

#### Relevant strengths

- **Readable symbolic representation:** LMX preserves MusicXML semantics and notation-oriented information better than MIDI.
- **Explicit conditioning:** melody skyline and harmonic profile provide interpretable control channels.
- **Synthetic paired data:** the PianoPairs strategy is directly transferable to repair and transformation tasks where aligned real data are scarce.
- **Difficulty features:** the 12 hand-crafted features and calibrated classifier suggest an interpretable difficulty-control layer.
- **Candidate mining:** CLaMP-based reranking is a useful model for selecting semantically similar transformation pairs.

#### Important mismatch

The model is primarily a one-way simplifier for two-stave piano arrangements. It does not explicitly model:

- source provenance;
- multiple musical sources;
- phrase-level alignment;
- edit operations;
- missing-note or notation-error repair;
- contrapuntal voice identity;
- minimality of edits;
- explanations of why a note was changed.

Its transformer remains largely opaque, and CLaMP embeddings provide similarity scores rather than human-readable explanations.

### Concrete research ideas

1. **Operation-labelled simplification and repair corpus**  
   Generate MusicXML pairs with explicit edit provenance: remove ornament, reduce chord density, shorten leap, simplify rhythm, repair duration, repair tie, resolve voice collision, or correct missing notes. Store the exact XML edit script alongside each pair.

2. **Explainable difficulty control**  
   Replace the opaque “easier” label with a vector of interpretable targets: note density, maximum hand span, leap size, polyphony, rhythmic subdivision, range, and voice crossings. Report feature deltas before and after generation.

3. **Constraint-aware mashup adaptation**  
   Extend the prefix to separately encode melody source, harmony source, accompaniment style, key, tempo, and phrase boundaries. Evaluate whether melody A can be retained while harmony/style B is introduced without violating voice-leading constraints.

4. **Minimal-edit repair model**  
   Use the difficulty-adaptation format for corruption-to-repair pairs. Mask only damaged regions and require unchanged context to remain identical. Rank candidates by repair confidence, edit locality, harmonic validity, and notation validity.

5. **Auditable generation pipeline**  
   Generate multiple candidates, then apply symbolic verifiers for:
   - melody preservation;
   - pitch-class/harmonic compatibility;
   - meter and duration validity;
   - playable hand span;
   - voice-crossing limits;
   - MusicXML schema validity.

   Return the accepted candidate together with the verifier outcomes and changed-note list.

6. **Independent evaluation benchmark**  
   Build a licensed benchmark of human-made simplified scores and repaired scores. Separate:
   - estimator-based difficulty;
   - symbolic complexity metrics;
   - expert ratings;
   - actual pianist performance;
   - student learning outcomes.

7. **Teacher-facing explanations**  
   Present each generated adaptation as: “difficulty reduced primarily by lowering left-hand density and maximum leap size; melody retained; harmonic profile changed by X.” This would convert the paper’s conditioning signals into usable explanations.

8. **Robust ablations**  
   Compare random pairing, confidence filtering, CLaMP filtering, explicit difficulty tokens, constrained decoding, and human-aligned pairs. This would clarify whether the improvement comes from the mining strategy, the representation, or the synthetic generator itself.

**Overall assessment:** The paper presents a useful open-data strategy for controlled symbolic-score transformation and offers a promising bridge between readable MusicXML generation and pedagogically motivated adaptation. Its strongest evidence concerns classifier-measured simplification and perceived easiness/readability. Its central claims about playability, educational impact, musical preservation, and general-purpose difficulty control remain insufficiently validated.

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
