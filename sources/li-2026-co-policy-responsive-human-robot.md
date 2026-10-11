---
title: "Co-policy: Responsive Human-Robot Co-Creation for Musical Performances"
authors: "Xuetao Li, Wenke Huang, Mang Ye, Zijian Liu, Jinhua Xie, Jifeng Xuan, and Miao Li"
year: 2026
doi: 10.48550/arXiv.2606.19914
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/li-2026-co-policy-responsive-human-robot.pdf"
pdf_filename: li-2026-co-policy-responsive-human-robot.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper’s central claim is that embodied musical co-creation should be treated as a closed loop: the human supplies an incomplete musical or semantic seed, the system generates a complementary response under musical and physical constraints, and a robot realizes it through timed physical interaction.

## 1. Document Information

- **Canonical source:** arXiv `2606.19914v1`; official PDF preserved as `li-2026-co-policy-responsive-human-robot.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zickq_ilmi.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

- **Title:** *Co-policy: Responsive Human-Robot Co-Creation for Musical Performances*
- **Authors:** Xuetao Li, Wenke Huang, Mang Ye, Zijian Liu, Jinhua Xie, Jifeng Xuan, and Miao Li.
- **Identifier/version:** arXiv:2606.19914v1, [cs.RO], **18 June 2026**.
- **Length:** 13 PDF pages.
- **Affiliations:** Wuhan University; Wuhan University of Technology; Nanyang Technological University.
- **Project page:** `https://xtli12.github.io/Co-policy/`
- **Paper status:** The PDF presents an arXiv v1 manuscript. The public repository README additionally cites *npj Artificial Intelligence* (2026), but the PDF itself does not establish a published venue.

The paper’s central claim is that embodied musical co-creation should be treated as a closed loop: the human supplies an incomplete musical or semantic seed, the system generates a complementary response under musical and physical constraints, and a robot realizes it through timed physical interaction.

---

### 2. Problem and claimed contribution

#### Problem

The authors identify two problems (§1, pp. 2–3):

1. **Semantic-to-musical grounding:** How can a robot convert an incomplete motif, style, rhythm, speech instruction, or live musical seed into a complementary response rather than copying it?
2. **Physical execution:** How can that response be executed accurately and quickly enough for interactive musical performance?

They contrast their task with:

- **Robotic playback:** The robot simply executes the user-specified notes.
- **Disembodied music generation:** A model generates symbolic or audio music without physical reachability, timing, or contact constraints.

The paper defines four dimensions of embodied co-creation (§1, p. 2):

- intent alignment,
- creative contribution/novelty,
- embodied feasibility,
- interaction responsiveness.

#### Claimed contributions

The authors claim:

1. A formal closed-loop formulation of embodied human-robot musical co-creation.
2. A modular architecture separating semantic grounding, constrained musical variation, and physical execution.
3. **GMP**, a single-pass Gaussian-mixture visuomotor policy intended to retain multiple feasible action modes without diffusion-policy denoising.
4. Real-robot chime experiments, ablations, latency measurements, ManiSkill2 checks, and blinded expert evaluation.

These are author claims; the evidence is strongest for the modular implementation and chime results, and weaker for broader claims about general musical intelligence or universal superiority over diffusion policies.

---

### 3. Architecture

### 3.1 Overall pipeline

**Primary anchor:** Fig. 1, p. 3; §2.1–§2.2, pp. 3–6; Algorithm 1, pp. 5–6.

At interaction step \(t\), the system receives:

- spoken instruction \(I_t\),
- human seed notes \(N_t^u\), extracted from audio,
- egocentric RGB image \(O_t\),
- inferred physical constraints \(c_t\).

It produces:

- robot note response \(N_t^r\),
- executable action segment \(\tau_t=[a_t,\ldots,a_{t+H}]\in\mathbb{R}^{H\times 6}\).

The paper formalizes the factorization as:

\[
N_t^r=f_{\text{plan}}(I_t,N_t^u,O_t,c_t;\mathcal A),
\qquad
\tau_t=f(O_t,N_t^r,c_t)
\]

