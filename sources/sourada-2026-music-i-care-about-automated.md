---
title: "Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills on (Almost) Any Music"
authors: Tomáš Sourada, Katia Vendrame, Jan Hajič
year: 2026
doi: 10.48550/arXiv.2607.06015
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/sourada-2026-music-i-care-about-automated.pdf"
pdf_filename: sourada-2026-music-i-care-about-automated.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

MusICA-MetaBench turns any user-supplied MusicXML score into a multiple-choice music-perception benchmark, poses the same question as audio, sheet image and symbolic text, and calibrates how many items are needed to detect a chosen accuracy difference — so evaluation can run on the user's own authorized repertoire instead of a fixed, leak-prone test set.

## 1. Document Information

- **Canonical citation:** Tomáš Sourada, Katia Vendrame, and Jan Hajič jr., “Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills on (Almost) Any Music,” arXiv:2607.06015v1 [cs.SD], 7 July 2026, 9 PDF pages. Header on every page: “Preprint – July 8, 2026”. No venue is claimed.
- **Affiliations:** Charles University (Sourada, Hajič jr.) and Brno University of Technology (Vendrame). [PDF p. 1]
- **DOI:** `10.48550/arXiv.2607.06015` (arXiv DOI; no publisher DOI in the PDF).
- **Code:** `https://github.com/tomsouri/MusICA-MetaBench-preprint` (from the batch metadata, not verified here).
- **Canonical integrity:** SHA-256 `0c2076583a28f5637379704f861b00a375daaa7f922e51641dc4f8107f11bea6`.
- **Rights boundary:** arXiv preprint; terms follow the arXiv licence, not restated here. Local research evidence only.
- **Primary category:** `interaction-and-evaluation`. The contribution is an evaluation instrument and a calibration recipe, not a model, dataset, or explanation method.
- **Evidence levels:** table values and section claims were re-read from the rendered PDF. Two errors in the earlier batch digest are corrected here: the per-modality percentages attributed to ChoraleBricks actually belong to ChoralSynth (Table 4), and the size-calibration claim “s = 780 for 1–2%” contradicts Table 2, which gives s = 750 for 3 pp and s = 1500 for 2 pp.

## 2. Key Contributions

### A generator, not a fixed benchmark

Question templates are instantiated against an ontology, crossed with the user's pieces, and filtered; ground truth and distractors come from a programmatic extractor over MusicXML, so no LLM annotates the answers. The same (question, piece, answer) item is then copied into three modality variants: ABC symbolic text, an audio mix, and a sheet-image PNG. [PDF pp. 2–3, Fig. 1]

### Cross-modal diagnosis

Because the question and the answer set are identical across modalities, a difference between symbolic and audio accuracy is a perceptual-modality difference rather than a different-task difference. This is the paper's main design claim: it separates “cannot read the notation” from “cannot hear the harmony”. [PDF pp. 1–3]

### Calibrated benchmark size

The authors formalise the question “how many items do I need?” as: for a user-defined minimum relevant effect E, find the smallest size s at which all pairwise model comparisons become significant after Bonferroni correction. They publish the resulting table, so a user can trade cost against resolution instead of guessing. [PDF pp. 3–4, Table 2]

### A distractor-validity check

A no-input arm and a noise-input arm test whether questions can be answered without perceiving the music. [PDF pp. 5–6, Fig. 3]

## 3. Methodology and Architecture

- **Question skills.** Five categories — pitch, interval, rhythmic notation, temporal proportion, and harmony (tonic, chord, chord progression) — chosen as the “analysis” level of Bloom's taxonomy shared by Kodály, ABRSM and GCSE pedagogy. Examples are in Table 1; each template is piece-level and answerable from every modality. [PDF pp. 3–4, Table 1]
- **Pipeline.** (1) instantiate templates from the ontology derived from music21 objects; (2) form the Cartesian product with pieces and run a Python extractor that returns ground truth plus a distractor pool drawn from the piece itself, with ontology distractors as fallback; (3) filter invalid items, subsample balanced by skill, then copy each item into symbolic (ABC via `abc_xml_converter`), audio (reference mix) and image (MusicXML PNG) variants. [PDF pp. 2–3, Fig. 1]
- **Item format.** Five options: one correct, three distractors, and “none of the other options is correct” (NOTA). NOTA is correct in 20% of items to match the uniform prior; options are shuffled at generation time; responses are parsed to letters. [PDF p. 3]
- **Calibration.** Sizes s ∈ {15, 75, 150, 300, 750, 1500} (1–100 questions per category-modality cell), 10 random subsets per size, 6 MLLMs, Shapiro–Wilk normality check, then shifted-accuracy paired t-tests over E ∈ {1…20, 25, 30} pp with Bonferroni correction. [PDF p. 4]
- **Data.** ChoraleBricks: ten chorales, soprano/alto/tenor/bass played by wind instruments, with MusicXML, PNG and multitrack audio. Its full benchmark would be 12,666 items (4,222 × 3 modalities), which motivates subsampling. Generalisation test: ChoralSynth, 20 synthetic choral pieces. [PDF pp. 3, 5–6]
- **Models.** Gemini 2.0/2.5/3.1 Flash Lite, Gemini 3.1 Pro, Qwen3 Omni 30B run locally, and “aggregated” pairs for GPT-4o, GPT-5 and Mistral in which one model handles audio and another handles visual/symbolic input. [PDF p. 3]

