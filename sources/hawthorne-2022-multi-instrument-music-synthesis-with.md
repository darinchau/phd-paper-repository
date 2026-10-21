---
title: "Multi-instrument Music Synthesis with Spectrogram Diffusion"
authors: "Curtis Hawthorne, Ian Simon, Adam Roberts, Neil Zeghidour, Josh Gardner, Ethan Manilow, and Jesse Engel"
year: 2022
doi: 10.48550/arXiv.2206.05408
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hawthorne-2022-multi-instrument-music-synthesis-with.pdf"
pdf_filename: hawthorne-2022-multi-instrument-music-synthesis-with.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Multi-instrument Music Synthesis with Spectrogram Diffusion

## One-line Summary

A T5-style encoder-decoder maps MT3 note tokens for arbitrary instrument combinations to 5.12-second mel-spectrogram segments, with a diffusion decoder conditioned on the previous segment and a GAN spectrogram inverter; it renders multi-instrument MIDI slightly faster than real time and beats an autoregressive decoder on FAD and reconstruction, though final fidelity is bounded by the inverter.

## 1. Document Information

- **Authors and affiliations:** Curtis Hawthorne, Ian Simon, Adam Roberts, Neil Zeghidour, Josh Gardner, Ethan Manilow, and Jesse Engel; Google Research Brain Team and University of Washington/Northwestern.
- **Venue and version:** ISMIR 2022; arXiv 2206.05408v3, 12 December 2022. 12 PDF pages: content pp. 1–6, references pp. 6–12.
- **Extraction:** full text via `pdftotext -layout`; Figure 1 (architecture), Figure 2 (diffusion), Table 1, and per-dataset appendix tables inspected.
- **Artifacts:** code and pretrained models at `https://github.com/magenta/music-spectrogram-diffusion`; audio examples in the online supplement.
- **Anchors:** architecture §3 pp. 2–4; diffusion decoder §3.2 p. 3; datasets §4 p. 4; metrics §5.1 p. 4; results Table 1 p. 4; conclusion §6 p. 5.

## 2. Key Contributions

1. **The inverse of MT3.** The same MIDI-like note-token vocabulary used for transcription is used for synthesis, so a single model can train on any paired audio/MIDI dataset regardless of instrument combination.
2. **A diffusion decoder for continuous spectrograms**, with segment-level autoregressive conditioning on the previously generated 5.12 s segment to avoid boundary artifacts.
3. **A two-stage real-time pipeline**: MIDI → mel spectrogram (transformer) → waveform (GAN inverter), with note-level control of composition and instrumentation.
4. **Quantitative comparison** showing diffusion beats an autoregressive spectrogram decoder on FAD and reconstruction at matched capacity, and that the base model is slightly faster than real time.

## 3. Methodology and Architecture

- **Input.** MT3 note events (instrument, pitch, velocity, onset, offset, with ties) for any number of instruments; all MIDI programs are mapped to 34 Slakh instrument classes plus drums.
- **Synthesis model.** T5.1.1 encoder-decoder. The note encoder has 2,048 positions; an optional context encoder takes 256 frames of the previous spectrogram segment. The decoder has 256 output positions, each 20 ms, so each segment is 5.12 s. Cross-attention concatenates note and context encoder outputs.
- **Diffusion decoder.** The decoder is trained as a DDPM: input is noised spectrogram, conditioning is note tokens + previous segment; the target is the added Gaussian noise, with an L1 loss and logSNR/cosine schedule. 1,000 reverse steps at inference; classifier-free guidance with 0.1 conditioning dropout and weight 2.0. FiLM injects the diffusion-time embedding at each layer.
- **Autoregressive baseline.** The same architecture with causal masking and MSE on continuous frames, plus fixed-variance dithering at sampling.
- **Vocoder.** A MelGAN-style GAN spectrogram inverter trained on 16k hours of uncurated music; STFT hop 320 (20 ms), frame 640, 128 log-mel bins, 16 kHz.
- **Data.** MAESTRO (piano), Slakh2100 (synthetic multi-instrument), Cerberus4 (synthetic), GuitarSet, MusicNet, URMP; MT3 preprocessing and splits, including Slakh's 10 random instrument subsets per track.

