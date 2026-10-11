---
title: "DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Controllable Music Generation"
authors: "Zhongjie Duan, Shengchuan Gao, Hong Zhang, and Yingda Chen"
year: 2026
doi: 10.48550/arXiv.2609.12774
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/duan-2026-diffsynth-music-audio-conditioned-kv.pdf"
pdf_filename: duan-2026-diffsynth-music-audio-conditioned-kv.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

The bibliography contains 36 references. The most central are ACE-Step-1.5 [4], Music-ControlNet [10], JASCO [11], Diffusion Templates [30], Demucs [26], pYIN [27], MuQ-MuLan [35], and AudioBox-Aesthetics [36].

## 1. Document Information

- **Canonical source:** arXiv `2609.12774v1`; official PDF preserved as `duan-2026-diffsynth-music-audio-conditioned-kv.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40xsw4_typ9.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

- **Title:** *DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Controllable Music Generation*
- **Authors:** Zhongjie Duan, Shengchuan Gao, Hong Zhang, Yingda Chen
- **Affiliations:** Alibaba Group; Shanghai Jiao Tong University
- **Source/version:** arXiv:2609.12774v1 [cs.SD], **11 September 2026**
- **Length:** 10 PDF pages; no appendix or supplementary section.
- **Official model link cited by the paper:** `https://modelscope.cn/models/DiffSynth-Studio/DiffSynth-Music`
- The paper contains one architecture figure, two result tables, and numbered equations (1)–(16). I inspected all pages and figures/tables.

The bibliography contains 36 references. The most central are ACE-Step-1.5 [4], Music-ControlNet [10], JASCO [11], Diffusion Templates [30], Demucs [26], pYIN [27], MuQ-MuLan [35], and AudioBox-Aesthetics [36].

---

### 2. Claimed contribution and control types

**Author claims** — Abstract; pp. 1–2, §1:

DiffSynth-Music adds audio conditioning to a pretrained music-generation DiT through layer-wise key/value injection. It provides five control types:

| Control | Intended information | Template |
|---|---|---|
| **Beats** | Rhythmic event timing | Control |
| **Vocals** | Melody, performance, possibly lyrics and singer identity | Control |
| **Accompaniment** | Harmony, rhythm, instrumental arrangement | Control |
| **Prosody** | Vocal pitch and timing with reduced phonetic/timbral information | Prosody |
| **Reference** | Global style, timbre, and production from a short excerpt | Reference |

The three templates are separately parameterized:

- **Control (C):** beats, vocals, accompaniment
- **Prosody (P):** resynthesized vocal signal
- **Reference (R):** short reference excerpt

The authors state that all templates can be combined during inference, but the reported experiments are **single-control evaluations**, not joint-control experiments.

---

### 3. Architecture: shared VAE and KV-cache injection

#### Problem formulation

Section 3.1, p. 3, defines:

\[
\mathcal{M}=\{\text{beats, vocals, accompaniment, prosody, reference}\}
\]

An active subset \(S\subseteq\mathcal{M}\) supplies control waveforms \(c_S\). The target waveform is \(x\), and text plus lyrics are \(y\).

The backbone consists of:

- text encoder \(T_\psi\),
- shared VAE encoder-decoder \((E_\omega,D_\omega)\),
- generation DiT \(F_\theta\).

The target latent is \(z_1=E_\omega(x)\); each control waveform is separately encoded as \(z_{c,m}=E_\omega(c_m)\). The generation backbone parameters \(\theta\) remain frozen.

#### Template modules

Section 3.2, pp. 3–4:

Each template \(A_{\phi_j}\), \(j\in\{C,P,R\}\), follows the backbone DiT architecture and is initialized from pretrained DiT weights. Template and generation branches have compatible hidden and attention dimensions but separate parameters.

For attention block \(\ell\), control \(m\), and head width \(d_h\):

\[
K_{\ell}^{A,m}=H_{\ell}^{A,m}W_{\ell,g(m)}^{A,K}
\]

