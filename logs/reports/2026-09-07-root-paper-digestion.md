# Root PDF Digestion — 7 September 2026

All **4/4 root-folder PDFs** were read in full: **51/51 pages**, including references and appended supplementary material. Each has an exact canonical PDF copy, source digest, domain page, reciprocal synthesis connection, and saved visual evidence.

| Paper | Pages | Main contribution | Paper page |
|---|---:|---|---|
| Diff-Symbo | 9 | Text-conditioned diffusion with segmentwise continuation | [Digest](../../wiki/generation-and-planning/lin-2026-diff-symbo-text-controlled-long.md) |
| MI-MIDI | 13 | Probing, prediction lenses, prompt patching, and bidirectional steering | [Digest](../../wiki/explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of.md) |
| MusPyExpress | 10 | Typed expression annotations and expression-aware symbolic modeling | [Digest](../../wiki/data-and-representation/long-2025-muspyexpress-extending-muspy-with-enhanced.md) |
| Dissonance Spectrum | 19 | Explicit rational pitch-relation attribution and auxiliary audio representation | [Digest](../../wiki/theory-and-constraints/wang-2026-beyond-frequency-dissonance-spectrum-for.md) |

## Findings That Affect Interpretation

**Diff-Symbo:** stronger classifier-free guidance raises attribute accuracy from 83.15% to 86.69% while reducing quality MOS from 3.54 to 3.40. The evaluated duration is 32 bars; several-minute or formal-coherence claims have less direct support. The method describes frozen BERT, whereas the ablation discussion ambiguously calls the improvement BERT fine-tuning. The linked demo was inspected, but training code was not established there and the anonymous template archive was inaccessible from this environment. [PDF pp. 3, 6–7]

**MI-MIDI:** interventions extend the evidence beyond the earlier SynTheory probing page, but best-layer/configuration selection is exploratory, “tempo/energy” is a note-density proxy, and two models do not isolate an architecture effect. The linked demo's filenames specify MIDI-LLM one-to-all directions from layer 14, including strengths up to 2 for register/polyphony. Those differ from the selected single-layer configurations in Tables 6–7. This is a showcase/configuration mismatch, not proof that the tables are invalid. The released experimental implementation was not available in the inspected demo. [PDF pp. 9–12; pinned demo script]

**MusPyExpress:** the Table 3 counts sum correctly to 3,513,641, but they imply 15.77 markings per all 222,820 files or 16.54 per 212,406 annotation-bearing files, rather than the reported 20.1. The relevant denominator remains unknown. The best metrical perplexity configuration also moves pitch-class entropy farther from the reference. Tagging is reported on validation data. [PDF pp. 2–4, 9–10]

**MusPyExpress artifact limits:** the linked branch has the 28 annotation classes, but MIDI annotation realization is opt-in. Generic seconds conversion integrates explicit tempo entries without itself realizing tempo spanners or fermatas. Two rendering paths access `music.infer_velocity`, which is not initialized in the inspected Music class; this is a potential runtime defect unless callers attach it. Convenience realization and MIDI export also use different pedal-duration multipliers. These static findings can affect use of the library, especially real-time workflows; their connection to the exact publication run and numerical impact remain unknown.

**Dissonance Spectrum:** the six-seed gains over matched CQT are small but consistently positive; corrected exact sign tests give .09375 rather than significance at .05. Theory-derived reference ranks and MusicQA text similarity do not establish listener preference or factual music understanding. The stated EmoMusic split ratio differs from its explicit 495/124/125 counts. A separately submitted Code and Data Archive is described but neither supplied nor publicly linked in the PDF, so implementation and predictions could not be checked. [PDF pp. 5–7, 10, 16–19]

## Artifact Evidence

Only paper-linked artifacts were inspected; no literature search was used. These checks did not execute model training, evaluate generated MIDI corpora, or listen to audio examples.

| Artifact | Inspected revision / scope | Boundary |
|---|---|---|
| [Diff-Symbo demo](https://github.com/apply74/Diff-symbo/tree/01b35819aa8318eb41e9733850ba6509982a68ac) | Root listing, README, and index with eight-bar/continuation/32-bar examples | Presentation content does not reproduce training or scores |
| [Diff-Symbo templates](https://anonymous.4open.science/r/templates-8DA8/) | Direct access attempt failed with connection refusal | Count and contents unchecked; not evidence that the archive is unavailable to everyone |
| [MI-MIDI demo](https://github.com/jpocwiar/MI-MIDI-Demo/tree/589e961040832686e6b24182c513ad6134a4f1b3) | Root listing, README, and script.js sample mapping | Static showcase; experimental pipeline not demonstrated |
| [MusPy expressive branch](https://github.com/salu133445/muspy/tree/dbeb120146280c7b2a145615598480326bc75baa) | README, annotation classes, MusicXML parser, Music class, MIDI output routes | Static code audit; no complete parser/rendering or experiment rerun |
| DS Code and Data Archive | Mentioned on PDF pp. 10, 16–17; no local archive or embedded public URL | Implementation and seed predictions unchecked |

## Synthesis Changes

- **Strengthen:** MI-MIDI supplies symbolic intervention evidence alongside recoverability, without proving explanation utility.
- **Strengthen and narrow:** Diff-Symbo supports contextual latent generation while preserving the control–quality and local-continuation/form distinctions.
- **Strengthen and narrow:** MusPyExpress supports retaining expression instructions, with explicit separation of preservation, realization, and inferred annotations.
- **Strengthen and narrow:** DS supports a scoped relational prior, while its perceptual and statistical boundaries remain visible.
- No existing paper result is replaced or contradicted by a commensurate new experiment. SynTheory's recorded code concerns remain unchanged.

The existing probing, music-domain biases, and symbolic foundation-model synthesis bodies were updated. New concepts cover [expression-aware representation](../../wiki/concepts/expression-aware-symbolic-representations.md) and [Dissonance Spectrum](../../wiki/concepts/dissonance-spectrum.md).

## Verification

New-record schemas, canonical paths, four original/copy SHA-256 comparisons, reciprocal synthesis links, and ten crop manifests/images pass. The catalog now contains ten paper pages, with **0/10 synthesis orphans**. Full-repository validation still finds ten pre-existing external PDF paths in five older source/wiki pairs; those records were left unchanged. Model results were not rerun, and unavailable artifacts remain unchecked rather than passing.
