---
title: "Do Language Models Need Music Supervision? Verifiable Rewards for Multi-Constraint Symbolic Music Generation"
authors: "Haoyue Liu and Xiaoying Tang et al."
year: 2026
doi: 10.48550/arXiv.2609.23665
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/liu-2026-do-language-models-need-music.pdf"
pdf_filename: liu-2026-do-language-models-need-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The paper introduces **MusicRLVR**, GRPO training using deterministic symbolic-music verifiers rather than human labels, a learned reward model, or music-domain SFT.

## 1. Document Information

- **Canonical source:** arXiv `2609.23665`; official PDF preserved as `liu-2026-do-language-models-need-music.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492s_3ko8.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Source inspected:** `/tmp/paper-digest/2609.23665.pdf` and `/tmp/paper-digest/2609.23665.txt`. I also re-extracted the PDF as `/tmp/paper-digest/reextract-2609.txt` and checked all 48 PDF pages, including appendices, tables, figures, and qualitative examples. The local PDF is **arXiv:2609.23665v2, 7 October 2026**—the no-suffix URL identifies the work, while the supplied file is v2.

### 1. Core contribution

The paper introduces **MusicRLVR**, GRPO training using deterministic symbolic-music verifiers rather than human labels, a learned reward model, or music-domain SFT.

The three central mechanisms are:

1. **Hard validation gate:** malformed or structurally invalid ABC receives zero reward.
2. **Graded per-family reward:** partial compliance receives credit, especially partial structural repetition.
3. **All-satisfied bonus:** jointly satisfying every requested constraint receives an additional binary reward.

The paper’s central claim is that verifier-only RL can teach a general language model to satisfy multiple symbolic-music constraints jointly.

**Evidence:** `/tmp/paper-digest/2609.23665.pdf`, pp. 2–5; `/tmp/paper-digest/reextract-2609.txt:103–112, 215–267`.

### 2. Exact verifier and reward design

#### Output and gate

The model generates **one monophonic tune in ABC notation**. The historical training/evaluation gate:

- extracts the ABC block;
- rejects failed extraction;
- rejects repeat signs `|:` and `:|`;
- rejects music21 parse errors or a parse timeout over 20 seconds;
- rejects fewer than eight notes;
- rejects fewer than four non-empty measures;
- rejects chord objects.

The stricter audit additionally rejects wrappers, missing required headers, lyrics, grace notes, multiple parts/voices, overlapping notes, chords, and other format violations.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:1359–1428`; PDF pp. 19–21.

#### Eight verifier families

| Family | Verification |
|---|---|
| Key | ABC header must match; music21 Aarden–Essen key analysis must be the requested key or its relative major/minor |
| Meter | Every bar sums to the requested time signature |
| Length | Exact requested number of non-empty bars; no pickup |
| Range | Every sounding pitch lies between requested MIDI bounds |
| Final | Last sounding pitch class matches; octave ignored |
| Rhythm | Every note duration belongs to the admissible duration set; rests fail |
| Leap | No adjacent sounding-pitch interval exceeds the requested semitone maximum |
| Structure | Sixteen bars divided into four-bar units; AABA/AABB/ABAB repetition and contrast constraints |

Structure is evaluated over bar signatures containing event type, MIDI pitch, duration, and rests. Repetition receives graded credit; contrast remains binary.

The key verifier is explicitly hybrid: literal `K:` headers alone are gameable, while music21 key analysis alone agrees with corpus labels on only 0.750 of 400 tunes.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:215–228, 242–267, 1359–1428`; PDF pp. 4, 19–22.

#### Reward equation

For valid output \(y\) and requested constraint set \(C\), with \(k=|C|\):

\[
R(y,C)=\alpha \frac{1}{k}\sum_{(f,\theta)\in C}s_f(y,\theta)
 +(1-\alpha)A(y,C)
\]

where:

- \(\alpha=0.7\);
- \(A(y,C)=1\) only when every requested verifier passes;
- \(s_f=v_f\) for seven non-structure families;
- \(s_{\text{structure}}=0.7\bar e+0.3v_{\text{contrast}}\);
- invalid outputs receive zero before partial credit.

GRPO uses group-relative advantages, group size \(G=8\), per-token KL penalty, clipping \(0.2\), and KL coefficient \(0.04\).

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:242–267, 299–347`; PDF pp. 4–5 and Appendix A, p. 12.

