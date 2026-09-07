---
title: "Dissonance Spectrum"
tags: [dissonance, explicit-theory, spectral-attribution, audio, evaluation-validity]
---

# Dissonance Spectrum

[[theory-and-constraints/wang-2026-beyond-frequency-dissonance-spectrum-for|Wang et al.]] define Dissonance Spectrum (DS) as a nonnegative time–frequency map that attributes a specified rational pitch relation to each active CQT bin. It answers where that relation occurs in a signal under a declared model; it does not directly estimate a listener's preference or explain a neural network's decision. [PDF pp. 2–5, 7]

## Mechanism

For a frequency ratio, search reduced rational candidates up to denominator/numerator bound Q. Prefer the lowest log₂(pq) complexity within a relative tolerance, otherwise take the nearest candidate. Normalize and octave-fold the resulting pitch-interval relation to an even kernel D̄. For target magnitude x(k,t), intrinsic DS is:

`d(k,t) = x(k,t) / K * sum_l[x(l,t) * D̄(p_l - p_k)]`.

Cross-reference DS substitutes a separate reference magnitude for x(l,t), allowing tonic- or chord-conditioned attribution. Frequency correlation avoids an explicit K×K×T pair tensor, but its index convention must be preserved: the supplement's increasing-lag layout requires a reversal relative to ordinary valid cross-correlation. The same mathematical relation is not a new observed modality; it reorganizes existing magnitude information. [PDF pp. 3–4, 10–11]

## Choices That Change the Claim

- **Reference:** intrinsic, tonic, and chord-reference forms answer different questions.
- **Octave folding:** assumes a pitch-chroma relation while retaining output-bin location; it omits register dependence in pair coefficients.
- **Normalization:** excerpt-level versus local-context normalization changes amplitude sensitivity; near gain-invariance under normalization is not independence from perceptual loudness.
- **Aggregation:** a maximum over frames differs from a sum over a sequential scale.
- **Downstream use:** interpretable input construction does not ensure faithful interpretation of a learned adapter or its host's output.

These boundaries follow the paper's definitions and controlled/downstream protocols. It excludes masking, critical-band roughness, learned tonal syntax, and listener-specific preference. [PDF pp. 3–7, 12–16]

## Evidence

Controlled interval ranks correlate strongly (Spearman .951), whereas diverse chord voicings correlate moderately (.626). Most reference orders are theory-derived and no new listener study is provided. Six-seed DS branches improve primary MusicQA/mean emotion endpoints by .0028/.0047 over matched CQT branches. Corrected exact sign tests yield .09375, and transformation/compression differences remain incompletely isolated. These are bounded indications of a useful prior, not universal dissonance validity. [PDF pp. 5–7, 19]

The separate implementation archive described in the PDF was neither supplied nor linked publicly there. Reproducing its extraction and model scores remains an open artifact task. Applying DS to symbolic generation is a proposed extension, not a result of this paper.

## Related Pages

- [[theory-and-constraints/wang-2026-beyond-frequency-dissonance-spectrum-for]] — primary evidence, configuration, full results, and archive gap.
- [[concepts/music-domain-inductive-biases]] — explicit relational priors versus learned architectural biases.
- [[concepts/music-theory-probing]] — constructing a theory quantity differs from measuring its recoverability inside a model.
