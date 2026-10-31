---
title: "Musical Composition Style Transfer via Disentangled Timbre Representations"
authors: Yun-Ning Hung, I-Tung Chiang, Yi-An Chen, Yi-Hsuan Yang
year: 2019
doi: 10.48550/arXiv.1905.13567
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hung-2019-musical-composition-style-transfer-via.pdf"
pdf_filename: hung-2019-musical-composition-style-transfer-via.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

Two autoencoder designs learn a timbre code and a pitch code from ordinary audio–MIDI pairs — one with separate encoders, one with a U-Net whose skip connections carry the pitch — so that re-orchestrating a recording becomes swapping one code, which a 40-person listening study judged better than a generic image-style-transfer baseline.

## 1. Document Information

- **Canonical citation:** Yun-Ning Hung, I-Tung Chiang, Yi-An Chen, and Yi-Hsuan Yang, “Musical Composition Style Transfer via Disentangled Timbre Representations,” arXiv:1905.13567v1 [eess.AS; cs.SD], 30 May 2019, 7 PDF pages. The arXiv comment states acceptance at the 28th International Joint Conference on Artificial Intelligence (IJCAI 2019); the PDF carries no proceedings header, so venue status rests on that metadata.
- **Affiliations:** Research Center for IT Innovation, Academia Sinica; KKBOX Inc., Taiwan. [PDF p. 1]
- **DOI:** `10.48550/arXiv.1905.13567` (arXiv DOI; the IJCAI proceedings DOI is not in the read text).
- **Artifacts:** code at `https://github.com/biboamy/instrument-disentangle`; demo at `https://biboamy.github.io/disentangle_demo/`. [PDF p. 2, p. 6]
- **Integrity note:** the arXiv metadata carries an admin note that the text overlaps with arXiv:1811.03271, an earlier paper by the same group. This record treats the overlap as declared and does not attempt to quantify it.
- **Canonical integrity:** SHA-256 `807ac47837222e30b37ccd8140214bd77430b00496922c53207f9dde8fdf58c5`.
- **Rights boundary:** arXiv preprint; terms follow the arXiv licence, not restated here. Local research evidence only.
- **Primary category:** `generation-and-planning`. The task is arrangement/style transfer; disentanglement is the method, not the deliverable.
- **Evidence levels:** Table 1 was mis-transcribed in the earlier batch digest — the instrument-activity-detection rows for Gururani et al. and for DuoED were swapped, and DuoED's average is 0.815 while Gururani's is 0.817. This record follows the rendered table.

## 2. Key Contributions

### Composition style transfer defined as arrangement

The paper separates *what* is played (pitch content: melody and harmony) from *how* it is orchestrated (instrument timbre), and treats rearrangement as keeping the first and replacing the second. Paired orchestration data is scarce, so it asks whether the factors can be separated from ordinary aligned audio–MIDI pairs. [PDF pp. 1–2]

### Two disentanglement designs

**DuoED** has separate timbre and pitch encoders with three decoders (pianoroll, instrument roll, pitch roll) and adversarial losses that push pitch information out of the timbre code and vice versa. **UnetED** has a single encoder and a U-Net pianoroll decoder whose skip connections carry the pitch information, so the latent has no legitimate route to pitch and can be pushed to be timbre-only by a fooled pitch classifier. [PDF pp. 3–4]

### A symbolic intermediate as the audit surface

The output is an explicit multi-track pianoroll, which is re-synthesised. The arrangement decision — which instrument plays which notes — is therefore visible before audio is rendered, in contrast to end-to-end audio style transfer. [PDF pp. 3–4, Fig. 4]

## 3. Methodology and Architecture

- **Input.** Constant-Q transform of 16 kHz audio, 512-sample window, 88 bins at 12 per octave, 10-second chunks, giving 88 × 312 frames. CQT is chosen over the short-time Fourier transform for its logarithmic pitch scale and low-frequency resolution. [PDF p. 3]
- **Targets.** A multi-track binary pianoroll (88 × T × M), plus instrument roll (M × T) and pitch roll (88 × T) obtained by summing the pianoroll along the appropriate axis. [PDF p. 3, Fig. 2]
- **DuoED losses.** Binary cross-entropy for pianoroll, instrument roll and pitch roll; adversarial terms feed the wrong code to each classifier (timbre code to the pitch decoder and pitch code to the timbre decoder) and update only the encoders, so decoders keep their predictive function. [PDF p. 3]
- **UnetED losses.** Cross-entropy for the pianoroll through the U-Net decoder, a timbre classifier on the latent, and a GAN-like pitch classifier that the encoder is trained to fool; skip connections supply the pitch the roll needs. [PDF p. 4]
- **Style transfer.** Encode source A for content (pitch code or skip path), take the timbre code from target clip B, decode to a new pianoroll, then synthesise audio. [PDF p. 4]
- **Training data.** MuseScore dataset, 344,166 paired MIDI/MP3 files, time-aligned; fully convolutional models with four residual blocks per encoder, twelve layers in encoder and pianoroll decoder, SGD with momentum 0.9 and learning rate 0.005. [PDF pp. 4–5]
- **Evaluation.** Instrument activity detection on the MedleyDB+Mixing Secret (M&M) test split of 69 songs, per-second AUC for five instruments, with a paired t-test against the strongest baseline; and a listening study on rearrangement. [PDF pp. 5–6]

