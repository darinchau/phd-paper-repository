---
title: "Automatic Analysis and Influence of Hierarchical Structure on Melody, Rhythm and Harmony in Popular Music"
authors: "Shuqi Dai, Huan Zhang, and Roger B. Dannenberg"
year: 2020
doi: 10.48550/arXiv.2010.07518
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/dai-2020-automatic-analysis-and-influence-of.pdf"
pdf_filename: dai-2020-automatic-analysis-and-influence-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

1. **Low-level repeated phrases**, using similarity in chords, rhythm onsets, and melody. 2. **Higher-level sections**, inferred from the arrangement of detected phrases and separator-like non-melodic material. 3. Statistical relationships between hierarchical position and **harmony, melody, and rhythm**.

## 1. Document Information

- **Canonical source:** arXiv `2010.07518v1`; official PDF preserved as `dai-2020-automatic-analysis-and-influence-of.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492t_k52k.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

**Paper:** Shuqi Dai, Huan Zhang, Roger B. Dannenberg, “Automatic Analysis and Influence of Hierarchical Structure on Melody, Rhythm and Harmony in Popular Music,” arXiv:2010.07518v1, 15 October 2020.  
**Files read:** `/tmp/paper-digest/2010.07518v1.pdf` and `/tmp/paper-digest/2010.07518v1.txt`. I also inspected rendered pages containing Figures 1–7. Repository files were not edited.

### 1. Core contribution

The paper presents a symbolic-MIDI method for detecting:

1. **Low-level repeated phrases**, using similarity in chords, rhythm onsets, and melody.
2. **Higher-level sections**, inferred from the arrangement of detected phrases and separator-like non-melodic material.
3. Statistical relationships between hierarchical position and **harmony, melody, and rhythm**.

The authors argue that hierarchy is not merely repetition at different time scales: phrase and section positions have measurably different musical behavior (Abstract; §§1, 5, 7).

**Interpretation:** This is primarily an analysis and controllability resource, not a generation model. It provides structural annotations and conditional musical statistics that could be used by a generator, mashup system, or repair system.

---

### 2. Corpus and preprocessing

#### Corpus

- **909 Chinese popular-song MIDI transcriptions** derived manually from audio (§3.2, PDF p. 4).
- Key and chord labels from audio were combined with automatically derived MIDI labels.
- Differences were resolved with heuristics.
- MIDI files contain a melody track, simplifying melody extraction.
- Melodies were quantized to sixteenth notes.
- The corpus spans approximately **seven decades** of music (§5, PDF p. 7).

The paper cites the Pop909 work by Wang et al. (2020), and says the dataset, annotations, and experimental results were released at:

`https://github.com/Dsqvival/hierarchical-structure-analysis` (§7, PDF p. 8).

#### Important caveat

The paper does **not** clearly report:

- a train/test split,
- the number of human annotators,
- inter-annotator agreement,
- the exact denominator for the reported 92%/93% structure accuracy,
- detailed corpus filtering or transcription-error rates.

Therefore, “92%” or “93%” should not be treated as a fully reproducible benchmark without the accompanying released artifacts.

---

### 3. Phrase representation

The structure is represented as alternating **labels and measure lengths**, with bar lines as boundaries (§3.1, PDF pp. 3–4).

Example:

```text
i4A8B8x4A8B8B8X2c4c4X2B9o2
```

Conventions:

- Uppercase letters: repeated melodic phrases.
- Lowercase letters: non-melodic phrases.
- `i`: introduction without melody.
- `o`: non-melodic ending.
- `X`/`x`: non-repeating melodic/non-melodic material.
- A number gives phrase duration in measures.
- `B9` can represent a near-repeat of `B8` with an additional measure.

Matching is based on overall similarity of:

- chord sequences,
- rhythm onset times,
- a melodic-distance function (§3.1, p. 3).

