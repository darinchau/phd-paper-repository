---
title: "On the Human and Computer Alignment of Attribute-Based Music Matches"
authors: "Roser Batlle-Roca, Woosung Choi, Joan Serrà, Fabio Morreale, Wei-Hsiang Liao, Xavier Serra, Emilia Gómez, Yuki Mitsufuji"
year: 2026
doi: 10.48550/arXiv.2609.00987
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/batlle-roca-2026-on-the-human-and-computer.pdf"
pdf_filename: batlle-roca-2026-on-the-human-and-computer.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-14
---

## One-line Summary

"**On the Human and Computer Alignment of Attribute-Based Music Matches**." arXiv:2609.00987v1 [cs.SD], **1 September 2026**, 15 pages. A perceptual triplet experiment with 83 expert raters shows that attribute-level framing (melody, harmony, rhythm, voice, timbre) yields substantial human agreement on music matches, introduces the MATCHA dataset (300 triplets, 1,105 annotations), and finds only partial, attribute-specific alignment between human judgments and the MiRA similarity metrics.

## 1. Document Information

- **Canonical source:** arXiv `2609.00987v1`; official PDF preserved as `batlle-roca-2026-on-the-human-and-computer.pdf` (SHA-256 `b5f306cc1251f0fc57cecfbd8ada14c10c51d42d61626540e91c4b5c0ad4e796`, 15 pages, PDF 1.7).
- **Bibliographic record:** Batlle-Roca, Roser (Universitat Pompeu Fabra, Music Technology Group); Choi, Woosung; Serrà, Joan; Morreale, Fabio; Liao, Wei-Hsiang (Sony AI); Serra, Xavier (UPF); Gómez, Emilia (UPF; European Commission Joint Research Centre); Mitsufuji, Yuki (Sony AI; Sony Group Corporation). Corresponding author roser.batlle@upf.edu. Preprint ("Preprint." footer, p. 1); no journal or conference venue stated in v1.
- **Reading provenance:** full text extracted from the PDF (all 15 pages read: main body pp. 1–7, references pp. 7–9, appendices A–C pp. 10–15). Figures 1 and 2 (pp. 5–6) were additionally rendered to PNG and visually inspected; per-cell values below are marked *approximate* where they come from that visual read rather than from prose, and the paper's prose-stated ranges take precedence.
- **Funding/context:** TRAMUCA project, a joint MTG-UPF / Sony AI / European Commission JRC collaboration (datasheet §C.1, PDF p. 13). Dataset repository: `https://github.com/roserbatlleroca/matcha`.
- **Evidence policy:** author claims, reported measurements, and repository inferences are kept distinct below. Nothing here is an independent reproduction.

## 2. Key Contributions

1. **Attribute-level perceptual experiment** (author claim): a triplet forced-choice study demonstrating "measurable human agreement in identifying attribute-level similarities across five attributes" (p. 1), in contrast to the chronically low inter-rater agreement reported for global musical similarity (Ellis et al. 2002; Flexer and Grill 2016).
2. **MATCHA dataset** (Musical Attribute-based Triplet Comparison with Human Annotations): 300 curated triplets (150 human-composed, 150 AI-generated) annotated by 83 expert participants, totaling 1,105 attribute-level perceptual assessments (~3.7 evaluations per triplet) across melody, harmony, rhythm, voice, and timbre (§4.1, pp. 4–5). Released with a Datasheets-for-Datasets record (Appendix C); intended as an evaluation benchmark with no train/val/test splits (§C.2, p. 14).
3. **Human–computer alignment analysis**: first validation of the MiRA framework's similarity metrics against human perceptual judgments per musical attribute, showing partial, attribute-specific alignment and supporting MiRA's multi-metric design (§4.3, pp. 5–6).

**Repository inference (not an author claim):** the attribute-level decomposition is an explainability move — it asks *why* two excerpts match rather than *whether* they match — and the dataset is directly reusable as a perceptual ground-truth benchmark for replication/similarity detectors, including symbolic ones, none of which the paper evaluates.

## 3. Methodology and Architecture

### Task design (§3.1, p. 3)

Triplet forced-choice: one reference excerpt plus two comparison excerpts (A, B); for a named attribute the participant selects A, B, or **Neither**. Optional free-text comments. The five attributes were defined in the task instructions as (Appendix A.1, p. 10):

- **Melody:** "The most prominent tune or memorable sequence of notes."
- **Harmony:** "Chord progressions and tonal relationships across time."
- **Rhythm:** "Tempo, beat patterns, and timing."
- **Voice:** "Vocal or singer characteristics, including singing style."
- **Timbre:** "Tone quality and instrumental texture."