## 4. Key Results and Benchmarks

**Instrument activity detection** (Table 1, per-second AUC) [PDF p. 5]:

| Method | Piano | Guitar | Violin | Cello | Flute | Avg |
|---|---|---|---|---|---|---|
| Hung & Yang 2018 | 0.690 | 0.660 | 0.697 | 0.774 | 0.860 | 0.736 |
| Liu et al. 2019 | 0.766 | 0.780 | 0.787 | 0.755 | 0.708 | 0.759 |
| Hung et al. 2019 | 0.718 | 0.819 | 0.682 | 0.812 | 0.961 | 0.798 |
| Gururani et al. 2018 | 0.733 | 0.783 | 0.857 | 0.860 | 0.851 | 0.817 |
| DuoED | 0.721 | 0.790 | 0.865 | 0.810 | 0.912 | 0.815 |
| UnetED | 0.781 | 0.835 | 0.885 | 0.807 | 0.832 | **0.829** |
| Hadad et al. 2018 (image transfer) | 0.745 | 0.807 | 0.816 | 0.769 | 0.883 | 0.804 |
| Liu et al. 2018a (image disentanglement) | 0.808 | 0.844 | 0.789 | 0.766 | 0.710 | 0.793 |

UnetED's average is significantly better than Gururani et al. (paired t-test, p < 0.05), but it loses on flute and cello, so the timbre code is not uniformly better per instrument. [PDF p. 5]

**Ablation** (Table 2, MuseScore only, no M&M fine-tuning) [PDF p. 5]: instrument-roll AUC is 0.731 (DuoED without adversarial), 0.741 (DuoED with), 0.733 (UnetED without), 0.754 (UnetED with). Summing the predicted pianoroll gives 0.778–0.783, higher than the timbre decoder alone, which the authors read as pitch information helping the instrument estimate.

**Listening study** (40 participants, 18 with composition experience; 12 source–target pairs; four-point Likert ratings of rhythmicness, harmonicity and overall quality) [PDF p. 6]: UnetED is rated better than DuoED on all three dimensions, adversarial training improves rhythmicness and harmonicity over the ablated UnetED, and the image-style-transfer baseline fails badly — it loses pitch content and produces empty tracks. Participants with a music background rate slightly lower but rank the systems the same way.

## 5. Limitations and Future Work

- **Dated scale and material.** Five instruments, 10-second chunks, synthesised MuseScore audio, 2019-era architectures; no modern baselines. [PDF pp. 4–5]
- **Detection is a surrogate.** High instrument-activity AUC does not prove the timbre code is pitch-free; only the rearrangement study touches the intended use.
- **Subjective task, no objective pitch metric.** Style transfer has no ground truth, and the paper reports no objective measure of pitch preservation in the rearranged pianorolls. [PDF p. 6]
- **Synthesiser-bounded audio.** Quality is limited by rendering the predicted pianoroll, not by the model's audio generation. [PDF p. 4]
- **No playing-technique modelling.** The pianoroll carries notes and instruments but not articulation or expression. [PDF pp. 3–4]
- **Adversarial training is unstable by nature** and no seed variance or repeated runs are reported. [PDF p. 5]
- **Unseen instruments and real recordings are untested.** The authors' stated future work is more instrument categories and singing voice. [PDF p. 6]

## 6. Related Work

- **Disentanglement as an explainability device.** Naming “what is played” and “how it is orchestrated” as separate codes makes each inspectable; this is the representation-level complement to the workflow transparency discussed in [[concepts/auditable-creative-editing-pipelines]].
- **Work identity versus performance.** The pitch/timbre split is an early version of the distinction between a work and its realisation that this repository uses for identity claims; see [[concepts/work-identity-versus-performance-variation]].
- **Modern timbre and style transfer.** [[generation-and-planning/cheng-2026-musetimbre-zero-shot-timbre-transfer]] performs zero-shot timbre transfer by controlling a frozen generator, the current-generation alternative to learned disentangled codes.
- **Arrangement and recombination.** [[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] and [[retrieval-and-recombination/davies-2014-automashupper-automatic-creation-of-multi]] recombine existing material; this paper instead re-orchestrates it, with an explicit symbolic intermediate that could be audited.
- **Symbolic analogue.** [[concepts/expression-aware-symbolic-representations]] describes the symbolic-side version of separating content from expression/instrumentation.

## 7. Glossary

- **AUC:** Area Under the ROC Curve.
- **BCE:** Binary Cross-Entropy.
- **CQT:** Constant-Q Transform.
- **DuoED:** Dual Encoder–Decoder model.
- **GAN:** Generative Adversarial Network.
- **IAD:** Instrument Activity Detection.
- **IJCAI:** International Joint Conference on Artificial Intelligence.
- **M&M:** MedleyDB + Mixing Secret evaluation corpus.
- **MIDI:** Musical Instrument Digital Interface.
- **SGD:** Stochastic Gradient Descent.
- **UnetED:** U-Net Encoder–Decoder model.