The paper does not give the complete melodic-distance or similarity equations; it refers readers to a longer external algorithm description.

---

### 4. Phrase-detection algorithm

#### Structure Description Length

The authors prefer shorter structural descriptions, treating structure as compression (§3.1, pp. 3–4).

The objective is:

\[
SDL(\Omega)=h|\Omega|+g\sum_{p\in P} avglen(p)
\]

where:

- \(\Omega\) is the proposed structure,
- \(|\Omega|\) is the number of phrase symbols,
- \(P\) is the set of phrase types,
- \(avglen(p)\) is the average length of instances of phrase \(p\),
- \(h=1.0\),
- \(g=1.3\).

The values of \(h\) and \(g\) were **manually tuned on training data** (§3.1, p. 4).

#### Three algorithmic stages

Given melody, chord analysis, and time signature (§3.3, p. 4):

1. **Find matched phrase pairs**
   - Equal-length, non-overlapping segments.
   - Candidate lengths: **4–20 measures**.

2. **Merge matches into phrase sets**
   - Each candidate phrase is a node in an undirected graph.
   - Matching phrases are connected by edges.
   - Phrase sets correspond to maximal cliques.

3. **Select the best structure**
   - Choose the structure minimizing SDL.
   - The resulting optimization is equivalent to a maximum-weight clique problem.
   - Since this is NP-complete, the implementation combines:
     - dynamic programming,
     - A* search,
     - heuristics.

The authors state that the number of phrase sets grows roughly linearly with song length, making the computation feasible for songs with hundreds of measures (§3.3, p. 4).

#### Runtime and accuracy

- Average runtime: **345 seconds per song** on a 2.3 GHz 8-core Intel Core i9 laptop with 64 GB RAM.
- For **80% of songs**, average runtime was **21 seconds**.
- The paper reports **92%** correct agreement with human-labeled structures (§3.3, p. 4).

Later, §6 reports **93%** accuracy against human labeling (PDF p. 8). The paper does not explain this discrepancy. It should be reported as **92% in the algorithm section and 93% in the discussion**, rather than silently selecting one value.

---

### 5. Section-detection algorithm

Sections are not detected by an independent learned segmentation model. They are inferred from the phrase-level representation (§4.2, PDF p. 5).

The rule is:

- successive **non-melodic phrases** and/or `X` phrases,
- with total length **greater than two measures**,
- indicate high-level section boundaries.

Example:

```text
i4A8B8x4A8X2B8B8c4c4B9o2
```

After removing separator phrases `i4`, `x4`, `c4c4`, and `o2`, the authors identify:

```text
A8B8 | A8X2B8B8 | B9
```

The resulting hierarchy is therefore:

```text
song
 └── sections
      └── repeated phrases
```

#### Section statistics

From Figures 3–5 and accompanying text (pp. 5–6):

- Most songs have **two or three sections**.
- Each section typically contains **one to six phrases**.
- More than **90% of songs have two or three distinct melodic phrases**.
- Each section usually contains **one to three distinct melodic phrases**.
- **20%** of sections exactly repeat the preceding section.
- **29%** of successive sections repeat a suffix of the previous section.
- **18%** repeat a prefix of the previous section.

---

### 6. Figures

The paper contains **seven figures and no tables**.

#### Figures 1–2: phrase statistics, p. 5

- **Figure 1:** Repeated melodic phrases cover roughly **50–90%** of most songs.
- **Figure 2:** Most melodic phrases are **4 or 8 measures** long, with smaller numbers of longer phrases.

#### Figures 3–5: section statistics, p. 6

- **Figure 3:** Number of high-level sections per song; the mode is two or three.
- **Figure 4:** Number of phrases per section; most sections contain a small number of phrases, generally one to six.
- **Figure 5:** Distribution of distinct melodic phrases in songs versus sections.

#### Figure 6: harmony by hierarchical position, p. 7

The authors condition on major-mode material and compare:

- background,
- phrase start,
- section start,
- phrase middle,
- phrase end within a section,
- phrase end at section end,
- section end.

Main observations:

- I is especially likely at the **start of a phrase** and **end of a section**.
- V is especially common at phrase endings within sections.
- I is more characteristic of section closure.
- All reported differences against the background condition are significant under one-tailed unpaired t-tests with **P < .0001**.

#### Figure 7: melody pitch by position, p. 7

Conditioned on an I chord in major mode:

- Scale degree 1 becomes especially common at the **end of sections**.
- Scale degree 3 is more common at **phrase starts** than at section endings.

#### Rhythm and duration result, p. 7

Phrase endings use longer notes than phrase beginnings or middles.

A particularly strong positional difference:

- Only **6.4%** of whole-or-longer notes occur at phrase endings in the middle of a section.
- **72%** occur at phrase endings that also end a section.

#### Historical trend, p. 7

Across the seven-decade corpus:

- Cross-phrase similarity decreases with composition date, with greater contrast between sections: **P < .01**.
- Phrase harmonic complexity increases with date, reflecting longer phrases and more chord-type variety: **P < .002**.

---

### 7. Harmony, melody, and rhythm findings

#### Harmony

At the end of a section:

- **58%** of major-mode progressions are V–I.
- V–I transition probabilities are:
  - **0.89** at phrase ends,
  - **0.84** at phrase ends in the middle of sections,
  - **0.94** at section ends,
  - compared with **0.47** at other positions.

The authors interpret this as evidence that section endings have a stronger cadential role than ordinary phrase endings (§5, p. 6).

#### Melody

The same chord context does not imply the same melodic distribution: pitch behavior depends on whether the location is a phrase start, phrase ending, or section ending (§5, pp. 6–7).

#### Rhythm

Longer notes are disproportionately associated with closure, especially section closure (§5, p. 7).

#### Music-theoretic interpretation

The authors note that half cadences occur more often at phrase ends in the middle of sections, consistent with the theoretical idea that a half cadence signals continuation (§6, p. 8).

**Author claim:** the algorithm discovers these effects without explicitly encoding music-theory concepts, so the results provide a data-driven test of some traditional theory.

**Interpretation:** The algorithm is useful as an auditable structural probe because its segmentation objective is based on repetition and similarity, while the theory-related regularities are measured afterward rather than hard-coded.

---

### 8. Limitations stated by the authors

1. **Manual parameters**
   - The phrase-level parameters, especially \(h=1.0\) and \(g=1.3\), were manually tuned.
   - The authors suggest style-specific automatic tuning (§6, p. 8).

2. **Corpus limitations**
   - Results come from Chinese popular music.
   - Western-pop generalization is only hypothesized, not tested.
   - Non-pop music remains future work.

3. **Section-boundary heuristic**
   - Non-melodic separator phrases are not present in every style.
   - Repeated forms such as `AABA|AABA` may lack the separators needed by the current method.
   - The authors call for more robust section indicators (§6, p. 8).

4. **Incomplete interaction analysis**
   - The authors describe the harmony, melody, and rhythm results as initial findings.
   - Variation between similar phrases and construction of contrasting phrases remain open questions.

5. **No generation experiment**
   - The paper suggests applications to imitation, generation, evaluation, and analysis.
   - It does not actually train or evaluate a long-form generator, mashup system, or repair system.

Additional methodological caveats suggested by the evidence:

- The system depends on transcribed melody and chord quality.
- The phrase detector assumes bar-aligned boundaries.
- The human comparison is underspecified.
- The reported 92% and 93% values are inconsistent.
- The optimization is computationally expensive for repeated use at scale.

---

### Relevance to the research programme

### Long-form symbolic generation

The paper supports a **hierarchical conditional generator** rather than a flat event-level model:

```text
section role
  → phrase identity/repetition pattern
    → harmonic progression
      → melody and rhythm
```

