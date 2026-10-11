---
title: "A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis"
authors: "Tina Raissi, Nhan Phan, Chenxiao Wang, and Mikko Kurimo"
year: 2026
doi: 10.48550/arXiv.2609.30075
category: other
source: raissi-2026-a-native-reference-phone-class.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/raissi-2026-a-native-reference-phone-class.pdf"
pdf_filename: raissi-2026-a-native-reference-phone-class.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper addresses interpretable automatic assessment of second-language pronunciation. Existing systems often output holistic proficiency scores without identifying acoustic-phonetic causes. The proposed method estimates pronunciation deviation without:

## Key Contributions

Core contribution:** construct a native-reference geometric space from self-supervised speech representations, then compare each learner’s context-dependent phone-class coordinates against native coordinates.

### 2. Method

#### Native reference geometry

**§2, p. 2:**

1. Extract frame-level representations \(H^\ell \in \mathbb{R}^{T \times D}\) from a self-supervised speech encoder.
2. Define context-dependent phone classes:
   - diphones: center phone plus left context;
   - triphones: center phone plus left and right context.
3. For each phone class \(p\), compute a centroid:

\[
\mu(p)=\frac{1}{|T_p|}\sum_{t\in T_p}h_t .
\]

4. Stack native centroids into \(M_{\text{nat}}\), subtract the global native mean, and compute rank-\(K\) SVD:

\[
\bar M_{\text{nat}}\approx U\Sigma V^\top.
\]

5. Use \(V\) as the native-reference basis and \(C_{\text{nat}}=U\Sigma\) as native phone-class coordinates.
6. For learner utterance \(r\):

\[
C^{r}_{L2}=(M^{r}_{L2}-\mathbf{1}\bar\mu_{\text{nat}}^\top)V.
\]

7. Compare only phone classes shared by native and learner speech:

\[
P_r^\star=P_{\text{nat}}\cap P^r_{L2}.
\]

8. Compute Euclidean, cosine, or diagonal Mahalanobis distance for each shared class and aggregate those distances at utterance level.

Two centroid strategies are tested:

- **center-unit averaging:** frames of the central phone only;
- **full-unit averaging:** frames from the full context-dependent unit.

The authors explicitly state that they do not train a predictor from distances to proficiency scores; they test whether raw distances correlate monotonically with hum

The complete evidence-grounded digest is in [`sources/raissi-2026-a-native-reference-phone-class.md`](../../sources/raissi-2026-a-native-reference-phone-class.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
