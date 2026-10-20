---
title: "NCM Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation"
authors: "Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi, Andrew Woen, Charles Ding, E. Kelly Buchanan, Simran Arora, Azalia Mirhoseini, and Christopher Ré"
year: 2026
doi: 10.48550/arXiv.2610.14162
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kumbong-2026-ncm-next-concept-modeling-fast.pdf"
pdf_filename: kumbong-2026-ncm-next-concept-modeling-fast.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-20
---
## One-line Summary

NCM replaces token-by-token decoding with a frozen multiscale residual VQ-VAE hierarchy plus a transformer that predicts one whole level of discrete codes at a time, coarse to fine, giving 10–31× faster text generation at matched quality; the music-relevant content is the level hierarchy, its decodability, and the coarse-code intervention probes, not any music result.

## 1. Document Information

- **Authors and affiliation:** Hermann Kumbong\*, Ishan S. Khare\*, Iddah Mlauzi, Andrew Woen, Charles Ding, E. Kelly Buchanan, Simran Arora†, Azalia Mirhoseini†, Christopher Ré†. Stanford CS / Stanford EE / Together AI. \*equal contribution, †equal senior authorship. [PDF p. 1]
- **Identifier:** arXiv `2610.14162v1` [cs.CL], submitted 2026-10-09. DOI `10.48550/arXiv.2610.14162` (arXiv-issued, DataCite). Cross-listed cs.AI and cs.LG (arXiv abstract page). Preprint; no venue is stated in the PDF.
- **PDF:** 40 pages, 1,343,534 bytes, SHA-256 `708a029c7f53d4f9f04ca5c93865afc9b3b5414acab3d7d9b887f313d04a5b4d`. Layout: main text pp. 1–13 (Figure 1 p. 1; §1 pp. 2–3; §2 pp. 3–4; §3 pp. 5–7; §4 pp. 8–12; §5 p. 13; acknowledgments p. 13); references pp. 14–18; appendix table of contents pp. 19–20; Appendices A–J pp. 21–40.
- **Canonical artifact:** downloaded from `https://arxiv.org/pdf/2610.14162v1` on 2026-10-20; preserved byte-identical in `papers/`. The HTML rendering (`arxiv.org/html/2610.14162v1`) was used only as a first pass; all numbers below were re-read from the PDF.
- **Reading coverage:** all 40 pages read from PyMuPDF text extraction, plus `pdftotext -layout` for table alignment checks. Figures 1, 2, 4, 5, 6, 9, 10, 13, 14, 15, 16, 17, 18, 19 and Tables 1–12 were checked against their captions. No crop-evidence manifest was produced; no quantitative claim in this record depends on pixel-level reading except where a caption labels a bar or line that the text does not also report (flagged inline).
- **Reading limits:** the Sudoku trajectory in Appendix J.7 (p. 40) is a grid image with no extracted numbers; Figure 6a's scaling curve is a plot whose per-point values are not stated in text or tables (only the axis ranges and entropy labels). Both are treated as qualitative here.
- **Code and model release (repository check, 2026-10-20):** `https://github.com/HazyResearch/ncm` exists, MIT licence, created 2026-10-11, last push 2026-10-14. Contents: `evaluate.py`, `models/` (`next_concept.py`, `quant.py`, `vae.py`, `vqvae.py`, `common.py`), `tokenization/` (`bpe_tokenizer.py`, `hf_tokenizer.py`, `sudoku_tokenizer.py`, `vqvae_tokenizer.py`), `scripts/eval_shard.py`, `scripts/eval_merge.py`, `config/eval/` only. The README points to Hugging Face checkpoints (`hazyresearch/ncm-checkpoints`) and tokenized datasets (`hazyresearch/ncm-datasets`). **No training script or training config is present**; the release is evaluation-first, and the paper's Table 5/Table 6 hyperparameters are the only training recipe. This is a repository observation, not an author claim.

## 2. Key Contributions

The paper's own framing [PDF p. 1, pp. 2–3]:

1. **A two-stage representation-then-generate pipeline for text.** Stage 1 trains a multiscale residual VQ-VAE tokenizer that maps a length-`L` token sequence to `K` levels of discrete codes with `ℓ1 < … < ℓK = L`. Stage 2 freezes the tokenizer and trains a single transformer to predict level `k` in parallel from the cumulative reconstruction `ẑ(k−1)`. Generation therefore costs `K ≪ L` forward passes. [PDF pp. 5–7]
2. **A coarse-to-fine generation schedule with no distillation.** The authors present NCM as an alternative to few-step diffusion samplers/distillation, which they say lose sample diversity and leave per-step cost unchanged. Each step of NCM processes only `ℓk` positions, and early levels are short. [PDF pp. 2–4]
3. **Empirical claims at ~100M generator scale:** matched or better generative perplexity than strong diffusion/flow baselines with 4–11× fewer function evaluations (NFE) on TinyStories, LM1B, OpenWebText; best summarization ROUGE among compared systems on XSum at 8 NFE; all-but-one non-AR BLEU on WMT14 De–En; state-of-the-art completely-solved Sudoku at 12 NFE; 10–31× wall-clock speedups; 4–5× fewer training tokens. [PDF pp. 9–12, Tables 2–3, Figures 5–7]
4. **A qualitative hierarchy probe.** Fixing the three coarsest levels and resampling the rest preserves story theme while changing names, objects, and wording; mixing two stories' coarse codes blends their content; replacing two level-1 codes changes characters/events while preserving parts of the narrative. [PDF pp. 32–34]
5. **An ELBO framing** showing the generator loss is a lower bound on text log-likelihood when conditioning is clean and level weights are uniform, and that the corruption and weighting actually used move the objective away from that bound. [PDF pp. 21–22]

**What the paper does not contribute:** any music, audio, or symbolic-score experiment; any constraint verifier; any faithfulness metric for the level hierarchy; any source-attribution or provenance mechanism. Every task is text (LM1B, OWT, TinyStories, XSum, WMT14) or the grid task Sudoku.

## 3. Methodology and Architecture

### 3.1 Multiscale residual tokenizer (stage 1)

- An encoder maps `x` to `z ∈ R^{L×d}`; at level `k` the residual `z(k−1)` is **downsampled** to `ℓk` vectors `uk = Down_k(z(k−1))`, each quantized to its nearest entry in level-`k` codebook `V_k`; a reconstruction operator `R_k` maps the selected codes back to length `L` and the cumulative reconstruction updates as `ẑ(k) = ẑ(k−1) + R_k(e_k(r_k))`, `z(k) = z − ẑ(k)`. [PDF p. 6, Eq. 7–8]
- **Nested dropout:** during training a cutoff `k ~ U{1..K}` is sampled and only the first `k` levels are retained, so early levels must carry usable information. Loss at the sampled cutoff = reconstruction cross-entropy + commitment MSE + codebook MSE, with a straight-through estimator. [PDF p. 7, Eq. 9]
- **Architecture detail worth noting:** Table 5 reports **0 encoder blocks for every dataset**; the encoder is essentially the token embedding plus downsampling, and the decoder is 1 block (4 for LM1B). Latent width `d = 384` everywhere (256 for Sudoku); codebooks 4,096 entries (8,192 for LM1B, **16 for Sudoku**). `K` is 32 (OWT), 12 (LM1B, TinyStories, Sudoku), 11 (WMT14), 8 (XSum). Tokenizer parameter counts 14.90M (Sudoku) to 144.00M (WMT14). [PDF p. 23, Table 5]
- Text vocabularies differ per task: GPT-2 (50,304 with padding), bert-base-uncased (30,528), custom BPE (8,192), Qwen3-0.6B (151,680), 12 symbols for Sudoku. [PDF pp. 22–23, Tables 4–5]

### 3.2 Generator (stage 2)