### 3. Data and benchmark

#### MusicConstraintBench

The benchmark contains **2,180 items**:

- Mixed: 300
- Single: 200
- Seen: 200
- Unseen: 200
- High-k: 160
- Structure: 120
- Dense: 500
- Edge: 500

It also includes **400 paraphrase items**.

The four held-out family pairs are:

- key–rhythm
- meter–leap
- final–structure
- length–range

The training prompts contain at most three constraints; the benchmark tests up to seven constraints.

#### Training data

- Source corpus: **IrishMAN**, approximately 45,000 Irish ABC tunes.
- Optional verifier-labelled SFT: **12,890** instruction–tune pairs plus 125 validation pairs.
- RL pool: **6,000 synthetic prompts**.
- Structure prompts were increased from 21% to **33.1%**.
- SFT labels are created by extracting measurable properties from tunes, rendering a subset as instructions, and re-verifying the pair.
- Held-out constraint pairs are excluded from both SFT and RL data.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:1037–1060, 1190–1214`; PDF pp. 5, 14–18.

### 4. Models and training

#### Models

Zero-shot baselines:

- Qwen3-4B-Instruct-2507
- Qwen3-8B
- Qwen3-32B
- Llama-3.1-70B
- MiniMax-M3
- ChatMusician-7B

Trained models:

- Qwen3-4B-Instruct-2507, full-parameter training
- Qwen3-8B, Direct MusicRLVR

Matched 4B runs:

- SFT
- rejection-sampling fine-tuning (RFT)
- Direct GRPO with binary reward \(R=A\)
- MusicRLVR from SFT initialization
- Direct MusicRLVR

#### Main training settings

- 300 optimizer updates
- 48 completions per update
- \(G=8\) rollouts per prompt
- learning rate \(10^{-6}\)
- completion cap: 768 tokens
- 6,000 synthetic RL prompts
- no chain-of-thought or requested reasoning
- Qwen3-8B uses thinking disabled

Infrastructure:

- Ascend 910B2 accelerators
- 64 GB HBM each
- CANN 8.2.RC1
- ms-swift 4.2.3
- vLLM 0.11.0 with vllm-ascend
- matched 4B training: two policy accelerators plus one rollout accelerator
- Qwen3-8B: two policy devices with ZeRO-3 and CPU offload plus a rollout device; reported runtime 15.7 hours

The 4B matched run is described as **under four hours on three accelerators**.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:104–112, 928–950, 980–1014, 1197–1214`; PDF pp. 2, 12–18.

### 5. Main results

All values below are all-satisfied rates under greedy decoding.

| Model | Mixed | Single | Seen | Unseen | High-k | Structure | Dense | Edge | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen3-4B | .160 | .225 | .100 | .040 | .037 | .100 | .008 | .010 | .068 |
| Qwen3-8B | .123 | .210 | .115 | .050 | .006 | .000 | .020 | .032 | .064 |
| Qwen3-32B | .363 | .535 | .250 | .190 | .094 | .267 | .074 | .112 | .204 |
| Llama-3.1-70B | .380 | .695 | .300 | .195 | .056 | .167 | .040 | .058 | .197 |
| MiniMax-M3 | .367 | .580 | .315 | .190 | .100 | .008 | .088 | .160 | .215 |
| ChatMusician-7B | .160 | .290 | .130 | .090 | .006 | .000 | .020 | .046 | .084 |
| SFT | .477 | .745 | .415 | .440 | .231 | .600 | .290 | .076 | .346 |
| RFT | .543 | .960 | .445 | .355 | .163 | .758 | .098 | .128 | .342 |
| Direct GRPO, \(R=A\) | .797 | .960 | .745 | .565 | .469 | .908 | .322 | .300 | .545 |
| MusicRLVR, SFT init. | .577 | .880 | .585 | .530 | .350 | .383 | .366 | .134 | .424 |
| **MusicRLVR, Direct 4B** | **.807** | **.985** | **.815** | **.595** | **.575** | **.967** | **.362** | **.310** | **.580** |
| MusicRLVR, Direct 8B | .657 | .915 | .705 | .645 | .431 | .900 | .404 | .252 | .530 |

