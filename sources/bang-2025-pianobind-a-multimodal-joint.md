---
title: "PianoBind: A Multimodal Joint Embedding Model for Pop-piano Music"
authors: "Hayeon Bang, Eunjin Choi, Seungheon Doh, and Juhan Nam"
year: 2025
doi: 10.48550/arXiv.2509.04215
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/bang-2025-pianobind-a-multimodal-joint.pdf"
pdf_filename: bang-2025-pianobind-a-multimodal-joint.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# PianoBind: A Multimodal Joint Embedding Model for Pop-piano Music

## One-line Summary

PianoBind trains audio, MIDI (MidiBERT), and text (RoBERTa) encoders into a shared 512-dimensional space on the PIAST pop-piano corpus, using audio–text and MIDI–text contrastive losses plus averaged audio+MIDI item embeddings at retrieval; it beats general-purpose models on in-domain and out-of-domain piano retrieval despite far less data, with median rank 10 versus 39 for CLaMP 3.

## 1. Document Information

- **Authors and affiliation:** Hayeon Bang, Eunjin Choi, Seungheon Doh, Juhan Nam; Graduate School of Culture Technology, KAIST.
- **Venue and version:** ISMIR 2025; arXiv 2509.04215v1, 4 September 2025. 8 PDF pages: content pp. 1–5, references pp. 6–8.
- **Extraction:** full text via `pdftotext -layout`; Figure 2 (training strategies), Tables 1–3, and §6 inspected.
- **Artifacts:** code, weights, and demo at `https://hayeonbang.github.io/PianoBind/`.
- **Anchors:** architecture §3.1 pp. 2–3; training strategies §3.2 p. 3; dataset §4.1 p. 3; results Table 1 p. 4; comparison Table 2 p. 4; design ablation Table 3 p. 4.

## 2. Key Contributions

1. **A piano-specific trimodal embedding** combining audio, symbolic MIDI, and text, where the symbolic branch is a pretrained MidiBERT and the text branch is RoBERTa.
2. **Two multi-source training strategies** for a small expert-annotated set plus a large weakly aligned set: mixed batch training versus pretraining on the weak set then finetuning on the expert set. The sequential strategy wins consistently.
3. **Multimodal item embeddings at inference**: averaging audio and MIDI embeddings improves retrieval, but only when the encoders were jointly trained.
4. **Evidence that domain specialisation beats general scale** on homogeneous piano data: PianoBind outperforms CLaMP 2/CLaMP 3 and CLAP/TTMR++ on both PIAST-AT (in-domain) and EMOPIA-Caps (out-of-domain).

## 3. Methodology and Architecture

- **Data.** PIAST-YT: 7,367 tracks (~900 h) of YouTube pop piano with metadata-derived text (weak alignment). PIAST-AT: 1,986 tracks (~17 h, 30 s excerpts) with expert tags across 31 genre/mood/style categories (strong alignment). MIDI for both is produced by automatic piano transcription and downbeat-synchronised; melody/chord features are extracted. EMOPIA-Caps is the out-of-domain set (88 tracks), with GPT-4o-paraphrased captions reviewed by a music expert.
- **Encoders.** Audio: modified ResNet-50 over 128-band log-mel spectrograms, 20 s at 16 kHz, MusCALL-style stem layers, blur pooling, downsampling. Symbolic: MidiBERT with Compound Word tokens (bar, position, pitch, duration); mean-pooled last hidden state because there is no CLS token. Text: RoBERTa with BPE, mean-pooled final layer. All project to 512 dimensions and are L2-normalised.
- **Objective.** Symmetric InfoNCE for audio–text and MIDI–text; the total is their average. Audio–MIDI contrastive loss is deliberately omitted because the MIDI is transcribed from the same audio and would add little semantic distinction.
- **Training.** AdamW, lr 5e-5, weight decay 0.2, batch 64, one A6000. Dynamic text dropout mixes available tags/captions in random order. Combined training samples PIAST-YT:PIAST-AT at 7:3; the alternative is pretrain on YT then finetune on AT.
- **Inference fusion.** Average the audio and MIDI embeddings for the item representation; query with the text embedding.

## 4. Key Results and Benchmarks

**In-domain (PIAST-AT, 199 tracks; Table 2, p. 4).** PianoBind's best trimodal model reaches Median Rank 10 and R@10 52.76, versus CLaMP 3_c2sa Median Rank 39 and R@10 14.57, and CLaMP 3_saas R@10 12.31. Audio-only and symbolic-only variants are worse (MedR 15 and 12; R@10 42.71 and 45.23).

**Out-of-domain (EMOPIA-Caps, 88 tracks; Table 2, p. 4).** PianoBind reaches R@10 51.28 and MedR 10, versus 46.15 and 12 for the best CLaMP 3 variant. The absolute numbers are low because the test set is small and the captions are free-form.

**Training strategy (Table 1, p. 4).** Pretrain-then-finetune beats mixed training across configurations; e.g. in-domain trimodal R@10 52.76 vs 37.68, out-of-domain 51.28 vs 46.15. The interpretation is that the 900-hour noisy set can overwhelm the 17-hour expert set in mixed batches.

**Loss design (Table 3, p. 4).** Averaged audio–text/MIDI–text loss beats the CLaMP 3_saas staged alignment: in-domain R@10 52.76 vs 13.56, out-of-domain 52.76 vs 41.03; the authors' reimplementation of saas (Ours_saas) reaches 33.66/30.77, so the comparison is not purely against the published model.

**What is not shown.** No listening test, no note-level alignment, no source-identity or transformation evaluation, and no test on classical piano. Retrieval here means "find the 20-second excerpt matching a caption", not "align two performances of the same work" or "decide whether two pieces can be mashed up".

## 5. Limitations and Future Work

- **Small, narrow evaluation.** 199 in-domain and 88 out-of-domain tracks; pop-piano only; no classical, jazz, or multi-instrument material.
- **Transcribed MIDI.** The symbolic branch learns from AMT output, so transcription errors are baked into the "symbolic" modality. The paper does not ablate against score-derived MIDI.
- **Caption quality.** PIAST-YT text is weak/metadata-derived; EMOPIA-Caps is LLM-paraphrased and expert-reviewed but still synthetic. Retrieval may reward caption style as much as musical content.
- **Global embeddings.** Like CLaMP 3, one vector per 20-second excerpt; temporal structure and note-level evidence are not represented.
- **No explanation.** Fusion weights are fixed averages, not learned or inspected; there is no attribution of a retrieval decision to notes, instruments, or words.

## 6. Related Work

- MuLan, MusCALL, CLAP, TTMR/TTMR++: audio–text joint embeddings.
- CLaMP, CLaMP 2, CLaMP 3: symbolic–text and trimodal retrieval.
- MidiBERT-Piano and PianoBART: symbolic piano pretraining.
- PIAST and EMOPIA: the multimodal piano datasets.
- AudioCLIP: the multi-pair contrastive template.

## 7. Glossary

- **MIR:** Music Information Retrieval.
- **InfoNCE:** Information Noise-Contrastive Estimation loss.
- **BPE:** Byte-Pair Encoding.
- **PIAST:** Piano dataset with Audio, Symbolic, and Text.
- **EMOPIA:** Emotion-based pop-piano dataset.
- **AMT:** Automatic Music Transcription.
- **R@K / MedR:** Recall at K / Median Rank.