- Factorization: `pθ(r1:K) = Π_k pθ(r_k | ẑ(k−1))`, and within a level `pθ(r_k | ẑ(k−1)) = Π_i pθ(r_k^i | ẑ(k−1))`, i.e. **all positions of a level are conditionally independent given the earlier levels' reconstruction**. [PDF pp. 6–7, Eqs. 4–5]
- **Training:** all `K` levels are predicted in one forward pass; each level's input is the (corrupted) cumulative reconstruction `z̃(k−1)` resized to `ℓk` positions; loss weights `wk ∝ ℓk^{−α}` with `α = 0` weighting every code equally and `α = 1` weighting every level equally. [PDF p. 7, Eq. 10, Algorithm 1]
- **Block-diagonal attention** is the chosen pattern in the unconditional setting: each level's input block attends only within itself, justified as sufficient because the block input already summarizes earlier levels. [PDF p. 7, p. 28, Table 9, Figure 11]
- **Conditioning corruption** is the paper's fix for exposure bias across levels: a fraction of conditioning codes is replaced by uniformly sampled codes from the same level's codebook (targets stay clean), with a linearly decreasing rate over levels. [PDF p. 7, p. 29, Figure 13]
- **Generation:** `K` sequential steps; at step `k` the transformer predicts all `ℓk` codes in parallel, they are added to the reconstruction, and after level `K` the VQ-VAE decoder produces token distributions from `ẑ(K)`; output tokens by argmax. [PDF p. 7, Algorithm 2]
- **Conditional generation:** prefix-LM attention. Prompt tokens are embedded with the frozen VQ-VAE encoder's token embedding table, prompt positions attend to each other, each target block attends to prompt + itself, prompts cannot attend to targets. [PDF p. 7]
- Generator scale: 25.46M (Sudoku) to 119.96M (WMT14) parameters, 8–12 blocks, hidden width 768 (512 for Sudoku), 12 heads (8 for Sudoku). Prefix length is 1 for unconditional tasks, 512 (XSum), 96 (WMT14), 91 (Sudoku). [PDF p. 24, Table 6]
- **Training-token accounting:** budgets count full-length positions including padding and repeated passes, not FLOPs. LM1B: `25,957×2,048×128 + 100,000×512×128 ≈ 13.36B` (6.80B tokenizer + 6.55B generator). OWT: `78,432×768×1,024 + 250,000×256×1,024 ≈ 127.22B` (61.68B + 65.54B). [PDF p. 24]

### 3.3 ELBO (Appendix A)