The paper’s headline comparison is Direct MusicRLVR increasing Qwen3-4B from **0.160 to 0.807 on Mixed**—the abstract rounds the trained figure to 0.797 in one comparison, while Table 2/Table 39 report 0.807 for the final Direct MusicRLVR checkpoint. This distinction should be preserved.

Notable baseline findings:

- Llama-3.1-70B parses 97% of Mixed items but jointly satisfies only 38%.
- Llama falls from 0.630 at one constraint to approximately 0.044 at four constraints.
- ChatMusician-7B does not outperform general-purpose models.
- MusicRLVR Direct solves 609 items that Qwen3-32B, Llama-3.1-70B, and MiniMax-M3 all fail; the reverse overlap is five items.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:367–430`; PDF pp. 1, 6–8.

### 6. Ablations and diagnostics

Reward ablation over all 2,180 items:

| Variant | Overall rate |
|---|---:|
| Default MusicRLVR | .580 |
| Gate on \(A\) only | .534 |
| \(\alpha=0\), binary reward | .545 |
| \(\alpha=.5\) | .502 |
| \(\alpha=1\), no all-satisfied bonus | .553 |
| Binary structure credit | .546 |
| Symmetric structure credit | .515 |
| Equal structure weights | .544 |
| Structure share 21% rather than 33% | .518 |

All variants underperform the default; the losses are especially large on High-k.

Additional findings:

- Direct training beats SFT initialization: Mixed .807 versus .577.
- SFT initialization often degenerates on structure: it passes repetition on 119/120 Structure items but contrast on only 50 and emits an all-identical tune on 69 items.
- Best-of-8 verifier reranking improves Direct MusicRLVR Mixed from .807 to .897, but training remains substantially better than zero-shot reranking.
- Direct MusicRLVR remains effective beyond the training constraint count: on the ladder, its rates are .647, .530, .362, .230, .160, and .087 for \(k=2\) through \(7\).
- On Edge parameters outside the RL prompt domain, Direct reaches .310; Qwen3-8B reaches .252.
- The stricter fixed-format gate causes no additional failures for the three matched RL checkpoints, although it substantially changes ChatMusician’s scores.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:530–586, 1970–2088`; PDF pp. 8–10, 28–32.

### 7. General capabilities

The paper reports no significant degradation on general benchmarks:

| Model | IFBench strict | IFBench loose | MMLU-Redux | GSM8K |
|---|---:|---:|---:|---:|
| Qwen3-4B zero-shot | 32.0 | 33.3 | 83.9 | 93.9 |
| MusicRLVR Direct 4B | 29.3 | 31.7 | 84.4 | 94.1 |
| Qwen3-8B zero-shot | 25.7 | 30.3 | 81.5 | 93.0 |
| MusicRLVR Direct 8B | 25.3 | 30.0 | 82.6 | 93.3 |

This supports the narrower claim that the method does not obviously destroy general instruction/reasoning performance, not that it improves general reasoning.

### 8. Limitations and artifact status

#### Explicit paper limitations

The method is limited to:

- short, monophonic ABC tunes;
- eight hand-designed verifier families;
- mostly Western tonal/Irish-style symbolic music;
- no polyphony, accompaniment, rich orchestration, or broad musical form;
- no perceptual musical-quality objective;
- no listener study or human preference evaluation;
- an all-satisfied compliance metric rather than musicality, originality, or usefulness.

The paper explicitly warns that satisfying verifiers does not establish musical quality.

The key verifier’s relative-key tolerance is also a substantive evaluation choice: exact-key rescoring lowers some results, though the main trained-checkpoint conclusions remain similar.

#### Artifact status