where \(\mathcal A\) is the semantic-anchor bank and \(f\) is GMP (§4.1, p. 11).

The three operational stages are:

1. **Semantic intent parsing:** Qwen-VL/F-Qwen produces a structured plan.
2. **Constrained musical variation:** a planner generates a complementary note plan.
3. **Embodied execution:** GMP maps visual context and target notes to six-DoF robot actions.

This decomposition is important for explainability because semantic, planning, perception, and execution failures are intended to remain separately inspectable.

---

### 3.2 Semantic anchors

**Primary anchors:** §2.2.1, pp. 5–6; Fig. 4, p. 6; §4.2, p. 11; `Real_robot/semantic_anchors.json`.

Each anchor contains:

- musical seed,
- score image,
- symbolic notes,
- style descriptor,
- meter/tempo or technical annotation,
- robot-playability tags,
- expected structured plan.

The paper gives an example of a structured VLM output:

```json
{
  "intent": "create",
  "style": "energetic",
  "tempo": 120,
  "human_seed": [3, 5, 6, 5],
  "robot_role": "accompaniment",
  "available_notes": [1, 2, 3, 5, 6],
  "max_latency_ms": 500
}
```

The intended role of anchors is not deterministic lookup. Rather, retrieved anchors are inserted into a fixed prompt template to constrain a generative model’s semantic reasoning.

The distilled prompt in Fig. 4 supplies:

- mood/style,
- seed notes,
- tempo,
- free and unavailable bells,
- task,
- requested note, hand, and dynamics assignments.

The paper’s illustrative example uses human notes **C4–E4–G4**. The replay baseline repeats those notes. The proposed system produces a **C–G–Am–Em** response with syncopation, accented downbeats, and avoidance of an unavailable F bell.

#### Important artifact qualification

The currently public repository confirms four anchor records—`joyful`, `energetic`, `peaceful`, and `dramatic`—with style descriptors, technical annotations, tempo ranges, and playability tags.

However, the released `ConstrainedMusicPlanner` currently uses a fixed playable set:

```python
[60, 62, 64, 65, 67, 69, 71]
```

and snaps generated notes to the nearest available note. The current repository’s latest commit explicitly states that the illustrative unavailable-bell state in the paper is **not produced by a shipped visual detector**. Therefore:

- the paper presents visually conditioned availability as part of the conceptual pipeline;
- the current artifact implements static seven-note playability and nearest-note snapping;
- the unavailable-F example should not be interpreted as independently verified dynamic perception output.

---

### 3.3 Constrained musical variation

**Primary anchors:** §2.2.1, pp. 5–6; Eq. 3, p. 5; Eq. 15, p. 11.

The paper says the robot response is constrained by:

1. **Motif consistency:** preserve recognizable structure from the human seed.
2. **Harmonic validity:** avoid tonal conflict.
3. **Novelty:** do not directly copy the input.
4. **Embodied playability:** respect reachable notes, timing, workspace, and latency.

The Methods section writes the candidate-selection objective as:

\[
N_t^r =
\arg\max_{N\in\mathcal C(N_t^u,c_t)}
[
S_{\text{sem}}(N)
+S_{\text{mus}}(N,N_t^u)
+S_{\text{nov}}(N,N_t^u)
-C_{\text{phy}}(N,c_t)
]
\]

where \(\mathcal C\) contains reachable and timing-valid candidates (§4.2, p. 11).

This is conceptually useful, but the paper does not provide a fully specified optimization algorithm, weights, or reproducible implementation of each score. The released planner is substantially more lightweight: it primarily constrains generated notes by snapping them to the fixed chime-note set and truncating to 16 notes.

---

### 3.4 GMP and GSA

**Primary anchors:** Fig. 2, p. 4; Fig. 3, p. 5; §2.1.1–§2.2.2, pp. 4–7; Fig. 10, p. 10; §4.3, p. 11.

#### Guided Self-Attention encoder

GMP’s visual encoder has two streams:

- **Swin Transformer:** global scene/layout features.
- **DenseNet:** local pixel/contact features.

The authors then couple them asymmetrically:

- queries from the global Swin stream,
- keys and values from the local DenseNet stream.

The intended effect is to use global context to determine which instrument region matters while retaining local contact-scale evidence.

The paper additionally uses:

- **AWCA:** Adaptive Weighting Channel Attention.
- **PSNL:** Patch-level Second-order Non-Local module.

The GSA representation is described as:

\[
h_t=\operatorname{GSA}(O_t)
\]

with subsequent conditioning on the robot note plan and constraints.

The authors explicitly caution that GSA does **not** formally guarantee perfect physical localization. Attention visualizations and ablations are offered as empirical diagnostics, not as proof of causal interpretability (§2.1.1, p. 4).

#### Conditional mixture-density action policy

GMP predicts:

\[
p(\tau_t\mid O_t,N_t^r,c_t)
=
\sum_{k=1}^{K}
\pi_k
\mathcal N(\tau_t;\mu_k,\Sigma_k)
\]

where:

- each component is a complete action mode,
- components do not represent individual joints,
- modes may correspond to top-down strikes, side swings, or gentle taps,
- \(K=6\) is used as a practical hyperparameter,
- covariance is diagonal or low-rank for numerical stability.

At inference, the policy selects either:

\[
\tau_t=\mu_{\arg\max_k\pi_k}
\]

or the mixture expectation:

\[
\tau_t=\sum_k \pi_k\mu_k
\]

The claimed advantage is avoiding the mean-action collapse of deterministic MSE behavior cloning while avoiding the repeated denoising steps of diffusion policies.

---

### 4. Constraints and execution

### Physical platform

**Primary anchor:** §2.3.1, p. 7; Fig. 5, p. 7; Fig. 11, p. 11.

The real-robot setup includes:

- desktop robot platform,
- egocentric camera,
- microphone,
- two six-degree-of-freedom arms,
- compliant dexterous hands,
- a flexible hand design intended to approximate human chime striking.

The system performs chime striking, with visual adaptation to chime placement demonstrated in Fig. 5(c).

#### Audio processing

Live audio is converted into symbolic notes using:

- onset detection,
- pitch tracking,
- rhythm quantization.

The paper treats audio as a high-level symbolic cue, not as dense acoustic feedback for contact control (§4.2, p. 11).

#### Execution constraints

The system is intended to account for:

- reachable bells,
- free versus unavailable instrument states,
- tempo limits,
- maximum response latency,
- hand assignment,
- strike dynamics,
- workspace limits,
- residual vibration.

The current artifact’s actual implementation is less complete than the conceptual description: audio extraction is implemented with onset detection and `librosa.piptrack`, while dynamic source separation, force feedback, and robust ringing-state estimation are not implemented.

---

### 5. Data and training

### Demonstrations

**Primary anchors:** Fig. 7, p. 7; §2.3.2, p. 8; §4.4, p. 12.

The authors collect **350 real-world trajectories**. Each trajectory contains:

- RGB observation \(O_i\), captured pre-action,
- target robot note plan \(N_i^r\),
- constraints \(c_i\),
- ground-truth six-DoF action segment \(\tau_i^g\).

The data tuple is:

\[
d_i=(O_i,N_i^r,c_i,\tau_i^g)
\]

The policy is trained with mixture negative log likelihood plus an auxiliary stabilization term:

\[
\mathcal L_{\text{GMP}}
=
-\log\sum_k\pi_{ik}
\mathcal N(\tau_i^g;\mu_{ik},\Sigma_{ik})
+
\sum_k
\|\pi_{ik}\mu_{ik}-\tau_i^g\|_2^2
\]

The paper does not report sufficient details to reproduce training fully, including:

- train/validation split,
- number of epochs,
- optimizer settings,
- exact action horizon,
- exact preprocessing,
- anchor-bank construction size,
- F-Qwen fine-tuning corpus and procedure.

The fine-tuned F-Qwen component is therefore not fully reproducible from the manuscript alone.