Deliberate framing choice: the word **"match"** instead of "replication", "plagiarism", or "copy", to assess perceived same-or-very-similar status per attribute without legal/technical priming (p. 3). Two worked examples (consensus of four independent musical experts) preceded the task; light gamification (points, ranking) and a prize draw (four €25 vouchers) encouraged engagement.

### Stimuli: 300 cases, ~10-second excerpts (§3.2, pp. 3–4; Table 1, p. 4)

| Section | Origin | Source | Cases | w/ vocals |
|---|---|---|---:|---:|
| HP | Human | SMP plagiarism dataset (Go and Kim 2026) | 75 | 61 |
| HV | Human | Discogs-VI version-identification dataset (Araz, Serra, and Bogdanov 2024) | 75 | 63 |
| AS | AI | Stable Audio Open generations (Evans et al. 2025), rock/electronic | 120 | 0 |
| AM | AI | Media-documented AI-plagiarism cases (Newton-Rex 2024, Suno; GEMA 2024) | 30 | 27 |

- Excerpt boundaries were adjusted to avoid interrupting the attribute under evaluation mid-phrase. SMP provides replicated-segment start annotations; for Discogs-VI, comparable fragments were located with madmom beat tracking and Essentia chroma / harmonic pitch profiles / MFCC-spectral descriptors.
- **Distractor (third-sample) conditions** for the human-composed cases: another track by the same artist as the reference (28%) or as the comparison sample (12%); a different section of the same recording (22%, timbre-similar); a similar genre/style piece (30%); random unsimilar song (8%). AM triplets follow the same protocol (53% same artist, 23% other section of the reference, remainder similar style). Vocals mostly English (55% of HP+HV cases).
- **Control cases:** 30 cases (10%, 15 SMP + 15 Discogs-VI) with straightforward ground truth, randomly mixed one per ten cases; participants scoring ≤ 0.25 control agreement were excluded.

### AI-generation pipeline for the AS section (§3.2 p. 3–4; Appendix B, pp. 12–13)

References drawn from the Free Music Archive (FMA). For each reference, two comparisons with controlled similarity:

- **"Less similar"**: text-prompt conditioning only. The reference is described by Music Flamingo (Ghosh et al. 2025), summarized by Qwen 3.5; Stable Audio Open then generates from random initial noise under that prompt.
- **"More similar"**: DDIM inversion (Song, Meng, and Ermon 2021) of the reference audio to obtain its (approximate) initial noise, then v-DDIM sampling with controlled stochasticity η ∈ {0.3, 0.5} (balanced across cases) plus the extracted text prompt. Inversion itself is deterministic (η = 0).

Hyperparameters (Table 4, p. 13): v-DDIM sampler, 100 diffusion steps, σ ∈ [0.1, 1.0], CFG scale −6.0 (inversion) / +6.0 (generation); fixed seed 42; stable-audio-open-1.0 checkpoint; single NVIDIA H100 PCIe (82 GB), CUDA 12.8, driver 570.172.08. The two-level design prevents both trivial ties and one-sided comparisons (Appendix B, p. 12).

### Participants and screening (§3.3, p. 4; Appendix A.3, pp. 10–11)

Web-based remote experiment, ~2 months of collection (10 March – 11 May 2026 per datasheet §C.3), approved by UPF's institutional ethics committee (CIREP). Funnel: 184 accessed → 67 completed no case and 8 only one (excluded) → 5 removed for control-case score ≤ 0.25 → 21 removed for completing 2–9 cases without encountering a control case → **83 final participants**. Predominantly men (60.2%), aged 25–34 (56.6%), Europe 68.7% / Asia 14.5%. Self-reported expertise (Table 2): Expert Music Professional 22 (26.5%), Trained Music Practitioner 31 (37.3%), Skilled Musician 20 (24.1%), Engaged Music Listener 10 (12.0%) — i.e. 63.8% in the top two categories. Roles (Table 3): music researcher 33.7%, musician/performer 32.5%, sound engineer 20.5%, composer/songwriter 4.8%, others ≤ 2.4%. Each triplet was rated by at least three participants, with extra annotations prioritized for ambiguous/tied cases.

### Alignment analysis (§4.3, p. 5)

Participant votes per case are aggregated into a normalized preference score

s = (n_B − n_A) / (n_A + n_B + n_N),

