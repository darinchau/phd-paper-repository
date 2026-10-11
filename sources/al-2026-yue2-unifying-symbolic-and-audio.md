---
title: "YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality"
authors: "Ruibin Yuan et al."
year: 2026
doi: 10.48550/arXiv.2609.33757
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-yue2-unifying-symbolic-and-audio.pdf"
pdf_filename: al-2026-yue2-unifying-symbolic-and-audio.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

YuE2 factorizes generation into an inspectable symbolic score, semantic tokens, and acoustic realization. It demonstrates score-guided editing and source-identity retrieval, but its 3.58B-scale, partly licensed data regime is not modestly reproducible and the score is not itself a faithful explanation.

## 1. Document Information

- **Canonical source:** arXiv `2609.33757v1`; official PDF preserved as `al-2026-yue2-unifying-symbolic-and-audio.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40l1x5_c3k5.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### YuE2 digest

### 1. Bibliography and artifact status

**Ruibin Yuan et al.**, “**YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality**,” *YuE2 Technical Report*, arXiv:**2609.33757v1 [eess.AS]**, submitted **27 September 2026**. The core contributors include Ruibin Yuan, Jiahao Pan, Junyan Jiang, Zhiyue Wu, Ziya Zhou, Jiankai Sun, Yizhi Li, and Ge Zhang; corresponding authors are Wei Xue and Yike Guo. Full contributor list: **paper p.22**.

- GitHub: `https://github.com/multimodal-art-projection/YuE`
- Hugging Face: `https://huggingface.co/m-a-p/YuE2-3B`
- Demo: `https://map-yue2.github.io/`
- WildSongBench data/evaluation: linked in Appendix A.

Evidence: `/tmp/paper-digest/2609.33757v1.txt:1-15,1379-1466`.

**License/reproducibility caveat.** The report says training is primarily on CC0 music and synthetic data, but “most” synthetic data are supplied by Tokenwave.AI **under license**. The report does not provide a complete freely reproducible corpus or state a single permissive license for all model weights, code, annotations, or data. The linked artifacts must therefore be checked separately before redistribution.

Evidence: `/tmp/paper-digest/2609.33757v1.txt:2449-2455`.

---

### 2. Central idea

YuE2 factorizes generation as:

\[
p(s,c,z\mid y)=p_{\mathrm{AR}}(s,c\mid y)\,p_{\mathrm{NAR}}(z\mid y,s,c)
\]

where:

- \(y\): text/style prompt and lyrics;
- \(s\): readable symbolic score in ABC notation;
- \(c\): 25-Hz discrete semantic music tokens;
- \(z\): 25-Hz, 64-dimensional continuous acoustic latents;
- waveform: decoded by a separately trained 48-kHz stereo VAE.

The model first writes melody, chords, key, meter, tempo, sections, and voices, then realizes performance and production detail in audio.

The symbolic score is **inspectable and editable**, but it is not a formal explanation of why the model made a musical decision. This distinction matters for explainable AI.

Evidence: **§§2.1–2.4, pp.3–5**; `/tmp/paper-digest/2609.33757v1.txt:170-317`.

---

### 3. Architecture and training scale

#### YuE2

The main model has approximately **3.58 billion parameters**:

- 28 Transformer layers;
- hidden width 2,048;
- feed-forward width 6,144;
- 16 query heads, 8 key/value groups, head width 128;
- 24,576-position context;
- 151,643-entry text vocabulary;
- 32,768-entry semantic vocabulary;
- bfloat16 training;
- RMSNorm and SwiGLU.

Each layer contains separate AR and NAR normalization, projections, and MLP experts around shared attention.

- Discrete score/semantic positions use causal attention.
- Acoustic positions use bidirectional attention.
- Acoustic prediction uses conditional flow matching.
- Joint objective: \(L=0.25L_{\mathrm{AR}}+L_{\mathrm{FM}}\).

Evidence: **§§2.3–2.4, Appendix C, pp.3–5 and 38–39**; `/tmp/paper-digest/2609.33757v1.txt:207-304,2474-2526`.

#### Training schedule

