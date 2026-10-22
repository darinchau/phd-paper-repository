---
title: "SMART: Tuning a symbolic music generation system with an audio domain aesthetic reward"
authors: Nicolas Jonason, Luca Casini, Bob L. T. Sturm
year: 2025
doi: 10.48550/arXiv.2504.16839
source: jonason-2025-smart-tuning-a-symbolic-music.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/jonason-2025-smart-tuning-a-symbolic-music.pdf"
pdf_filename: jonason-2025-smart-tuning-a-symbolic-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [audio-reward, reinforcement-learning, symbolic-generation, grpo]
---

## Summary

SMART renders a piano MIDI generator's outputs to audio, scores them with Meta Audiobox Aesthetics, and fine-tunes the generator with GRPO. A 14-participant pilot finds a significant rating gain (+1.22 points, p = 0.002), and the outputs shift toward more notes, wider pitch and velocity ranges, and fewer empty beats. Aggressive optimisation raises the proxy reward while collapsing diversity, which makes the paper both a template for audio-grounded symbolic tuning and a warning about proxy rewards.

## Key Contributions

- Audio-domain reward tuning for a symbolic generator, with no symbolic preference model. [§3]
- A behavioural profile of the tuned model (notes, polyphony, empty beats, pitch range, velocity). [§5.1]
- Preliminary human evidence of improved listener ratings. [§4]
- A documented diversity collapse under over-optimisation. [§5.2]

## Methodology and Architecture

A base piano MIDI model is trained on a large MIDI corpus. GRPO samples completions, renders them with a fixed soundfont, obtains MAA scores, and updates the policy against a frozen reference. The main condition runs 200 steps with β = 0.04; a 1000-step, β = 0.0 condition probes over-optimisation.

## Results

- Listener ratings: +1.22 points on average, p = 0.002, 14 participants and 407 usable ratings. [§4]
- Post-tuning outputs have more notes, higher polyphony, zero empty-beat rate, wider pitch/velocity ranges, and lower mean velocity. [§5.1]
- MAA scores of tuned outputs often exceed MAA scores of real performances, which the authors interpret as a proxy-validity warning, not as superiority. [§5.1]
- 1000-step optimisation increases reward while making average piano rolls repetitive. [§5.2, Fig. 6]

The paper measures output aesthetics and feature shifts, not what the symbolic model internally learned; there is no probe, no note-level attribution, and no test of whether the gain survives outside the reward model's biases.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — audio-grounded symbolic generation and the attribution gap.
- [[overviews/cross-modal-supervision-transfer]] — audio-derived signals as supervision for symbolic models.
- [[generation-and-planning/yu-2026-midi-repa-improving-text-to-music]] — the reverse direction, symbolic alignment improving audio generation.
