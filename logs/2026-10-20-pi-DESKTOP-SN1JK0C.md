# 2026-10-20 — NCM (Kumbong et al., arXiv 2610.14162) ingestion

## Scope and completion

User-requested digest of **NCM — "Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation"**, Hermann Kumbong\*, Ishan S. Khare\*, Iddah Mlauzi, Andrew Woen, Charles Ding, E. Kelly Buchanan, Simran Arora†, Azalia Mirhoseini†, Christopher Ré† (Stanford CS / Stanford EE / Together AI); arXiv `2610.14162v1` [cs.CL], submitted 2026-10-09. Ingested per the digest command convention as registry step MISC NCM-Digest.

- PDF provenance: downloaded directly from `https://arxiv.org/pdf/2610.14162v1`, 40 pages, 1,343,534 bytes; canonical copy in `papers/kumbong-2026-ncm-next-concept-modeling-fast.pdf`; SHA-256 `708a029c7f53d4f9f04ca5c93865afc9b3b5414acab3d7d9b887f313d04a5b4d` in the source record.
- Full-paper evidence: all 40 pages read from PyMuPDF text extraction with per-page markers; `pdftotext -layout` used to cross-check table alignment. Main text pp. 1–13; references pp. 14–18; Appendices A–J pp. 21–40 (ELBO, datasets, architecture tables, baseline provenance, extra results, ablations, tokenizer analysis, hierarchy probes, limitations, qualitative samples).
- Figure check that mattered: the level-schedule ablation (Figure 10b, p. 27) was rendered to PNG and read as an image. Plain text extraction emits the six Gen. PPL labels in a different order from the x-axis categories, which would have bound the best and worst schedules to the wrong ladders. Visual reading gives Lin. 88.4, Quad. 59.6, Sqrt 196.7, Log. 168.2, Exp. 57.7, Cos. 77.8 — exponential and quadratic best, square-root and logarithmic worst. The first draft of the source record had this inverted; it was corrected before validation. Figure 13 (code corruption, p. 29) was also read as an image to recover the sweep values (rate 0 ≈ 50 Gen. PPL, 0.5 ≈ 22, 0.75 ≈ 26).
- Extraction tool: system Python PyMuPDF 1.28.2 in the temporary directory; the shared `.venv` was not modified.

## Records

- `papers/kumbong-2026-ncm-next-concept-modeling-fast.pdf` + `sources/kumbong-2026-ncm-next-concept-modeling-fast.md` + `wiki/other/kumbong-2026-ncm-next-concept-modeling-fast.md`.
- `wiki/concepts/hierarchical-latent-reasoning.md` updated: heading widened to "Distinguishing Kinds of Hierarchy" (a third kind now exists), new section "Resolution Hierarchies: Learned Code Ladders" (NCM's level schedule as a measured lever, level-by-level decoding, the three coarse-code probes, and the zero-encoder-block caveat), an NCM paragraph in Claim Delta, and a reciprocal Related Pages entry.
- `wiki/overviews/2026-symbolic-music-literature-map.md` updated: one `### other` entry, one body sentence in "Adjacent and low-relevance methods" placing NCM as a text-domain resolution ladder, and one Related Papers entry.

Category decision: `other`. NCM's primary contribution is a text-generation architecture plus a multiscale tokenizer; it fits no music-domain category despite touching representation, generation, and evaluation themes, matching the precedent of the other cross-domain method papers (LapSRN, RCAN, CDDFuse, ArtiAgent). The reason is stated on the wiki page itself.

## Supersede check

No contradictions with existing wiki content. Deltas: (1) **strengthens** the hierarchy concept page's claim that a decodable intermediate structure is worth building for — NCM gives a cheap, measured construction (exponential/quadratic level ladders halve Gen. PPL against linear at equal budget) plus a reusable probe shape (fix coarse codes, resample fine; mix coarse codes from two sources; replace individual coarse codes); (2) **narrows** the word "concept": with zero encoder blocks the coarse codes are downsampled learned residuals, the paper defines "concept" as exactly the coarse-level information, and the probes are single stories with two seeds, author-marked diffs, no matched-rate unrelated-story control, and no effect size over a sample; (3) **unchanged** for music: no symbolic task, no constraint verifier, no explanation or human-utility study, so the transfer contract's requirement for named musical objects at the slow level is untouched; (4) a correction to the batch map's "generate and then verify" reading is not implied — NCM has no verifier, so its Sudoku result is learned constraint satisfaction, not verifiable generation.

## Repo-side verification carried into the record

Repository check on 2026-10-20, recorded in the source record with explicit provenance: `HazyResearch/ncm` exists (MIT, created 2026-10-11, last push 2026-10-14) with `evaluate.py`, `models/` (generator, VQ/VQ-VAE, quantization), `tokenization/`, `scripts/eval_shard.py`, `scripts/eval_merge.py`, and `config/eval/` only; the README points to Hugging Face checkpoints (`hazyresearch/ncm-checkpoints`) and tokenized datasets (`hazyresearch/ncm-datasets`). **No training script or training config is released**, so training reproduction rests on Tables 5–6. This is a repository observation, not an author claim. The README additionally states that `evaluate.py` reports "solved, cell and valid-grid rates" for Sudoku; the paper itself reports only completely-solved boards, which is recorded as an evidence boundary rather than a result.

## Synthesis gaps noted

- No concept page yet covers **discrete tokenization and reconstruction fidelity for symbolic music**. NCM's exact-reconstruction framing (99.86–100% token recovery, with named-entity/numerals/diacritics failures) is the clean statement of the property a symbolic codec must have before a copying or attribution audit can separate codec error from model choice; the `hierarchical-latent-reasoning` page can carry the pointer, but a dedicated anchor should be created if a second symbolic-tokenizer paper arrives.
- The map's header still says "55 papers" while the list has grown past it; left unchanged in this digest to keep the edit scoped, flagged here.

## Validation and status

- `validate_paper_records.py`: 74 source records, 74 paper pages, 11 synthesis pages, and crop evidence — 0 errors.
- `audit_synthesis_orphans.py`: 0/74 orphans.
- `build_indexes.py --date 2026-10-20` run after ingestion; `index.md` and `indexes/other.md` regenerated.
- Evidence limitations preserved in the source record: several conditional quality rows are borrowed from Hu et al.; timing for conditional baselines without released checkpoints was measured on randomly initialized weights (same architecture and sampling config, timing only); wall-clock is one H100, batch 16, 1,024 sequences; the OWT "competitive" claim is time-matched, not quality-matched (NCM Gen. PPL 83.12 vs DUO 77.69 and FLM 62.23); diversity is unigram entropy only; the Sudoku trajectory grid (p. 40) and the scaling curve's per-point values are figure-only and treated as qualitative.
