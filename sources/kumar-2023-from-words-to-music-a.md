---
title: "From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation"
authors: "Adarsh Kumar and Pedro Sarmento"
year: 2023
doi: 10.48550/arXiv.2304.08953
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kumar-2023-from-words-to-music-a.pdf"
pdf_filename: kumar-2023-from-words-to-music-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. **Q1:** Can subword tokenization improve musical structure and quality in generated symbolic music? 2. **Q2:** Do improvements generalize between **BPE** and **Unigram** tokenization? — §1, pp. 1–2

## 1. Document Information

- **Canonical source:** arXiv `2304.08953v2`; official PDF preserved as `kumar-2023-from-words-to-music-a.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zowbg_p1sf.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

**Adarsh Kumar and Pedro Sarmento.** “From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation.” **arXiv:2304.08953v2 [cs.SD], 25 April 2023.** The PDF is 10 pages and identifies the authors as affiliated with IIT Kharagpur and Queen Mary University of London. No journal or conference publication is specified in the paper.

- Official identifier: `arXiv:2304.08953v2`
- PDF margin/version marker: p. 1
- Paper title/authors: p. 1
- No appendix; references occupy pp. 8–10.

### 2. Research question and claimed contribution

The paper asks:

1. **Q1:** Can subword tokenization improve musical structure and quality in generated symbolic music?
2. **Q2:** Do improvements generalize between **BPE** and **Unigram** tokenization?  
   — §1, pp. 1–2

The authors claim that BPE and Unigram:

- reduce sequence lengths;
- allow longer music to be generated within the same inference time;
- improve structural metrics;
- work across melody-only, polyphonic, and multi-instrument datasets;
- are compatible with several existing musical tokenization schemes.  
  — Abstract, §1, §7, pp. 1–2, 7

**Interpretation:** The central contribution is an empirical token-compression study, not a new generative architecture or a semantic music representation.

### 3. Tokenization schemes and baselines

#### Pipeline

The pipeline is:

1. MIDI/GuitarPro input;
2. musical event tokenizer;
3. mapping musical events to Unicode symbols/characters;
4. BPE or Unigram tokenizer;
5. Transformer sequence modeling;
6. detokenization back to musical events.  
   — Figure 2, p. 3; §3.2, p. 4

Each song is treated as one sentence-like sequence. Figure 1 illustrates repeated character n-grams versus repeated musical-event sequences.

#### Compared representations

| Musical tokenizer | Base vocabulary | BPE | Unigram |
|---|---:|---:|---:|
| REMI | 227 | 300 | 300 |
| MIDI-Like | 331 | 1,000 | 1,000 |
| DadaGP | 2,104 | 5,000 | 5,000 |

— Table 1, p. 4

The baseline is called **“base”** in the methodology and **“Original”** in Tables 2–3; Table 4 uses “Base.” It is the same no-subword condition.

- **BPE:** repeatedly merges frequent adjacent symbol pairs.
- **Unigram:** begins with a larger vocabulary and prunes tokens probabilistically according to likelihood/loss.
- Both are applied after musical event tokenization, not directly to raw MIDI bytes.  
  — §2.1, §3.2, pp. 2, 4

### 4. Datasets, splits, models, and training

| Dataset | Subset | Musical content | Musical tokenizer | Model |
|---|---:|---|---|---|
| Folk Songs | 1,000 samples | Monophonic, single instrument, MIDI | REMI | Music Transformer |
| MAESTRO | 400 samples | Polyphonic, single instrument, MIDI | MIDI-Like | Music Transformer |
| DadaGP | 2,000 Rock songs | Polyphonic, multi-instrument, GuitarPro | DadaGP | Transformer-XL |

— §3.1 and §3.3, pp. 3–4

#### Model/training details

- Folk and MAESTRO:
  - 3-layer Transformer;
  - embedding dimension 256;
  - Music Transformer implementation;
  - Google Colab Free Tier;
  - P100 GPU with 16 GB memory.
- DadaGP:
  - Transformer-XL architecture based on Huang and Yang (2020);
  - Quadro RTX 6000 with 24 GB memory.
- Libraries:
  - PyTorch;
  - Hugging Face;
  - MidiTok;
  - Hugging Face tokenizers;
  - MusPy and MusDr for evaluation.
- Approximate training time:
  - Folk: 20 minutes;
  - MAESTRO: 3 hours;
  - DadaGP: 3 days.
- 20 songs were generated per model configuration.  
  — §5.1 and Table 7, pp. 5–6

#### Missing split/reproducibility information

The paper does **not** specify:

- train/validation/test boundaries;
- whether the tokenizer was trained only on the training split;
- exact dataset versions and preprocessing filters;
- random seeds;
- batch size, optimizer, learning rate, context length, number of heads, or update count;
- generation temperature/top-k/top-p;
- exact Transformer-XL configuration;
- statistical confidence intervals or significance tests.

The paper refers to a “testing corpus” when defining metric comparisons, but does not document the split construction. This is a major reproducibility limitation.

The PDF links to base-model repositories, MusDr, Hugging Face tokenizers, and a Google Drive containing samples, but does not provide a complete experiment repository or configuration archive. — p. 5 footnotes and §5.1

### 5. Evaluation metrics

#### Structural and musical metrics

- **Structureness Indicator (SI):** based on fitness-scape plots and self-similarity matrices; intended to measure repeated musical content.
- The paper prints the evaluated windows as `SI⁸₃`, `SI¹⁵₈`, and `SI₁₅`, defining the general notation \(SI^u_l\), where \(l,u\) are lower and upper time bounds.
- They call these SI-short, SI-medium, and SI-long.
- Higher SI is not inherently better because excessive repetition can be undesirable; generated values should be close to real data.
- **Pitch Class Entropy (H):** entropy of a normalized 12-dimensional pitch-class histogram.
- **Groove Similarity (GS):** pairwise similarity of bar-level onset vectors using \(1-\mathrm{HammingDist}(g_a,g_b)\).  
  — §4.1, p. 4

#### Efficiency metrics

- Average number of tokens per song.
- Number of original musical tokens generated for equal inference time.
- NLL, with an explicit warning that it is not directly comparable because subword models have larger vocabularies and therefore more parameters.  
  — §§4.2–4.3, p. 4

### 6. Exact objective results

The following values reproduce Tables 2–4.

#### Folk Songs — Table 2, p. 5

| Metric | Real | Base | BPE | Unigram |
|---|---:|---:|---:|---:|
| SI-short | 0.4637 | 0.2707 | 0.3376 | 0.2712 |
| SI-medium | 0.4959 | 0.2759 | 0.3379 | 0.2719 |
| SI-long | 0.4543 | 0.2583 | 0.3340 | 0.2451 |
| H | 2.6011 | 2.6924 | 2.6754 | 2.6842 |
| GS | 0.9987 | 0.9984 | 0.9986 | 0.9985 |

**Interpretation:** BPE is closer to real data on every listed metric. Unigram provides little or no structural improvement over the base model on this simple melody-only dataset.

#### MAESTRO — Table 3, p. 5

| Metric | Real | Base | BPE | Unigram |
|---|---:|---:|---:|---:|
| SI-short | 0.3228 | 0.5119 | 0.3880 | 0.3483 |
| SI-medium | 0.3066 | 0.4663 | 0.3334 | 0.2828 |
| SI-long | 0.2343 | 0.4173 | 0.3031 | 0.2205 |
| H | 3.0555 | 2.5152 | 2.8705 | 2.9297 |
| GS | 0.9917 | 0.9971 | 0.9942 | 0.9936 |

**Interpretation:** Unigram is closest to real data on all five metrics; BPE also substantially reduces the base model’s structural mismatch.

#### DadaGP — Table 4, p. 5

| Metric | Real | Base | BPE | Unigram |
|---|---:|---:|---:|---:|
| SI-short | 0.5069 | 0.5110 | 0.5125 | 0.4894 |
| SI-medium | 0.5270 | 0.4219 | 0.4892 | 0.4539 |
| SI-long | 0.4972 | 0.2943 | 0.4397 | 0.3924 |
| H | 2.5842 | 2.0529 | 2.3084 | 2.4333 |
| GS | 0.9991 | 0.9994 | 0.9993 | 0.9992 |

**Interpretation:** The base model is marginally closest on SI-short, BPE is best on SI-medium and SI-long, and Unigram is closest on entropy and groove similarity. Thus, the result is broadly favorable to subword tokenization but not uniformly superior on every metric.

#### Representation efficiency — Tables 5–6, p. 5

Average tokens per song:

| Dataset | Base | BPE | Unigram |
|---|---:|---:|---:|
| Folk | 796 | 359 | 436 |
| MAESTRO | 12,925 | 8,831 | 8,618 |
| DadaGP | 5,332 | 2,875 | 2,954 |

Original musical tokens generated for the same inference time:

| Dataset | Base | BPE | Unigram |
|---|---:|---:|---:|
| Folk | 500 | 1,307 | 994 |
| MAESTRO | 1,000 | 1,570 | 1,534 |
| DadaGP | 1,000 | 1,437 | 1,828 |

The strongest compression occurs for Folk and DadaGP. For DadaGP, Unigram generates the most original musical tokens under the paper’s equal-inference-time protocol.

#### NLL — Table 7, p. 6

| Dataset | Base | BPE | Unigram |
|---|---:|---:|---:|
| Folk | 0.08 | 0.13 | 0.11 |
| MAESTRO | 2.58 | 3.16 | 3.62 |
| DadaGP | 0.10 | 0.11 | 0.11 |

The authors correctly caution that NLL does not track generated musical quality here and is confounded by vocabulary size and parameter count. — §4.3, §5.2, pp. 4, 6

### 7. Subjective and figure-based evidence

There is **no formal subjective listening study**. Section 6 is explicitly an “individual subjective analysis.” — §6, p. 6

- **Figure 3, p. 6:** MAESTRO BPE sample 19 contains rests from measures 24–28. The authors say this interrupts the preceding musical idea despite good structural metrics.
- **Figure 4, p. 6:** DadaGP BPE sample 18 allegedly preserves guitar techniques including hammer-ons, pull-offs, bends, slides, and vibrato.
- **Figure 5, p. 7:** DadaGP Unigram sample 10 repeats a pattern from measures 1–2 in measures 7–8, while adding connecting notes from measure 5.
- **Figure 6, p. 7:** MAESTRO fitness-scape plots show BPE and Unigram as visually closer to real data than Base; the authors judge Unigram best among the three.

**Interpretation:** These examples support plausibility and motif recurrence, but they cannot establish listener-perceived quality, playability, source identity, or general musical usefulness.

### 8. Author claims versus interpretation

#### Author claims

- Subword tokenization improves representation efficiency.
- BPE and Unigram generally improve structural metrics.
- Improvements appear across different musical tokenizers, datasets, and model types.
- Benefits are especially visible for longer repetitive structures and complex data.
- Musical expressivity tokens in DadaGP are preserved despite lower frequency.
- Music-theory-aware hybrid tokenization is a promising direction.  
  — §§5.2–7, pp. 5–7

#### Interpretation and methodological qualification

The paper’s strongest conclusion—improvement independent of dataset, format, tokenizer, and model—is not fully isolated by the design:

- Folk, MAESTRO, and DadaGP are each permanently paired with different musical tokenizers.
- DadaGP uses Transformer-XL while the first two datasets use Music Transformer.
- Vocabulary sizes and therefore embedding/output parameters differ.
- Training is equalized approximately by wall-clock time, not by optimization steps, data exposure, or parameter count.
- No uncertainty estimates are reported.

Therefore, the evidence supports **a useful compression hypothesis**, but not a definitive causal claim that BPE or Unigram alone explains every observed improvement.

### 9. Limitations relevant to our programme

The paper does not address:

- two-source composition or mashups;
- alignment between musical sources;
- conflict detection or classification;
- minimal repair;
- provenance;
- protected source material;
- explanation faithfulness;
- source identity preservation;
- harmony/voice-leading compatibility;
- human musician controls;
- explicit latent-variable representations.

Its SI metric rewards repetition and is not a direct measure of coherence. H and GS are coarse distributional measures. The almost-saturated GS values around 0.99 also suggest limited discriminative power in these experiments.

### 10. Relevance to explicit MIDI/event representations

#### Direct relevance

The paper provides evidence that reversible event-sequence compression can extend the effective musical horizon of an autoregressive model. This is particularly relevant to explicit MIDI/event models because:

- the representation remains symbolically interpretable;
- subword tokens correspond to recurring event sequences;
- detokenization can recover exact original event tokens;
- compression is strongest where event streams are long and structurally repetitive;
- multi-track DadaGP benefits despite already using Transformer-XL.

#### Important distinction

This is **not** a semantic latent representation in the usual continuous-latent or VQ-latent sense. BPE/Unigram tokens are corpus-frequency-based chunks. They do not necessarily correspond to motifs, phrases, harmonic functions, voices, or repairable musical concepts.

For explicit event representations, the central design question is therefore:

> Can we obtain the sequence-length benefits of learned chunks while preserving event-level semantics, provenance, legality, and controllability?

### 11. Concrete modern research ideas

1. **Train-only, reversible musical tokenizers.**  
   Compare atomic events, BPE, Unigram, WordPiece, constrained musical BPE, and discrete latent codes. Fit tokenizers only on training data and report exact detokenization, compression ratio, event horizon, and parameter-matched performance.

2. **Concurrency-aware event chunks.**  
   Extend adjacency-only BPE with legal beat/bar/voice slices that can represent simultaneous notes, chord spans, sustain/pedal states, ties, and expressive events. Reject merges that cross malformed note-on/note-off boundaries.

3. **Provenance-preserving mashup tokenization.**  
   Add source-A/source-B, voice, phrase, and alignment identifiers. Prohibit merges across protected source boundaries unless explicitly allowed. Every generated chunk should map back to its contributing original events.

4. **Conflict-aware repair tokens.**  
   Represent detected clashes—pitch, meter, harmony, register, voice-leading, density—as structured conflict spans. Use chunk-level infilling for candidate repairs but evaluate edits at atomic-event level.

5. **Hierarchical representation.**  
   Maintain atomic MIDI events for exact editing and add beat-, bar-, phrase-, and motif-level tokens as auxiliary views. This would provide long context without losing inspectability.

6. **Rate–distortion–musicality objective.**  
   Optimize not merely token count but a multi-objective trade-off among:
   - sequence length;
   - exact reconstruction;
   - structural coherence;
   - source identity;
   - compatibility;
   - edit locality;
   - explanation faithfulness.

7. **A stronger evaluation protocol.**  
   Use source-disjoint train/test splits and compare representations under equal model size, training steps, wall-clock budget, and generated event budget. Report SI, pitch/harmony, groove, repetition diversity, invalid-event rate, long-range dependency measures, and confidence intervals.

8. **Mashup/repair benchmark.**  
   Evaluate overlay, transition, and recomposition separately. For repair, measure:
   - conflict diagnosis accuracy;
   - responsible-event localization;
   - minimum edit distance;
   - preservation of protected material;
   - source identity;
   - structural coherence;
   - musician-rated usefulness;
   - explanation/counterfactual faithfulness.

9. **Theory-guided subword learning.**  
   Use musical constraints as merge priors rather than allowing frequency alone to determine vocabulary. Candidate merges could be favored when they form repeated motifs, harmonic units, phrase endings, or valid voice-leading patterns.

**Bottom line:** The paper is useful evidence that subword compression can improve the computational context available to symbolic music models, especially for complex event streams. It does not establish that frequent chunks are meaningful musical units, nor does it solve the provenance, compatibility, diagnosis, and minimal-repair requirements central to our symbolic mashup and repair programme.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `data-and-representation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
