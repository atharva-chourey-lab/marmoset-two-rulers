# One Brain, Two Rulers: The Hippocampal Formation Measures 21% Smaller After Perfusion Fixation in the Same Marmoset Brains

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24409374.svg)](https://doi.org/10.5281/zenodo.24409374)

Neuroanatomy · 2026

Author: Atharva Chourey
Affiliation: Atharva Chourey Lab (independent research lab)

*Manuscript — not yet peer-reviewed.*

## Abstract

Comparative neuroanatomy pools brain volumes measured in different states of the same organ — alive, fixed, sectioned — as if the state were immaterial. This paper tests that assumption in the one design that isolates it: the same brain, scanned in vivo and again ex vivo after perfusion fixation, with the same atlas and the same pipeline — the paired design first run by Yoshimaru et al. (2024) at n = 12, run here at n = 30 on the public Brain/MINDS paired label set, under a pre-registration fixed before any download. Using the Brain/MINDS marmoset MRI dataset (Hata et al., 2023; NA216/eNA91), we pre-registered a paired test with fixed thresholds before any download, and measured all 30 animals that carry both an in-vivo and an ex-vivo label image under the shipped Label052 (Hashikawa) atlas. The hippocampal formation reads a median 21.0% smaller in the fixed brain (IQR −23.1% to −17.6%; all 30 pairs negative), against a registered threshold of 10%; total labelled gray matter reads 10.4% smaller (IQR −12.3% to −7.3%; 28 of 30 pairs negative), against a registered threshold of 5%. Both registered thresholds were crossed, and none of the registered kill conditions fired. The shift is structure-dependent, not a uniform scale factor: 72 of 104 labels shrink by more than 2% at the median, while 17 read larger ex vivo, concentrated at the frontal/olfactory pole. A paired preparation effect of ~21% in the hippocampal formation is the same order as the cross-archive discrepancies the field argues about; it cannot be dismissed as cohort noise.

*Keywords:* marmoset; Brain/MINDS; perfusion fixation; hippocampal formation; MRI volumetry; pre-registration; measurement

## Key results

- **Hippocampal formation: −21.0% after fixation** — median paired shift (IQR −23.1% to −17.6%), with all 30 of 30 pairs negative; median volumes 0.272 cm³ in vivo → 0.217 cm³ ex vivo. Registered threshold was 10%.
- **Total labelled gray matter: −10.4%** — median paired shift (IQR −12.3% to −7.3%), 28 of 30 pairs negative; 4.46 cm³ → 4.00 cm³. Registered threshold was 5%. (Declared scope, Amendment A2: the shipped atlas labels gray matter only, so this arm is a labelled-gray-matter total; white matter is outside the test.)
- **Pre-registered end to end** — thresholds and three kill conditions were committed before any download; none of the kills fired, and the paired n (30) is exactly what the dataset supplies, with no sampling.
- **Structure-dependent, not a scale factor** — 72 of 104 labels shrink by more than 2% at the median; the deepest shifts are substantia nigra (−29%/−26%), thalamus (−28%/−28%) and amygdala (−27%/−25%), while 17 labels read larger ex vivo, concentrated at the frontal/olfactory pole and flagged as probable atlas-warp boundary behaviour.
- **Scoped claim** — the test shows the preparation ruler is real and large in a paired design. It does not by itself explain the cross-archive Two Rulers gap (~1.6×): fixation shrinks MRI volumes, while the histology side of that gap involves sectioning and shrinkage correction on top of fixation.
- **Prior art, on the record** — Yoshimaru et al. (2024, *Scientific Reports* 14, 26901) ran the paired design first, at n = 12 on their own cohort, and found significant shrinkage (hippocampal formation ≈ −12%, read from their Fig. 3). This study is the largest paired re-measurement — n = 30, public data, pre-registered, direct label counting — and finds a larger effect (−21.0%). Why the two estimates differ by ~9 points (estimator, protocol, cohort) is an open question, flagged in the paper rather than resolved.

## Read the paper

- [paper.md](paper.md) — full text (Markdown)
- [paper.pdf](paper.pdf) — full text (PDF)

## Sources and fidelity

Every quantitative claim in the paper is traced to its source file in [SOURCES.md](SOURCES.md). Novelty claims were checked against the published literature before release; where a prior work already held a claim, the paper says so and cites it. *Correction, 2026-11-18: an external review surfaced one prior the original check missed — Yoshimaru et al. (2024). The paper now cites it in §1, §4 and the references, and the claim is framed as what it is: the largest paired re-measurement, not the first paired test. The correction is recorded in NOVELTY-ADDENDUM-2026-11-18.md, included in this repository.*

## Licence

This work is licensed under a [Creative Commons Attribution 4.0 International Licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may share and adapt it with attribution to Atharva Chourey, Atharva Chourey Lab.

## Cite this work

Chourey, Atharva (Atharva Chourey Lab). Public manuscript record, v1.0.0-publication. Zenodo. https://doi.org/10.5281/zenodo.24409374
