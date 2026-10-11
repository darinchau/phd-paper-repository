---
title: "Tracing Inputs, Verifying Outputs: Validating Attribution in Music Generation"
authors: "Taejun Kim et al."
year: 2026
doi: 10.48550/arXiv.2610.09637
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-tracing-inputs-verifying-outputs-validating.pdf"
pdf_filename: al-2026-tracing-inputs-verifying-outputs-validating.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Tracing Inputs, Verifying Outputs: Validating Attribution in Music Generation**.” arXiv:**2610.09637v1**, [cs.SD], 7 October 2026; PDF footer says “Preprint. October 8, 2026.” 15 pages. Neutune and KAIST; correspondence: Taejun Kim.

## 1. Document Information

- **Canonical source:** arXiv `2610.09637v1`; official PDF preserved as `al-2026-tracing-inputs-verifying-outputs-validating.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zickp_ysvq.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliographic record

**Taejun Kim, Wonil Kim, Jongmin Jung, Hyeongseok Wi, Sangeun Kum, Keunhyoung Luke Kim, Taehyoung Kim, Dongjoo Moon, Seungsoon Park, Taewan Kim, Virginie Berger, Juhan Nam, and Jongpil Lee.**  
“**Tracing Inputs, Verifying Outputs: Validating Attribution in Music Generation**.” arXiv:**2610.09637v1**, [cs.SD], 7 October 2026; PDF footer says “Preprint. October 8, 2026.” 15 pages. Neutune and KAIST; correspondence: Taejun Kim.

The paper provides audio examples at `https://neutune.github.io/attr2027demo/`.

Key related bibliography:

- Kim et al. (2025), *From generation to attribution: Music AI agent architectures for the post-streaming era*.
- Morreale et al. (2025), *Attribution-by-design: Ensuring inference-time provenance in generative music systems*.
- Serra et al. (2025), *Supervised contrastive learning from weakly-labeled audio segments for musical version matching* — the CLEWS comparator.
- Li et al. (2024), MERT.
- Wu et al. (2023), CLAP.
- Gong et al. (2026), ACE-Step 1.5.
- Rouard et al. (2024), Nistal et al. (2024), and Parker et al. (2024) on audio-conditioned music generation.

The full reference list is on pp. 9–10.

---

### 2. Central attribution question

#### Authors’ definition

The paper separates attribution into two claims:

1. **Input-use claim:** a particular audio source was used during generation.
2. **Musical-effect claim:** that source’s musical characteristics shaped the output.

The authors argue that neither output similarity nor input records alone establishes both claims (p. 1, Abstract/Introduction; p. 2, §2.1).

- Output similarity can identify resemblance but cannot prove the source was used as an input.
- A provenance log can establish that an input was supplied but cannot prove that its musical characteristics affected the output.

Their proposed evidence is therefore:

> **recorded input provenance + controlled evidence that the recorded input changes the generated output + a separate audit for unrecorded training-data reproduction.**

#### Interpretation for mashups

This is primarily an **audio-generation attribution framework**, not a symbolic provenance framework. It tests whether a generator responds causally to conditioning inputs, but it does not establish that particular source melodies, chord events, or rhythmic motifs survived in the output.

---

### 3. MixAudio: conditioning and provenance design

#### Interface

Figure 1 and §3 (p. 3) show an audio-only, stem-level generator:

- One registered **prompt recording per generated stem**.
- Optional shared **context audio**, usually a mix of existing stems.
- Generated stems are produced separately and assembled section by section.
- No text is supplied to the generator.
- A track section is the unit of generation.
- Prompts are normally 1–2-second excerpts from the same stem and section as the target.

The generator accepts either:

1. **New-song generation:** prompts only.
2. **Remix generation:** existing stems are placed in the context and new/replaced stems are generated over them.

#### Architecture described in the paper

The model uses discrete audio tokens from a neural codec with residual vector quantization. Prompts, context, and targets are concatenated into one sequence:

- Context is prepended.
- Context and targets share temporal positional encoding.
- Section key and beat positions are additional inputs.
- Stem-level positional encoding binds prompt \(i\) to target \(i\).
- Requesting more stems appends more prompt–target pairs.

The paper gives no displayed architecture equations or detailed training objective. It defines the evaluation formulas operationally in Appendix B.

#### Rights-accounting convention

The authors associate:

- **Prompt use** with the recording-side contribution of the reference performance.
- **Context use** with the composition-side contribution shaping harmony and tempo.

They explicitly state that this is based on observed model behavior, **not on copyright law** (p. 3, §2.4).

