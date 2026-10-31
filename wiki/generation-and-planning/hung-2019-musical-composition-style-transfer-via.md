---
title: "Musical Composition Style Transfer via Disentangled Timbre Representations"
authors: Yun-Ning Hung, I-Tung Chiang, Yi-An Chen, Yi-Hsuan Yang
year: 2019
doi: 10.48550/arXiv.1905.13567
category: generation-and-planning
source: hung-2019-musical-composition-style-transfer-via.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hung-2019-musical-composition-style-transfer-via.pdf"
pdf_filename: hung-2019-musical-composition-style-transfer-via.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - style-transfer
  - timbre
  - disentanglement
  - arrangement
  - instrument-activity-detection
  - listening-study
---
## Summary

The paper asks whether pitch content and instrument timbre can be separated using only ordinary aligned audio–MIDI pairs, so that re-orchestrating a recording becomes swapping one latent code. Two designs are compared: separate timbre and pitch encoders with adversarial separation, and a single encoder feeding a U-Net pianoroll decoder whose skip connections carry the pitch. The U-Net variant reaches 0.829 average AUC on instrument activity detection and is preferred for rearrangement in a 40-person listening study, while a generic image-style-transfer baseline loses the pitch content entirely.

## Key Contributions

- **A clear task definition.** Composition style transfer is arrangement: keep melody and harmony, replace instrumentation, without paired orchestrations for training.
- **Two disentanglement strategies with different mechanisms.** DuoED separates the codes adversarially; UnetED removes the reason for the latent to carry pitch by routing pitch through skip connections.
- **An inspectable symbolic intermediate.** The model emits a multi-track pianoroll before rendering, so the arrangement decision is visible.
- **Both representation and task evaluation.** Instrument activity detection as a representation probe, plus a listening study on the actual rearrangement task.

## Methodology and Architecture

Input is a constant-Q transform (88 bins, 512-sample window, 16 kHz, 10-second chunks). Targets are a multi-track binary pianoroll plus instrument and pitch rolls summed from it. DuoED trains two encoders and three decoders with binary cross-entropy and adversarial losses that feed the wrong code to the wrong classifier and update only encoders. UnetED trains one encoder with a U-Net pianoroll decoder and a fooled pitch classifier, with skip connections supplying pitch. Style transfer encodes a source clip for content, takes the timbre code from a target clip, decodes a new pianoroll, and synthesises audio. Training uses 344,166 paired MIDI/MP3 files from MuseScore.

The complete evidence-grounded digest, with page anchors and the corrected Table 1, is in [`sources/hung-2019-musical-composition-style-transfer-via.md`](../../sources/hung-2019-musical-composition-style-transfer-via.md).

## Results

UnetED reaches 0.829 average AUC for instrument activity detection across five instruments, against 0.817 for the strongest prior method and 0.815 for DuoED, a difference that is significant by paired t-test but not uniform per instrument (UnetED loses on flute and cello) [PDF p. 5, Table 1]. The ablation shows adversarial training helps both designs, and instrument estimates summed directly from the pianoroll score higher (0.778–0.783) than the timbre decoder alone (0.731–0.754), which the authors read as pitch information aiding instrument detection [PDF p. 5, Table 2]. In the listening study with 40 participants, UnetED beats DuoED on rhythmicness, harmonicity and overall quality, adversarial training improves rhythm and harmony, and the image-style-transfer baseline fails badly by dropping pitch content and creating empty tracks [PDF p. 6].

## Related Papers

- [[concepts/work-identity-versus-performance-variation]] — the pitch/timbre split is an early operational version of separating a work from its realisation.
- [[concepts/auditable-creative-editing-pipelines]] — the pianoroll intermediate gives decision auditability that end-to-end audio style transfer lacks.
- [[generation-and-planning/cheng-2026-musetimbre-zero-shot-timbre-transfer]] — the modern alternative: zero-shot timbre transfer by controlling a frozen generator instead of learning disentangled codes.
- [[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] — rearrangement by recombining existing audio, the neighbouring task this paper does not attempt.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