## 4. Key Results and Benchmarks

**Aggregate (Table 1, p. 4).** Mean over evaluation datasets.

| Model | VGGish recon. ↓ | VGGish FAD ↓ | TRILL recon. ↓ | TRILL FAD ↓ | Transcription F1 ↑ | RT factor |
|---|---:|---:|---:|---:|---:|---:|
| Small autoregressive | 3.70 | 1.03 | 7.27 | 0.39 | 0.31 | 10.55 |
| Small, no context | 3.49 | 1.07 | 6.16 | 0.46 | 0.31 | 2.82 |
| Small, with context | 3.56 | 1.10 | 6.40 | 0.53 | 0.25 | 3.07 |
| Base, with context | 3.13 | 1.00 | 2.74 | 0.27 | 0.36 | 1.05 |
| Ground truth, encoded | 2.14 | 0.51 | 1.54 | 0.05 | 0.36 | 12.25 |
| Ground truth, raw | 0.00 | 0.00 | 0.00 | 0.00 | 0.63 | — |

Lower recon./FAD is better; higher transcription F1 and RT factor (faster than real time when >1) are better. The base diffusion model is best on TRILL FAD/reconstruction and matches the encoded ground truth's transcription F1 (0.36), which is the inverter ceiling; raw audio allows 0.63. The autoregressive baseline is not catastrophic but is consistently worse; segment context fixes boundary artifacts that the small model shows without it.

**Qualitative.** The model reproduces fret/picking noise on GuitarSet and breath/vibrato on URMP, and renders plausible velocities despite velocity tokens being reduced to on/off. Occasional loudness inconsistency and artifacts remain; fidelity does not match the training audio.

**What is not measured.** No listening test, no musicality rating, no comparison with a real synthesizer/soundfont, and no note-level error analysis beyond transcription F1. The "real-time" claim is about the base model on the authors' hardware, not a general deployment guarantee.

## 5. Limitations and Future Work

- **Inverter ceiling.** The spectrogram inverter bounds audio quality; the encoded-ground-truth row shows that even perfect synthesis of the mel representation cannot exceed 0.36 transcription F1, while raw audio reaches 0.63.
- **Segment boundaries and long-term consistency.** Context conditioning mitigates but does not solve timbre/loudness drift across segments; the model samples a different realization for each segment.
- **Underspecified synthesis.** The same notes can be dry or reverberant, synthetic or real, with or without vibrato; the model samples from that space rather than following a style control.
- **Instrument mapping.** 34 Slakh classes plus drums lose timbral detail and some GM distinctions.
- **No perceptual validation.** FAD and transcription F1 are proxies; the paper's claim of expressive synthesis rests on examples.
- **Compute and data.** Training on six datasets and 16k hours of uncurated audio is not a small-lab recipe.

## 6. Related Work

- MT3: the note-token vocabulary and multi-instrument transcription precedent.
- WaveNet, SampleRNN, Jukebox, AudioLM, SoundStream: waveform and codec-based synthesis.
- DDSP and MIDI-DDSP: interpretable, instrument-specific synthesis with fine control.
- Tacotron: the spectrogram-then-vocoder two-stage template.
- MelGAN: the spectrogram inverter.
- DDPM, Imagen, classifier-free guidance: the diffusion machinery.

## 7. Glossary

- **MIDI:** Musical Instrument Digital Interface.
- **DDPM:** Denoising Diffusion Probabilistic Model.
- **FAD:** Fréchet Audio Distance.
- **GAN:** Generative Adversarial Network.
- **MT3:** Multi-Task Multitrack Music Transcription.
- **mel spectrogram:** a log-compressed time–frequency representation on a perceptual frequency scale.
- **RT factor:** real-time factor; >1 means faster than real time.