When context is mixed into the final released master, the context recording’s rights holder is also recorded. This is an accounting design, not a legal determination.

---

### 4. Data, protocol, and baseline

#### Evaluation data

Table 4, Appendix A (p. 11):

| Source | Tracks | Sections/instances | Target stems | Contextless | Hours |
|---|---:|---:|---:|---:|---:|
| Training | 1,922 | 2,073 | 5,030 | 515 | 7.1 |
| Validation | 168 | 2,086 | 4,960 | 518 | 6.9 |
| MoisesDB | 112 | 1,058 | 2,266 | 282 | 5.6 |
| MUSDB18 | 150 | 1,593 | 2,778 | 458 | 8.3 |

Total: **6,810 instances and 15,034 target stems** (§4.1, p. 4).

Protocol:

- Sections shorter than 2 seconds or longer than 40 seconds are excluded.
- Context assignment probabilities: no context 0.15, one/two stems 0.45, three or more stems 0.40.
- Prompts are 1–2-second excerpts from the target stem’s own recording.
- Vocal stems are never prompts or targets, although vocals may occur in context.
- External beats are estimated with All-In-One; external tracks have no supplied key.
- One fixed-seed generation per instance.
- Outputs are discarded if fewer than 15% of 100-ms frames exceed −60 dBFS.
- ACE generates stems sequentially: rhythm, bass, then remaining stems.

#### Baseline

The baseline is **ACE-Step 1.5, 2B, Lego mode**. It was selected because it is the only runnable system the authors found that simultaneously:

- accepts a per-stem audio prompt,
- accepts audio context,
- conditions on the audio prompt itself,
- and generates individual stems.

Other systems were excluded for lacking context, lacking audio prompts, requiring text conversion, or producing fixed stem configurations (Table 5, p. 11).

---

### 5. Conditioning-faithfulness experiments

#### Prompt adherence

Table 1, §4.2 (p. 4), Appendix B.1 (p. 12):

- **MERT/style:** centered cosine similarity of MERT-v1-330M embeddings.
- **MFCC/timbre:** cosine similarity of averaged 20-dimensional MFCC vectors.
- `Δ = Matched − Random`.
- Random uses another track’s prompt from the same source.

| Source/system | MERT matched | MERT random | Δ | MFCC matched | MFCC random | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Training MixAudio | .550 | .014 | **.535** | .914 | .554 | **.360** |
| Training ACE | .549 | .121 | .428 | .838 | .602 | .236 |
| Validation MixAudio | .516 | .000 | **.516** | .911 | .550 | **.361** |
| Validation ACE | .534 | .123 | .411 | .831 | .602 | .229 |
| MoisesDB MixAudio | .582 | .124 | **.457** | .920 | .599 | **.321** |
| MoisesDB ACE | .652 | .264 | .388 | .912 | .674 | .237 |
| MUSDB18 MixAudio | .599 | .183 | **.416** | .942 | .667 | **.276** |
| MUSDB18 ACE | .624 | .313 | .311 | .942 | .756 | .186 |

**Authors’ claim:** MixAudio has the larger matched-versus-random margin for every source and both metrics. ACE’s higher raw MERT matched scores are misleading because its random generations also resemble unrelated prompts.

#### Controlled input swaps

Table 2, p. 4; discussion p. 5. Values are averaged over all four sources.

##### Prompt replacement

| Measure | MixAudio base | MixAudio swap | ACE base | ACE swap |
|---|---:|---:|---:|---:|
| Similarity to substituted prompt, MFCC | .63 | **.89** | .69 | **.85** |
| Similarity to original prompt, MFCC | .92 | **.64** | .88 | **.70** |
| Harmony with original context, chroma | .20 | .22 | .10 | .06 |

##### Context replacement

| Measure | MixAudio base | MixAudio swap | ACE base | ACE swap |
|---|---:|---:|---:|---:|
| Harmony with substituted context, chroma | .00 | **.21** | .00 | .06 |
| Harmony with original context, chroma | .21 | **.02** | .10 | .06 |
| Timbre with original prompt, MFCC | .92 | **.89** | .88 | **.87** |

Scale anchors:

- MFCC unrelated/matched: **.66/.92**
- Chroma unrelated/matched: **.02/.20**

**Authors’ interpretation:** MixAudio independently controls prompt-derived timbre and context-derived harmony. ACE follows prompt timbre but not context harmony.

#### Tempo and pitch transformations

Table 6, Appendix B.2 (pp. 12–13):

