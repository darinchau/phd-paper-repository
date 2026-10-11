---
title: "Rubric-Based Optimization for Text-to-Music Generation"
authors: "Ping Wang, Guang Yang, Shao-Rong Su, Junkai Wu, Pang Wei Koh, and Noah A. Smith"
year: 2026
doi: 10.48550/arXiv.2610.03589
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2026-rubric-based-optimization-for-text.pdf"
pdf_filename: wang-2026-rubric-based-optimization-for-text.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

> Use broad rubric rewards for qualities difficult to formalize, but use exact symbolic objectives wherever reliable measurements exist.

## 1. Document Information

- **Canonical source:** arXiv `2610.03589v1`; official PDF preserved as `wang-2026-rubric-based-optimization-for-text.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zyjba_hx0s.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Digest: *Rubric-Based Optimization for Text-to-Music Generation*

### Bottom line

**Yes, the method is adaptable to our research, but the exact setup is not Qwen-lab-scale.** The generators are only **300M MusicGen-small** and **3.5B ACE-Step**, both frozen and adapted with LoRA. The largest component is the **30B Qwen3-Omni evaluator**, used only for inference; a **7B Qwen2-Audio** evaluator also works. The main cost is rating generated audio, not pretraining.

For our symbolic mashup/repair work, the most transferable idea is:

> Use broad rubric rewards for qualities difficult to formalize, but use exact symbolic objectives wherever reliable measurements exist.

That maps naturally to perceptual coherence versus explicit harmony, voice-leading, provenance, source identity, and repair constraints.

---

### 1. Bibliography and version status

- **Title:** *Rubric-Based Optimization for Text-to-Music Generation*
- **Authors:** Ping Wang, Guang Yang, Shao-Rong Su, Junkai Wu, Pang Wei Koh, Noah A. Smith
- **Affiliations:** University of Washington and Allen Institute for AI
- **Identifier shown in PDF:** `arXiv:2610.03589v1 [cs.SD]`
- **PDF date:** 2 October 2026
- **Status:** “Preprint. Under review.”
- **DOI:** `10.48550/arXiv.2610.03589`
- **Length:** 27 PDF pages, including references and appendices.

Evidence: PDF page 1; extracted text `/tmp/paper-digest/2610.03589v1.txt:1-15`.

#### Version ambiguity

The supplied PDF consistently identifies itself as **v1**. You reported that the API now returns a later **v2** from October 2026. I have **not treated v2 as equivalent**: all findings below refer specifically to the downloaded v1. The PDF contains no v2 change log or comparison.

---

### 2. Research question and contribution

The paper asks whether a pretrained audio-language model can judge multiple musical qualities through a natural-language rubric and provide a useful post-training reward without:

- collecting human preference annotations;
- training a separate reward model;
- optimizing only one narrow automatic metric.

The authors compare:

1. **DPO** from rubric-ranked preference pairs:
   - MusicGen-small;
   - ACE-Step v1.

2. **DiffusionNFT** using rubric scores directly as online scalar rewards:
   - ACE-Step v1 only.

3. **Specialized objective rewards** for:
   - tempo;
   - key;
   - instrumentation.

Main claim: rubric rewards improve several broad perceptual evaluators simultaneously, while exact objective rewards are much better for measurable attributes.

Evidence: abstract and introduction, pp. 1–2; `/tmp/paper-digest/2610.03589v1.txt:16-96`.

---

### 3. Models and data

#### Generators

| Generator | Size | Role |
|---|---:|---|
| MusicGen-small | 300M | Autoregressive EnCodec-token generator; DPO |
| ACE-Step v1 | 3.5B | Flow-matching diffusion transformer; DPO and DiffusionNFT |

Both pretrained generators remain frozen; only LoRA adapters are trained.

Evidence: §3.1, p. 3; `/tmp/paper-digest/2610.03589v1.txt:136-146`.

#### ALM raters

| Rater | Size/status |
|---|---:|
| Music Flamingo | Music-specialized open-weight ALM |
| Qwen2-Audio | 7B |
| Qwen3-Omni | 30B, largest tested |

All are open-weight, greedily decoded at temperature 0.

Important scale interpretation: **Qwen3-Omni is the judge, not the generator being trained.** The paper does not pretrain or fully fine-tune a Qwen-scale model.

Evidence: §3.2, p. 3; Appendix A.9, pp. 16–17; `/tmp/paper-digest/2610.03589v1.txt:147-160,997-1003`.

#### Data

**MusicCaps**

- 5,521 expert-written captions.
- Train: 4,416.
- Validation: 552.
- Test: 553.
- MusicGen clips: 8 seconds.
- ACE-Step clips: 30 seconds.

**MTG-Jamendo attribute prompts**

| Attribute | Train prompts | Evaluation prompts |
|---|---:|---:|
| Tempo | 32,943 | 1,024 |
| Key | 32,522 | 1,024 |
| Instrumentation | 5,500 | 500 |

Evaluation prompts come from disjoint tracks. The authors state that they are not used for selection, only for recording curves.

Evidence: §3.3, p. 3; Appendix A.7, pp. 15–16; `/tmp/paper-digest/2610.03589v1.txt:162-189,953-984`.

---

### 4. Rubric and ALM scoring

The general MusicCaps rubric has seven dimensions:

| Dimension | Weight |
|---|---:|
| Prompt alignment | 0.25 |
| Style and instrumentation | 0.15 |
| Melody and motif | 0.10 |
| Rhythm and groove | 0.10 |
| Structure and ending | 0.15 |
| Production quality | 0.15 |
| Overall musicality | 0.10 |

Each dimension includes:

- definition;
- audible evidence;
- anchors at 0, 2, 5, 8, and 10;
- calibration note;
- weight.

The reward is the weighted mean:

\[
R_{\text{rubric}}(x,c)=\sum_k w_k s_k(x,c).
\]

The rater must return strict JSON. Malformed output is retried once and then rejected. Values are not clamped or silently replaced with zero.

The full rubric explicitly instructs raters not to reward loudness, density, complexity, or instrument count automatically. It also asks them to inspect endings, clipping, dropouts, looping, and transitions.

Evidence: §4.1, p. 4; Appendix A.2–A.3, pp. 12–13; full prompts Appendix A.12, pp. 17–27; `/tmp/paper-digest/2610.03589v1.txt:210-240,735-790,1060-1862`.

#### Prompting variants

- **Joint prompting:** one ALM call returns all seven scores.
- **Dimension-wise prompting:** seven separate conversations, one per dimension, with deterministic dimension shuffling.

DPO uses joint prompting only because dimension-wise scoring would multiply rating cost by seven. DiffusionNFT compares both.

The paper finds prompting strategy materially affects results: Music Flamingo collapses under joint prompting but behaves better dimension-wise.

---

### 5. Preference-pair construction and DPO

For each of the 4,416 training captions:

1. Generate six candidates from the pretrained generator.
2. Rank them by rubric reward.
3. Pair each of the top two with each of the bottom two.
4. Discard ties, duplicate waveforms, and pairs whose score gap is below margin \(m\).
5. Fix the resulting preference set before training.

Thus, at most four preference pairs are created per caption, although filtering leaves fewer.

The preference set is:

\[
\mathcal{D}_{\text{pref}} =
\{(c,x^+,x^-):R(x^+,c)-R(x^-,c)\ge m\}.
\]

MusicGen uses exact autoregressive token likelihoods. ACE-Step lacks token likelihoods, so the authors construct an offline flow-matching DPO surrogate using shared timestep and noise.

The authors explicitly conjecture that this two-sample, single-timestep surrogate contributes to ACE-Step’s weak DPO performance.

Evidence: §4.2, p. 4; Appendix A.4, pp. 13–14; `/tmp/paper-digest/2610.03589v1.txt:241-253,791-856`.

#### DPO configurations

- MusicGen LoRA rank: 8, \(\alpha=16\).
- ACE-Step LoRA rank: 16, \(\alpha=32\).
- MusicGen: batch size 1, four gradient-accumulation steps, 100 warm-up steps, two epochs.
- ACE-Step: 30-second clips and flow-matching surrogate.

Training pairs:

| Generator/rater | Pairs | Steps/epochs |
|---|---:|---:|
| MusicGen + Music Flamingo | 3,132 | 2 epochs |
| MusicGen + Qwen2-Audio | 650 | 2 epochs |
| MusicGen + Qwen3-Omni | 30 | 600 steps |
| ACE-Step + Music Flamingo | 2,688 | 2 epochs |
| ACE-Step + Qwen2-Audio | 2,234 | 1,500 steps |
| ACE-Step + Qwen3-Omni | 3,339 | 1,500 steps |

Evidence: Appendix A.10, p. 17; `/tmp/paper-digest/2610.03589v1.txt:1030-1051`.

---

### 6. DiffusionNFT setup

DiffusionNFT differs from DPO in that it:

- samples from the current policy at every update;
- scores groups of candidates online;
- centers and normalizes rewards within each group;
- pulls the model toward above-average samples;
- pushes away from below-average samples through an implicit negative prediction;
- regularizes toward the pretrained model.

MusicCaps configuration:

- 4 candidates per prompt;
- 8 prompts per update;
- 125 updates;
- approximately 4,000 rated clips per run;
- 30-second clips;
- LoRA rank 32, \(\alpha=64\);
- AdamW, learning rate \(3\times10^{-4}\);
- gradient clipping 1.0;
- fp32 training;
- seed 42;
- 40 DPM-Solver steps;
- guidance scale 1.0;
- advantage clipping \(A_{\max}=5\);
- KL weight \(10^{-3}\);
- EMA adapter weights.

Attribute runs use 24 candidates per update, 48 prompts per update, 15-second clips, and 60/50/30 update budgets for tempo/key/instrumentation.

Evidence: §4.3, p. 5; Appendix A.5 and A.10, pp. 14–17; `/tmp/paper-digest/2610.03589v1.txt:257-274,857-892,1005-1051`.

---

### 7. Exact main results

All values are changes relative to the untrained generator.

#### 7.1 DPO using single automatic metrics

| Generator | Preference source | CLAP | SongEval | Audiobox |
|---|---|---:|---:|---:|
| MusicGen | CLAP | +0.0129 | +0.0510 | −0.1871 |
| MusicGen | SongEval | +0.0054 | +0.1951 | −0.3453 |
| MusicGen | Audiobox | −0.0186 | −0.0529 | +0.5842 |
| ACE-Step | CLAP | −0.0043 | +0.0049 | −0.0077 |
| ACE-Step | SongEval | −0.0021 | −0.0019 | −0.0052 |
| ACE-Step | Audiobox | +0.0011 | −0.0028 | +0.0015 |

Interpretation: MusicGen demonstrates the narrow-reward trade-off clearly. Each metric improves when optimized, but at least one independent evaluator declines.

Evidence: Table 1, p. 12; Figure 1, p. 6; `/tmp/paper-digest/2610.03589v1.txt:720-731`.

#### 7.2 DPO using ALM rubric preferences

| Generator | Rater | CLAP | SongEval | Audiobox |
|---|---|---:|---:|---:|
| MusicGen | Music Flamingo | +0.0055 | +0.0104 | +0.0354 |
| MusicGen | Qwen2-Audio | +0.0051 | +0.0222 | +0.0315 |
| MusicGen | Qwen3-Omni | +0.0013 | +0.0031 | +0.0311 |
| ACE-Step | Music Flamingo | +0.0008 | +0.0012 | −0.0101 |
| ACE-Step | Qwen2-Audio | +0.0033 | +0.0129 | −0.0054 |
| ACE-Step | Qwen3-Omni | +0.0026 | +0.0093 | +0.0141 |

On MusicGen, all three raters improve all three external evaluators, although gains are smaller than the best single-metric gains.

On ACE-Step, changes are small and inconsistent.

Evidence: Table 2, p. 13; §5.1, pp. 6–7; `/tmp/paper-digest/2610.03589v1.txt:347-399,751-760`.

#### 7.3 DiffusionNFT on ACE-Step

| Rater | Prompting | CLAP | SongEval | Audiobox |
|---|---|---:|---:|---:|
| Music Flamingo | Joint | −0.0392 | −0.2249 | −0.9210 |
| Music Flamingo | Dimension-wise | +0.0127 | +0.0528 | +0.1917 |
| Qwen2-Audio | Joint | −0.0576 | +1.1983 | +0.8848 |
| Qwen2-Audio | Dimension-wise | −0.0753 | +0.6062 | +0.5142 |
| Qwen3-Omni | Joint | +0.0080 | +0.0204 | +0.4183 |
| Qwen3-Omni | Dimension-wise | +0.0180 | +0.1057 | +0.3385 |

Qwen3-Omni is the most balanced rater. Dimension-wise prompting gives the largest CLAP and SongEval gains. Joint prompting gives the larger Audiobox gain.

The paper’s strongest claim is that DiffusionNFT extracts much more from the rubric than ACE-Step’s offline DPO surrogate, but the comparison is not a clean optimizer-only ablation because the configurations were tuned separately.

Evidence: Table 3, p. 13; Figure 2, p. 7; `/tmp/paper-digest/2610.03589v1.txt:402-469,764-774`.

#### 7.4 Untrained reference scores

| Generator | Clip length | CLAP | SongEval | Audiobox |
|---|---:|---:|---:|---:|
| MusicGen-small | 8 s | 0.23 | 2.22–2.24 | 6.48–6.51 |
| ACE-Step, DPO runs | 30 s | 0.17–0.18 | 2.21 | 6.25 |
| ACE-Step, DiffusionNFT runs | 30 s | 0.22 | 1.96 | 6.32 |

These baselines matter because some apparently large absolute deltas, particularly Qwen2-Audio’s SongEval increase, correspond to very different relative changes across metrics.

Evidence: Table 4, p. 14; `/tmp/paper-digest/2610.03589v1.txt:820-827`.

---

### 8. Specialized reward results

The paper compares Qwen3-Omni rubric rewards with direct analyzers.

#### Objective rewards

- **Tempo:** Beat This tracker; reward is 1 within ±5 BPM and decays exponentially outside that range.
- **Key:** S-KEY; exact match over 24 tonic/mode classes, with enharmonic normalization.
- **Instrumentation:** Essentia MTG-Jamendo classifier; reward contrasts requested instruments against the strongest non-requested instrument among guitar, piano, synthesizer, bass, and drums.

#### Table 5 trajectories

| Task/condition | Values at successive update checkpoints |
|---|---|
| Tempo, objective | 0.268, 0.435, 0.523, 0.545, **0.555**, 0.524, 0.500 |
| Tempo, rubric | 0.277, 0.289, 0.245, 0.270, 0.290, 0.343, **0.353** |
| Key, objective | 0.043, 0.058, 0.099, 0.123, **0.126**, 0.112 |
| Key, rubric | 0.045, 0.047, 0.048, 0.040, 0.045, 0.045 |
| Instrumentation, objective | 0.414, 0.498, **0.592**, 0.538 |
| Instrumentation, rubric | 0.414, 0.436, **0.443**, 0.402 |

The authors summarize the result as:

- direct tempo optimization approximately doubles the score;
- direct key optimization raises accuracy from chance, about 4%, to about 13%;
- direct instrumentation optimization improves the contrastive score by roughly 40%;
- rubric transfer is approximately one-quarter of the tempo gain, one-sixth of the instrumentation gain, and effectively zero for key.

The rubric’s own score keeps rising even when the actual target attribute does not. This is strong evidence that **a judge’s confidence is not sufficient evidence that the intended property improved**.

Evidence: §5.3, p. 8; Figure 3 and Table 5, pp. 8 and 14–15; `/tmp/paper-digest/2610.03589v1.txt:476-508,832-850`.

---

### 9. Human listening test

The tested system was the best run: ACE-Step + Qwen3-Omni + dimension-wise DiffusionNFT.

- 40 non-vocal MusicCaps captions.
- Same seed for trained and untrained clips.
- 30-second clips.
- Seven listeners.
- 52 total pairwise judgments.
- Trained model preferred in 36/52 judgments: **69%**.
- Bootstrap 95% interval: **48–89%**.
- Sign-test \(p=0.008\).

This is encouraging but small: it is not a large human evaluation and the interval includes near-chance outcomes.

Evidence: §4.5 and §5.4, pp. 5 and 9; `/tmp/paper-digest/2610.03589v1.txt:295-305,501-514`.

---

### 10. Limitations and reproducibility

#### Limitations stated by the authors

- Only open-weight ALMs were tested.
- Closed ALMs were considered unaffordable for the number of ratings.
- Only MusicGen-small and ACE-Step v1 were evaluated.
- Clips are short, limiting long-range structure, transitions, and endings.
- Automatic evaluators cover only part of musical quality.
- Harmony, voice leading, dynamics, phrasing, stylistic authenticity, and originality lack well-validated evaluators.

Evidence: §6, p. 9; `/tmp/paper-digest/2610.03589v1.txt:516-554`.

#### Reproducibility strengths

The paper provides:

- data splits;
- generation lengths;
- rating prompts;
- rubric definitions;
- prompt versions and hashes;
- model checkpoint identifiers;
- training hyperparameters;
- exact reward definitions;
- evaluation procedure;
- seed 42 for DiffusionNFT.

The paper says each run records its resolved configuration, git commit, dataset path, rubric version, prompt version, and prompt hash.

Evidence: Reproducibility statement, p. 9; Appendices A.7–A.12, pp. 15–27; `/tmp/paper-digest/2610.03589v1.txt:577-584,953-1060`.

#### Missing artifact information

In the supplied v1 PDF I found:

- no public code repository URL;
- no released LoRA checkpoints;
- no hardware specification;
- no GPU count, memory, wall-clock time, or FLOP estimate;
- no explicit artifact archive or experiment-tracking URL.

The paper is therefore **methodologically specified but not fully artifact-reproducible from the PDF alone**.

---

### Relevance to our symbolic mashup and repair programme

### What transfers directly

#### 1. Separate broad perceptual rewards from exact symbolic rewards

For symbolic music:

**Broad rubric dimensions**

- perceived coherence;
- stylistic fit;
- phrase continuity;
- musicality;
- source recognizability;
- arrangement plausibility;
- transition quality.

**Exact or near-exact symbolic objectives**

- key and mode;
- meter and beat alignment;
- harmonic compatibility;
- dissonance;
- parallel fifths/octaves;
- voice-leading distance;
- pitch/register range;
- note overlap and playability;
- source-note preservation;
- motif coverage;
- cadence completion.

The paper strongly supports using the second class directly whenever reliable analysis is available.

#### 2. Preference construction for mashup candidates

For each source pair and prompt:

1. Generate several candidate alignments or repairs.
2. Score them with a vector of symbolic objectives plus a perceptual rubric.
3. Pair high-scoring candidates against low-scoring candidates.
4. Train a small reranker, policy, or symbolic generator with DPO.

Do not reduce compatibility, identity, novelty, and coherence to one hidden scalar during evaluation. Preserve the separate dimensions and report the Pareto frontier.

#### 3. Rubric-based candidate diagnosis

The paper’s seven dimensions can be adapted to a mashup rubric:

- source-A identity;
- source-B identity;
- harmonic compatibility;
- rhythmic compatibility;
- phrase/form coherence;
- orchestration/role clarity;
- repair minimality;
- overall musicality.

However, the original ALM returns **only scores**, not explanations. Its strict prompt explicitly forbids reasoning. Therefore, these scores would be useful as evaluation evidence but would not constitute faithful explanations.

#### 4. Provenance-preserving explanations

For each accepted repair, record:

- source notes and phrases affected;
- transformation operation;
- symbolic conflict detected;
- objective score before/after;
- rubric score before/after;
- counterfactual alternatives;
- whether source identity was preserved.

This would turn the paper’s score-based optimization into an auditable rationale graph rather than an opaque “the judge preferred it.”

### What should not be copied uncritically

- Do not use a general ALM to judge key, meter, or voice-leading when symbolic analyzers can calculate them.
- Do not treat a rising reward as evidence of real improvement; the paper explicitly shows reward/evaluation divergence.
- Do not use a single weighted score as the sole success criterion for mashups.
- Do not assume dimension-wise ALM scores are independent merely because they are prompted separately.
- Do not call rubric scores explanations without testing faithfulness through counterfactual edits.

### Practical modest-scale replication

A realistic version for us would avoid training a Qwen-scale generator:

1. Use a small symbolic Transformer or reranker.
2. Generate 4–8 candidate mashups or repairs per source pair.
3. Use exact symbolic analyzers for harmony, rhythm, voice-leading, identity, and minimality.
4. Render only shortlisted candidates to audio.
5. Optionally use a 7B audio-language model or a local music critic for broad perceptual scoring.
6. Train LoRA or DPO on the resulting pairs.
7. Evaluate separately on compatibility, source identity, structural coherence, novelty, playability, and explanation faithfulness.

This is substantially smaller than the paper’s largest judge setup. The expensive component can be restricted to a small candidate pool, while most symbolic objectives are cheap and deterministic.

### Overall assessment

**Author-supported conclusion:** ALM rubrics can provide broad, multi-aspect post-training rewards, but their usefulness depends strongly on the rater, prompting strategy, and whether the scores actually track the desired property.

**My interpretation for our project:** This is not evidence that we need Qwen-scale training. It is evidence for a **hybrid critic architecture**:

- symbolic analyzers for constraints and repair correctness;
- rubric or human preference signals for perceptual coherence and musical value;
- provenance-aware traces for explanations;
- multi-objective evaluation rather than one scalar benchmark.

No files were edited.

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