- YuE2 data: approximately **346,000 audio hours**.
- AR pretraining: **60,000 updates**.
- Joint AR-NAR training: **40,000 updates**.
- Annealing: **6,000 updates**.
- Global batch size: **256**.
- Context: up to 24,576 positions.
- Hardware: **64 NVIDIA H800 GPUs**.
- Optimizer: Adam; gradient clipping 1.0.
- Training precision: bfloat16.

The report also compares against a separate LM+DiT system with two approximately **1.7B-parameter** components, totaling **3.4B parameters**. Its DiT receives **900,000 updates**.

Evidence: `/tmp/paper-digest/2609.33757v1.txt:2489-2526,2997-3002`.

#### Four YuE2 training tasks

The same checkpoint is trained with:

1. score + semantic tokens;
2. semantic tokens without score;
3. score without semantic tokens;
4. direct audio generation without either.

This makes the planning/no-planning comparison possible without training separate YuE2 checkpoints.

Evidence: Appendix C, Table 14, `/tmp/paper-digest/2609.33757v1.txt:2499-2518`.

---

### 4. Data and annotation pipeline

YuE2 does not learn aligned symbolic/audio supervision from ordinary recordings directly. It constructs three frozen targets offline:

\[
x\rightarrow (s,c,z)
\]

#### MERT2

MERT2 supplies semantic targets.

- Input: 24-kHz mono audio.
- 128-bin log-mel frontend.
- 25-Hz sequence.
- 24-layer Conformer, width 1,024, FFN width 4,096, 16 heads.
- Multi-View Target Synthesis combines:
  - MuQ layer 7;
  - Qwen2-Audio-Instruct layer 32;
  - a learned fusion network;
  - four-level residual vector quantization.
- Separate branches use causal adaptation for generation and bidirectional context for analysis.
- Final semantic tokenizer: **32,768-entry CVQ**, **375 bits/s**.

Training data:

- **700,000 hours** for MERT2 foundation pretraining.
- Full-song adaptation uses recordings of 30–360 seconds.
- Four stages: foundation pretraining, full-song/causal adaptation, supervised fine-tuning, semantic quantization.

Evidence: **§3.1 and Appendix B.1–B.2, pp.5–8 and 33–34**; `/tmp/paper-digest/2609.33757v1.txt:319-360,2107-2177`.

#### SheetSage2

SheetSage2 supplies symbolic supervision:

- beat, downbeat, meter;
- key;
- chords;
- musical structure;
- vocal and instrumental melody.

SheetSage2-AR uses a frozen MERT2-FS encoder, low-rank adapters, and a six-layer RoFormer decoder. Training labels are generated by SheetSage2-Prober from:

- expanded SheetSage/Song lead-sheet data;
- POP909;
- HarmonixSet;
- MIDI AutoLabel Dataset;
- Segmented Lakh MIDI Subset;
- rendered MIDI audio.

SheetSage2-AR training corpus:

- **441,094 recordings**;
- **28,434 hours**;
- 884 validation recordings.

The model serializes attributes chronologically into a shared event vocabulary, then converts decoded events to ABC.

Evidence: Appendix B.3, `/tmp/paper-digest/2609.33757v1.txt:2202-2305`.

---

### 5. Main results

#### WildSongBench

Evaluation uses **192 prompts**, 15 genre buckets, 94 Chinese and 98 English prompts, with lyrics and multilingual/code-switched requests.

Standard selection: two candidates per prompt, with lowest phoneme error rate after four ASR transcriptions.

YuE2:

- SongBench Musicality: **5.9075**
- SongBench Global Avg: **6.7316**
- AudioBox PQ: **8.2598**
- Q3O prompt alignment: **4.6819**
- PER: **0.0844**

Best-of-8:

- Musicality: **6.2666**
- Global Avg: **6.9632**
- AudioBox PQ: **8.2714**
- Q3O: **4.7009**

The authors report YuE2 as best among evaluated public systems on SongBench Musicality and Global Avg. Best-of-8 has the highest observed mean across all evaluated systems on those metrics. These are author-reported comparative results, not evidence that the model universally matches proprietary systems.

Evidence: **§4.1, Tables 1–2, pp.9–11**; `/tmp/paper-digest/2609.33757v1.txt:559-645`.

#### Expert listening

