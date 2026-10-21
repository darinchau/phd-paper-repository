---
title: "PianoBind: A Multimodal Joint Embedding Model for Pop-piano Music"
authors: "Hayeon Bang, Eunjin Choi, Seungheon Doh, and Juhan Nam"
year: 2025
doi: 10.48550/arXiv.2509.04215
source: bang-2025-pianobind-a-multimodal-joint.md
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bang-2025-pianobind-a-multimodal-joint.pdf"
pdf_filename: bang-2025-pianobind-a-multimodal-joint.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [piano, multimodal-embedding, audio, midi, text, retrieval, piast, domain-specific]
---

# PianoBind: A Multimodal Joint Embedding Model for Pop-piano Music

## Summary

PianoBind is a domain-specialised alternative to CLaMP 3. It aligns audio (ResNet-50 on mel spectrograms), symbolic piano (MidiBERT), and text (RoBERTa) in a 512-dimensional space using audio–text and MIDI–text InfoNCE, and averages audio and MIDI item embeddings at retrieval. Trained on PIAST's 900-hour weak YouTube set plus 17 hours of expert annotations, it reaches median rank 10 on in-domain and out-of-domain piano retrieval, versus 39 and 12 for CLaMP 3. The result supports two claims: sequential pretrain-then-finetune beats mixing a large noisy set with a small clean one, and joint training is a precondition for useful inference-time fusion. The evaluation is small and pop-piano only.

## Key Contributions

- Trimodal piano embedding with a pretrained symbolic encoder and an audio encoder, avoiding the text-bridge detour.
- Sequential multi-source training (weak pretraining → expert finetuning) clearly beats mixed batches in this low-resource regime.
- Inference-time audio+MIDI fusion improves retrieval only when the encoders were jointly trained; fusion of separately optimised CLaMP 3 variants degrades performance.
- Strong in-domain and out-of-domain retrieval with orders of magnitude less training data than general-purpose models.

## Methodology and Architecture

PIAST-YT (7,367 tracks, ~900 h) provides weak audio–text pairs; PIAST-AT (1,986 tracks, ~17 h) provides expert 31-tag annotations. MIDI is transcribed from audio and downbeat-synchronised. Encoders: ResNet-50 over 128-band log-mel (20 s, 16 kHz); MidiBERT over compound-word tokens (bar/position/pitch/duration), mean-pooled; RoBERTa over BPE text, mean-pooled. All map to 512-d and are L2-normalised. Loss: symmetric InfoNCE averaged over audio–text and MIDI–text; no audio–MIDI term because the MIDI is derived from the audio. Training: AdamW, lr 5e-5, batch 64, one A6000, dynamic text dropout. Two strategies compared: mixed 7:3 batches, or pretrain on YT then finetune on AT. Evaluation: text→music retrieval on 199 PIAST-AT tracks and 88 EMOPIA-Caps tracks.

## Results

| Setting | PianoBind | Best baseline | Anchor |
|---|---:|---:|---|
| In-domain R@10 | 52.76 | 14.57 (CLaMP 3_c2sa) | Table 2, p. 4 |
| In-domain MedR | 10 | 39 (CLaMP 3_c2sa) | Table 2, p. 4 |
| Out-of-domain R@10 | 51.28 | 46.15 (CLaMP 3_c2sa) | Table 2, p. 4 |
| Out-of-domain MedR | 10 | 12 (CLaMP 3_c2sa) | Table 2, p. 4 |
| Mixed vs sequential (trimodal, ID R@10) | 37.68 vs 52.76 | — | Table 1, p. 4 |
| Averaged loss vs saas (ID R@10) | 52.76 vs 13.56 | — | Table 3, p. 4 |

The baselines are general-purpose and were not trained on PIAST, so part of the gap is domain specialisation rather than architecture. The test sets are small (199 and 88 items), and no confidence intervals are reported. The paper does not evaluate note-level alignment, same-work performance matching, or transformation robustness.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the joint-embedding route in its domain-specialised, small-data form.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — the general-purpose text-bridged system PianoBind outperforms on piano.
- [[retrieval-and-recombination/fernandez-mendez-2026-descriptor-injected-cross-modal-learning]] — direct audio–MIDI alignment instead of text-mediated alignment.
- [[concepts/transcription-as-supervision]] — PIAST MIDI is AMT output, so the symbolic branch inherits transcription errors.
- [[data-and-representation/huang-2025-musetok-symbolic-music-tokenization-for]] — another piano-specific representation with understanding probes.