## 4. Key Results and Benchmarks

**Calibration (Table 2).** Minimum detectable effect in percentage points per benchmark size [PDF p. 4]:

| s | 15 | 75 | 150 | 300 | 750 | 1500 |
|---|---|---|---|---|---|---|
| min effect (pp) | 30 | 12 | 8 | 6 | 3 | 2 |

All observed gaps of at least 6 pp are significant at s = 300, and in practice gaps of at least 3.5 pp also are. [PDF p. 4]

**ChoraleBricks, s = 300, one instance (Table 3)** [PDF p. 5]: Gemini 3.1 Pro 59.0% (12 h, $58.4), Qwen3 Omni 30B 46.3%, Gemini 3.1 FL 45.7% (18 min, $0.3), agg-GPT-5 42.0%, agg-GPT-4o 41.0%, Gemini 2.5 FL 41.0%, Gemini 2.0 FL 40.3%, agg-Mistral 39.3%, random 20.0%.

**Cross-modal pattern.** Averaged over models, accuracy(symbolic) > accuracy(image) > accuracy(audio), and most between-model variation comes from the symbolic modality; in audio almost all models cluster except Gemini 3.1 Pro (high) and GPT-5 (below chance). [PDF p. 5, Fig. 4]

**ChoralSynth, s = 300 (Table 4)** [PDF p. 6]: Gemini 3.1 Pro 47.0% overall (audio 31, ABC 75, image 35), Gemini 3.1 FL 33.3% (23/49/28), Gemini 2.5 FL 32.0% (22/47/27), random 20%. Performance falls most in audio and image; the authors attribute this to voice-specific labels that a mixed recording cannot reveal and to multi-page concatenated score images.

**Perception check.** In the ChoralSynth run, mean accuracy is 28% in the normal setup versus 17% with no input and 20.1% with noise input against a 20% random baseline, which supports “perception is required” while also showing that the distractors are weaker than ideal. [PDF pp. 5–6, Fig. 3]

**Cost.** Total LLM experiment cost is 730 USD, dominated by the leading-edge models. [PDF p. 6]

## 5. Limitations and Future Work

- **Scope.** Western tonal repertoire, one or more *monophonic* voices, MusicXML mandatory for ground truth. Polyphonic piano and non-Western traditions are explicitly future work. [PDF p. 6]
- **Small corpora.** Ten chorales and twenty synthetic pieces; item variance across pieces is high, which the authors observe as higher standard deviation on ChoralSynth at fixed size. [PDF pp. 5–6]
- **Distractor weakness.** The no-input arm scores above chance partly because the prompt asks the model to analyse a file that is absent and some models refuse; the authors propose a “try to guess” prompt. Individual skill scores are not mapped to graded syllabi such as ABRSM. [PDF p. 6]
- **Feature recognition only.** The questions test naming and counting of theory features, not emotion, style, or compositional judgement. [PDF pp. 3–4]
- **No human ceiling.** There is no expert baseline, so the top 59% has no reference point.
- **Aggregated systems.** GPT and Mistral entries pair different models for audio and vision, which confounds any per-modality comparison for those rows. [PDF p. 3]
- **Snapshot models.** Preview Gemini versions and current prices will age; the authors say the design, not the leaderboard, is the contribution.

## 6. Related Work

- **Cross-modal evaluation as a diagnostic.** This is the closest published instrument to the repository's interest in whether a model's stated reason is grounded in the modality it actually used; see [[concepts/audio-symbolic-modality-gap]] and [[overviews/audio-symbolic-transfer]].
- **Probing versus benchmarking.** [[concepts/music-theory-probing]] covers representation probes on fixed models; MetaBench instead measures observable task accuracy in a controlled item format. The two answer different questions: recoverability inside a model versus behaviour at the interface.
- **Evaluation validity in this repository.** [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] supplies the cautionary case for evaluation protocols; MetaBench's programmatic ground truth and no-input control are the same family of safeguards.
- **Symbolic controllability work that could be tested with it.** [[theory-and-constraints/mcleod-2020-a-modular-system-for]] and [[generation-and-planning/wang-2020-learning-interpretable-representation]] both make claims about interpretable harmonic or latent structure that a cross-modal, size-calibrated benchmark could interrogate.

## 7. Glossary

- **ABC:** a text-based score notation used as the symbolic modality.
- **ABRSM:** Associated Board of the Royal Schools of Music, a graded music-examination system.
- **GCSE:** General Certificate of Secondary Education, a UK school qualification.
- **MLLM:** Multimodal Large Language Model.
- **MCQ:** Multiple-Choice Question.
- **NOTA:** “None of the other options is correct”.
- **OMR:** Optical Music Recognition.
- **pp:** percentage points.