| Intervention | Metric | Oracle | MixAudio | ACE |
|---|---|---:|---:|---:|
| Prompt time-scaled ×0.9/1.1 | Output tempo unchanged | 100% | **95%** | 91% |
| Prompt time-scaled | Chroma Δ | ≈0 | −.003 | +.003 |
| Prompt time-scaled | MFCC Δ | ≈0 | −.005 | −.005 |
| Prompt pitch-shifted ±2 semitones | Chroma Δ | ≈0 | −.005 | −.025 |
| Prompt pitch-shifted | MFCC Δ | ≈0 | −.006 | −.006 |
| Context time-scaled ×0.9/1.1 | Output follows tempo | ≈90% | **83%** | 58% |
| Context time-scaled | MFCC Δ | ≈0 | −.005 | −.008 |
| Context transposed ±2 semitones | Chroma accuracy | ≈86% | **76%** | 33% |
| Context transposed | MFCC Δ | ≈0 | −.001 | +.002 |

**Authors’ claim:** MixAudio follows context tempo and transposition while preserving prompt timbre. ACE’s apparently stable harmony under prompt transformations reflects its failure to follow context in the first place.

#### What this actually verifies

The controlled swaps provide stronger evidence than similarity alone that:

- changing a prompt changes generated timbre;
- changing context changes generated harmony and tempo;
- the effects are at least partly separable.

They do **not** prove that the generator copied identifiable musical events from the prompt. They show controlled dependence on input properties.

---

### 6. musicDNA memorization audit

#### Purpose

Even if the logged inputs faithfully affect outputs, the model may reproduce a training stem not supplied as an input. Section 4.3 therefore searches generated stems against training stems.

A memorization is defined as reproducing a training stem, in recording or composition, other than the conditioning inputs.

- **Named memorization:** the record already names the reproduced work’s rights holders.
- **Unnamed memorization:** the record does not name them.
- Only unnamed memorization counts against the attribution record.

#### Retrieval protocol

- 497 validation queries and 497 training queries.
- Only melody-carrying instruments are audited; bass and drums are excluded.
- Training queries reuse the exact training conditioning; the query’s own conditioning track is excluded from search.
- Four retrievers:
  - musicDNA,
  - CLEWS,
  - CLAP,
  - MERT.
- Thresholds are set at the top 5% of validation scores and transferred to training:
  - musicDNA distance ≤ **0.672**
  - CLEWS distance ≤ **0.812**
  - CLAP cosine ≥ **0.971**
  - MERT cosine ≥ **0.974**

musicDNA and CLEWS use 20-second mono, 16-kHz windows with 5-second hops. The score is the minimum squared Euclidean distance between query and training windows. CLAP and MERT use maximum centered cosine similarity.

#### Listener classification

Figure 2 (p. 5) defines the decision tree:

- **A: Duplicate:** same dataset stem registered more than once; counted as named memorization.
- **B: Unrelated:** no shared melody or chord progression.
- **C: Commonplace:** only stock material.
- **Type I: Recording:** same composition and same timbre; recording reproduced.
- **Type II: Composition:** composition reproduced in a different timbre and copied element is core.
- **D: Incidental:** different-timbre composition resemblance, but copied element is incidental.

The audit pool contains:

- 171 flagged generated stems,
- 213 query–retrieved-match listening cases,
- 32 confirmed memorization cases:
  - 1 Type I,
  - 31 duplicates,
- 139 non-memorization cases.

Three paper authors judged the cases. They agreed on the category in 178/213 cases (84%, Fleiss κ=.75), and on whether a case was memorization in 191/213 (90%, κ=.82).

#### Table 3 results

Validation, 25 flags per retriever:

- musicDNA: 9 duplicates, 16 unrelated.
- CLEWS: 7 duplicates, 12 unrelated, 6 commonplace.
- CLAP: 1 duplicate, 24 unrelated.
- MERT: 3 duplicates, 22 unrelated.

Training:

- musicDNA, 34 flags: 1 Type I, 19 duplicates, 13 unrelated, 1 commonplace.
- CLEWS, 35 flags: 1 Type I, 14 duplicates, 16 unrelated, 4 commonplace.
- CLAP, 31 flags: 31 unrelated.
- MERT, 24 flags: 7 duplicates, 17 unrelated.

There were **no Type II or D cases**.

The single unnamed Type I reproduction recurred under all eight random seeds with its original conditioning, but **0/8** times when context was removed. The authors infer that the highly specific context drew the memorized stem out.

#### Detector comparison

Figure 3, §4.4 (p. 7):

