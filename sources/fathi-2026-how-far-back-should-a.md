---
title: "How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models"
authors: "Amir Fathi"
year: 2026
doi: 10.48550/arXiv.2610.02837
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fathi-2026-how-far-back-should-a.pdf"
pdf_filename: fathi-2026-how-far-back-should-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I inspected `/tmp/paper-digest/2610.02837v1.pdf`, the extracted text, all page breaks, Tables I–IX, Figures 1–8, Equations (1)–(4), and the reproducibility/audit appendix.

## 1. Document Information

- **Canonical source:** arXiv `2610.02837v1`; official PDF preserved as `fathi-2026-how-far-back-should-a.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zsu6b_2lp6.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and scope

**Amir Fathi**, “**How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models**,” arXiv:**2610.02837v1** [cs.SD], **2 October 2026**, 17 pages. University of Alberta.

I inspected `/tmp/paper-digest/2610.02837v1.pdf`, the extracted text, all page breaks, Tables I–IX, Figures 1–8, Equations (1)–(4), and the reproducibility/audit appendix.

#### Page anchors

- **pp. 1–2:** Abstract, introduction, related work
- **pp. 2–4:** Corpora, splits, tokenization
- **pp. 4–5:** Autoencoder and exact-context predictors
- **pp. 5–6:** Evaluation protocol
- **p. 6:** Table II, Figure 1, context sweep
- **p. 7:** Table III, Table IV, repeat-lag and erasure analyses
- **pp. 8–9:** Figure 5, trained-model history restriction; O’Neill’s and MusicNet
- **pp. 9–11:** Seed dependence, averaging predictor, autoencoder-seed analysis
- **pp. 11–13:** Generation analysis, Table VII, Figure 7
- **pp. 13–15:** Audit of earlier result, limitations, discussion, Figure 8
- **pp. 15–17:** Conclusion, Tables VIII–IX, reproducibility appendix, references

---

### Core question and headline conclusion

The paper asks:

1. How does autoregressive symbolic-music prediction change as available history increases?
2. What information is actually being used by long-context models?

**Author’s main claim:** On the rendered Nottingham and O’Neill’s folk-score representations, most of the large long-context improvement is caused by **exact copying of earlier repeated passages**, rather than a general ability to model long-range musical structure.

This is strongly supported by:

- Repeat-conditioned NLL curves.
- Targeted erasure of earlier occurrences.
- A simple nearest-copy baseline.
- Test-time removal of distant history from a trained 336-token model.
- Replication on a second folk corpus.

The claim is explicitly narrower than “music requires 336-token context”: the effect depends heavily on the representation, especially the expansion of written repeat signs.

---

### 1. Data, representations, and splits

### Corpora

#### Nottingham

- Jukedeck MIDI release of the Nottingham Music Database.
- Approximately 1,000 folk tunes.
- Melody-only rendering retained.
- Written repeat signs are expanded, creating exact note-for-note repetitions.
- Split by tune: **729 train / 150 validation / 154 test**.
- Token counts: **382K / 90K / 84K**.
- Windows: **2,789 / 809 / 660**.
- Nonconstant 48-token test blocks occurring verbatim in training: **0.0%**.

#### O’Neill’s

- *O’Neill’s Music of Ireland: Eighteen Hundred and Fifty Melodies*.
- Norbert Paap ABC transcription distributed with music21.
- Written repeats expanded with music21.
- Fifteen unparseable or too-short tunes excluded.
- Split: **1,397 train / 295 validation / 302 test**.
- Tokens: **738K / 115K / 158K**.
- Windows: **7,121 / 687 / 1,505**.
- Verbatim test blocks in training: **0.6%**.
- Only **129 of 302** test tunes are long enough for the complete 384-token evaluation window.

#### MusicNet

- 323 aligned MIDI scores of classical solo/chamber recordings.
- Files grouped by composer and movement.
- Final split: **221 train / 54 validation / 48 test**.
- Tokens: **577K / 141K / 116K**.
- Windows: **1,091 / 267 / 218**.
- Verbatim test blocks in training: **0.0%**.
- No MusicNet autoencoder was trained; only token predictors were evaluated.

#### MAESTRO v3

- Recorded piano performances with the official composition-level split.
- **962 train / 137 validation / 177 test** performances.
- Tokens: **4,586K / 560K / 575K**.
- Windows: **9,072 / 1,094 / 1,113**.
- Verbatim test blocks in training: **0.2%**.

### Common symbolic representation

- Quantized to **four steps per quarter note**.
- A 4/4 bar therefore contains **16 grid steps**.
- At each step, only the **highest active pitch** is retained.
- No onset symbol is represented; a sustained pitch and repeated attack can become identical.
- Token 0 is rest; 47 consecutive pitches form the vocabulary.
- Out-of-range pitches are clamped.
- MAESTRO token results are additionally rerun with an **89-token unclamped vocabulary** covering rest plus MIDI pitches 21–108.

This is therefore a **monophonic skyline representation**, not a full polyphonic piano representation.

### Train/test safeguards

The authors group pieces before splitting when they share at least half of the smaller piece’s nonconstant 16-token patterns. Groups are merged transitively.

They report:

- No Nottingham, MusicNet, or MAESTRO near-duplicate crossing the final split.
- O’Neill’s has 18 overlapping blocks from seven test tunes below the 50% grouping threshold.
- Excluding those O’Neill’s tunes changes the 6-to-336-token reduction only from **70.6% to 70.3%**.

Training windows are extracted only after splitting.

---

### 2. Context-length protocol

### Contexts

Separate models are trained at each context:

\[
T \in \{6,18,48,96,192,336\}
\]

For the latent sequence these correspond to:

\[
k \in \{1,3,8,16,32,56\}
\]

latent steps, with six input tokens per latent step.

- Nottingham/O’Neill’s: 384-token windows, final 48 tokens are targets.
- Windows begin every 48 tokens and are never padded.
- MAESTRO/MusicNet: non-overlapping 480-token windows, final 144 tokens are targets.
- Longest context exactly fits before the first target, so all context lengths use identical target positions.

The context-0 token baseline is the empirical unigram distribution. The latent context-0 baseline is the marginal probability of each bit.

### Predictors

Two-layer causal Transformer:

- Hidden width: 384
- Four attention heads
- Feed-forward width: 768
- GELU
- Dropout: 0.2
- Learned relative-position terms
- Approximately 2.47–2.50M parameters
- AdamW, learning rate \(10^{-3}\)
- Weight decay \(10^{-4}\)
- Batch size 32
- Gradient clipping 1.0
- Label smoothing 0.06
- Three seeds: 42, 7, 0

The attention bands are deliberately asymmetric. The first layer attends to at most the most recent 18 tokens; the second layer covers the remaining history. The authors verify the actual receptive field by gradient inspection.

### Latent representation

A 48-token span is mapped to 8 latent steps, each containing \(D=64\) binary variables.

- Latent step \(j\) depends exclusively on tokens \(6j,\ldots,6j+5\).
- Encoder: stride-6 width-6 convolution, 256 channels, pointwise convolutions, residual blocks.
- Decoder mirrors this structure.
- Binary codes use a straight-through estimator:

\[
z = \operatorname{sign}(\tanh(z_{\mathrm{cont}})) + 0.05\epsilon
\]

with Gaussian noise during training.

The authors emphasize that this is **not bit-level compression**: 64 bits per latent step exceeds the roughly 33.5 bits needed to encode six 48-way tokens.

---

### 3. Exact results

### Table II: test NLL by context

Values are mean ± sample SD over three seeds. Token and latent NLLs are different quantities and should not be compared numerically.

| Context | Nottingham latent | Nottingham token | O’Neill’s latent | O’Neill’s token | MusicNet token | MAESTRO latent | MAESTRO token* |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.958 | 4.366 | 0.931 | 4.383 | 5.295 | 0.978 | 5.319 |
| 6 | 0.857 ± .002 | 1.391 ± .015 | .845 ± .005 | 1.692 ± .014 | 2.512 ± .066 | .887 ± .0004 | 3.283 ± .002 |
| 18 | .842 ± .002 | 1.440 ± .021 | .818 ± .003 | 1.543 ± .019 | 2.366 ± .003 | .881 ± .00003 | 3.177 ± .002 |
| 48 | .834 ± .005 | 1.529 ± .090 | .771 ± .005 | 1.449 ± .017 | 2.159 ± .004 | .879 ± .0004 | 3.097 ± .006 |
| 96 | .775 ± .004 | 1.274 ± .326 | .730 ± .009 | 1.160 ± .015 | 2.080 ± .003 | .877 ± .0004 | 3.040 ± .009 |
| 192 | .571 ± .015 | .567 ± .008 | .580 ± .002 | .791 ± .012 | 2.050 ± .009 | .877 ± .00010 | 3.013 ± .005 |
| 336 | .465 ± .009 | .405 ± .006 | .419 ± .007 | .497 ± .011 | 2.067 ± .004 | .877 ± .0004 | 2.987 ± .005 |

\*MAESTRO token values use the 89-token unclamped rerun.

#### Nottingham

- Token NLL: **1.391 → 0.405**, a reduction of **0.986 bits/token**, or **71%**.
- Latent NLL: **0.857 → 0.465**, a reduction of **0.392 bits/bit**, or **46%**.
- Token prediction initially worsens from 6 to 48 tokens.
- The major improvement occurs at 96–336 tokens.
- The 96-token token result has high seed variability: SD **0.326**.

#### O’Neill’s

- Token NLL: **1.692 → 0.497**, reduction **1.195 bits/token**, or **71%**.
- Latent NLL: **0.845 → 0.419**, reduction **0.426 bits/bit**, or **50%**.
- More stable than Nottingham at 96 tokens.
- The same long-context/copying pattern appears.

#### MusicNet

- Token NLL: **2.512 → 2.067**, reduction **0.445 bits/token**, or **18%**.
- **97%** of the reduction is already attained by 96 tokens.
- The 336-token model is slightly worse than the 192-token model by **0.017 bits**.

#### MAESTRO

- Token NLL: **3.283 → 2.987**, reduction **0.296 bits/token**, or **9%**.
- **82%** of the reduction is reached by 96 tokens.
- The remaining 96-to-336 improvement is **0.054 bits/token**.
- Latent NLL changes only from **0.887 to 0.877**, approximately **1%**.

The authors do **not** test contexts beyond 336 tokens.

---

### 4. Causal copying evidence

### Repeat definition

For target \(x_t\), let \(h_t\) be its preceding 16-token history. The repeat lag is the distance to the nearest earlier matching history:

\[
\ell_t = \min\{t-j : 17 \leq j<t,\ h_j=h_t\}.
\]

A repeat is “in view” when the context contains both the earlier history and its continuation:

\[
\ell_t + 16 \leq T.
\]

The four repeat bins become visible at contexts 48, 96, 192, and 336.

### Repeat prevalence

At 336 tokens, the share of targets with an in-view 16-token repeat is:

- Nottingham: **71.0%**
- O’Neill’s: **73.3%**
- MusicNet: **10.5%**
- MAESTRO: **0.8%**

The corresponding token NLL reductions are:

- Nottingham: **71%**
- O’Neill’s: **71%**
- MusicNet: **18%**
- MAESTRO: **9%**

The authors correctly describe this as descriptive evidence, not a statistical test.

### Repeat-conditioned NLL

On Nottingham:

- At 192 tokens, repeats 81–176 tokens back score about **0.20 bits/token**.
- Repeats 177–320 tokens back remain around **0.96** because they are not yet visible.
- At 336 tokens, the latter fall to approximately **0.18**.
- Non-repeated targets remain around **0.93**.

For latent prediction, the same threshold behavior appears, though the repeated passage may map to a different latent code.

### Targeted erasure: Table IV

For targets with an in-view repeat, the authors overwrite the earlier matching history and its continuation with material from another tune. A matched control overwrites unrelated spans of equal size.

#### Nottingham

| Model/context | Clean | Erased | Control |
|---|---:|---:|---:|
| Token, 192 | .22 | 1.10 | .22 |
| Token, 336 | .19 | 1.06 | .19 |
| Latent, 192 | .37 | .87 | .38 |
| Latent, 336 | .35 | .81 | .35 |

#### O’Neill’s

| Model/context | Clean | Erased | Control |
|---|---:|---:|---:|
| Token, 192 | .37 | 1.28 | .38 |
| Token, 336 | .22 | 1.24 | .22 |
| Latent, 192 | .47 | .78 | .47 |
| Latent, 336 | .33 | .71 | .33 |

Thus, targeted corruption destroys the copying advantage, while equally large unrelated corruption does not.

A complementary intervention replaces only the copied continuation token with a random pitch:

- Nottingham 336-token token model: probability assigned to injected token rises from **0.3% to 62%**.
- O’Neill’s: **0.8% to 51%**.
- Repeated five times with stable results.

### Copy baseline

The baseline searches the context for 32-, 16-, then 8-token matches and interpolates the copied continuation with the 6-token model.

Validation-fitted interpolation weights:

- Nottingham: 0.965 for 32-token matches, 0.869 for 16-token matches, 0.625 for 8-token matches.
- O’Neill’s: 0.969, 0.890, 0.733.
- MusicNet: 0.902, 0.866, 0.760.
- MAESTRO: 0.553, 0.586, 0.510.

Results:

- Nottingham copy baseline: **0.469 bits/token**, recovering **94%** of the Transformer’s reduction.
- O’Neill’s: recovers **97%**.
- MusicNet: recovers **72%**, although only 42% of the Transformer’s reduction occurs on targets matched by the baseline.
- MAESTRO: recovers only **11%**.

The MusicNet result is therefore suggestive but not a clean causal attribution to copying.

### Test-time history restriction

A trained 336-token model is tested with only the latest \(R\) tokens, either by truncating the history or replacing older positions.

Nottingham:

- Full history: **0.405**
- 192-token history: approximately **0.576–0.591**
- 96-token history: approximately **1.008–1.078**

O’Neill’s:

- Full history: **0.497**
- 192-token history: approximately **0.861–0.877**
- 96-token history: approximately **1.460–1.491**

MusicNet and MAESTRO change only slightly when restricted to 96 tokens, consistent with their gains being mostly realized by 96 tokens.

---

### 5. Optimization and architecture findings

### Abrupt copying acquisition

Ten additional Nottingham token models were trained for 200 epochs without early stopping.

At 96 tokens:

- Six of ten runs abruptly improve after long plateaus.
- Drops occur between epochs **41 and 172**.
- Four runs never acquire the stronger copying solution.
- All runs reach their best validation NLL between epochs **135 and 193**.

At 192 tokens:

- All ten runs acquire the transition.
- They finish between **0.55 and 0.56 bits/token**.

The authors describe this as qualitatively reminiscent of induction-head emergence, but explicitly state that their intervention evidence does **not identify induction heads**.

### Averaging predictor

The earlier draft used a mean-pooled predictor with no direct mechanism for privileging a recent or specific distant position.

On Nottingham latent prediction:

- Causal predictor at 336 tokens: **0.465 bits/bit**
- Mean-pooled predictor: **0.891 bits/bit**

The averaging predictor therefore creates apparent context saturation by failing to retrieve specific distant continuations.

### Latent autoencoder seeds

Two additional Nottingham autoencoders produce similar qualitative curves, but autoencoder-seed variation is sometimes larger than predictor-seed variation:

- Test reconstruction accuracy: **99.93% and 99.91%**.
- 6-to-336 reductions: approximately **45%, 48%, and 43%** across autoencoders.
- At 336 tokens, autoencoder SD is **0.024 bits/bit**, versus predictor-seed SD **0.009**.

---

### 6. Audit of the earlier saturation result

The earlier draft reported saturation around 16 tokens. The current paper identifies several methodological failures.

### 1. Split leakage

Earlier Nottingham data randomly split three renderings of each tune:

- **92.4%** of test sequences had another rendering of the same tune in training.
- **58.4%** of nonconstant 48-token test blocks appeared verbatim in training.

Earlier chunked MAESTRO and MusicNet splits also allowed source-performance overlap:

- **99.6%** of MAESTRO test chunks came from performances also contributing training chunks.
- **100%** for MusicNet.
- Verbatim test-block overlap was lower: 1.7% and 19.8%, respectively.

### 2. Overlapping latent receptive fields

The earlier latent step \(j\) depended on tokens approximately \(4j-3\) through \(4j+18\). Neighboring context latents could therefore expose tokens overlapping the target’s own receptive field.

This generated artificial short-context gains.

### 3. Mean pooling

The earlier v5 predictor averaged all context positions and could not selectively retrieve a distant occurrence.

### 4. Per-file tempo grid

A tempo estimate independently computed for every file:

- Made the median Nottingham tune **1.64× longer** than its score representation.
- Mapped equivalent melodies to different grids.
- Obscured near-duplicates.
- Revealed four cross-split near-duplicate tunes after restoring the score grid.

### 5. Unequal effective attention bands

An early exact-context rerun divided attention bands approximately equally. Its nominal 336-token context therefore had an effective copying range of only about half the advertised context.

The corrected model uses a short first band and a long second band.

The authors do not attribute a quantitative fraction of the old curve to any single error because several components changed jointly.

---

### 7. Generation analysis

Generation is explicitly secondary and is not treated as a music-quality metric.

Setup:

- 100 Nottingham test primes per model.
- Each prime begins with the same 336 tokens.
- Generate 480 tokens.
- Temperature tuned on validation tunes.
- Statistics: adjacent repetition ratio, token entropy, block variety.
- Structural repetition rate detects repeated 16-token histories.

The corrected real-data reference band is **0.03–0.17** distance for 100 held-out test streams. The closest generated set scores **0.19**, so no generated set falls inside the start-of-tune or random-segment reference bands; one falls inside the end-of-tune band.

Long-context models generate repeated passages internally:

- Token 336 model: repetition rate approximately **0.41**.
- Latent 336 model: approximately **0.35**.
- Short-context models exhibit little structural repetition.

However, no generated set is claimed to match held-out music under the distance metric.

The latent models require low temperatures and generate binary-code combinations rarely or never observed in the training codes. The authors warn that the generation statistics should not be interpreted as a general measure of variety or quality.

---

### 8. Cross-dataset interpretation

### Author’s interpretation

The paper argues that exact repetition is jointly determined by:

1. Musical structure.
2. The chosen symbolic representation.
3. Preprocessing decisions such as repeat-sign expansion.

The folk corpora are rendered scores with explicit repeats. MAESTRO is expressive performance data sampled on a fixed 125 ms grid; exact token-level recurrence is much rarer.

The paper is careful not to claim that folk music inherently needs longer context than piano music.

### Important caveats

- MAESTRO uses only the top voice.
- No onset information is retained.
- Exact 16-token recurrence misses ornamented or transposed repetition.
- O’Neill’s and Nottingham results apply only to tunes long enough to fill the evaluation window.
- The retained O’Neill’s subset is intrinsically more repetitive than excluded short tunes.
- Contexts beyond 336 tokens are not evaluated.
- The 2.5M-parameter models and few-million-token training regime are small relative to modern music

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
