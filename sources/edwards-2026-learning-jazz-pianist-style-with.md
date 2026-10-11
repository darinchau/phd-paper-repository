---
title: "Learning Jazz Pianist Style with Cross-Attention Conditioning"
authors: "Drew Edwards, Akira Maezawa, and Simon Dixon"
year: 2026
doi: 10.48550/arXiv.2610.02918
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/edwards-2026-learning-jazz-pianist-style-with.pdf"
pdf_filename: edwards-2026-learning-jazz-pianist-style-with.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper cites Aria [4], PiJAMA [14], the Deep Pianist Identification benchmark [5], Flamingo [15], and Classification Accuracy Score [6] as its main methodological precedents.

## 1. Document Information

- **Canonical source:** arXiv `2610.02918v1`; official PDF preserved as `edwards-2026-learning-jazz-pianist-style-with.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zsu6a_5qdz.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded paper digest

**Inspection scope:** 8/8 PDF pages and extracted text inspected, including Tables 1–3, Figures 1–6, Equations 1–3, references, AI-use statement, ethics statement, and acknowledgments.

### 1. Bibliography and version

**Drew Edwards, Akira Maezawa, and Simon Dixon.** “Learning Jazz Pianist Style with Cross-Attention Conditioning.” *Proceedings of the 27th International Society for Music Information Retrieval Conference*, Abu Dhabi, UAE, 2026. **arXiv:2610.02918v1 [cs.SD], 2 October 2026.** CC BY 4.0.  
[p. 1 footnote; arXiv header]

The paper cites Aria [4], PiJAMA [14], the Deep Pianist Identification benchmark [5], Flamingo [15], and Classification Accuracy Score [6] as its main methodological precedents.

### 2. Research question and contribution

The paper asks whether a symbolic music model can learn and reproduce **individual jazz pianist identity**, not merely genre or mood.

The authors make three main claims:

1. Aria representations encode pianist identity sufficiently well for high-accuracy classification.
2. A learned artist embedding injected through gated cross-attention improves stylistic fidelity during free generation.
3. The classifier can locate unusually characteristic moments within a performance.

The paper explicitly distinguishes these effects from teacher-forced likelihood: perplexity changes little, while classifier-based free-generation evaluations change substantially. [p. 1, Abstract/§1; p. 6, §8]

### 3. Data and splits

#### Dataset

- Source: **PiJAMA-30**, 30 jazz pianists with aligned audio and automatically transcribed MIDI. [p. 2, §3]
- The authors remove **22 recordings containing ensemble playing**.
- Selected subset: **PiJAMA-12**, chosen for separability rather than broad coverage.
- Artists:

  - Art Tatum
  - Erroll Garner
  - Abdullah Ibrahim
  - Horace Parlan
  - Tete Montoliu
  - Oscar Peterson
  - Hank Jones
  - Dick Hyman
  - Cedar Walton
  - George Cables
  - Andy Laverne
  - Dave McKenna

- Dataset size: **779 songs / approximately 57 hours**.
- Per-artist counts range from **28 Horace Parlan songs to 187 Dick Hyman songs**.
- Splitting is at the **song level**, intended to prevent train/test leakage.
- PiJAMA-12 split: **1,383 training, 175 validation, and 177 test sequences**, where the sequence split is at 4,096 tokens. The test sequences correspond to **80 held-out songs**. [p. 2, §3; p. 3, Table 1; p. 4, Table 3]

#### Tokenization

Aria’s **AbsTokenizer** represents each note with three token types:

- pitch–velocity
- onset
- duration

Sequence lengths:

- Generation: **4,096 tokens**, approximately **1,200 notes**
- Classification: **1,024 tokens**, approximately **300 notes**

[p. 2, §3]

#### Artist selection

The authors compute per-track embeddings using **Aria-CL**, Aria’s contrastive variant. They rank artists using:

- leave-one-out k-nearest-neighbor accuracy
- silhouette score

The 12 artists with the most separable embedding distributions are retained. Figure 1 visualizes these embeddings using t-SNE. [p. 2, Figure 1, §3]

**Interpretation:** this is a favorable test of conditioning: the classes were selected because they are already relatively separable. It does not establish performance for arbitrary or closely related pianists.

### 4. Aria representations and embeddings

The generation backbone is the **Aria medium model**:

- 659 million parameters
- 16 transformer layers
- hidden dimension \(d=1536\)

For classification, the authors fine-tune the full backbone and apply a linear head to the hidden state at the end-of-sequence token. Training uses class-balanced cross-entropy, pitch/tempo/velocity augmentation, learning rate \(10^{-5}\), batch size 16, and 15 epochs. [p. 2–3, §4.1]

There are two distinct embedding uses:

1. **Aria-CL track embeddings:** used only for artist selection and visual analysis.
2. **Learned artist embeddings:** trained as part of the conditional generator.

The conditional context is shown as \(E_{\text{artist}}\in\mathbb{R}^{4\times d}\), i.e. four learned vectors per artist. [p. 3, §4.2, Figure 2]

### 5. Classifier

The same Aria-based classifier is used as the principal style-fidelity evaluator.

#### Classification results

| Method / dataset | Chunk | Clip | Track |
|---|---:|---:|---:|
| ResNet-50 on DPI-20 | — | 80.5 | 94.4 |
| Aria classifier on DPI-20 | 84.1 | 90.4 | **96.9** |
| Aria classifier on PiJAMA-12 | **95.8** | — | **98.8** |
| Aria classifier on PiJAMA-30 | 90.2 | — | **99.4** |

[p. 3, Table 1]

The authors report that each PiJAMA classifier misses one short track. Track-level decisions use majority voting, with mean-logit tie breaking.

**Author claim:** the Aria classifier exceeds the published DPI-20 ResNet-50 track-level result.

**Interpretation:** this establishes strong discriminability of the selected performers, but classification accuracy is not equivalent to perceptual proof that listeners recognize the same stylistic features.

### 6. Cross-attention generator

The authors insert gated cross-attention after self-attention in the **last 8 of 16 transformer layers**.

The stated update is:

\[
x' = x + g\cdot \mathrm{CrossAttn}(x,E_{\text{artist}})
\]

- Queries: music sequence
- Keys and values: artist embedding
- Scalar gate \(g\), initialized to **0.1**
- Artist-context dropout: **0.3**
- Added parameters: **78M**, approximately **12%** over the 659M base model

[p. 3, Equation 1, Figure 2, §4.2]

The authors motivate cross-attention as a persistent conditioning channel, unlike an artist token placed only at the beginning of the sequence.

#### Training

- Full model and adapter fine-tuned
- 15 epochs
- 4,096-token sequences
- AdamW
- Weight decay: **0.02**
- Linear warmup: **0.5 epoch**
- Peak learning rate: **\(5\times10^{-6}\)**
- Effective batch size: **32**
- fp16
- One NVIDIA RTX 6000
- Approximately **18 hours**
- A no-cross-attention fine-tuned baseline uses identical hyperparameters

[p. 3, §4.2]

Generation uses:

- temperature **0.95**
- top-\(k=50\)
- top-\(p=0.95**

### 7. Style-fidelity results and ablations

#### Teacher-forced evaluation

| Model | Test NLL | Perplexity | Agreement |
|---|---:|---:|---:|
| Pretrained Aria | 2.43 | 11.41 | 25% |
| Fine-tuned, no cross-attention | 1.94 | 6.96 | 37% |
| Cross-attention model | **1.92** | **6.82** | **70%** |

[p. 3, Table 2]

The agreement column is mean sliding-window agreement at prompt length \(P=256\), not teacher-forced accuracy.

**Author claim:** cross-attention greatly improves style fidelity even though perplexity improves only marginally over the fine-tuned baseline.

#### Sliding-window free-generation protocol

For each validation example:

- Prompt lengths \(P\in\{128,256,512\}\)
- Generate up to 4,096 tokens
- Classify 1,024-token windows
- Window stride: 128 tokens
- Score: fraction classified as the true artist

Modes:

1. True artist conditioning
2. Same architecture with conditioning zeroed
3. Fine-tuned no-cross-attention baseline
4. Pretrained Aria

Figure 3 shows the conditioned model maintaining a large advantage throughout generation. At \(P=256\), the mean agreement is:

- Cross-attention: **70%**
- Fine-tuned no-CA baseline: **37%**
- Pretrained Aria: **25%**

The zero-context ablation tracks the no-CA baseline, supporting the claim that the improvement comes from the conditioning signal rather than merely the additional parameters. [p. 3–5, Table 2, Figure 3, §5]

The curves still decay with generation length. The authors interpret this as a persistent but incomplete style anchor rather than complete replacement of the prompt’s style.

#### Per-artist variation

At \(P=256\), Figure 4 reports agreement ranging from:

- **96%:** Hank Jones
- **96%:** Dick Hyman
- **29%:** Cedar Walton

Andy Laverne has high real-data classification accuracy but only **35%** conditioned agreement. Hank Jones reaches **96%** agreement with only **69 training sequences**, whereas Dave McKenna reaches approximately **49%** despite substantially more data. [p. 4–5, Figure 4]

**Author interpretation:** stylistic distinctiveness and consistency may matter more than data volume.

**Caution:** the evidence is correlational, and the artists were preselected for separability.

#### Prompt/conditioning mismatch

When the prompt comes from artist A but conditioning specifies artist B:

- Prompt artist agreement falls from **40% to 27%**
- Conditioning artist agreement rises from **15% to 24%**
- Values converge near token position **1,500**

This result supports a gradual shift from prompt-derived identity toward the explicit conditioning identity. [p. 4, §5]

### 8. Synthetic-transfer evaluation

This is the paper’s strongest attempt to reduce dependence on the pretrained evaluator.

Protocol:

- Take each training sequence.
- Use its first 256 tokens as prompt.
- Generate a 4,096-token continuation.
- Discard the prompt.
- Produce **4,782 synthetic 1,024-token sequences**.
- Train a new classifier exclusively on generated MIDI.
- Test on real PiJAMA-12 held-out performances.

#### Results

| Classifier training data | Chunk | Song |
|---|---:|---:|
| Real PiJAMA-12 | 95.8 | 98.8 |
| Real data, ResNet-50 from scratch | 93.1 | 97.5 |
| Synthetic only, Aria classifier | **87.1** | **95.0** |
| Synthetic only, ResNet-50 from scratch | 70.2 | 91.3 |

[p. 4, Table 3]

The real test set contains **80 songs and 591 chunks**. The caption notes that the clip evaluation uses approximately 30-second piano-roll clips rather than token chunks.

**Author claim:** a classifier trained only on generated material learns structure that transfers to real performances. The result also survives when the classifier has no Aria pretraining.

**Interpretation:** this is stronger evidence than evaluating with the same pretrained classifier, but it remains a classifier-mediated measure rather than a human perceptual test.

### 9. Memorization and diversity checks

The paper addresses three possible confounds. [p. 4–5, §6]

#### Memorization

- Pitch/interval n-gram overlap with training data:
  - below **5% at \(n=6\)**
  - **1% or below at \(n=10\)**
- Maximum 8-second piano-roll Jaccard similarity:
  - generated versus closest training track: **0.20**
  - held-out real performance versus closest training track: **0.32**
- Each continuation’s own source recording is excluded.
- No generation was anomalously close to an unrelated training or test track.

#### Mode collapse

Same-artist generated sequences have **1.5–3.5×** higher pairwise 4-gram Jaccard similarity than different-artist generations, matching the ratio observed in real data. Absolute similarities remain far below 1.0.

#### Possible Aria pretraining overlap

The authors acknowledge that Aria’s pretraining corpus may share recordings with PiJAMA. They report:

- No behavioral replay signature from unconditioned Aria.
- The transfer result survives with a classifier trained from scratch.
- The two corpora used different transcription systems.

These checks reduce, but do not completely eliminate, concerns about source overlap or transcription-specific artifacts.

### 10. Characteristic-moment method

The classifier is repurposed to find regions that are unusually characteristic **within one performance**.

For every 1,024-token window \(w\), stride 128:

\[
m(w)=\ell_{\text{true}}(w)-\max_{j\ne\text{true}}\ell_j(w)
\]

The raw margin is normalized per track:

\[
z(w)=\frac{m(w)-\mu_T}{\sigma_T}
\]

A Gaussian smoothing filter with \(\sigma=1.5\) windows produces a continuous characteristicness curve. [p. 5, Equations 2–3]

#### Art Tatum example

For “Sophisticated Lady”:

- Most characteristic region: approximately **125 seconds**
- Peak: **\(z=+1.9\)**
- Least characteristic example: approximately **160 seconds**
- Trough: **\(z=-1.2\)**
- The peak contains dense activity spanning over five octaves.
- Notes per second are similar:
  - characteristic: **10.6**
  - least characteristic: **9.7**
- Pitch range:
  - characteristic: **5.2 octaves**
  - least characteristic: **4.4 octaves**

The authors interpret this as evidence that the classifier responds to specific gestures, not simply overall note density. They relate the Tatum peak to Dick Hyman’s description of “rapid runs in both hands.” [p. 5–6, Figure 6]

Across 80 test tracks:

- Median peak z-score: **0.90**
- Maximum: **1.99**, Art Tatum
- Erroll Garner has no comparable peak across four tracks; maximum **0.59**

**Author interpretation:** Tatum’s identity may concentrate in salient gestures, whereas Garner’s style may be distributed more uniformly.

**Important limitation:** the method identifies classifier-relative evidence, not necessarily musicologically causal features. A follow-up would need human or expert validation and counterfactual tests.

### 11. Limitations and artifacts

#### Explicitly acknowledged by the authors

- No human listening study; the authors call a DownBeat-style Blindfold Test the most important next step. [p. 6, §8]
- Only 12 selected pianists.
- Only solo piano.
- Artist conditioning has not been tested with lead sheets, chord progressions, or melodic constraints.
- Scaling to less separable artists remains open.
- Style interpolation and classifier-free guidance are proposed but not evaluated.
- Ethics concern: unauthorized imitation of living artists. [p. 8, §11]

#### Additional methodological limitations

These are interpretations rather than direct author claims:

- **Selection bias:** PiJAMA-12 is selected for embedding separability, so the results may overestimate general style-conditioning performance.
- **Identity versus style:** high artist classification can reflect recording, transcription, repertoire, era, or production cues rather than a cleanly isolated pianist style.
- **Classifier dependence:** both major evaluations rely on classifiers; the synthetic-transfer test reduces evaluator reuse but does not replace perceptual evaluation.
- **No unseen-artist generalization:** the model learns embeddings for known artists and is not tested on new pianist identities.
- **No source preservation:** generation is continuation-based. It does not preserve an explicit source melody, phrase, chord progression, or provenance trace.
- **Missing uncertainty reporting:** the paper does not report confidence intervals, multiple random seeds, or significance tests for the main fidelity numbers.
- **Transcription artifacts:** PiJAMA uses automatic MIDI transcription, and the paper notes that its data and Aria’s possible pretraining data may have different transcription origins.
- **Representation ambiguity:** the model’s learned artist embedding is shown to influence output, but the paper does not establish which interpretable musical attributes each embedding controls.

### 12. Relevance to source identity and mashups

#### Direct relevance

The paper provides a useful operational definition of **performer identity preservation**:

- train a real-data identity classifier;
- evaluate generated windows against the intended identity;
- train a new classifier on synthetic outputs and test on real performances;
- locate high-evidence regions using within-track logit margins.

This is relevant to source identity in symbolic mashups, but only indirectly.

#### What it does not solve

The model does not:

- combine two source pieces;
- preserve recognizable source motifs;
- document note-level source contributions;
- diagnose incompatibilities;
- perform minimal repair;
- distinguish content identity from style identity;
- evaluate harmony, voice-leading, cadence, or structural coherence.

Thus, it is better viewed as a **style-control component** than as a complete mashup or provenance-preserving recomposition method.

### 13. Concrete research ideas for explainable symbolic music

1. **Two-source cross-attention mashup model**  
   Use separate cross-attention streams for source-A content, source-B content, and performer/style identity. Add explicit source masks and provenance labels for every generated note or phrase.

2. **Style-conditioned recomposition benchmark**  
   Compare:
   - source A content with source A style;
   - source A content with source B style;
   - unconstrained B-style generation.  
   Measure source recognizability, style attribution, structural coherence, and musical compatibility separately.

3. **Characteristic-region explanations with counterfactuals**  
   Use the paper’s z-score detector to identify style-bearing passages, then remove, transpose, reharmonize, or replace those passages. Test whether classifier attribution changes as predicted.

4. **Identity/content disentanglement**  
   Train paired probes for:
   - performer identity,
   - melody,
   - harmony,
   - rhythm,
   - phrase position.  
   Evaluate whether artist embeddings change identity evidence without changing protected source content.

5. **Provenance-preserving style transfer**  
   Freeze protected source notes and allow style-conditioned edits only in designated roles—ornamentation, voicing, rhythm, accompaniment, or articulation. Produce an operation log and compare generated identity against source preservation.

6. **Conflict-aware repair**  
   Use artist/style embeddings to detect when a mashup’s rhythmic or harmonic material is inconsistent with the target style. Search minimal edits, then verify:
   - style improvement,
   - source identity retention,
   - compatibility,
   - explanation faithfulness.

7. **Human Blindfold evaluation**  
   Reproduce the paper’s classifier tests alongside musician/listener judgments. Test whether classifier-selected characteristic moments are actually recognized as pianist-specific by experts.

8. **Ablation matrix**  
   Extend the paper’s zero-context ablation with:
   - random artist embeddings;
   - swapped artist embeddings;
   - gate-size sweeps;
   - different cross-attention layer ranges;
   - interpolated artist embeddings;
   - structure-conditioned generation.

**Bottom line:** the paper offers strong evidence that Aria plus persistent artist cross-attention can encode and transmit performer-discriminative structure, especially under free generation. Its most valuable contribution for this research programme is the combination of **classifier-based identity evaluation and localized characteristic-region analysis**. Its central gap for explainable mashups is that artist identity is not yet connected to explicit source provenance, structural constraints, or faithful musical explanations.

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