- musicDNA flagged 29/32 confirmed memorizations: **recall .91**.
- CLEWS flagged 22/32: **recall .69**.
- Among its flags:
  - musicDNA: 29/59 confirmed, **precision .49**.
  - CLEWS: 22/60 confirmed, **precision .37**.
- CLAP flags were dominated by unrelated stems: 96–100% of its flags were category B.
- MERT flags were also mostly unrelated: 71–88% category B.
- MusicGen-style token test: 4 flags, all unrelated.
- MusicLM-style token test: 1 confirmed memorization and 33 unrelated flags.

**Authors’ claim:** musicDNA is the strongest tested detector for this audit, but the result is conditional on the flagged pool, catalog, model, thresholds, and human labels.

#### Important limitations stated by the authors

- Counts are **lower bounds**: unflagged memorization is never reviewed.
- Results apply to this model and catalog, not the architecture generally.
- Only melody-carrying instruments were audited.
- Vocal targets and lyrics were absent; lyrics may cause more composition-level memorization.
- Because no Type II case occurred, the detector comparison did not test copying of composition in a different timbre.
- Human labels came from three authors.
- Duplicate registrations dominate the confirmed matches and reflect dataset curation problems rather than model memorization.

---

### 7. Figures, tables, and equations

#### Figures

- **Figure 1, p. 3:** provenance-by-conditioning flow; prompt rights, context rights, generated stems, and final mix.
- **Figure 2, p. 5:** listener decision tree for duplicates, unrelated matches, commonplace material, recording memorization, composition memorization, and incidental copying.
- **Figure 3, p. 7:** detector-score distributions. Composition/version retrievers separate confirmed cases better than CLAP, MERT, or token matching.
- **Figure 4, p. 15:** MOS comparison. MixAudio lies between ACE and real stems; its largest advantage over ACE is context fit.

#### Tables

- **Table 1, p. 4:** prompt adherence.
- **Table 2, p. 4:** prompt/context swaps.
- **Table 3, p. 6:** human memorization classifications.
- **Table 4, p. 11:** data composition.
- **Table 5, p. 11:** baseline eligibility.
- **Table 6, p. 12:** tempo/pitch counterfactuals.
- **Table 7, p. 13:** prior memorization-audit protocols.
- **Table 8, p. 14:** FAD and subjective quality.

There are no conventional displayed mathematical equations in the paper. The important operational definitions are:

- `Δ = Matched − Random` for prompt adherence.
- MFCC cosine for timbre.
- centered MERT cosine for style.
- Pearson correlation over bar-averaged 12-bin chromagrams for harmony.
- minimum squared Euclidean window distance for musicDNA/CLEWS.
- maximum centered cosine for CLAP/MERT retrieval.
- ≥80% exact level-0 token matches for the MusicGen-style test.

---

### 8. Generation-quality results

Table 8, pp. 14–15:

#### MixAudio

| Source | FAD ×10⁻³ | Quality MOS | Prompt MOS | Context MOS |
|---|---:|---:|---:|---:|
| Validation | .596 | 2.81 ± .29 | 3.36 ± .32 | 3.45 ± .39 |
| MoisesDB | .997 | 2.77 ± .33 | 3.34 ± .33 | 3.43 ± .42 |
| MUSDB18 | 1.010 | 2.80 ± .27 | 3.18 ± .31 | 3.20 ± .30 |
| All | .868 | 2.80 ± .17 | 3.29 ± .19 | 3.36 ± .22 |

#### ACE

| Source | FAD ×10⁻³ | Quality MOS | Prompt MOS | Context MOS |
|---|---:|---:|---:|---:|
| Validation | .935 | 2.36 ± .25 | 2.73 ± .34 | 2.56 ± .44 |
| MoisesDB | 1.570 | 2.46 ± .28 | 2.62 ± .33 | 2.32 ± .34 |
| MUSDB18 | 1.571 | 2.02 ± .26 | 2.26 ± .30 | 2.29 ± .30 |
| All | 1.359 | 2.28 ± .16 | 2.54 ± .19 | 2.39 ± .21 |

Real-stem all-source reference MOS: quality **3.68 ± .14**, prompt **3.99 ± .13**, context **3.76 ± .15**.

The authors report MixAudio above ACE on all three quality dimensions and lower FAD on every source. The quality evaluation is supportive context, not evidence of attribution itself.

---

### 9. What the paper does and does not verify for symbolic mashups