The analysis snapshot contains:

- 351 participations;
- 289 online sessions;
- 62 paid experts with conservatory or audio-AI backgrounds;
- 4,439 retained pairwise evaluations overall;
- 3,602 expert evaluations in the reported expert comparisons.

For YuE2 best-of-8:

- preferred over Suno v4.5 overall: **57.3% vs 30.5%**;
- nearly balanced against Suno v5: **40.4% vs 39.9%**;
- Suno v6 preferred overall: **59.3% vs 31.6%**;
- average tie-adjusted audio-quality preference across six proprietary systems: **58.9%**, 95% CR1 CI 55.6–62.2%.

The best-of-8 result is partly a **selection-budget result**: eight generated candidates are ranked using SongBench Musicality, Q3O, and PER.

Evidence: **§4.1, Figure 7, Appendix D.4, pp.10–12 and 47–54**.

#### Planning ablation

Same checkpoint, prompts, lyrics, candidate budget, and decoder:

- overall: planning preferred **49.3%**, no planning **34.6%**;
- musicality: **45.0% vs 29.4%**;
- melody: **44.0% vs 29.5%**;
- chord progression: **39.0% vs 21.0%**.

Overall and musicality differences are statistically significant under the paper’s clustered CR1 protocol.

Evidence: **§4.2, Figure 8, Table 21, pp.11–12 and 51–54**; `/tmp/paper-digest/2609.33757v1.txt:730-850,3072-3139`.

#### Unified MoT versus separate LM+DiT

With the same symbolic planning and representations:

- overall: MoT preferred **53.4% vs 35.6%**;
- audio quality: **48.5% vs 29.6%**;
- text alignment: approximately balanced;
- preferences also favor MoT for musicality, vocals, and accompaniment.

This supports the authors’ claim that joint AR-NAR modeling is beneficial, but the comparison remains within one authors’ implementation and training recipe.

Evidence: **§4.3, Figure 10, pp.13–14**.

---

### 6. Score faithfulness, editing, and covers

#### Score-to-audio agreement

For corresponding score/audio pairs:

- melody similarity: **0.9464**;
- chord similarity: **0.9246**;
- rhythm F1: **0.9396**;
- exact key agreement: **0.9307**;
- tempo within 8%: **0.9869**;
- form content similarity: **0.7799**;
- section-boundary F1: **0.8724**.

Mismatched-score and no-score controls are dramatically lower. Correct score/audio assignment reached **100%** in the evaluable two-candidate assignment task.

Evidence: **§5.1, Table 3, Appendix D.1, pp.14 and 40–42**.

#### Editing

After editing the ABC score and regenerating the entire song:

- melody edit pitch accuracy: **84.17%**;
- harmony edit chord agreement: **79.54%**;
- rhythm edit relative-onset accuracy: **73.43%**;
- key edit weighted score: **90.58/100**;
- tempo edit accuracy: **95.68%**;
- unedited-content preservation: approximately **90.16–94.34%**.

The model therefore supports selective musical intervention, but regeneration is global and preservation is measured largely through automatic transcription.

Evidence: **§5.2, Table 4, Appendix D.2, pp.15 and 42–44**.

#### Zero-shot covers

Evaluation:

- 948 unseen SHS100K works;
- 3,792 outputs per YuE2 condition;
- retrieval gallery: 10,545 recordings;
- no cover-specific fine-tuning.

Full-score YuE2:

- CLEWS mAP: **0.647**;
- Discogs-VINet mAP: **0.288**;
- SongEcho: 0.419 and 0.122;
- without chords: 0.598 and 0.179;
- without score: 0.006 and 0.004.

Removing symbolic conditioning improves style adaptation and musicality but destroys work-identity retrieval. This is highly relevant to provenance: the score carries source identity, especially harmonic identity.

Evidence: **§5.3, Table 5, Appendix D.3, pp.16–17 and 44–46**.

---

### 7. MERT2 and SheetSage2 results

- MERT2-30s leads external baselines on **14 of 15 MARBLE metrics**.
- MERT2-FS leads or remains competitive, within 1.87 points of MERT2-30s across the reported metrics.
- At 375 bits/s, the MERT2 tokenizer leads **five of six** matched representation metrics.
- SheetSage2-AR leads **12 of 15** benchmark–metric pairs.
- SheetSage2-AR exceeds its own label generator on **10 of 15** pairs.

