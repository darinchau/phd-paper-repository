---
title: "Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills on (Almost) Any Music"
authors: Tomáš Sourada, Katia Vendrame, Jan Hajič
year: 2026
doi: 10.48550/arXiv.2607.06015
category: interaction-and-evaluation
source: sourada-2026-music-i-care-about-automated.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/sourada-2026-music-i-care-about-automated.pdf"
pdf_filename: sourada-2026-music-i-care-about-automated.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - music-evaluation
  - multimodal-benchmark
  - music-perception
  - benchmark-calibration
  - evaluation-validity
---
## Summary

MusICA-MetaBench converts a user's own MusicXML scores into a multiple-choice benchmark of music-theory feature recognition, asks each question in audio, sheet-image and symbolic form, and calculates how many items a user needs to detect a chosen accuracy difference. On a ten-chorale corpus, the best model reaches 59% overall while audio accuracy trails the symbolic modality by a wide margin; the paper also shows that its questions fail without perceptual input, though not by as much as the authors would like.

## Key Contributions

- **On-demand benchmarking.** Question templates plus a programmatic MusicXML extractor produce ground truth and distractors, so no LLM writes the reference answers and a user can evaluate on private or newly composed repertoire.
- **One question, three modalities.** The same item appears as ABC text, audio mix, and score image, which turns a cross-modal accuracy gap into evidence about the modality rather than the task.
- **Calibrated size.** A published table maps benchmark size to the smallest detectable model difference, making the cost-resolution trade-off explicit rather than conventional.
- **A validity check.** No-input and noise-input arms test whether perception is needed, and the authors report that both remain above chance, which exposes distractor weakness instead of hiding it.

## Methodology and Architecture

Five question skills — pitch, interval, rhythmic notation, temporal proportion, harmony — are instantiated from a music21-derived ontology, crossed with pieces, filtered, and balanced by skill. Each item has five options including “none of the other options is correct”, correct in 20% of items to match the uniform prior. Modality variants are ABC conversion, the reference audio mix, and a rendered PNG. The 4,222 base items of the ChoraleBricks corpus become 12,666 items across three modalities; the calibration study subsamples to sizes between 15 and 1,500 with ten random draws each and paired t-tests over shifted accuracy vectors.

The complete evidence-grounded digest, with page anchors and the corrected reading of Tables 2–4, is in [`sources/sourada-2026-music-i-care-about-automated.md`](../../sources/sourada-2026-music-i-care-about-automated.md).

## Results

A size of 300 items detects a 6-point accuracy difference; 750 detects 3 points and 1,500 detects 2 [PDF p. 4, Table 2]. On ChoraleBricks at s = 300, Gemini 3.1 Pro leads at 59.0% against a 20% random baseline, at 12 hours and $58.4 per run; the cheaper Gemini 3.1 Flash Lite reaches 45.7% in 18 minutes [PDF p. 5, Table 3]. Across models, symbolic accuracy exceeds image accuracy, which exceeds audio accuracy [PDF p. 5, Fig. 4]. On the synthetic ChoralSynth corpus the best model drops to 47.0% overall with audio at 31, symbolic at 75 and image at 35 [PDF p. 6, Table 4]. The perception check reports 28% mean accuracy in the normal setup versus 17% with no input and 20.1% with noise input against a 20% baseline [PDF p. 6].

## Related Papers

- [[concepts/audio-symbolic-modality-gap]] — the concept this benchmark operationalises at evaluation time: the same musical fact is not equally accessible in audio, image, and symbolic form.
- [[overviews/audio-symbolic-transfer]] — the batch overview on what transfers between audio and symbolic representations, where a calibrated cross-modal instrument is directly useful.
- [[concepts/music-theory-probing]] — the representation-side alternative: probes ask what a fixed model encodes, this benchmark asks what a model can report.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — the repository's reference case for evaluation-protocol risk in music-theory tasks.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