| Question | Evidence from paper | Verdict |
|---|---|---|
| Was a registered audio source supplied to generation? | Stem-level input record | Yes, if the system log is trusted. |
| Did the generator respond to prompt timbre/style? | Prompt swaps and MFCC/MERT results | Supported for MixAudio. |
| Did the generator respond to context harmony/tempo/key? | Context swaps and transformations | Supported for MixAudio. |
| Is a particular source melody present in the output? | No symbolic event alignment or note-level attribution | Not verified. |
| Are particular chord events copied from a donor? | Chroma correlation only; no chord-event provenance | Not verified. |
| Are all mashup sources represented in the output? | One prompt per target plus optional shared mix context | Not verified. |
| Is an absent, unauthorized training source reproduced? | musicDNA audit | Partially investigated; absence is not established. |
| Is a source’s legal contribution recording-side or composition-side? | Model-specific accounting convention | Not a legal conclusion. |
| Does the system preserve provenance through symbolic transformations? | No symbolic representation or transformation ledger | Not addressed. |
| Does it test composition copying in a different timbre? | No Type II cases | Explicitly not tested. |

The strongest transferable idea is **causal input validation**: replacing one conditioning source while holding other conditions fixed is more informative than merely measuring similarity.

The weakest transfer is the memorization audit. musicDNA is an audio version-identification system, and its measured success is mainly on recording/version-level matches and duplicate registrations. It does not demonstrate reliable detection of transformed symbolic material.

---

### 10. Concrete research directions for provenance-preserving recomposition

1. **Event-level provenance ledger**

   Represent each output note/event with:

   ```text
   source_id
   source_track
   source_section/bar
   source_event_span
   operation: copy | transpose | retime | ornament | interpolate | newly generated
   transformation parameters
   model/version/seed
   ```

   This would extend MixAudio’s stem-level record to bar-, phrase-, or event-level provenance.

2. **Symbolic counterfactual swaps**

   Run factorial experiments that separately replace:

   - melody donor,
   - harmony donor,
   - rhythm donor,
   - instrumentation/timbre donor,
   - form/section context.

   Measure note-level changes in pitch, intervals, onset positions, chord labels, voice leading, contour, and groove while holding seed and unrelated inputs fixed.

3. **Source-presence metrics**

   Add explicit metrics for:

   - exact event/n-gram recall,
   - transposition-invariant interval recall,
   - rhythm-pattern recall,
   - chord-progression recall,
   - phrase-boundary/form recall,
   - output attribution precision,
   - causal effect size from donor removal or replacement.

   This would answer “is source \(s\) present?” rather than only “does the output sound similar?”

4. **Symbolic musicDNA analogue**

   Search outputs against all donor and training scores using several invariant representations:

   - exact pitch/onset sequences,
   - transposition-invariant intervals,
   - rhythm-only patterns,
   - chord-function sequences,
   - melody contour,
   - voice-leading graphs,
   - motif-level approximate matching.

   Calibrate thresholds on deliberately unrelated and commonplace material, then have independent musicians label composition-level copying.

5. **Multi-source attribution tests**

   Shared context mixes obscure which contributor shaped an output. Separate every context stem and run:

   - leave-one-source-out tests,
   - donor replacement tests,
   - pairwise and higher-order combinations,
   - Shapley-style contribution estimates,
   - interaction tests for harmony–melody combinations.

6. **Transformation-aware provenance**

   Test known legal/creative transformations:

   - transposition,
   - tempo scaling,
   - rhythmic quantization,
   - octave displacement,
   - ornamentation,
   - reharmonization,
   - instrument reassignment,
   - melodic fragmentation and recombination.

   A provenance system should preserve the source link even when surface audio similarity falls substantially.

7. **Explicit source-preserving generation**

   Train or constrain a symbolic generator to emit source tags alongside events. The decoder could enforce:

   - selected source events must survive,
   - source events may be transformed only within declared limits,
   - newly generated events receive an explicit “novel” tag,
   - output phrases cannot silently switch donor identity.

8. **Independent audit of the audit**

   As this paper acknowledges, logging alone should not be trusted. Store hashes of input assets, section boundaries, transformations, model checkpoint, seed, and output events. Then separately audit the output against the complete training and licensed-source catalogs.

### Bottom line

The paper provides a persuasive demonstration that **input records can be strengthened by controlled evidence that different audio inputs control different output properties**. MixAudio follows prompt timbre and context harmony/tempo substantially better than ACE under these tests.

For symbolic mashups, however, it does **not** verify note-level source presence, transformed melodic reuse, chord-event provenance, or complete absence of unrecorded source material. Its most valuable contribution is therefore methodological: combine immutable input records with counterfactual input swaps and independent output audits, then extend those tests from audio stems to symbolic events and transformations.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `explainability-and-auditability`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