Concrete implementation ideas:

1. Generate a section skeleton first.
2. Assign phrase roles such as:
   - introduction,
   - repeated A/B phrase,
   - transition,
   - phrase end within section,
   - section-ending phrase.
3. Condition harmony, melody, and rhythm on both:
   - local phrase position,
   - global section position.
4. Use the paper’s empirical distributions as interpretable priors:
   - V at phrase endings inside sections,
   - I and V–I at section endings,
   - longer notes at closure,
   - scale-degree-1 emphasis at section endings.

Evaluation should separate:

- phrase repetition accuracy,
- section recurrence,
- cadence placement,
- pitch-role distributions,
- rhythm-duration distributions,
- long-range structural coherence.

### Mashups and recombination

The phrase/section representation offers a useful compatibility layer:

1. Detect phrase and section structures independently in two songs.
2. Align segments by structural role rather than only by local similarity.
3. Prefer transfers such as:
   - section-ending material to section-ending positions,
   - phrase-middle material to phrase-middle positions,
   - A/B phrase correspondences.
4. Score candidate boundaries using:
   - chord transition compatibility,
   - cadence type,
   - melodic register and scale-degree behavior,
   - rhythm density and note-duration profile.
5. Preserve repeated phrase identity when recombining, so a mashup does not destroy source-level repetition.

**Research hypothesis:** mashups that preserve hierarchical role should be more coherent and more explainable than those aligned only by beat or chord similarity.

### Symbolic repair

The paper suggests a concrete diagnostic representation for repair:

- Detect a song’s phrase/section structure.
- Flag anomalies when a location violates the learned role distribution:
  - non-cadential harmony at a section ending,
  - short-note continuation where a section closure is expected,
  - inconsistent phrase repetition,
  - melody that fails to reflect phrase versus section position.
- Propose minimal repairs:
  - substitute a compatible cadence,
  - extend or shorten a phrase,
  - restore a repeated phrase,
  - alter only the boundary rhythm or melodic closure.

Each repair can expose an explanation such as:

> “This edit changes the boundary from a phrase-internal V ending to a section-final V–I cadence, matching the detected structural role.”

That would directly support explainable, auditable repair rather than unconstrained rewriting.

---

### Concrete research ideas

1. **Style-conditioned hierarchical segmentation**
   - Replace fixed \(h,g\) values with style-specific parameters learned from annotated corpora.
   - Compare MDL, Bayesian, and discriminative objectives.

2. **Separator-free section detection**
   - Extend the phrase graph with recurrence, contrast, novelty, and harmonic-profile change.
   - Test explicitly on `AABA|AABA` and Western-pop datasets.

3. **Role-conditioned generation benchmark**
   - Generate melodies and chord sequences conditioned on:
     - phrase start,
     - phrase middle,
     - phrase end within section,
     - section end.
   - Evaluate against the paper’s distributions and human judgments.

4. **Structure-aware mashup benchmark**
   - Compare beat-aligned, chord-aligned, phrase-aligned, and section-role-aligned recombination.
   - Measure boundary coherence, source identity preservation, repetition integrity, and listener preference.

5. **Evidence-grounded repair**
   - Build a repair system whose candidate edits are justified by detected phrase identity and position-conditioned statistics.
   - Evaluate minimality, structural restoration, harmonic validity, and explanation faithfulness separately.

6. **Modern replication**
   - Reproduce the 909-song analysis with explicit train/test splits, annotator agreement, confidence intervals, and exact algorithmic details.
   - Resolve the paper’s 92% versus 93% discrepancy.

### Bottom line

The paper’s strongest contribution is an interpretable bridge between **symbolic structure detection** and **position-dependent musical behavior**. Its phrase/section representation is directly reusable for long-form planning, source-aware mashups, and explainable boundary repair. Its evidence is promising but corpus-specific, partly underspecified, and not yet a demonstrated generation result.

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