With a point-mass variational distribution `q(r1:K|x) = 1{r1:K = r*1:K(x)}` (the tokenizer's deterministic assignment), the ELBO reduces to `log pψ(x|r*1:K) + log pθ(r*1:K)`, and the gap is `−log pθ,ψ(r*1:K|x)`. The bound is tight only if the generator posterior puts probability one on the tokenizer's hierarchy. The authors state that "conditioning corruption and nonuniform level weighting modify that objective", i.e. the reported training configuration is **not** a pure ELBO maximizer, and nested dropout plus the VQ losses are outside the bound. [PDF pp. 21–22, Eqs. 15–18]

## 4. Key Results and Benchmarks

All numbers are the paper's own, with provenance flags where the paper itself borrows or simulates.

### 4.1 Tokenizer reconstruction and utilization (Table 1, PDF p. 8)

| Dataset | Exact reconstruction (%) | Mean codebook utilization (%) |
| --- | --- | --- |
| OWT | 99.99 | 83.10 |
| LM1B | 99.86 | 89.31 |
| TinyStories | 99.98 | 90.12 |
| XSum | 99.79 | 86.20 |
| WMT14 | 98.79 | 61.89 |
| Sudoku easy/med/hard | 100.00 / 100.00 / 100.00 | 80.73 / 83.85 / 80.73 |

The authors stress that image-like "imperceptible" reconstruction error is consequential in text (one wrong digit invalidates a Sudoku). Reported failure modes on the OWT tokenizer are named entities, diacritics, numerals, usernames, markup, and word boundaries. [PDF pp. 8, 31, Table 11]

### 4.2 Unconditional generation (Figure 5 p. 9; Table 8 p. 26)

Generative perplexity uses GPT-2-large as reference; mean per-sample unigram entropy `H` is reported because lower Gen. PPL can be bought with lower diversity.

| Dataset | NCM NFE | NCM Gen. PPL | NCM H | Strongest baseline Gen. PPL | Baseline H | Data Gen. PPL / H |
| --- | --- | --- | --- | --- | --- | --- |
| TinyStories | 12 | 15.41 | 3.98 | 15.43 (FMLM+, 128 NFE) | 3.90 | 9.67 / 3.96 |
| LM1B | 12 | 93.05 | 4.31 | 97.30 (DUO, 128 NFE) | 4.30 | 53.51 / 4.31 |
| OWT | 32 | 83.12 | 5.42 | 62.23 (FLM, 1024 NFE); DUO 77.69 / 5.55 | 5.33 (FLM) | 14.15 / 5.44 |

**Evidence boundary:** on OWT, NCM's Gen. PPL (83.12) is **worse** than DUO's (77.69) and FLM's (62.23); it is better matched to the data entropy (5.42 vs data 5.44) while FLM sits below the data entropy. The abstract's "competitive with the strongest DLM while running 10× faster" is therefore a **time-matched** claim (Figure 5's OWT panel plots Gen. PPL against seconds per 1,024-token sequence, batch 16), not a quality-matched one. On LM1B and TinyStories the claim is quality-matched at lower NFE. GPT-2-large is not the only scorer tested: Table 7 averages Mistral-7B, Llama-3.1-8B, Gemma-2-9B, and Qwen-3-14B on LM1B and reports NCM lowest on average (83.24 vs DUO 92.52, FLM 104.59, MDLM 114.31). [PDF p. 25, Table 7]

### 4.3 Conditional generation (Table 2, PDF pp. 9–10)

| Setting | Method | Size | BLEU (WMT14 De–En) | NFE | ROUGE-1/2/L (XSum) | NFE |
| --- | --- | --- | --- | --- | --- | --- |
| AR | reference | 99M | 25.2 | 64 | 30.5 / 10.2 / 24.4 | 64 |
| No guidance | E2D2 (best diff. on WMT) | 99M | 24.8 | 64 | 28.4 / 8.3 / 22.0 | 64 |
| No guidance | AURORA-LM (best XSum) | 130M | – | – | 34.7 / 12.2 / 26.6 | 128 |
| No guidance | **NCM** | 120M / 88M | **22.6** | **11** | **35.0 / 12.8 / 28.0** | **8** |
| Guided | ELF | 140M | 26.4 | 128 | 36.0 / 12.2 / 27.8 | 128 |
| Guided | AURORA-LM | 130M | – | – | 36.3 / 13.4 / 28.6 | 184 |
| Guided | NCM + CFG | 120M / 88M | 23.9 | 22 | 35.3 / 13.0 / 28.2 | 16 |
| Guided | **NCM + MBR** | 120M / 88M | **25.2** | 132 | **37.3 / 14.0 / 29.6** | 128 |

NFE counts generator calls, and each classifier-free-guidance step is counted as two. MBR uses `K = 12` candidates on WMT14 and `K = 16` on XSum. Two boundaries matter: (i) unguided NCM is **below** the AR and E2D2 BLEU on WMT14 (22.6 vs 25.2 / 24.8), so the "all but one non-AR" claim is about non-AR methods only; (ii) NCM+MBR uses 128–132 NFE, i.e. **not fewer** than the 64–184 NFE of the guided baselines it beats, so the advantage is that fewer NFE per candidate frees the budget for more candidates, not that it wins at lower total NFE. MDLM, DUO, E2D2, and SeqDiffuSeq rows are taken from Hu et al. [13] (marked † in the table), not re-run. [PDF pp. 9–10, 24–25]

### 4.4 Reasoning: Sudoku (Table 3, PDF p. 10)

Metric: percentage of **completely solved** boards; difficulty defined by given clues (40/35/30 for easy/medium/hard); baseline numbers taken from Agarwal et al. [49], evaluation setup follows S-FLM [50].

| Method | Size | NFE | Easy | Medium | Hard |
| --- | --- | --- | --- | --- | --- |
| AR sample | 25M | 128 | 13.9 | 5.1 | 0.6 |
| AR greedy | 25M | 128 | 14.6 | 5.1 | 1.0 |
| MDLM | 29M | 128 | 92.0 | 77.1 | 30.2 |
| DUO | 29M | 128 | 96.3 | 84.7 | 58.4 |
| FLM | 29M | 128 | 94.2 | 82.7 | 44.5 |
| FMLM+ | 29M | 16 | 97.7 | 92.8 | 81.3 |
| **NCM** | 25M | **12** | **99.5** | **96.5** | **86.1** |

The authors attribute the gap to global refinement: later levels can correct earlier partial solutions, whereas AR commits left to right. The paper reports only complete-solve rates — no cell-level accuracy, no validity rate, and no constraint-violation breakdown. (The released README says `evaluate.py` also prints "solved, cell and valid-grid rates"; that extra granularity is a code artifact, not a paper result.) [PDF p. 10; repo README checked 2026-10-20]

### 4.5 Scaling (Figure 6, PDF p. 11)

- **Model scaling:** 97M / 317M / 725M LM1B generators sharing one frozen tokenizer, fixed generator training-token budget; Gen. PPL decreases and sample entropy stays high (`H = 4.34 / 4.34 / 4.31`). Exact per-point Gen. PPL is only in the plot and is not quoted in text or a table.
- **Test-time scaling:** MBR over `K` candidates improves monotonically with diminishing returns; the text reports `+4.48` ROUGE-1 from `K = 1` to `K = 256`.

### 4.6 Efficiency (Figures 1, 5, 7; §4.6 pp. 11–12)

- Wall-clock measured end-to-end for 1,024 sequences at batch size 16 on one NVIDIA H100 SXM 80GB: **21× faster than DUO on LM1B** (11× fewer NFE, better Gen. PPL) and **31× faster than AURORA-LM on XSum** (16× fewer NFE, comparable ROUGE). The authors attribute the gap to both fewer NFE and lower per-step cost from short coarse levels.
- **Baseline timing caveat (Appendix D.2, p. 25):** MDLM/DUO/E2D2/SeqDiffuSeq quality numbers come from Hu et al.; for conditional baselines **without released checkpoints**, "we benchmark sampling time using randomly initialized weights with the same model architecture and task-specific sampling configuration reported for those tasks. These runs are used only for timing." A randomly initialized network does identical arithmetic, so the timing comparison is structurally fair on FLOPs, but it is a simulation of the baseline, not a measurement of the published system.
- Training budget: 13.36B token positions on LM1B vs 66B for the baselines (≈4.9× fewer, Fig. 7); 127.22B on OWT vs 500B+ (≈4× fewer). Both include tokenizer training. The paper offers as one explanation that "NCM's fixed coarse-to-fine order simplifies learning relative to the many generation orders learned by diffusion baselines" — flagged as a hypothesis, not tested.

### 4.7 Ablations (Appendix F, PDF pp. 26–30)

All on TinyStories with 10k-step generators unless stated; reference data Gen. PPL 9.67, `H = 3.96`.

| Factor | Setting | Result |
| --- | --- | --- |
| Number of levels `K` | 4 / 8 / 16 / 32 (linear 1→128) | Gen. PPL improves monotonically; `H = 4.22 / 4.15 / 4.11 / 4.08`; all four reconstruct ≥ 99.95% of tokens. Ablation has **no** code corruption, so Fig. 9c's reconstruction curves are the clean-conditioning regime. |
| Level schedule (`K = 12`, 1→128) | linear / quadratic / sqrt / log / exp / cosine | final Gen. PPL 88.4 / **59.6** / 196.7 / 168.2 / **57.7** / 77.8; `H` 4.09 / 4.06 / 4.21 / 4.20 / 4.05 / 4.08 (bars read off Figure 10b; the text does not interpret the ranking). Exponential and quadratic ladders are best; square-root and logarithmic are the worst of the six, so "a schedule that refines slowly" is not automatically the right prior. |
| Attention pattern | block-causal / 2-level sliding / block-diagonal | Gen. PPL 19.63 / 17.84 / **15.41**; time for 1,024 samples 7.90 / 6.83 / **5.65** s; `H` 4.01 / 3.99 / 3.98. |
| Context encoder (XSum) | frozen T5-small vs own VQ-VAE encoder | T5-small +0.10 ROUGE-1, +0.15 ROUGE-2, +0.24 ROUGE-L for +35.3M parameters (+40%); the paper keeps its own encoder. |
| Loss weighting `α` | 0 → 1.5 | Coarse-level share of loss 19% → 63%; Gen. PPL 18.9–19.0 for `α ≤ 1`, 19.4 at `α = 1.5`. |
| Code corruption | 0 → 0.75 mean (linear decreasing per level) | 0 → Gen. PPL ≈ 50 (`H` 4.06); 0.25 → ≈ 26; 0.5 → ≈ 22 (`H` 3.97), the authors' "recipe" setting; 0.75 → ≈ 26. Non-zero corruption more than halves Gen. PPL; excessive corruption weakens the conditioning signal (Figure 13 values read off the plot). |

The `K` and schedule ablations both train fresh tokenizers for 40k steps and then 10k-step generators (the main TinyStories generator trains for 50,000 updates, Table 6), so their absolute Gen. PPL is not comparable to the main TinyStories number (15.41). The paper does not present them as comparable, but the two training regimes differ and the K-ablation values exist only as a plot.

### 4.8 Hierarchy probes (Appendix H, PDF pp. 32–34)

These are the paper's only evidence about *what* the levels represent.

1. **Fixing the three coarsest levels, resampling the other nine** with two seeds per story: outputs keep the broad theme (girl seeking warmth and a moving garment; Tim alarmed by something in the sky) and change names, objects, and wording. The figure captions report 44%, 51%, 42%, 54% of words changed, computed by the authors' own highlighting, with deletions unmarked. [PDF pp. 32, Figure 17]
2. **Mixing coarse representations of two different stories** and generating the finer levels: outputs blend elements from both sources (drawing/billboard plus cold-weather/moving-object; Tim plus Max/rain). [PDF p. 33, Figure 18]
3. **Replacing two level-1 codes** with random codes observed at that level across validation stories, same sampling seed for clean and perturbed runs: characters, objects, and events change while parts of the narrative persist. Codes are indexed by 8 equal regions of the 128-token grid; examples are `3165→512`, `410→2383`, `1474→219`, `4055→2225`. [PDF p. 34, Figure 19]
4. **Level-by-level decoding** of one WMT14 translation (Table 12, p. 36) shows intermediate quality is **not monotonic**: per-level BLEU 6.0, 7.2, 6.3, 16.0, 17.5, 17.7, 24.2, 51.7, 38.9, 56.3, 77.8. This is a single run and the authors treat it as illustrative.

**What the probes do and do not establish.** They show that coarse codes are *sufficient* to steer theme and *necessary-ish* for identity/objects in the authors' examples, i.e. decodable and manipulable. They do not quantify effect size across a sampled set, do not include a control that replaces codes with unrelated-story codes at the same rate, do not report a faithfulness metric, and do not test whether the same coarse codes always produce the same theme. No faithfulness or interpretability claim is made in the paper's own terms.

## 5. Limitations and Future Work

Author-stated [PDF p. 35, Appendix I]:

- `K` and the per-level lengths `ℓk` are **fixed**, so even a short continuation traverses the full hierarchy; an input-dependent schedule would adapt compute to example complexity.
- The tokenizer is trained **separately** from the generator, decoupling representation learning from the generative objective; end-to-end training is suggested.
- Main experiments are ~100M generators; the scaling study reaches 725M only on LM1B.
- Generations show "occasional artifacts at coarse-level transitions".

Repository-inferred, not author-stated:

- **Reconstruction error is measured on the tokenizer alone.** Table 1's 99.86–100% exact recovery is teacher-level codec fidelity on held-out text; no comparable measurement is reported for the *generated* code hierarchies, so the end-to-end error rate of a generation (tokenizer error plus generator error) is unknown. The conditioning-corruption ablation is the closest proxy and is reported only as Gen. PPL.
- **The "concept" is a residual-downsampling artefact, not a semantic unit.** With zero encoder blocks (Table 5), the coarse levels are downsampled learned features rather than semantically supervised units; the paper's use of *concept* is explicitly defined as "the information carried by the coarse levels of the hierarchy" (p. 5) and nothing more. Nothing in the paper tests whether a coarse code corresponds to a nameable unit (topic, entity, plan).
- **Speed claims mix measured and simulated baselines** (Appendix D.2) and use a single GPU/batch setting; no multi-hardware or batching sweep is reported, and NFE is not a sufficient cost model across architectures — which the paper itself argues when it rejects NFE-only comparisons.
- **Sudoku has no verifier in the loop.** Correctness is learned; the paper reports no constraint-check pass and no guarantee of validity, so the result is evidence that coarse-to-fine refinement helps a fixed-clue grid task, not that NCM can enforce symbolic constraints (chord, voice-leading, metre) at generation time.
- **Diversity is measured as unigram entropy only.** That is a lexical diversity proxy; no n-gram distinctness, self-BLEU, or semantic diversity measure is reported, and no human evaluation of any kind.

## 6. Related Work

The paper's own positioning [PDF pp. 3–4]:

- **Diffusion and flow LMs:** discrete (D3PM/Austin et al., SEDD/Lou et al., MDLM/Sahoo et al.), continuous (CDCD, CANDI, AURORA-LM), few-step and distillation routes (DUO diffusion duality, self-distillation through time, Flow Map LMs), block-autoregressive diffusion (BD3-LM, Fast-dLLM v2), and production DLMs (LLaDA, Mercury, DiffusionGemma, DFlash).
- **Discrete latent and next-scale prediction (images and audio):** VQ-VAE, VQ-VAE-2, VQGAN, residual quantization (RQ-VAE), SoundStream and EnCodec, VAR's next-scale prediction, HMAR.
- **Hierarchical / concept-level text generation:** MEGABYTE, H-Net dynamic chunking, Large Concept Models, ConceptLM, Dynamic Large Concept Models, HDLM (next semantic scale prediction).
- **Downstream baselines:** ELF (embedded language flows), E2D2 (encoder-decoder diffusion), SeqDiffuSeq, MDLM, DUO, SEDD, Eso-LM, FMLM+ / posterior refinement, S-FLM.
- **Verification-adjacent:** MBR decoding (Bertsch et al.).

Nearest neighbours in this wiki: [[concepts/hierarchical-latent-reasoning]] (slow/fast latent computation and the distinction between computation hierarchy and representation hierarchy), [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] (patch-level representation hierarchy in symbolic music), [[generation-and-planning/wang-2026-latticesmc-where-to-spend-inference]] (where to spend inference compute in chunked generators), [[other/lai-2017-deep-laplacian-pyramid-networks-for]] (coarse-to-fine residual reconstruction outside music).

## 7. Glossary

- **NCM (Next-Concept Modeling):** the paper's two-stage coarse-to-fine text generation framework.
- **DLM (diffusion language model):** a non-autoregressive LM that generates by iterative denoising.
- **AR (autoregressive):** left-to-right next-token generation.
- **VQ-VAE (vector-quantized variational autoencoder):** autoencoder whose latents are replaced by nearest codebook entries.
- **RVQ / residual quantization:** successive codebooks quantize the residual left by earlier codebooks.
- **Multiscale residual quantization:** residual quantization where each level has a different number of codes (shorter coarse levels, longer fine levels), as in VAR.
- **Next-scale prediction:** generating a coarse scale in parallel, then finer scales conditioned on it (VAR, HMAR).
- **Nested dropout:** training with a random level cutoff so partial (coarse-only) reconstructions remain informative.
- **Cumulative reconstruction `ẑ(k)`:** sum of the contributions of levels 1..k; the generator's conditioning signal at level k+1.
- **Level schedule `ℓk`:** the sequence of code counts from coarsest to finest.
- **NFE (number of function evaluations):** generator calls per output; each CFG step counts as two.
- **CFG (classifier-free guidance):** mixing conditional and unconditional logits; applied per scale in NCM.
- **MBR (minimum Bayes risk) decoding:** sample `K` candidates and keep the one with highest average similarity to the others.
- **Gen. PPL (generative perplexity):** perplexity of generated text under a reference LM (GPT-2-large here).
- **`H` (mean per-sample unigram entropy):** diversity proxy reported next to Gen. PPL.
- **ELBO (evidence lower bound):** variational lower bound on log-likelihood; Appendix A's bound is tight only for the exact tokenizer hierarchy.
- **ELBO gap:** `log p(x) − ELBO`, here `−log pθ,ψ(r*|x)`.
- **OWT / LM1B / XSum / WMT14 / TinyStories:** OpenWebText, One Billion Word, Extreme Summarization, WMT 2014 De–En, and the TinyStories synthetic corpus.
- **Block-diagonal attention:** each level's block attends only to itself; the chosen NCM pattern.
