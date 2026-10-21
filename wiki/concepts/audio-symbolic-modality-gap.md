---
title: "The Audio–Symbolic Modality Gap"
tags: [audio, midi, cross-modal, contrastive-learning, representation, alignment, modality-gap]
---

# The Audio–Symbolic Modality Gap

Audio is a continuous waveform shaped by timbre, room, recording chain, and performance nuance. Symbolic music is a discrete event sequence of pitch, onset, duration, velocity, and instrument. Matching them requires deciding which aspects of the waveform are musically relevant and which are recording artefacts. The "modality gap" is the empirical fact that naive contrastive training on matched pairs converges slowly and yields weak retrieval, because the two encoders start from different statistics and the shared information is a small part of each signal.

## Why the Gap Is Hard

- **Different invariances.** A symbolic encoder naturally ignores timbre and room; an audio encoder naturally encodes them. Contrastive learning must learn to discard exactly the information that dominates the audio embedding.
- **Many-to-one mapping.** One score can be rendered by many instruments, tempi, articulations, and rooms. A paired audio–MIDI sample is one point in a large set of valid realisations, so an invariance objective can pull the symbolic embedding toward recording-specific detail.
- **Temporal resolution.** Symbolic events are sparse and precise; audio frames are dense and blurred. Global pooling (one vector per piece) destroys the correspondence even when the encoders are good.
- **Label asymmetry.** Audio has no explicit note boundaries; MIDI has exact ones. The pairing is only as good as the alignment/transcription that produced it.

## Measured Evidence

- **CLaMP 3** aligns audio and symbolic through text rather than direct pairs. Its emergent audio↔symbolic retrieval reaches MRR 0.031–0.058 against a random baseline of 0.0075, while symbolic↔symbolic reaches 0.31–0.53. The gap is roughly an order of magnitude. The authors call the alignment "relatively weak" and recommend paired data.
- **Descriptor injection** on MAESTRO raises audio–MIDI retrieval from 73.4% to 84.0% with an eight-band spectral-dynamics descriptor, and zeroing that descriptor collapses performance by 75–78 points. This shows that a hand-crafted spectral prior can dominate the alignment, but the same model fails under transposition/velocity perturbation (S < 18%), so the alignment is brittle.
- **PianoBind** avoids direct audio–MIDI contrastive learning: it aligns each modality to text and fuses at inference. It works well for retrieval but does not produce a note-level audio–symbolic correspondence.
- **Spectrogram diffusion** shows the inverse direction: the note-token model can reach the spectrogram inverter's ceiling (transcription F1 0.36), while raw audio allows 0.63. The bottleneck is the audio representation, not the note sequence.

## What Would Count as Closing It

A useful audio–symbolic space should support, at minimum: same-work retrieval across instruments and recordings; localisation of a motif or a conflicting note; robustness to transposition, tempo, and timbre; and a calibrated notion of uncertainty. Current systems provide global retrieval, not localisation, and none reports all four. Text-bridged alignment is a pragmatic workaround, not evidence that the modalities share a fine-grained representation.

## Related Pages

- [[overviews/audio-symbolic-transfer]] — the four routes and where the gap bites.
- [[concepts/transcription-as-supervision]] — the label chain that produces most paired data.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — text-bridged alignment and its measured weakness.
- [[retrieval-and-recombination/fernandez-mendez-2026-descriptor-injected-cross-modal-learning]] — descriptor injection and its brittleness.
- [[retrieval-and-recombination/bang-2025-pianobind-a-multimodal-joint]] — domain-specific trimodal retrieval.
- [[generation-and-planning/hawthorne-2022-multi-instrument-music-synthesis-with]] — the inverse mapping and its audio-side ceiling.