---

### 6. Baselines and results

### 6.1 Expert co-creation evaluation

**Primary anchors:** Table 1, p. 7; Fig. 8, p. 8.

Ten professional chime players rated anonymized, randomized clips on:

- intent alignment,
- creative contribution/novelty,
- musical coherence,
- complementarity/response fluency.

Ratings are retained without removing high or low scores.

The clearest aggregate results are:

| Setting | Planner/policy | AVG |
|---|---:|---:|
| Semantic music | Qwen-VL with GMP | 61.6 |
| Semantic music | Anchored F-Qwen with GMP | **74.8** |
| Concerto | Qwen-VL with GMP | 51.4 |
| Concerto | Anchored F-Qwen with GMP | **62.0** |

The paper reports:

- F-Qwen improves semantic co-creation relative to Qwen-VL by approximately **7.4–13.3 points**, depending on policy.
- It improves concerto co-creation by approximately **3.5–9.6 points**, depending on policy.
- Under the same action policy, Co-policy is reported as better than diffusion policy by:
  - **74.8 vs. 66.3** for semantic co-creation;
  - **62.0 vs. 55.8** for concerto co-creation.

Baselines include:

- ManiSkill2 first-place-style policy, retrained on chime demonstrations;
- diffusion policy;
- RH20T-style behavior cloning;
- DROID-adapted behavior cloning;
- GR00T;
- Qwen-VL without fine-tuning/anchoring;
- F-Qwen with semantic anchoring.

The authors’ interpretation is that semantic anchoring improves the quality of the musical response, while action-policy choice affects how effectively that response is physically realized.

### 6.2 Objective chime-striking results

**Primary anchor:** Table 2, p. 10.

Metrics:

- \(Acc_a\): action success without vibration/sound interference;
- \(Acc_t\): tuning accuracy;
- \(Acc=Acc_aAcc_t\): combined accuracy;
- post-command action frequency.

| Method | \(Acc_a\) | \(Acc_t\) | \(Acc\) | Frequency |
|---|---:|---:|---:|---:|
| ManiSkill2-1st | 0.60 | 0.73 | 0.44 | 15.2 Hz |
| RH20T-style BC | 0.65 | 0.78 | 0.51 | 10.1 Hz |
| Diffusion Policy | 0.68 | 0.83 | 0.56 | 1.01 Hz |
| DROID-adapted BC | 0.62 | 0.75 | 0.47 | 14.2 Hz |
| **Co-policy/GMP** | **0.78** | **0.88** | **0.69** | **18.6 Hz** |

The tuning metric is:

\[
Acc_t =
\operatorname{clip}_{[0,1]}
\left(
1-\frac{|F_s-F_t|}{|F_s-F_n|}
\right)
\]

where \(F_s\), \(F_t\), and \(F_n\) are struck, target, and adjacent-note frequencies.

#### Important interpretation

The frequency number is **not full speech-to-action latency**. It measures only the post-command visuomotor loop after an executable command is available. The paper explicitly excludes:

- VLM planning time,
- robot communication delay,
- actuation delay,
- full speech processing latency.

Thus the 18.6 Hz result supports a low-latency policy-side execution claim, not an end-to-end interactive-latency claim.

### 6.3 ManiSkill2 generalization

**Primary anchors:** Fig. 6, p. 7; Fig. 9, p. 9.

The authors use ManiSkill2 only as a secondary visuomotor generalization sanity check across:

- Pour,
- Fill,
- Hang,
- Excavate.

The simulation result is not the central evidence for musical co-creation. The paper provides plotted success rates but does not provide a full numerical table in the text extraction.

---

### 7. Ablations

**Primary anchor:** Table 3, p. 10; §2.3.3, p. 9.

The full model has:

- \(Acc_a=0.78\),
- \(Acc_t=0.88\),
- \(Acc=0.69\).

Removing components gives:

| Removed component | \(Acc_a\) | \(Acc_t\) | \(Acc\) | Absolute \(Acc\) drop |
|---|---:|---:|---:|---:|
| Swin Transformer stage | 0.57 | 0.65 | 0.37 | 0.32 |
| DenseNet block | 0.62 | 0.68 | 0.42 | 0.27 |
| GSA | 0.68 | 0.70 | 0.48 | 0.21 |
| GMP mixture head, replaced by linear head | 0.71 | 0.75 | 0.53 | 0.16 |

The paper describes these drops as contributions of approximately **32%, 27%, 21%, and 16%**, respectively. More precisely, they are absolute combined-accuracy differences from the full model.

The authors correctly characterize these as component diagnostics rather than a complete factorial ablation. They do not establish that the modules are independently necessary under all instruments, datasets, or horizons.

---

### 8. Figures and tables

- **Fig. 1, p. 3:** End-to-end Co-policy architecture and comparison with diffusion policy.
- **Fig. 2, p. 4:** GMP latent action modes; components represent complete striking strategies, not individual joints.
- **Fig. 3, p. 5:** GSA global/local streams, AWCA, PSNL, and target-bell localization.
- **Fig. 4, p. 6:** Distilled prompt and C4–E4–G4 replay versus complementary response example.
- **Fig. 5, p. 7:** Semantic co-creation, concerto co-creation, and random chime relocation.
- **Fig. 6, p. 7:** ManiSkill2 tasks.
- **Fig. 7, p. 7:** Human demonstration collection in joint space.
- **Table 1, p. 7:** Expert co-creation ratings.
- **Fig. 8, p. 8:** Planner/policy heatmaps, planner gains, radar plots, and task-wise shifts.
- **Fig. 9, p. 9:** ManiSkill2 success-rate comparison.
- **Fig. 10, p. 10:** GMP encoder architecture.
- **Table 2, p. 10:** Chime accuracy and post-command frequency.
- **Table 3, p. 10:** GMP ablations.
- **Fig. 11, p. 11:** Attention diagnostics, compliant hand, and robot-perspective variability.

---

### 9. Limitations and artifact status

### Limitations acknowledged by the authors

**Primary anchor:** §3, pp. 9–11.

The authors acknowledge:

1. Validation is primarily on a single chime instrument.
2. The musical vocabulary is restricted by available notes, anchor-bank coverage, and instrument geometry.
3. Audio note extraction is vulnerable to servo noise, impact sounds, and reverberation.
4. Audio is used as a high-level symbolic cue rather than dense contact feedback.
5. There is no tactile or force-feedback recovery after mis-strikes.
6. Evaluation uses short interaction windows.
7. Long-term improvisation, partner adaptation, memory, and higher-level musical form are not addressed.
8. The compliant hand only approximates human striking.
9. Small visual changes can yield multiple feasible trajectories.

### Public artifact

The public GitHub repository currently contains:

- `Real_robot/` real-robot music code;
- `semantic_anchors.json`;
- `music_creation.py`;
- prompt and speech-handling code;
- GSA/GMP-related policy code;
- ManiSkill2 infrastructure;
- demonstrations and GIFs;
- configuration files;
- static project webpage.

The paper claims that processed demonstrations, generated note plans, anonymized ratings, evaluation scripts, prompt templates, anchor schema, and trained-model configuration files are released where permissions allow. Raw participant videos are restricted or anonymized.

The artifact is useful for architectural inspection, but reproducibility caveats remain:

- the paper does not specify all training details;
- the current public planner is simpler than the full mathematical formulation;
- the current code supports legacy deterministic checkpoints when a GMP checkpoint is absent;
- dynamic unavailable-bell detection is not present in the current code;
- the current public repository should not be treated as proof that every reported trained checkpoint and raw dataset is downloadable.

---

### 10. Relevance to explainable controllable symbolic music mashups and repair

### Directly transferable ideas

#### 1. Semantic anchors as explanation-bearing control interfaces

The anchor bank provides a compact, inspectable representation of:

- style,
- tempo/meter,
- technical constraints,
- playability,
- expected response role.

For symbolic mashups, an anchor could contain:

- source-track identity,
- section/motif,
- genre/style,
- key and tempo,
- rhythmic density,
- harmonic compatibility rules,
- allowable transformation types.

For repair, it could contain:

- defect type,
- affected region,
- preservation requirements,
- acceptable substitutions,
- structural role.

The anchor should be displayed alongside the generated result so that users can distinguish retrieved intent constraints from model invention.

#### 2. Structured intermediate plans

The JSON plan is more explainable than direct unconstrained generation. A symbolic music version should expose:

```json
{
  "role": "bass_accompaniment",
  "source_motif": "...",
  "target_style": "...",
  "key": "...",
  "tempo": 120,
  "preserve": ["rhythm", "cadential contour"],
  "transform": ["reharmonize", "add_syncopation"],
  "constraints": ["range", "voice_leading", "no_parallel_fifths"]
}
```

This enables deterministic validation before rendering or committing the music.

#### 3. Separate semantic intent, musical planning, and realization

The paper’s factorization maps naturally to symbolic systems:

1. parse user intent;
2. construct a constrained symbolic transformation;
3. render, align, or export the result.

For mashups, this separation supports independent inspection of:

- semantic mismatch,
- alignment failure,
- harmonic conflict,
- over-copying,
- structural discontinuity.

For repair, it supports separate evaluation of:

- defect localization,
- repair proposal,
- preservation of unaffected material,
- musical validity.

#### 4. Multi-objective novelty rather than unrestricted novelty

The paper’s four constraints are directly useful for controllable generation:

- preserve recognizable source material;
- maintain harmonic validity;
- add measurable novelty;
- obey realization constraints.

For mashups, novelty should be measured relative to both source tracks while preserving groove, phrase boundaries, and style. For repair, novelty should be localized strictly to defective regions.

#### 5. Mixture-based alternatives

GMP’s action modes suggest a symbolic analogue: generate a calibrated set of alternative transformations rather than one opaque continuation.

Examples:

- candidate reharmonizations;
- alternative phrase alignments;
- different rhythmic overlays;
- multiple repair substitutions;
- distinct voice-leading solutions.

Each candidate can carry:

- probability,
- violated or satisfied constraints,
- explanation,
- confidence,
- human-selection affordance.

The key transferable principle is not the specific robotic Gaussian policy; it is preserving multimodality without averaging incompatible solutions.

#### 6. Factorized evaluation

The expert evaluation dimensions are valuable for symbolic systems:

- intent alignment,
- novelty,
- coherence,
- complementarity.

For repair, add:

- defect removal,
- preservation fidelity,
- structural consistency,
- edit locality,
- human acceptability.

This is preferable to a single “quality” score that hides whether a system was creative but unfaithful, or faithful but musically inert.

#### 7. Counterfactual component tests

The paper’s Qwen-VL versus F-Qwen comparison and action ablations suggest a useful protocol:

- no anchors versus anchors;
- unconstrained versus constrained planner;
- single candidate versus candidate set;
- no harmonic checker versus harmonic checker;
- no edit-locality constraint versus edit-locality constraint.

Report each component’s effect on alignment, novelty, coherence, and constraint violations.

---

### 11. Overall assessment

**Author-supported conclusion:** Co-policy demonstrates a modular, physically grounded chime-playing system with higher reported expert scores, chime-striking accuracy, and policy-side action frequency than the tested baselines.

**My interpretation:** The paper’s strongest contribution for explainable symbolic music AI is not GMP itself. It is the architectural separation between:

- explicit semantic control,
- constrained symbolic variation,
- inspectable intermediate plans,
- realization-aware execution,
- factorized evaluation.

The evidence does **not** yet establish broad musical creativity, general-purpose mashup capability, robust dynamic instrument perception, or end-to-end real-time speech-to-action performance. For symbolic mashup and repair research, the most valuable transferable design is an anchor-conditioned, schema-constrained planner that emits auditable transformation plans and multiple validated candidates rather than a monolithic sequence generator.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `interaction-and-evaluation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