with n_A, n_B, n_N the counts of A, B, Neither responses; s ∈ [−1, 1], negative = preference for A. Alignment with MiRA metrics is measured by Kendall's τ (rank-based, tie-robust, non-parametric). MiRA's four metrics (§2.2, p. 2): **CoverID** (cover-song identification via cross-recurrence quantification, Serrà, Serra, and Andrzejak 2009; melodic/harmonic correspondence), **KL divergence** over PaSST audio-classifier embeddings (Koutini et al. 2022), **CLAP** (language-audio contrastive embeddings, Wu et al. 2023), and **Discogs-EffNet (DEfNet)** (style/timbre embeddings, Alonso-Jiménez et al. 2020).

## 4. Key Results and Benchmarks

### Human inter-annotator agreement (§4.2, pp. 4–5; Figure 1, p. 5)

- Six of 300 cases (2%) tied on at least one attribute; excluded from agreement percentages, retained in Fleiss' κ.
- **Melody is the most reliable attribute across categories: agreement > 85%, κ ≈ 0.60.** Harmony and timbre produce the lowest agreement. Case-level agreement ranges 50–100% (M = 77.3%, SD = 12.4); melody most consistent overall (81.6%), harmony most contested (75.0%). Voice annotations (151 vocal triplets) yield moderate agreement, κ ∈ [0.32, 0.47].
- Human-composed sets (HP, HV) achieve the highest reliability, closely followed by AM; **AS exhibits near-chance agreement (κ ≤ 0.19) with dominant Neither selections (52–64%, vs 17–34% in other subsets)**. The authors attribute this to acoustic artifacts introduced by their own generation pipeline (text conditioning and DDIM inversion insufficient to capture melodic lines / timbral textures), i.e. a generation and triplet-construction artifact rather than rater failure (§4.2 p. 5, §5 p. 6).
- *Approximate figure read (Figure 1, rendered p. 5; prose ranges primary):* agreement % HP melody 85.6 / harmony 77.4 / rhythm 80.4 / voice 79.0 / timbre 74.5; HV melody 85.0, timbre 80.2; AS melody 75.9, harmony 69.3; AM melody 86.0, timbre 73.6. κ: HP melody 0.60, timbre 0.31; AS melody 0.18, harmony 0.09, rhythm 0.19, timbre 0.14; AM melody 0.61, timbre 0.20. Voice is not annotated for AS (instrumental).

### Human–computer alignment (§4.3, pp. 5–6; Figure 2, p. 6)

- **AS subset diverges systematically:** τ ∈ [−0.11, 0.21], mostly non-significant, several slightly negative (metric prediction opposite to the human majority). Treated as a generation/triplet artifact and set aside; the remaining subsets are aggregated as the non-AS group (N = 270).
- **Non-AS patterns (author claims, p. 5):**
  - **CoverID** aligns most strongly and significantly (p < 0.05) with **melody and harmony**, particularly in HV — matching its cover-song-identification design.
  - **CLAP and DEfNet** give the broadest alignment, correlating strongly with **rhythm, timbre, and voice**; CLAP excels at vocal similarity, DEfNet is slightly more consistent across rhythmic structure.
  - **KL divergence (PaSST)** shows moderate alignment for rhythm, voice, timbre but fails to capture melodic/harmonic dimensions, attributed to its broad audio representations.
  - **AM mirrors the human-composed trends** with wider confidence intervals (N = 30).
- *Approximate figure read (Figure 2 heatmap, rendered p. 6; two independent visual reads agreed on patterns but not on every cell — treat all cell values as approximate, prose as authoritative):* non-AS CoverID τ ≈ 0.39* (melody), 0.39* (harmony), 0.30* (rhythm), 0.03 (voice), 0.16 (timbre); non-AS DEfNet τ ≈ 0.24* / 0.31* / 0.50* / 0.42* / 0.51* across melody→timbre; non-AS CLAP τ ≈ 0.14 / 0.19 / 0.37* / 0.48* / 0.48*; non-AS KL τ ≈ 0.07 / 0.09 / 0.26* / 0.28* / 0.32*. AS cells range ≈ −0.11…0.21 with at most isolated significance. (* = bolded as p < 0.05 in the figure.)
- **Overall conclusion (author claim):** no single metric aligns with all attributes; different metrics capture complementary musical dimensions — empirical support for MiRA's multi-metric design, and a pointer to missing attribute-specific metrics (they single out voice).

### Dataset distribution (Appendix C, pp. 13–15)

Metadata and annotations public via GitHub; audio via Zenodo. Commercial-track audio restricted by copyright; the AS audio subset is to be released CC-BY-NC 4.0 following paper acceptance (Stability AI license compliance). Explicitly not to be used "as a final legal decision or definitive evidence for copyright infringement or plagiarism disputes" (§C.5, p. 15).

## 5. Limitations and Future Work

### Explicitly acknowledged (§5–§5.1, pp. 5–7)