\[
V_{\ell}^{A,m}=H_{\ell}^{A,m}W_{\ell,g(m)}^{A,V}
\]

The resulting per-control cache is:

\[
C_t^{(m)}
=A_{\phi_{g(m)}}(z_{c,m};\eta_t)
=\{(K_{\ell}^{A,m},V_{\ell}^{A,m})\}_{\ell\in\mathcal{J}}
\]

The shared VAE is important because all controls occupy a common latent representation. However, the method combines **attention memories**, not raw waveforms.

#### KV injection

Section 3.3, pp. 4–5:

The generation DiT predicts:

\[
\hat v_t=F_\theta(z_t,t,h_y;C_t)
\]

At each selected attention block:

\[
\tilde K_\ell=[K_\ell^G;K_\ell^A],\qquad
\tilde V_\ell=[V_\ell^G;V_\ell^A]
\]

The attention output is:

\[
O_\ell^G=
\operatorname{softmax}
\left(
\frac{Q_\ell^G\tilde K_\ell^\top}{\sqrt{d_h}}
\right)\tilde V_\ell
\]

Only generation queries produce outputs; the softmax spans generation and control keys.

The authors distinguish temporal semantics:

- beats, vocals, accompaniment, and prosody retain temporal alignment with the generated sequence;
- reference excerpts preserve internal ordering but are not assigned absolute output positions.

#### Fixed, reusable cache

Section 3.2 and §3.5, pp. 4 and 6:

Because control inputs are noise-free, the template timestep is fixed to the clean-data endpoint \(t=1\). Other template inputs are held constant:

\[
\eta_t=\eta_1,\qquad C_t^{(m)}=C_1^{(m)}
\]

Thus each active control requires one template forward pass; its layer-wise KV cache is reused throughout generation. This is an efficiency design, although the paper reports no actual latency or memory measurements.

---

### 4. Control-signal construction

Section 3.4, pp. 5–6.

Training examples are represented as:

\[
\mathcal{D}
=
\{(x_i,y_i,S_i,c_{i,S_i})\}_{i=1}^{N}
\]

The authors construct pairs from approximately **60,000 private music recordings**.

#### Beats

Essentia’s Degara beat tracker estimates timestamps \(\tau_k\). Beats are rendered as exponentially decaying sinusoidal pulses:

\[
b(s)=\sum_{k=1}^{N_b}h_{\text{beat}}(s-\tau_k),
\qquad
c_{\text{beats}}(s)=\frac{b(s)}{\|b\|_\infty}
\]

Each pulse is 10 ms, uses a 1 kHz carrier, and is zero outside its support. This conveys beat timing but not drum timbre or rhythmic subdivisions.

#### Vocals and accompaniment

Demucs separates each recording into:

- vocal estimate,
- accompaniment estimate.

The paper explicitly notes that vocals may retain lyrics and singer identity.

#### Prosody

The channel-averaged vocal signal \(v[n]\) is resynthesized using:

- fourth-order 30 Hz Butterworth low-pass filtering,
- second-order 80 Hz Butterworth low-pass filtering,
- pYIN pitch estimation over 65–1000 Hz,
- hop size \(H=512\).

The envelope is:

\[
\tilde e[n]
=
F_{80}^{(2)}
\left(F_{30}^{(4)}(|v|)\right)[n],
\qquad
e[n]=
\frac{\tilde e[n]}{\max_k\tilde e[k]+\epsilon}
\]

Pitch estimates are forward-filled; leading gaps use the first valid estimate; trajectories are interpolated to the sample grid with constant boundary extension. No voicing mask is applied.

The carrier and resynthesized signal are:

\[
\phi[n]
=
\frac{2\pi}{f_s}\sum_{k=0}^{n}f[k],
\qquad
r[n]=e[n]\sin(\phi[n])
\]

\[
c_{\text{prosody}}[n]
=
r[n]\frac{\max_k|v[k]|}{\max_k|r[k]|+\epsilon}
\]

The mono result is replicated across channels. The paper says this reduces, but does not guarantee removal of, linguistic content or vocal identity.