The paper says that the benchmark and verifiers **will be released** and describes release scripts, hashes, evaluation files, and reproducibility artifacts. The supplied paper/text does not itself establish that a public repository or checkpoints are currently accessible. Therefore:

- **Author claim:** release is intended/promised.
- **Verified here:** only the local PDF and extracted text were available.
- **Not verified:** public checkpoint, code, dataset, or release URL.

**Evidence:** `/tmp/paper-digest/reextract-2609.txt:592–610, 1227–1239, 2790–2810`; PDF pp. 10, 17–18, 48.

### Relevance to source attribution

### What transfers directly

MusicRLVR offers a useful training pattern for attribution-aware symbolic generation:

- decomposable verifiers produce interpretable reward traces;
- each constraint family can expose a failure reason;
- the all-satisfied bonus encourages joint rather than isolated compliance;
- held-out combinations provide a template for testing attribution generalization.

For source attribution, analogous verifiers could check:

- source identity of each segment, motif, or phrase;
- whether claimed source metadata agrees with the generated material;
- whether borrowed material remains within a permitted transformation;
- whether transitions preserve explicit source boundaries;
- whether non-target sources are absent when exclusion is requested.

### What does **not** transfer automatically

The paper does **not** solve source attribution. Its verifiers check musical properties, not origin. A model could satisfy key, meter, rhythm, and form while:

- copying the wrong source;
- blending sources without traceability;
- inventing provenance metadata;
- replacing source material entirely while preserving superficial constraints.

Therefore attribution must be represented as a formal object—source IDs, aligned spans, transformations, and provenance evidence—not as a natural-language instruction alone.

### Relevance to symbolic mashup and repair

### Mashup

A natural extension is a multi-source constraint set:

- source A/B segment assignments;
- phrase-boundary alignment;
- key and meter compatibility;
- permitted transposition/time-stretch bounds;
- transition smoothness;
- motif preservation;
- no unintended material from excluded sources.

The reward should include both **source-faithfulness** and **musical compatibility**. A global all-satisfied reward alone risks rewarding a fluent but source-unfaithful mashup.

### Repair

For repair, verifiers should be paired with identity-preservation constraints:

- preserve all unaffected events exactly;
- limit edit distance or changed-note ratio;
- preserve source attribution for untouched spans;
- repair only the specified defect;
- verify local and global constraints after repair.

This is essential because MusicRLVR’s current objective rewards a valid final tune, not minimal or faithful repair. Without edit-preservation reward, a model could “repair” by discarding the damaged input and generating a new compliant tune.

### Concrete research ideas

1. **Attribution-aware RLVR:** add verifiers for source-span identity, motif overlap, transformation legality, and provenance consistency.
2. **Preserve-first repair reward:** combine verifier compliance with token/event-level preservation, edit locality, and explicit defect correction.
3. **Counterfactual attribution tests:** evaluate on held-out source pairs and unseen combinations, analogous to the paper’s held-out constraint pairs.
4. **Verifier-trace explanations:** return per-family and per-span verdicts, failed conditions, and minimal counterexamples alongside each generation.
5. **Anti-gaming audits:** test whether the policy exploits metadata, trivial transposition, degenerate repetition, or source-independent outputs.
6. **Quality–compliance separation:** add human or learned musical-quality evaluation only as a secondary objective; retain deterministic verifiers for hard constraints.
7. **Polyphonic extension:** replace monophonic ABC checks with event-level multi-track verifiers for harmony, voice leading, instrumentation, and source-specific layers.
8. **Provenance-constrained mashup benchmark:** create tasks where each output event must be traceable to source A, source B, or an explicitly marked transition, with held-out source combinations and repair corruptions.

**Bottom line:** the paper provides strong evidence that dense, decomposable symbolic verifiers can teach multi-constraint compliance without music-domain supervised initialization. Its most valuable lesson for attribution, mashup, and repair is the reward architecture—not the current musical verifier set. Attribution and repair require additional preservation/provenance verifiers; otherwise the objective rewards valid-looking outputs rather than faithful transformations.

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