- Similarity ≠ plagiarism; computational similarity cannot prove memorization or infer generation mechanisms — replication assessment here is a perceptual/computational approximation that flags risky cases (p. 6).
- **Similarity-by-construction:** HP/HV/AM stimuli were selected for pre-established strong similarity and AS generations were conditioned toward the reference, so the reported agreement reflects human consistency on already-similar material and may not generalize to arbitrary pairs (p. 6).
- Western-centric repertoire and contemporary production; findings may not transfer to non-Western traditions (p. 7).
- Only five attributes; lyrics, structure, dynamics, texture, expressive performance, emotion not covered (p. 7). Attributes are naturally intertwined and not fully isolable (p. 7).
- Triplet forced-choice simplifies similarity into discrete decisions among predefined alternatives (p. 7).
- Future work (authors): more attributes, non-Western repertoires, MiRA extensions with attribute-specific metrics (voice named), MATCHA as benchmark for replication-assessment approaches (p. 7).

### Additional evidence boundaries (repository inference)

- **Controlled AI generation covers only Stable Audio Open** (chosen for its open, CC-licensed training data); the AM cases come from proprietary systems (Suno) with unknown prompts and generation-attempt counts (p. 6), so no open generator–closed generator comparison is controlled.
- The AS failure means the paper's alignment evidence for AI-generated material rests on 30 uncontrolled AM cases; the N = 270 aggregate is dominated by human-composed pairs.
- Agreement statistics are computed over ~3.7 raters per case with vote aggregation into a single preference score; per-rater variance and rater-expertise stratification are not reported in the main text.
- Figure 2's exact per-cell τ values are not restated numerically in the prose; the numbers above are approximate visual reads (two reads agreed on direction/pattern, not on every magnitude).
- No symbolic-domain metric is evaluated; all four MiRA metrics operate on audio.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor; places this paper in the evaluation/attribution cluster.
- [[explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism]] — complementary machine-side view: COPYCAT-style plagiarism detection with version-identification embeddings, where MATCHA supplies the missing perceptual grounding for exactly this class of similarity metrics.
- [[explainability-and-auditability/yu-2026-truemuse-a-benchmark-for-data]] — data-attribution benchmarking for text-to-music models; MATCHA adds the human-perception axis to attribution evaluation.
- Prior perception literature the paper builds on: Ellis et al. 2002 and Flexer and Grill 2016 (low inter-rater agreement for global similarity); Müllensiefen and Frieler 2004 (single-attribute judgments increase agreement); Novello, McKinney, and Kohlrausch 2006/2011 (perceptual evaluation of music similarity).
- Framework under test: MiRA (Batlle-Roca et al. 2024, ISMIR) — CoverID, KL/PaSST, CLAP, DEfNet. Alternative framing: Barnett, García, and Pardo 2024 (data attribution via CLMR/CLAP embeddings).

## 7. Glossary

- **Match** — the experiment's framing for two excerpts perceived as the same or very similar with respect to a given attribute; avoids legal terms (replication/plagiarism/copy).
- **MATCHA** — Musical Attribute-based Triplet Comparison with Human Annotations; the dataset introduced by this paper (300 triplets, 1,105 expert annotations, 5 attributes).
- **MiRA** — Music Replication Assessment framework (Batlle-Roca et al. 2024): four complementary similarity metrics (CoverID, KL/PaSST, CLAP, DEfNet) for flagging replication in AI-generated music.
- **CoverID** — cover-song identification via cross-recurrence quantification of chroma representations; sensitive to melodic/harmonic correspondence.
- **CLAP / DEfNet** — contrastive language-audio and Discogs-style/timbre embedding models; broad semantic-stylistic-timbral similarity.
- **KL divergence (PaSST)** — distributional distance over Patchout-faithful audio-transformer embeddings; broad audio resemblance.
- **DDIM inversion** — deterministic inversion of a diffusion model mapping an audio latent back to initial noise; used to generate near-reconstructions with controlled stochasticity.
- **Triplet forced-choice** — experimental paradigm: pick which of two comparisons better matches a reference on a named attribute (A / B / Neither).
- **Fleiss' κ** — chance-corrected multi-rater agreement for nominal categories; ≥ 0.60 read as substantial.
- **Kendall's τ** — rank-based ordinal association measure, robust to ties; used for metric–human alignment.
- **Preference score s** — per-case vote aggregate (n_B − n_A)/(n_A + n_B + n_N) ∈ [−1, 1].
- **HP / HV / AS / AM** — stimulus sections: Human-Plagiarism (SMP), Human-Versions (Discogs-VI), AI-SAO (Stable Audio Open), AI-Media (press-documented cases).
