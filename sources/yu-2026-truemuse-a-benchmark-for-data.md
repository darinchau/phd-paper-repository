---
title: "TrueMuse: A Benchmark for Data Attribution in Text-to-Music Models"
authors: "Jiawei Yu and Jian Liu"
year: 2026
doi: 10.48550/arXiv.2610.00835
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2026-truemuse-a-benchmark-for-data.pdf"
pdf_filename: yu-2026-truemuse-a-benchmark-for-data.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

It constructs attribute-specific text-to-music models by fine-tuning existing diffusion generators on known source clips. It then evaluates black-box retrieval methods that attempt to recover those source clips from generated audio.

## 1. Document Information

- **Canonical source:** arXiv `2610.00835v1`; official PDF preserved as `yu-2026-truemuse-a-benchmark-for-data.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zzje7_rtkn.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### TrueMuse digest — arXiv:2610.00835v1

### Version and bibliography

- **Title:** *TrueMuse: A Benchmark for Data Attribution in Text-to-Music Models*
- **Authors:** Jiawei Yu and Jian Liu, University of Georgia.
- **Local artifact analyzed:** `2610.00835v1.pdf`, 19 PDF pages; header identifies **arXiv:2610.00835v1 [cs.LG], 30 Sep 2026**.
- **Version ambiguity:** you report that the arXiv API lists **v2**. The findings below refer exclusively to the downloaded **v1**. Results, wording, and appendices should be rechecked against v2 before citation.
- **Status:** preprint; no venue or repository URL is supplied. The paper says: **“Code and Dataset will be released upon acceptance”** (p.1).

### What the paper actually contributes

This is primarily a **controlled benchmark**, not a new end-to-end source-attribution model.

It constructs attribute-specific text-to-music models by fine-tuning existing diffusion generators on known source clips. It then evaluates black-box retrieval methods that attempt to recover those source clips from generated audio.

The learned “mapper” is a linear projection on top of frozen audio embeddings; it is an enhanced baseline, not the central generative model.

---

### Benchmark construction

#### Core procedure

Pages 3–4, §3.1, Figure 1, Equations (1)–(2):

1. Start with a pretrained text-to-music diffusion model.
2. Select a small source set \(D_c\) for musical attribute \(c\).
3. Fine-tune only the denoising U-Net using an association prompt such as:

   > “a recording of [V] musician”

   where `[V]` is a rare identifier such as `sks`.
4. Generate new audio using contextual and style prompts containing the identifier.
5. Treat \(D_c\) as the known attribution target.

The authors describe inclusion in fine-tuning as controlled ground truth. Strictly, this is **known training-set provenance**, not proof that every source clip causally influenced every generated output.

#### Four attribution sets

Table 1 and §§3.1.1–3.1.4, pp.4–5:

| Set | Attributes | Source construction | Clips/attribute |
|---|---:|---|---:|
| Melody-Centric | 50 | Short FMA clips with identifiable pitch contours | 1 |
| Instrument-Centric | 25 | YouTube clips dominated by an instrument | 3 or 6 |
| Musician-Centric | 50 | Different tracks by the same FMA artist | 3 or 6 |
| Genre-Centric | 8 | Clips from six different musicians per genre, using frequent FMA genres | 3 or 6 |

The design attempts to test progressively more abstract properties:

- melody: pitch structure invariant to instrumentation;
- instrument: timbre invariant to musical context;
- musician: recurring artist style across compositions;
- genre: shared stylistic structure rather than individual artist identity.

#### Dataset scale

Table 1, p.4:

- **133 attributes**
- **797 total fine-tuning clips** across the 3- and 6-clip configurations
- **648 fine-tuned generator models**
  - Melody: 150
  - Instrument: 150
  - Musician: 300
  - Genre: 48
- **95,456 generated samples**
- 15 contextual prompts per attribute.
- Style prompts:
  - 28/28/8 for Melody, Instrument, and Musician across AudioLDM2/Mustango/Stable Audio Open;
  - 28 for Genre across all three generators.
- Four generated waveforms per prompt.

Per-generator totals:

- AudioLDM2: 37,152 samples
- Mustango: 37,152
- Stable Audio Open: 21,152

#### Prompt construction

Pages 4–5 and Appendix A.1, pp.12–13:

- Prompts were generated using **Claude**, based on official examples from each generator.
- Contextual prompts vary scene, accompaniment, and sonic environment.
- Style prompts vary genre while retaining the target attribute.
- Prompts were used “as-is.”
- Stable Audio Open receives only eight style genres for Melody, Instrument, and Musician because of limited caption diversity.

This introduces a potentially important confound: prompt generation quality and prompt distribution are part of the benchmark.

---

### Generators and fine-tuning

Appendix A.2, Table 2, p.13:

| Generator | Checkpoint | Parameters |
|---|---|---:|
| AudioLDM2 | `cvssp/audioldm2` | 712M |
| Mustango | `declare-lab/mustango` | 1.4B |
| Stable Audio Open | `stabilityai/stable-audio-open-1.0` | 1.1B |

All generate ten-second clips. AudioLDM2 and Mustango output 16-kHz audio; Stable Audio Open outputs 44.1-kHz audio and is resampled to 16 kHz.

Fine-tuning details, Appendix A.6.1, p.15:

- Only the denoising U-Net is fine-tuned.
- Text encoder, VAE, and music-structure embeddings remain frozen.
- Learning rate: \(4\times10^{-6}\).
- AudioLDM2 and Mustango: AdamW.
- Stable Audio Open: Adam.
- One clip: 300 steps, batch size 1.
- Three clips: 1,000 steps, batch size 3.
- Six clips: 1,500 steps, batch size 4.

**Internal inconsistency:** Appendix A.2 says Stable Audio Open is “the largest” at 1.1B parameters, but Table 2 lists Mustango at 1.4B. The table should be treated as authoritative unless v2 corrects this.

---

### Attribution methods and metrics

#### Retrieval formulation

§3.2 and §4, pp.5–6:

- Query: generated audio \(\hat{x}\).
- Ground-truth gallery items: source clips in \(D_c\).
- Additional gallery:
  - source clips from test attributes;
  - 228,000 ten-second JamendoMaxCaps distractor clips.
- Similarity: cosine similarity.
- Main metric: **Recall@10**, defined as the fraction of source clips from \(D_c\) retrieved in the top 10, averaged over generated queries.
- Appendix metrics: Recall@1, Recall@5, Recall@100, and MAP.

#### Encoders

§4 and Appendix A.4, pp.6 and 14:

- MERT-v0
- MERT-v0-public
- Music2Vec-v1
- DAC-16k

MERT and Music2Vec embeddings are aggregated to 9,984 dimensions. DAC produces 12,288-dimensional codebook histograms.

#### Mapper baseline

Pages 6 and 15:

- Frozen encoder embeddings are passed through separate linear mappings for generated queries and source clips.
- Mappers are trained with symmetric NT-Xent contrastive loss.
- Frobenius regularization coefficient: \(\lambda=0.05\).
- Initialized as the identity via zero delta weights and bias.
- Adam, batch size 32, initial learning rate \(10^{-3}\), cosine decay.
- Up to 200 epochs; early stopping patience 20.
- Contrastive temperature \(\beta=1\).

The authors omit white-box baselines because cited methods do not release source code and are tied to particular generators or training data.

---

### Main results

All results below are from the v1 paper.

#### Encoder difficulty

Figure 2 and §4.1, p.7:

Reported average R@10 without the mapper:

- MERT-v0-public: **0.397**
- MERT-v0: **0.357**
- Music2Vec-v1: **0.226**
- DAC-16k: **0.129**

With mappers:

- MERT-v0: **0.357 → 0.400**
- MERT-v0-public: **0.397 → 0.441**

The authors interpret this as evidence that music-understanding pretraining is more useful than waveform-reconstruction objectives. That interpretation is plausible, but encoder architecture, pretraining data, and representation format are not perfectly controlled.

#### Generator difficulty

Reported average R@10:

- Stable Audio Open: **0.487**
- Mustango: **0.205**
- AudioLDM2: **0.140**

The authors suggest Stable Audio Open is easier because it produces outputs closer to its fine-tuning examples, potentially reflecting memorization or constrained prompting. The experiment does not directly establish memorization; it establishes easier retrieval.

#### Attribution-set difficulty

Reported average R@10:

- Instrument-Centric: **0.465**
- Musician-Centric: **0.305**
- Melody-Centric: **0.239**
- Genre-Centric: **0.101**

The ordering supports the authors’ interpretation that concrete acoustic properties are easier for current encoders than abstract stylistic categories.

#### Prompt-type ablation

Figure 3 and §4.2, p.8:

Average R@10 for mapper training:

| Encoder | Contextual | Style | Mixed |
|---|---:|---:|---:|
| MERT-v0 | 0.365 | 0.430 | — |
| MERT-v0-public | 0.400 | 0.478 | — |

Selected per-attribute values:

- MERT-v0, Melody: **0.26 contextual, 0.48 style, 0.39 mixed**
- MERT-v0-public, Melody: **0.29, 0.53, 0.43**
- MERT-v0-public, Musician: **0.51, 0.60, 0.56**
- MERT-v0-public, Instrument: **0.66, 0.64, 0.64**
- MERT-v0-public, Genre: **0.14, 0.14, 0.14**

The largest prompt sensitivity occurs for melody. Style prompts may constrain the target more directly, but this also means they may create an easier and less natural benchmark than open-ended generation.

#### Joint versus single-task mapper

Figure 4 and §4.3, p.8:

- Musician-Centric: **0.352 → 0.364**
- Genre-Centric: **0.101 → 0.098**
- Overall average change: **0.003**

Joint training across all four attribute types was approximately as good as separate mappers. This is a useful efficiency result, but it does not show that the underlying musical concepts are genuinely disentangled.

#### Three versus six source clips

Figure 5 and §4.4, p.9:

Average R@10:

- All conditions: **0.309 → 0.210**
- Musician: **0.352 → 0.214**
- Instrument: **0.473 → 0.374**
- Genre: **0.101 → 0.041**

Encoder-specific decreases:

- MERT-v0-public: **−0.128**
- MERT-v0: **−0.121**
- Music2Vec: **−0.096**
- DAC-16k: **−0.051**

Generator-specific decreases:

- Stable Audio Open: **−0.174**
- Mustango: **−0.075**
- AudioLDM2: **−0.048**

The immediate metric effect is partly mechanical: six clips create a larger source set and make individual retrieval more difficult. It also tests whether the fine-tuned model represents a broader attribute distribution.

#### Other metrics

Appendix A.5, pp.14–18:

R@1, R@5, R@100, and MAP preserve the main ordering:

1. MERT variants outperform Music2Vec and DAC.
2. Stable Audio Open is easiest.
3. Mappers help MERT most, especially on Mustango.
4. Six-clip attribution is harder.

The appendix mostly provides plots rather than complete numerical tables, limiting exact reproducibility from the paper alone.

---

### Limitations and reproducibility

#### Explicit author limitation

§5, p.9: the authors characterize TRUEMUSE as an initial benchmark covering a representative but limited set of models, attributes, and prompt conditions.

#### Additional evidence-based limitations

1. **Inclusion is not causal influence.**  
   A clip being in \(D_c\) does not prove that it contributed to a particular generated waveform. The benchmark measures retrieval of known fine-tuning sources, not true per-example influence.

2. **It does not test original pretraining-data attribution.**  
   The source clips are inserted through controlled post-training fine-tuning. This is much easier to define than attribution within a massive original training corpus.

3. **Small-set fine-tuning may induce memorization.**  
   Especially for Stable Audio Open, high retrieval may reflect reproduction of fine-tuning material rather than robust concept attribution.

4. **No white-box comparison.**  
   Influence functions, unlearning, and parameter-based methods are discussed but not evaluated.

5. **No uncertainty reporting.**  
   The paper gives aggregate values but does not report confidence intervals, repeated-seed variance, or statistical significance.

6. **Source-data availability is incomplete.**  
   YouTube clips are used under fair use and are not redistributed. The paper does not specify source IDs, exact random seeds, or complete provenance records in the v1 artifact.

7. **Prompt-generation dependence.**  
   Claude-generated prompts, used without human filtering, can affect both generation quality and attribution difficulty.

8. **No symbolic or event-level evaluation.**  
   All audio is ten seconds and evaluated with audio embeddings; there is no note, beat, motif, voice, harmony, or phrase attribution.

9. **Artifact not yet available in v1.**  
   The promised code and dataset have no URL, release version, license, or checksum.

Compute cost is reported as approximately **637 NVIDIA A100 80-GB GPU-hours** (Appendix A.6.3, p.16).

---

### Training-data attribution versus mashup source attribution

This distinction is essential.

#### TrueMuse’s task

> Given generated audio from a model fine-tuned on source set \(D_c\), retrieve the training/fine-tuning clips responsible for the target attribute.

The “source” is a **training example**.

#### Mashup/input attribution

For a mashup or repair system, the task is usually:

> Given input sources A and B and an output, identify which input notes, phrases, voices, motifs, or transformations contributed to each output event.

That requires:

- temporal or symbolic alignment;
- segment- or event-level attribution;
- attribution under transposition, orchestration, rhythmic transformation, and recomposition;
- separation of source identity from generic style;
- provenance through edits and repairs;
- potentially causal tests by masking or removing input material.

TrueMuse does none of these. Its prompts are experimental conditioning text, not source material being attributed. Therefore, calling it a “source-attribution model” would be misleading for symbolic mashup provenance.

---

### Relevance to explainable symbolic composition, mashup, and repair

#### Directly useful ideas

- **Controlled provenance:** create models whose source sets are known by construction.
- **Attribute hierarchy:** separately evaluate melody/motif, rhythm, instrument/voice, artist/style, harmony, and genre.
- **Prompt/context robustness:** test whether attribution survives changes in accompaniment, orchestration, register, meter, and form.
- **Distractor galleries:** evaluate against large collections rather than only the true source candidates.
- **Joint versus task-specific attribution:** test whether one provenance model can cover melody, harmony, rhythm, and voice.
- **Source-set size ablation:** measure how attribution changes when a source identity is represented by one excerpt versus many excerpts.

#### Concrete research directions

1. **Symbolic TrueMuse.**  
   Fine-tune a symbolic generator on known MIDI phrase sets with source identifiers. Evaluate event-level Recall@k, segment IoU, motif retrieval under transposition, and voice/harmony attribution.

2. **Causal provenance benchmark.**  
   For every generated piece, compare:
   - source inclusion;
   - source deletion or masking;
   - retraining or adapter ablation;
   - output-level attribution.  
   This would distinguish provenance from actual causal influence.

3. **Mashup provenance graphs.**  
   Represent each output note or phrase as linked to source A, source B, both, or newly generated material, including transformations such as transposition, rhythmic quantization, reharmonization, and orchestration.

4. **Repair explanations.**  
   For a conflict-aware repair system, require:
   - protected source events;
   - minimal edits;
   - conflict labels;
   - before/after counterfactuals;
   - explanation faithfulness tests.

5. **Music-theoretic encoders.**  
   Replace general audio encoders with separate symbolic representations for pitch contour, rhythm, harmony, voice-leading, phrase structure, and texture. Test whether attribute-specific or joint mappings work better.

6. **Identity–compatibility evaluation.**  
   Adapt TrueMuse’s retrieval setup, but report source identity separately from:
   - compatibility;
   - structural coherence;
   - novelty;
   - playability;
   - explanation faithfulness.

### Bottom line

TrueMuse is valuable as an early **controlled benchmark for training-data retrieval in text-to-music systems**. Its strongest contribution is the systematic comparison across attributes, generators, encoders, prompt types, and source-set sizes. Its central limitation is conceptual: known inclusion in a small fine-tuning set is only a proxy for causal data attribution.

For your research, the most useful adaptation is not to reuse its audio retrieval model directly, but to borrow its controlled-provenance methodology and extend it to **event-level symbolic attribution, causal source influence, and provenance-preserving mashup repair**.

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
