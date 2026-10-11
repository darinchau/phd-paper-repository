---
title: "Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts"
authors: "Chao Peter Yang, Cynthia Rudin, Yue Jiang, Simon Mak, and Stephen Ni-Hahn"
year: 2026
doi: 10.48550/arXiv.2609.32788
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yang-2026-getting-motif-ated-controllable-ai.pdf"
pdf_filename: yang-2026-getting-motif-ated-controllable-ai.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts**.” arXiv:**2609.32788v1**, `[cs.LG]`, 26 September 2026. Listed as a NeurIPS 2026 Creative AI Track paper. The PDF contains 18 pages: main paper pp. 1–6, references pp. 7–8, appendices pp. 8–11, and the NeurIPS checklist pp. 11–18.

## 1. Document Information

- **Canonical source:** arXiv `2609.32788v1`; official PDF preserved as `yang-2026-getting-motif-ated-controllable-ai.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40l1x7_q3gz.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and version

**Yang, Chao Peter; Cynthia Rudin; Yue Jiang; Simon Mak; Stephen Ni-Hahn.**  
“**Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts**.” arXiv:**2609.32788v1**, `[cs.LG]`, 26 September 2026. Listed as a NeurIPS 2026 Creative AI Track paper. The PDF contains 18 pages: main paper pp. 1–6, references pp. 7–8, appendices pp. 8–11, and the NeurIPS checklist pp. 11–18.

- Code: <https://github.com/cpyang123/motigen>
- Demo: <https://motigen-site.github.io/>
- Authors cite NotaGen [Wang et al., 2025], Theme Transformer [Shih et al., 2022], FIGARO [von Rütte et al., 2023], and MIR motif-discovery literature.

I inspected all PDF pages, figures, tables, appendices, and the supplied extracted text.

---

### 1. Core contribution

**Author claim — Abstract, pp. 1–2; Conclusion, p. 6:**  
MotiGen retrofits motif control onto a pretrained symbolic music language model by combining:

1. A structured `%motif:` ABC prompt line.
2. A scalar attention bias toward motif-prompt tokens.
3. Two-phase curriculum training:
   - motif-centered crops;
   - full annotated scores.
4. A shared motif extractor/evaluator.

The reported full system contains the prompted motif in **92.3%** of generated pieces.

**Interpretation:** This is primarily a controllability and motif-grounding paper, not a source-preserving recomposition or provenance paper. The motif is abstract and transformed, rather than an exact source excerpt.

---

### 2. Pretrained base model and data

#### Base model

**Section 3.4, p. 4; Appendix A, pp. 8–9**

MotiGen fine-tunes the public **NotaGen-large** checkpoint:

- NotaGen pretraining: approximately **1.6M ABC-notation pieces**.
- NotaGen author fine-tuning: approximately **9k classical scores** with period/composer/instrumentation prompts.
- Architecture:
  - 20-layer patch-level encoder;
  - 6-layer character-level decoder;
  - hidden size 1280;
  - patch length 1024;
  - patch size 16;
  - patch-streaming regime.
- Fine-tuning:
  - AdamW;
  - learning rate `10^-5`;
  - batch size 1;
  - early stopping for up to 10 epochs on held-out loss.

#### MotiGen training data

**Section 3.4, p. 4; Appendix B, p. 9; Appendix D, p. 11**

- OpenScore Lieder: approximately **1.3k Romantic-era songs**, using the `V:1` vocal line.
- Irishman corpus: **216k+ monophonic folk tunes**.
- All pieces are wrapped as single-voice ABC scores.
- Data are augmented across **12 keys**.
- Phase-1 focused set: **650k+ motif-centered crops**.
- The model is trained only for **monophonic** generation.
- The extracted length-4 motif distribution contains **210 distinct patterns** and is highly skewed:
  - `(0,-1,-1,-1)` occurs 62,356 times;
  - the two most common patterns account for approximately **48%** of annotated pieces;
  - a pattern such as `(0,3,3,3)` occurs only twice.

**Caveat:** The paper alternates between describing the full source pool as 200k+/217k pieces and describing 12-key augmentation. It does not clearly state whether those counts refer to unique pieces or augmented instances.

---

### 3. Motif representation

#### Abstract representation

**Section 3.1, pp. 3–4; Figure 2, p. 4; Appendix C, pp. 9–11**

A motif is encoded as signed, transposition-invariant interval classes:

- `+1/-1`: step;
- `+2/-2`: skip;
- `+3/-3`: leap;
- initial `0`: anchor for the first note.

Example:

```text
(0, 3, -1, -1)
```

means a starting note, leap upward, then two downward steps.

The representation:

- uses diatonic letter-step distance;
- preserves direction;
- distinguishes enharmonic spellings;
- collapses immediate repeated pitches;
- ignores rhythm and durations;
- does not require exact pitches.

Example from Figure 2:

```text
%motif:v1:step_skip_leap: 0,3,-1,-1
```

An optional concrete realization is supplied as:

```text
%motif:abc: G B d c
```

In abstract-only inference, the model is expected to emit its own concrete realization.

#### Extraction

**Section 3.1, p. 3; Algorithm 1, p. 11**

The parser:

1. parses the ABC melody;
2. removes immediate equal-pitch repetitions;
3. scans windows of length 4–10, stride 1;
4. converts each window to interval classes;
5. selects the most frequent pattern.

The experiments focus on length-4 motifs.

Appendix C reports a transposition test over **2,353 pieces × 12 keys**: extracted motifs were identical except for 29 cases attributed to inconsistent source encodings.

**Important limitation:** The evaluator recognizes any occurrence of the same coarse interval-class contour, in any key and anywhere in the melody. It does not require the original pitch sequence, rhythm, phrase position, or source notes.

---

### 4. Prompting, attention bias, and curriculum

#### Attention bias

**Section 3.2, p. 4; Figure 3, p. 5**

At patch-level attention, MotiGen modifies the attention logits:

```text
αij = qi kjᵀ / √d + β · 1[j ∈ M]
```

where `M` is the set of patch positions belonging to `%motif:` lines.

Reported settings:

- `β = 4`: selected operating point;
- `β = 2`: little effect;
- `β ≥ 8`: generation collapses.

The bias is used during training and inference so the model learns to use the emphasized prompt channel rather than receiving only post-hoc steering.

#### Curriculum

**Section 3.3, p. 4; Figure 3, p. 5; Appendix A, pp. 8–9**

- **Phase 1 — focused crops:** crops extending approximately **±5 measures** around motif occurrences, with the original header and motif prompt lines.
- **Phase 2 — full pieces:** complete scores annotated with their extracted motifs.
- Figure 3 indicates motif bias is off during Phase 1 and on during Phase 2, with phase-matched evaluation.
- Appendix A explicitly warns that evaluating a bias-trained checkpoint with bias disabled distorts the training curve.

**Interpretation:** The crop phase is intended to reduce the distance between the prompt and relevant musical evidence; the full-score phase teaches recurrence, variation, and integration over longer contexts.

---

### 5. Evaluation protocol

**Section 4, p. 5; Appendix C, pp. 10–11**

For each model–motif pair:

- 24 motifs total:
  - 8 from ranks 1–10, band A;
  - 8 from ranks 11–40, band B;
  - 8 from ranks 41–210, band C.
- 50 generated pieces per motif.
- Decoding:
  - top-k = 9;
  - top-p = 0.9;
  - temperature = 1.2.
- Evaluation excludes prompt lines when measuring body containment.

#### Metrics

1. **Body containment:** whether the generated melody contains the target pattern at least once.
2. **Realization faithfulness:** whether the model’s emitted `%motif:abc:` line itself realizes the requested abstract pattern.

The paper describes a 2×2 containment/faithfulness interpretation, but does not provide a separate joint contingency table.

---

### 6. Main results and ablations

#### Table 1 — Main ablation, p. 6

Pooled over 24 motifs × 50 samples = **1,200 generations**. Intervals are 95% Wilson intervals.

| Configuration | Containment | Faithfulness | Motifs/measure |
|---|---:|---:|---:|
| MotiGen, `β=4` + curriculum | **92.3%** [90.7, 93.7] | **93.0%** [91.4, 94.3] | **0.25** |
| No attention bias | 77.8% [75.4, 80.1] | 75.8% [73.3, 78.2] | 0.18 |
| No cropped phase | 86.7% [84.6, 88.5] | 87.2% [85.2, 89.0] | 0.22 |
| No bias and no cropped phase | 79.4% [77.0, 81.6] | 76.1% [73.6, 78.4] | 0.19 |
| No motif prompt base rate | 36.8% [34.1, 39.5] | — | 0.06 |

**Author interpretation:** Attention bias contributes most; the cropped phase has a milder average effect but matters more for tail motifs and smaller datasets. The components are complementary.

**Notable inconsistency:** Section 4.1 describes the base rate as **35.9%**, whereas Table 1 reports **36.8%**.

#### Table 2 — Data scaling, Appendix B, p. 10

Point estimates are containment A/B/C followed by faithfulness A/B/C.

| Training size | Full recipe | No bias | No crop | Neither |
|---|---|---|---|---|
| 1k | C: 55.0/27.2/19.0; F: 20.2/4.2/1.5 | C: 54.0/30.2/20.5; F: 14.2/4.8/3.0 | C: 52.8/29.0/16.5; F: 15.0/4.2/1.0 | C: 53.5/31.5/16.0; F: 10.5/3.2/1.2 |
| 10k | C: 84.8/64.5/53.0; F: 84.5/68.0/59.2 | C: 73.5/61.0/43.5; F: 58.2/49.8/38.0 | C: 68.5/39.2/21.2; F: 38.8/21.0/4.2 | C: 60.2/46.8/20.2; F: 21.8/10.5/3.2 |
| Full | C: 96.2/94.0/86.8; F: 95.2/96.8/87.0 | C: 89.8/86.5/57.2; F: 85.5/86.8/55.2 | C: 95.8/87.0/77.2; F: 95.0/87.2/79.5 | C: 87.8/84.0/66.5; F: 82.2/80.8/65.2 |

Unprompted baselines:

- 1k: containment A/B/C = 47.0/30.2/14.5;
- 10k: 47.8/32.5/16.0;
- full: 53.2/38.0/19.0.

**Interpretation:** The strongest evidence is for full and 10k training. At 1k, all systems have poor faithfulness and the full recipe is not uniformly best, so the paper’s broad “full recipe advantage” should not be generalized to extremely small data.

---

### 7. Quality and qualitative evidence

**Figure 4 and Section 4.2, p. 6**

The case study prompts `(0,3,-1,-1)` and compares one MotiGen melody with a Fable 5-generated ABC melody.

Author claims:

- MotiGen contains the motif and transformed occurrences.
- MotiGen uses more varied rhythms and connecting material.
- MotiGen realizes both sixth and fifth leaps.
- Fable 5 repeatedly uses essentially the same sixth-up realization and produces mostly motif repetitions plus a short cadence.

**Limitations of this evidence:**

- It is one qualitative example.
- Fable 5 is not a matched symbolic-music baseline.
- There is no human listening test.
- There are no objective musicality, harmonic coherence, playability, diversity, style, or novelty metrics.
- “Motifs/measure” measures motif occurrence density, not musical quality.
- The paper explicitly defers larger-scale human evaluation.

Thus, the 92.3% result is strong evidence of automatic pattern containment, but not evidence of overall composition quality.

---

### 8. Limitations and artifact status

#### Stated or directly evident limitations

- Monophonic only; no harmony, accompaniment, voice-leading, or polyphonic interaction.
- No human evaluation.
- Coarse four-note interval-class representation.
- Tail motifs are substantially harder than frequent motifs.
- Attention bias can collapse generation at high values.
- Results are tied to ABC notation, NotaGen, and the selected corpora.
- No explicit unseen-composer, unseen-style, or piece-level leakage analysis is reported.
- Exact train/validation split, random seeds, and per-run timing are not fully specified despite the checklist claiming complete reproducibility.
- The paper contains draft-quality reference notes, including:
  - “TODO: verify venue/pages” for one reference;
  - “Check for a published version before submission” for MuPT.

#### Artifacts

**Appendix A, p. 8; repository inspection**

The paper claims code and a demo are available. The public GitHub repository currently contains:

- motif extraction and containment code;
- a demo notebook;
- ABC rendering utilities;
- five training examples;
- 20 generated ABC samples and a manifest;
- README and MIT license.

The repository is at commit:

```text
2b18160f405d0e1c8597d766497869f77d333162
```

The repository appears to be an evaluation/sample companion release, not a complete training pipeline or released MotiGen checkpoint. The paper relies on the public NotaGen checkpoint but does not clearly identify a downloadable MotiGen model checkpoint.

---

### 9. Relevance to source-preserving symbolic mashups

#### Useful transferable ideas

**Author-supported method:**

- Structured motif prompts provide an inspectable control interface.
- The evaluator is deterministic and transposition-invariant.
- The emitted concrete realization can be logged alongside the abstract request.
- Focused crops are a plausible way to teach prompt-to-content grounding.
- Attention bias provides a tunable control-strength parameter.

**Interpretation for provenance-preserving mashups:**

A mashup system could represent each source contribution as:

```text
%source:A:motif:...
%source:B:motif:...
```

and retain:

- source piece ID;
- original note span;
- transformation type;
- transposition;
- rhythmic changes;
- generated occurrence locations;
- confidence and evaluator result.

However, MotiGen itself does **not** provide source provenance. Its motif evaluator proves only that a coarse contour appears somewhere in the output. It does not establish that the output copied, transformed, or preserved a particular source passage.

#### Concrete research directions

1. **Dual-source provenance prompts**  
   Condition on separate motifs from sources A and B, with source IDs and protected roles such as melody, bass, or accompaniment.

2. **Richer motif representations**  
   Add rhythm, meter position, phrase boundaries, pitch intervals, voice, harmony, and allowable transformation classes. Keep the coarse contour as one abstraction level rather than the entire identity representation.

3. **Provenance-aware training crops**  
   Crop source passages around known motifs while preserving note-level source IDs. Train the model to emit attribution metadata for every realized occurrence.

4. **Conflict-aware recomposition**  
   Detect clashes between source motifs—meter, harmony, register, dissonance, cadence—and search minimal repairs while preserving protected notes.

5. **Separate evaluation dimensions**  
   Measure:
   - exact source-note retention;
   - transformed motif recall;
   - source A/B attribution precision;
   - source identity;
   - compatibility;
   - structural coherence;
   - novelty;
   - playability;
   - explanation faithfulness.

6. **Causal control tests**  
   Compare prompt removal, motif substitution, attention-bias changes, and counterfactual source prompts. This would test whether the model actually uses the prompt rather than reproducing frequent training patterns.

7. **Leakage-resistant splits**  
   Split by source piece and composer before transposition augmentation. Include unseen motifs, rare motifs, and cross-style conditions.

8. **Polyphonic extension**  
   Adapt the prompt and evaluator to melody–bass–harmony roles, then test whether enforcing one source motif damages the other source’s identity or musical coherence.

### Bottom line

MotiGen offers a promising, relatively simple recipe for **abstract motif controllability** in a pretrained symbolic music model. Its strongest evidence is the large increase in automatic contour containment, especially from the matched attention bias and focused-crop curriculum. For the research program here, its most valuable components are the explicit prompt representation, deterministic transposition-invariant evaluator, and prompt-grounding curriculum. Its central gap is precisely provenance: it does not identify, preserve, or explain contributions from particular source pieces, and it does not evaluate mashup compatibility or source identity.

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