#### Reference

A contiguous \(\Delta=10\)-second excerpt is selected from the mixed recording:

\[
\tau^\star\in
\arg\max_{\tau\in\mathcal{T}_x}
\operatorname{Loudness}(x[\tau:\tau+\Delta])
\]

\[
c_{\text{reference}}
=
x[\tau^\star:\tau^\star+\Delta]
\]

It is intended to guide style, timbre, and production without imposing an output timeline.

#### Joint conditioning

Each active control is encoded separately. Their keys and values are concatenated in a fixed order:

\[
K_\ell^A=[K_\ell^{A,m}]_{m\in S},
\qquad
V_\ell^A=[V_\ell^{A,m}]_{m\in S}
\]

The paper gives accompaniment plus prosody as an intended example: preserve instrumental structure and vocal melody while allowing different vocal timbre. This is an architectural example, not a reported quantitative joint-conditioning result.

---

### 5. Training and inference

Section 3.5, p. 6.

The adapter is trained with conditional flow matching. Given:

\[
z_1=E_\omega(x),\qquad
z_0\sim\mathcal{N}(0,I),\qquad
t\sim p(t)
\]

the linear path is:

\[
z_t=(1-t)z_0+tz_1
\]

with target velocity:

\[
u_t^\star=\frac{dz_t}{dt}=z_1-z_0
\]

The loss is:

\[
\mathcal{L}_{\mathrm{CFM}}(\phi)
=
\mathbb{E}_{\mathcal{D},t,z_0}
\left[
w(t)
\left\|
\hat v_t(\phi)-u_t^\star
\right\|_2^2
\right]
\]

Frozen during template-only optimization:

- text encoder,
- VAE,
- generation DiT.

Gradients pass through the injected KV tensors to update the selected template modules.

Reported inference settings, §4.1, p. 6:

- classifier-free guidance scale: **4**
- inference steps: **50**
- generation duration: same as the test sample

The paper does **not** report optimizer, learning rate, batch size, number of training steps, hardware, parameter counts, or training compute.

---

### 6. Evaluation protocol

Section 4.1–4.2, pp. 6–7.

Test set:

- 100 samples total
- 50 English-lyric samples from MUSDB18-HQ
- 50 Mandarin-lyric samples from a private dataset
- prompts and lyrics annotated using Qwen3-Omni

Baselines:

- ACE-Step-1.5-XL-SFT
- DiffRhythm-2
- HeartMuLa-3B
- MiniMax-Music3
- LeVo-2-Large

Metrics:

- beats: Beat-F1, Cemgil
- vocals: V-MSE, phoneme error rate (PER)
- accompaniment: A-MSE
- prosody: Pitch50
- reference: MuLan-A
- general quality: AudioBox-Aesthetics CE, CU, PC, PQ
- text alignment: MuLan-T

The paper explicitly describes AudioBox-Aesthetics as an automatic proxy, **not a human listening evaluation**.

---

### 7. Exact reported results

#### Table 1: control adherence, p. 7

Arrows indicate preferred direction.

| Model | Beat-F1 ↑ | Cemgil ↑ | V-MSE ↓ | PER ↓ | A-MSE ↓ | Pitch50 ↑ | MuLan-A ↑ |
|---|---:|---:|---:|---:|---:|---:|---:|
| ACE-Step-1.5-XL-SFT | 0.3031 | 0.1983 | 0.0158 | 0.1928 | 0.0221 | 0.0366 | 0.6836 |
| DiffRhythm-2 | 0.3049 | 0.1998 | 0.0119 | 0.3264 | 0.0204 | 0.0314 | 0.6820 |
| HeartMuLa-3B | 0.3012 | 0.1956 | 0.0182 | 0.2626 | 0.0320 | 0.0347 | 0.5712 |
| MiniMax-Music3 | 0.2921 | 0.1923 | 0.0160 | 0.2663 | 0.0237 | 0.0402 | 0.6566 |
| LeVo-2-Large | 0.2892 | 0.1910 | 0.0165 | 0.2707 | 0.0281 | 0.0349 | 0.5144 |
| **DiffSynth-Music** | **0.8496** | **0.8088** | **0.0006** | **0.1451** | **0.0023** | **0.4671** | **0.8088** |