Important reproducibility qualification: several comparison baselines use published or released checkpoints, but some results are retrained or re-evaluated under protocol adjustments described in Appendix B.

Evidence: **§6, Tables 6–11, pp.18–21 and 33–37**.

---

### 8. What is genuinely transferable

#### Transferable ideas

1. **Progressive musical commitment:** separate composition, semantic performance, and acoustic realization.
2. **A score as an intermediate interface:** use a readable symbolic artifact between prompt and audio.
3. **Offline target construction:** derive symbolic and semantic supervision from recordings.
4. **Fixed-prefix rendering:** editing and covers can reuse the same score-to-audio model.
5. **Matched ablations:** compare planning/no-planning with the same checkpoint and decoder.
6. **Separate adherence from preservation:** measure whether an edit happened and whether protected material survived.
7. **Source-identity retrieval:** useful for evaluating provenance preservation.

#### Not realistically transferable at modest scale

- Training a 3.58B model on 346,000 hours with 64 H800s.
- Recreating MERT2 from 700,000 hours.
- Reproducing Tokenwave’s licensed synthetic corpus and Qwen3-Omni/SongFormer annotation pipeline.
- Claiming frontier audio quality from a small symbolic dataset.
- Treating best-of-8 automatic selection as a cheap substitute for model quality.
- Assuming ABC alone provides faithful explanations, conflict diagnosis, or provenance.

---

### 9. Relevance to explainable symbolic mashup and repair

YuE2 is a strong **engineering precedent for an editable intermediate score**, but it is not a mashup or repair system.

It does not:

- align two source compositions;
- classify musical conflicts;
- identify responsible notes or voices;
- search minimal repairs;
- preserve two source identities simultaneously;
- output a rationale graph;
- evaluate explanation faithfulness.

Its cover experiment preserves **one work’s identity** while changing style. That is useful for provenance-preserving generation, but a two-source mashup introduces conflicts that YuE2 does not study.

The most valuable transferable mechanism is therefore:

> symbolic plan → explicit edit → regenerated audio → adherence/preservation audit

For your research, the missing layer should be an explicit symbolic conflict-and-provenance system before any audio renderer.

---

### 10. Modest-scale adaptation plan

#### Phase 1: symbolic-only pilot

- Start with short classical piano or lead-sheet material.
- Represent notes, voices, bars, meter, key, chords, motifs, phrases, and provenance IDs.
- Train a 100–300M symbolic planner, or begin with retrieval plus constrained search.
- Require every generated event to retain source attribution and transformation history.
- Evaluate compatibility, identity, coherence, novelty, playability, and explanation faithfulness separately.

#### Phase 2: repair and mashup search

Implement explicit operations:

- transpose;
- rhythmic quantization or substitution;
- chord replacement;
- voice reassignment;
- phrase deletion/insertion;
- cadence repair;
- bridge generation.

Use protected spans and a cost function favoring minimal changes. Produce a rationale graph:

`conflict → affected notes/voices → operation → musical reason → counterfactual alternatives`.

#### Phase 3: audio realization

Avoid reproducing YuE2 initially.

- Use a deterministic MIDI renderer for the first experiments.
- Then use an existing licensed score-conditioned audio model or a small renderer.
- Train only on approximately 100–1,000 hours of legally usable paired or synthetically rendered material.
- Keep the symbolic system independent so audio quality cannot hide symbolic failures.

#### Phase 4: YuE2-inspired evaluation

Run matched tests:

1. plan versus no-plan;
2. edited versus unedited;
3. protected-source preservation;
4. source-identity retrieval;
5. conflict diagnosis accuracy;
6. minimality of repair;
7. explanation faithfulness;
8. musician/listener judgments.

**Bottom line:** YuE2 demonstrates that a readable score can improve and control full-song generation, but its scale and proprietary data regime are not modestly reproducible. For your programme, transfer the score interface, audit methodology, and provenance-aware conditioning—not the 3.58B end-to-end training ambition.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `generation-and-planning`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
