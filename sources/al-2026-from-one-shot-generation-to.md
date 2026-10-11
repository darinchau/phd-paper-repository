---
title: "From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing"
authors: "André Ricardo Ducca Fernandes et al."
year: 2026
doi: 10.48550/arXiv.2609.34994
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-from-one-shot-generation-to.pdf"
pdf_filename: al-2026-from-one-shot-generation-to.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The authors’ central claim is deliberately narrow: LoRA can make a general-purpose instruction LLM reliably follow an operation-aware, persistent symbolic-editing contract in the tested Irish traditional-music setting. They explicitly do **not** claim superior musical quality, human-AI co-creativity, or novelty for fine-tuning itself (PDF pp. 1, 11–14; `/tmp/paper-digest/2609.34994v1.txt:595-666`).

## 1. Document Information

- **Canonical source:** arXiv `2609.34994v1`; official PDF preserved as `al-2026-from-one-shot-generation-to.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40f07a_uku0.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliographic record and scope

- **Paper:** André Ricardo Ducca Fernandes, Jean-Pierre Briot, Simone Diniz Junqueira Barbosa, and Hélio Côrtes Vieira Lopes, “From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing.”
- **Version:** arXiv:2609.34994v1, `[cs.AI]`, 28 September 2026; preprint dated September 2026.
- **Length:** 16 PDF pages: Sections 1–8 occupy pages 1–14; references occupy pages 14–16. **There is no appendix in v1.**
- **Primary evidence:** `/tmp/paper-digest/2609.34994v1.pdf`; extracted text `/tmp/paper-digest/2609.34994v1.txt`, especially lines 1–35, 257–321, 328–418, 427–490, 503–665, and 710–730.

The authors’ central claim is deliberately narrow: LoRA can make a general-purpose instruction LLM reliably follow an operation-aware, persistent symbolic-editing contract in the tested Irish traditional-music setting. They explicitly do **not** claim superior musical quality, human-AI co-creativity, or novelty for fine-tuning itself (PDF pp. 1, 11–14; `/tmp/paper-digest/2609.34994v1.txt:595-666`).

### ABC state-transition contract

#### Formalization

Section 3.1 defines an authoritative persistent ABC artifact:

\[
s_t = F_{o_t}(s_{t-1}, u_t, r_t)
\]

where:

- \(s_{t-1}\): current ABC artifact;
- \(u_t\): natural-language user request;
- \(o_t\): resolved operation;
- \(r_t\): operation scope;
- \(s_t\): revised artifact passed directly to the next turn.

The operation determines both authorized changes and preservation invariants. A response must first contain parseable ABC; only then does the operation-specific checker evaluate compliance (PDF p. 5; `/tmp/paper-digest/2609.34994v1.txt:255-275`).

#### Operation contract

| Operation | Role/scope | Required behavior |
|---|---|---|
| **Create a melody** | Initialization/replacement | Establish a new melody artifact. |
| **Create a melody with chords** | Initialization/replacement | Establish a melody plus chord-bearing artifact. |
| **Add chords** | Whole artifact | Add quoted chord symbols while preserving the melody. |
| **Inpainting** | Selected bars, one to four parsed bars | Rewrite the target bars; preserve material outside the target. |
| **Transpose** | Whole artifact | Change tonal content/key while preserving rhythmic and structural relations; transpose chord symbols when present. |

The paper uses “two artifact-initialization variants and three editing operations” in the abstract, although five user-facing operation names are trained (PDF pp. 1, 5–6; `/tmp/paper-digest/2609.34994v1.txt:20-32`, `306-316`).

The clearest qualitative chain is:

> Create a melody → Add chords → Inpainting, bars 3–5 → Transpose.

Every returned ABC artifact becomes the input state for the next request (Figure 2, PDF p. 5; `/tmp/paper-digest/2609.34994v1.txt:239-249`, `312-316`).

#### Important schema limitation

The paper gives an operation **semantics**, but not a formal machine-readable operation schema. It does not publish a JSON schema specifying fields such as operation name, scope, target bars, source artifact identifier, expected invariants, or provenance metadata. The “496,038 JSONL records” statement describes the dataset container, not its record schema.

### Data generation

#### Musical corpus

- Irish Massive ABC Notation / IrishMan corpus released with TunesFormer.
- 216,284 tunes total.
- 214,122 training tunes.
- 2,162 validation tunes.
- Dialogue construction uses training material; validation material supplies held-out comparison baselines.
- Domain is primarily monophonic Irish lead-sheet music with optional chord annotations.

Evidence: PDF p. 5; `/tmp/paper-digest/2609.34994v1.txt:279-302`.

#### Synthetic dialogue construction

The authors construct six interaction scenarios combining:

1. melody-only versus chord-bearing artifacts; and
2. creation-first versus user-supplied-artifact initialization.

Generation rules include:

- chord addition pairing an unannotated melody with its chord-annotated counterpart;
- inpainting one to four parsed bars and copying the non-target material;
- transposition by a sampled interval, including chord symbols;
- 856 natural-language template records across 19 internal prompt types.

Dataset totals:

- **496,038 JSONL records**;
- **495,853** records contain at least one supervised operation;
- **3,241,509** user-assistant operation instances;
- mean **6.535 operations per record**;
- range **1–20 operations** among non-empty records.

Evidence: PDF p. 6; `/tmp/paper-digest/2609.34994v1.txt:304-321`.

### Model and LoRA training

- Base: **Llama 3.1 8B Instruct**.
- Adaptation: supervised instruction fine-tuning with LoRA.
- LoRA rank \(r=64\).
- LoRA alpha \(\alpha=16\).
- Dropout: **0.1**.
- No bias adaptation.
- Causal-language-model task type.
- Maximum sequence length: **8,192 tokens**.
- Epochs: **2**.
- Per-device batch size: **1**.
- Learning rate: **\(10^{-4}\)**.
- Optimizer: `paged_adamw_32bit`.
- Scheduler: cosine.
- Weight decay: **0.1**.
- Warm-up ratio: **0.05**.
- Maximum gradient norm: **1.0**.
- Gradient checkpointing enabled.
- The trained adapter is merged into the base model for evaluation; the result is provisionally called **ABC-LLM**.

Evidence: PDF p. 6; `/tmp/paper-digest/2609.34994v1.txt:323-333`.

The paper does not report hardware, random seeds, detailed train/validation splitting of the synthetic dialogues, decoding parameters, or a released training script.

### Evaluation design and checker

Each model is evaluated on:

- **500 dialogues**;
- 250 melody-only chains with three responses;
- 250 chord-bearing chains with four responses;
- seven evaluated output states;
- **250 attempts per state**;
- **1,750 attempted output states per model**.

“Create a melody with chords” is trained but is not a separate state in this evaluation (PDF pp. 6–7; `/tmp/paper-digest/2609.34994v1.txt:335-369`).

#### Admission versus compliance

The authors correctly separate:

1. **ABC extraction/syntax admission:** whether output contains parser-usable ABC;
2. **checker admission:** whether it reaches the relevant operation checker;
3. **conditional operation compliance:** whether the admitted output satisfies the requested transformation and invariants.

Malformed output is excluded from the conditional compliance denominator; valid ABC that violates the operation contract is admitted but non-compliant (PDF p. 7; `/tmp/paper-digest/2609.34994v1.txt:373-386`).

The paper describes checker behavior but does not provide checker pseudocode, exact normalization rules, parser version, tolerance rules, or a formal schema.

Reported operation-level checks include:

- **Add chords:** compare melody bars before and after; check expected quoted chord symbols.
- **Inpainting:** compare non-target bars for preservation and target bars for modification.
- **Transpose:** check requested resulting key and preservation of structural/rhythmic relations.

### Exact reliability results

#### Overall

| Measure | Base Llama | LoRA-adapted |
|---|---:|---:|
| Extractable ABC | 1,234 / 1,750 = **70.5%** | 1,750 / 1,750 = **100%** |
| Checker admission | 514 / 1,750 = **29.37%** | 1,739 / 1,750 = **99.37%** |
| Conditional compliance | **0.7205** | **0.9798** |
| Strict feature eligibility | 14 / 1,750 = **0.8%** | 1,548 / 1,750 = **88.5%** before equalization |

Evidence: Table 1 and Figure 7, PDF pp. 8–10; `/tmp/paper-digest/2609.34994v1.txt:427-477`, `568-579`.

#### Table 1 values

The printed/extracted Table 1 reports these values:

| State | Base admission | FT admission | Base compliance | FT compliance |
|---|---:|---:|---:|---:|
| Add Chords | .276 | .996 | .3910 | .9702 |
| Generation before harmonization | — | — | .7148 | .9514 |
| Inpaint + chords | .300 | .996 | .7942 | .9904 |
| Transpose + chords | — | — | .8221 | .9796 |
| Melody generation | .348 | .980 | .7346 | .9832 |
| Melody inpainting | — | — | .6944 | .9915 |
| Melody transpose | .332 | .984 | .8548 | .9923 |
| Overall | .2937 | .9937 | .7205 | .9798 |

The extracted table contains blank admission cells for several chained states; I do not infer values that are not explicitly recoverable from the paper. Evidence: Table 1, PDF p. 9; `/tmp/paper-digest/2609.34994v1.txt:446-464`.

Additional checker diagnostics for the fine-tuned model:

- Chord addition preserved **4,639 of 4,644** compared melody bars.
- Expected quoted chord symbols appeared in **224 of 249** admitted turns.
- Inpainting preserved **8,886 of 9,043** non-target bars.
- Inpainting modified **1,168 of 1,230** target bars.
- Transposition matched the requested key in **492 of 496** admitted turns.

Evidence: PDF p. 9; `/tmp/paper-digest/2609.34994v1.txt:442-469`.

### Musical-feature analysis

The authors explicitly treat these as **formative, reference-relative descriptors**, not absolute musical-quality scores.

#### Methods

- Nine pitch/rhythm comparisons.
- Pairwise Euclidean distances.
- Kullback–Leibler divergence.
- Overlap area (OA).
- Mirror-image KDE support correction from Schuster because distances are non-negative and ordinary Gaussian KDE leaks mass below zero.
- Chord-bearing states additionally use chord-tone/non-chord-tone ratio (**CTnCTR**).
- Pitch-in-scale and chord-in-scale rates use Mann–Whitney tests with Holm correction.
- Scenario equalization reduces the fine-tuned feature population from 1,548 to **1,471**.
- All **63 planned comparisons**—nine features across seven states—are calculable for the adapted model; the base population is too sparse for equivalent analysis.

Evidence: PDF pp. 7, 9; `/tmp/paper-digest/2609.34994v1.txt:388-397`, `471-490`.

#### Fine-tuned OA ranges

| Evaluated state | OA range across nine features |
|---|---:|
| Add Chords | **0.8952–0.9724** |
| Generation before harmonization | **0.8297–0.9687** |
| Inpainting with chords | **0.9315–0.9853** |
| Transposition with chords | **0.8301–0.9862** |
| Melody generation | **0.8727–0.9711** |
| Melody inpainting | **0.8875–0.9731** |
| Melody transposition | **0.7972–0.9730** |

CTnCTR OA:

- Add Chords: **0.9718**
- Inpainting with chords: **0.9652**
- Transposition with chords: **0.9696**

Pitch-/chord-in-scale comparisons are ceiling-heavy: reference and candidate medians are **1.0 in all ten comparisons**; candidate rates are slightly higher under the implemented definitions.

The paper reports ranges rather than a full per-feature result table, so it does not support stronger claims about which individual musical characteristics improved.

### LCS and corpus-overlap analysis

The paper uses Longest Common Subsequence similarity as a corpus-overlap measure, explicitly **not** as a plagiarism detector.

Representation:

- note pitch classes and chord pitch-class sets encoded relative to the resolved tonic;
- invariant to consistent global transposition;
- preserves durations and event order.

Comparison:

- candidate-to-training overlap;
- validation-to-training overlap as held-out baseline;
- descriptive high-overlap flag: **LCS copy > 0.8**;
- Mann–Whitney tests compare distributions.

Results:

- The adapted model’s seven thresholded high-overlap rates were all below their corresponding held-out validation rates.
- Reference baseline rates reported: **15.60%** for chord-bearing references and **27.60%** for melody-only references.
- Add Chords had an unadjusted distribution difference, **p = 0.0072**, but its flagged rate was **14.47%**, below the **15.60%** held-out rate.
- Other six comparisons had **p = 0.0622–0.5852**.
- Author conclusion: no systematic increase in high-overlap sequences under this representation and threshold.

The authors explicitly state that this does not prove absence of memorization, plagiarism, authorship, or intent (PDF pp. 7, 9, 11; `/tmp/paper-digest/2609.34994v1.txt:398-418`, `486-490`, `645-655`).

### Qualitative case and prototype

#### Four-turn case

The author-selected evaluated dialogue is identified as **song_id=44**:

1. Create in **A Dorian, 6/8** — establishes melody.
2. Add chords — inserts **“Am”** and **“G”** while preserving melody.
3. Inpaint bars **3–5** — rewrites those bars and retains other bars.
4. Transpose to **C Dorian** — transposes melody and chord symbols together.

Figure 8 shows a schematic ABC state sequence. The paper stresses that it illustrates the evaluated semantics but is not evidence of abstract musical understanding (PDF pp. 9, 12; `/tmp/paper-digest/2609.34994v1.txt:503-505`, `583-589`, `619-639`).

#### NONOTO integration

The authors extended the model-agnostic NONOTO score editor with a natural-language/ABC path:

- inspect or edit symbolic material;
- request an operation in natural language;
- receive revised ABC;
- visualize notation;
- audition via existing audio/MIDI facilities.

It is presented as an architectural demonstration, **not** a professional composition environment or HCI evaluation (PDF pp. 10, 13; `/tmp/paper-digest/2609.34994v1.txt:550-563`, `669-704`).

### Limitations and artifact status

#### Explicit limitations

The authors limit the evidence to:

- Irish traditional music;
- five operations;
- curated prompt templates;
- primarily monophonic lead-sheet ABC;
- fixed whole-artifact scope for chord addition and transposition;
- local bar scope for inpainting.

They do not establish:

- cross-genre generalization;
- superior musical quality;
- human-AI co-creativity;
- preference over BeatEdit, MusiChat, deterministic algorithms, or constraint solvers;
- absence of memorization or plagiarism.

Transposition is particularly revealing: the authors acknowledge that a deterministic symbolic algorithm is preferable when exact transposition alone is required (PDF pp. 11–13; `/tmp/paper-digest/2609.34994v1.txt:595-666`).

#### Artifact/reproducibility status

In the complete v1 PDF and extracted text, I found:

- no public code URL;
- no dataset URL;
- no model-adapter download;
- no license;
- no checker implementation;
- no detailed operation-record schema;
- no appendix;
- no full per-feature table;
- no detailed decoding or hardware specification.

Therefore, the paper is technically informative but not independently reproducible from the manuscript alone. The authors do disclose that ChatGPT was used only after the research and experiments for English editing, organization, and exposition; they claim that the research problem, system, protocol, execution, and scientific analysis were developed without generative-AI assistance (PDF p. 14; `/tmp/paper-digest/2609.34994v1.txt:735-744`).

### Relevance to source-preserving mashups, repair, and provenance

#### Directly useful ideas

1. **Persistent authoritative state:** the current symbolic artifact, rather than a fresh regeneration, is the input to every subsequent edit.
2. **Typed operations:** each natural-language request resolves to an operation with explicit authorized-change and preservation rules.
3. **Invariant-based checking:** correctness is not merely “valid music”; it includes unchanged melody, unchanged non-target bars, or preserved rhythm/structure.
4. **Denominator-aware evaluation:** syntax failures, operation failures, musical-feature analysis, and overlap analysis are reported separately.
5. **Minimal-edit framing:** the inpainting contract is a useful starting point for repair systems that should alter only damaged regions.
6. **LLM plus deterministic mechanisms:** the paper itself argues that exact transformations should remain deterministic where possible.

#### Missing provenance capabilities

The paper’s “preservation” is structural, not provenance-aware. It does not retain:

- source-file identifiers;
- event- or bar-level lineage;
- source attribution after copying or transformation;
- provenance DAGs;
- edit histories;
- hashes or immutable state versions;
- distinction between copied, transformed, generated, and repaired material;
- multiple simultaneous source artifacts.

Its LCS experiment measures corpus-relative overlap, not source provenance or copyright lineage. Thus it should not be treated as a provenance solution.

### Concrete research directions

1. **Typed provenance-bearing state:** augment each ABC event/bar with stable IDs, source ID, source span, transformation history, confidence, and pre/post hashes.
2. **Operation records:** represent requests as structured objects such as `{operation, scope, target_bars, input_state_hash, invariants, provenance_policy}` while retaining the natural-language request.
3. **LLM planner + deterministic executor:** let the LLM resolve intent and propose material, but use deterministic ABC transformations and validators for transposition, copying, bar preservation, and repair.
4. **Mashup-specific operations:** add `import_source`, `align_sources`, `borrow_span`, `crossfade`, `reharmonize`, and `replace_with_attribution`, each with source-preservation and conflict rules.
5. **Repair metrics:** measure changed-event precision, unchanged-event recall, minimal edit distance, target-repair success, musical validity, and provenance completeness.
6. **Provenance-aware overlap analysis:** combine tonic-relative LCS with exact and approximate source matching, copied-span attribution, and transformation-aware lineage—not merely a >0.8 overlap flag.
7. **Constraint-programming hybrid:** use the LLM for intent interpretation and candidate generation, with a solver enforcing hard invariants such as meter, bar duration, voice continuity, source protection, and no-unattributed copying.
8. **Human evaluation:** test whether musicians perceive the system as preserving intent, controlling edits, and making authorship/source contributions intelligible.
9. **Broader stress tests:** evaluate cross-genre repertoires, polyphony, longer untemplated conversations, invalid intermediate states, and nested/local scopes such as “transpose bars 5–8.”

**Bottom line:** the paper provides a strong operational template for persistent, checker-backed symbolic editing, but its notion of preservation stops at musical structure. For explainable source-preserving mashups and repair, the key extension is to make every preserved or changed symbolic event explicitly traceable to its source and edit history.

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