The authors claim the best value on all seven control metrics. Relative to ACE-Step:

- Beat-F1: 0.3031 → 0.8496
- Cemgil: 0.1983 → 0.8088
- V-MSE: 0.0158 → 0.0006
- PER: 0.1928 → 0.1451
- A-MSE: 0.0221 → 0.0023
- Pitch50: 0.0366 → 0.4671
- MuLan-A: 0.6836 → 0.8088

Important qualification: the DiffSynth row combines **different single-control runs**. It is not one model output simultaneously satisfying all five controls.

#### Table 2: general quality and text alignment, p. 7

| Model/configuration | CE | CU | PC | PQ | MuLan-T |
|---|---:|---:|---:|---:|---:|
| ACE-Step-1.5-XL-SFT | 7.3748 | 7.6975 | 6.4335 | 8.1016 | 0.4024 |
| DiffRhythm-2 | 7.2611 | 7.5567 | 6.0345 | 8.0152 | 0.4565 |
| HeartMuLa-3B | 7.6634 | 7.8523 | 6.2728 | 8.2712 | 0.3757 |
| MiniMax-Music3 | 7.3914 | 7.6760 | 6.2354 | 8.0465 | 0.3604 |
| LeVo-2-Large | 7.7488 | 7.9951 | 6.7954 | 8.4514 | 0.2383 |
| DiffSynth (Beats) | 7.4484 | 7.8041 | 6.0063 | 8.2155 | 0.3810 |
| DiffSynth (Vocals) | 7.1020 | 7.4263 | 6.1119 | 8.0604 | 0.3452 |
| DiffSynth (Accompaniment) | 7.3535 | 7.5773 | 6.4119 | 8.0555 | 0.3485 |
| DiffSynth (Prosody) | 7.2742 | 7.6471 | 6.1338 | 8.0704 | 0.3625 |
| DiffSynth (Reference) | 7.4436 | 7.7328 | 6.0139 | 8.2418 | 0.3900 |

The authors characterize quality as broadly comparable. Their more specific evidence is:

- PQ for DiffSynth configurations: **8.0555–8.2418**, near ACE-Step’s **8.1016**
- MuLan-T: **0.3452–0.3900**, within the baseline range **0.2383–0.4565**
- Some aesthetics scores and all DiffSynth MuLan-T scores are below ACE-Step.

---

### 8. Ablations, limitations, and reproducibility

#### Ablations

There is **no formal ablation table or ablation section**. Missing comparisons include:

- KV injection versus residual or concatenated-feature injection
- fixed cache versus timestep-varying cache
- shared versus separate VAEs
- template initialization from DiT versus random initialization
- separate templates versus one universal template
- control ordering and positional encoding
- prosody preprocessing choices
- effects of cache normalization or control strength
- joint-control performance
- scaling with multiple simultaneous controls

#### Explicit or evident limitations

1. **No joint-control evaluation.** Architecture claims composability, but quantitative results are single-control.
2. **No human listening study.** The conclusion explicitly says future work will evaluate joint conditioning and musical quality with human studies.
3. **Private training data.** The approximately 60k-recording training set is not available.
4. **Small test set.** Only 100 samples are reported, with no confidence intervals or seed variance.
5. **Automatic separation and extraction errors.** The paper acknowledges that beat tracking, source separation, and pitch estimation errors affect conditioning data (§2.5, p. 3).
6. **Prosody is not guaranteed to remove identity or lyrics.** The authors explicitly state this.
7. **Control metrics may conflate copying and useful control.** Low vocal/accompaniment MSE can reward reproduction without demonstrating musically desirable transformation.
8. **No explicit conflict handling.** The method concatenates control memories but does not explain what happens when controls disagree.
9. **No provenance mechanism.** KV attention does not provide note-level source attribution, edit history, or identity guarantees.
10. **Incomplete training disclosure.** Key optimization and compute details are absent.

#### Artifact availability

The paper claims release of the three template models and gives the ModelScope URL above. It does not provide, in the paper:

- a public training dataset,
- preprocessing code,
- training code,
- model sizes,
- licenses,
- checkpoint hashes,
- a detailed reproduction configuration,
- a public evaluation script.

---

### 9. Relevance to source-controlled symbolic mashups

#### Useful transferable ideas — interpretation

1. **Separate control channels.** The distinction between rhythm, melody/performance, accompaniment, prosody, and global reference maps naturally onto symbolic mashup roles: meter, motif, voice, harmony, bass, texture, and style.
2. **Local versus global conditioning.** Aligned controls can constrain event timing and structure; reference excerpts can guide style without forcing temporal alignment.
3. **Composable memories.** Separate source-specific caches could provide a mechanism for combining material from source A and source B without first destructively mixing their waveforms.
4. **Frozen backbone plus trainable adapters.** This is attractive for adapting a pretrained renderer while preserving its existing text/lyrics behavior.
5. **Cached controls.** Precomputed control representations could make interactive search over transformations more practical.

#### Critical mismatch with the symbolic-mashup objective

The paper controls **audio realization**, not symbolic structure or provenance.

Its latent/KV representation does not directly expose:

- note identity,
- voice assignment,
- motif boundaries,
- harmonic function,
- source ownership,
- transformations applied to source material,
- protected notes,
- conflict causes,
- repair rationale,
- counterfactual alternatives.

The paper’s “reference consistency” and low signal MSE should therefore not be interpreted as evidence of provenance preservation. Audio resemblance can result from copying, timbral similarity, or embedding similarity without preserving recognizable source contributions in an inspectable way.

For the repository’s research goal, DiffSynth-Music is best viewed as:

- a possible **acoustic rendering or conditioning baseline**;
- inspiration for modular control interfaces;
- not a solution to conflict-aware, provenance-preserving symbolic recomposition.

---

### 10. Concrete research directions

1. **Symbolic KV adapters.** Encode MIDI/event streams into layer-wise keys and values, with explicit channels for source ID, voice, motif, harmony, meter, and transformation type. Compare this against token concatenation and direct symbolic constraints.

2. **Provenance-aware attention.** Maintain source-specific caches \(C^A\) and \(C^B\), log attention mass by source, and test whether attention attribution predicts human judgments of source identity.

3. **Protected-material constraints.** Use a symbolic decoder or constrained search to guarantee preservation of selected notes, motifs, cadences, or bass lines while allowing specified transformations.

4. **Conflict-aware cache arbitration.** Detect incompatible rhythm, harmony, register, or voice-leading constraints before generation. Learn or search for minimal repairs rather than simply concatenating conflicting memories.

5. **Hybrid symbolic/audio controls.** Combine exact symbolic beat/chord/melody controls with audio reference conditioning. Evaluate whether symbolic controls improve temporal and harmonic faithfulness while audio controls improve timbre and performance.

6. **Synthetic provenance benchmark.** Construct known-source mashups with ground-truth note ownership, transformations, alignment, and conflict labels. Evaluate separately:
   - source identity,
   - compatibility,
   - structural coherence,
   - novelty,
   - playability,
   - explanation faithfulness.

7. **Joint-control ablation suite.** Reproduce the paper’s architecture while varying control combinations, ordering, cache normalization, fixed versus dynamic templates, and control strength. Measure whether controls interfere or compose.

8. **Acoustic realization after symbolic search.** Use symbolic recomposition as the transparent decision layer, then use a DiffSynth-like adapter to render the resulting arrangement while retaining the symbolic provenance graph.

**Bottom line:** DiffSynth-Music offers a compelling modular mechanism for audio control—shared latent encoding plus reusable layer-wise KV memory—but its evidence supports single-control acoustic adherence, not joint controllable composition, symbolic reasoning, or provenance-preserving mashups.

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
