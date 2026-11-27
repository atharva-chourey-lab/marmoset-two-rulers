# One Brain, Two Rulers: The Hippocampal Formation Measures 21% Smaller After Perfusion Fixation in the Same Marmoset Brains

Author: Atharva Chourey
Affiliation: Atharva Chourey Lab (independent research lab)

*Manuscript in preparation — not yet peer-reviewed.*

## Abstract

Comparative neuroanatomy pools brain volumes measured in different states of the same organ — alive, fixed, sectioned — as if the state were immaterial. This paper tests that assumption in the one design that isolates it: the same brain, scanned in vivo and again ex vivo after perfusion fixation, with the same atlas and the same pipeline — the paired design first run by Yoshimaru et al. (2024) at n = 12, run here at n = 30 on the public Brain/MINDS paired label set, under a pre-registration fixed before any download. Using the Brain/MINDS marmoset MRI dataset (Hata et al., 2023; NA216/eNA91), we pre-registered a paired test with fixed thresholds before any download, and measured all 30 animals that carry both an in-vivo and an ex-vivo label image under the shipped Label052 (Hashikawa) atlas. The hippocampal formation reads a median 21.0% smaller in the fixed brain (IQR −23.1% to −17.6%; all 30 pairs negative), against a registered threshold of 10%; total labelled gray matter reads 10.4% smaller (IQR −12.3% to −7.3%; 28 of 30 pairs negative), against a registered threshold of 5%. Both registered thresholds were crossed, and none of the registered kill conditions fired. The shift is structure-dependent, not a uniform scale factor: 73 of 104 labels shrink by more than 2% at the median, while 19 read larger ex vivo, concentrated at the frontal/olfactory pole. A paired preparation effect of ~21% in the hippocampal formation is the same order as the cross-archive discrepancies the field argues about; it cannot be dismissed as cohort noise.

*Keywords:* marmoset; Brain/MINDS; perfusion fixation; hippocampal formation; MRI volumetry; pre-registration; measurement

## 1. Introduction: the state of the brain is part of the measurement

Brain volumes enter comparative neuroanatomy as if they were properties of species. They are, in fact, properties of specimens in particular states, measured by particular pipelines: an MRI of a living brain, an MRI of the same brain after perfusion fixation and dissection, a histological series after sectioning and shrinkage correction. The lab's audit of a comparative neuroanatomy archive (Atharva Chourey Lab, 2026, *Lost Atlas*) found that the two great compilations of hippocampus volumes — the shrinkage-corrected histological lineage and the MRI atlas — disagree by a factor of ~1.6× across 343 paired species. A disagreement of that size invites two readings. It may be biology. Or it may be the rulers: the possibility that preparation and measurement state move a volume by as much as the effects the field debates.

Cross-archive comparisons cannot separate those readings, because the archives differ in cohort, species sampling, era and pipeline all at once. What separates them is a paired design: the same brain measured in two states, everything else held constant. If the preparation ruler is negligible, paired in-vivo and ex-vivo volumes should agree to within a few percent. If it is not, the paired shift measures it directly, with cohort differences excluded by construction.

The paired design itself is not new: Yoshimaru et al. (2024, *Scientific Reports* 14, 26901) scanned 12 marmosets in vivo and ex vivo after perfusion fixation, using the Hashikawa 52-region atlas, and reported significant shrinkage in whole brain, gray matter, white matter and cerebellum (ex vivo/in vivo ≈ 0.83–0.86), with a significant hippocampal-formation reduction plotted but not quantified in text (≈ −12% read from their Fig. 3). The present study is a re-measurement at larger n on the public Brain/MINDS paired label set, by direct label counting rather than deformation fields; its hippocampal estimate (−21.0%) is larger than Yoshimaru's, a discrepancy attributable to estimator, protocol and cohort differences that we flag rather than resolve.

The Brain/MINDS marmoset programme makes that design possible. Its open MRI dataset (Hata et al., 2023) contains both an in-vivo cohort (NA216) and an ex-vivo cohort (eNA91) of common marmosets, with per-individual label images under a single shipped atlas, and an explicit in-vivo/ex-vivo pairing in the dataset's own individual-information sheets. This paper pre-registered a paired test on that dataset — thresholds, kill conditions, and scope amendments declared under the registration's own rules — and measured every animal the dataset pairs.

The result is that the same marmoset brains, scanned alive and after perfusion fixation, do not agree: the hippocampal formation reads ~21% smaller in the fixed brain, and total labelled gray matter ~10% smaller. Section 2 describes the dataset, the pairing and the registered test. Section 3 reports the headline shifts and the per-structure pattern. Section 4 states carefully what this does and does not show — in particular, what it does not do is explain the cross-archive Two Rulers gap, whose direction and mechanism are different; what it adds is a large-n, pre-registered estimate to the paired evidence (Yoshimaru et al., 2024) that preparation effects are not negligible.

## 2. Methods

### 2.1 Data: Brain/MINDS marmoset MRI (NA216 / eNA91)

The data are the Brain/MINDS marmoset MRI dataset of Hata et al. (2023, *Scientific Data* 10:221): in-vivo cohort NA216 and ex-vivo cohort eNA91, dataset DOI 10.24475/bminds.mri.thj.4624, CC-BY 4.0. The dataset is a git-annex repository at datasets.brainminds.jp; per-individual label files were served directly by the portal's media endpoint with no registration or login at any point. The whole project download — 60 label files plus metadata — was 31 MB, against a registered cap of 10 GB.

Labels are the dataset's shipped Label052 images: the Hashikawa atlas merged to 52 regions per hemisphere (104 labels), warped into each animal's native structural space. The hippocampal formation is labels 38 (left) and 90 (right); the subiculum (labels 25/77) is shipped separately and is kept separate throughout. One labelling subtlety matters for side-specific comparisons: in the shipped files, labels 1–52 sit on opposite sides in the in-vivo and ex-vivo images (verified from the NIfTI headers in all 30 pairs — label 38 lies on the opposite side of label 90 in the ex-vivo files relative to the in-vivo files). Throughout this paper, “left” follows the in-vivo header, and ex-vivo label IDs are remapped (k ↔ k+52) before any side-specific comparison. Bilateral and total figures are sums across both sides and are unaffected by the remapping. In-vivo labels live on a 0.27 mm isotropic grid and ex-vivo labels on a 0.10 mm isotropic grid; every volume was computed from its own file's header zooms, identically on both sides — the lab's standing rule for cross-grid volumetry.

### 2.2 Pairing

Pairing is documented in the dataset itself. The sheet `individual_information_exvivo.xlsx` carries an explicit "in vivo Data" column mapping each ex-vivo animal to its in-vivo counterpart (e.g. ex003 → i052); 31 of the 50 ex-vivo label filenames also carry the pair code as a suffix, and the filename suffixes agree with the sheet wherever both exist. No pairing was inferred by the lab.

### 2.3 The registered test, and two declared amendments

The test was registered on 2026-11-17, before any data download. The registered decide-test required ≥30 paired animals and fixed the verdict thresholds in advance: a LIVE verdict if the median paired shift exceeded 5% for total brain or 10% for the hippocampal formation. Three kill conditions were registered: K1, pairing unresolvable; K2, median paired shift below 2% across all labelled regions at n ≥ 30; K3, a login or registration gate on the data. None fired: the pairing is documented in the dataset's own sheets, the observed shifts are an order of magnitude above the K2 bound, and no gate was encountered.

Two scope amendments were declared under the registration's rules, after source inspection and before any volume was computed:

- **A1 — the paired labelled n is 30, not 91.** The ex-vivo cohort has 91 scans, but only 50 animals carry a Label052 image, and of those 50 exactly 30 have a documented in-vivo counterpart that also carries a label image. The registered decide-test required ≥30 pairs; the dataset supplies exactly 30. All 30 were measured; there was no sampling.
- **A2 — "total brain" is operationalised as total labelled gray matter.** Label052 covers gray-matter regions only, and no per-individual whole-brain mask ships in the dataset, so the registered total-brain arm is computed as the sum of all 104 labels on each side. This is stated, not hidden: the −10.4% figure reported below is a gray-matter total, and white matter is outside this test.

### 2.4 Confound check

The in-vivo→ex-vivo age gap is small (median 0.13 years, maximum 1.36 years) and every animal was adult. Any residual growth across that gap would push ex-vivo volumes *up*, opposite to the direction observed; growth cannot manufacture the headline shift.

## 3. Results

### 3.1 Headline: both registered thresholds crossed

| Registered test | Threshold | Result (n = 30 pairs) | Verdict |
|---|---|---|---|
| Total labelled gray matter (Amendment A2) | median shift > 5% | **−10.4%** (IQR −12.3 to −7.3; 28/30 pairs negative) | LIVE |
| Hippocampal formation (labels 38 + 90) | median shift > 10% | **−21.0%** (IQR −23.1 to −17.6; **30/30 pairs negative**) | LIVE |

In absolute volumes, the medians across the 30 pairs move from 4.46 cm³ in vivo to 4.00 cm³ ex vivo for total labelled gray matter (median paired shift −10.4%, mean −9.0%, range −16.0% to +7.0%), and from 0.272 cm³ to 0.217 cm³ for the hippocampal formation (median paired shift −21.0%, mean −20.7%, range −31.0% to −6.4%). The hippocampal result is unanimous in direction: every one of the 30 animals reads smaller after fixation, left (−22.0%) and right (−20.1%) alike. The separately shipped subiculum shifts less (left −12.4%, right −8.1% at the median).

### 3.2 The shift is structure-dependent, not a scale factor

Across all 104 labels, the shift is not a uniform shrinkage that a single correction constant could undo: 73 of 104 labels have a median shift below −2%, 12 sit within ±2%, and 19 read *larger* ex vivo. The largest shrinkages are subcortical and medial: substantia nigra (−30%/−27%), thalamus (−28%/−27%), amygdala (−27%/−24%), insular cortex (−26%/−25%), entorhinal cortex (−21%/−20%) and septal nucleus (−19%/−21%). The positive outliers cluster at the frontal/olfactory pole (olfactory bulb +9%/+20%, olfactory nucleus +22%/+15%, ventral lateral prefrontal cortex +15%/+29%, orbitofrontal cortex +10%/+12%). We flag these as most plausibly atlas-warp boundary behaviour at the brain's edge in the ex-vivo space rather than tissue growth; this is the main label-level caveat of the study, and it does not touch the headline structures, which sit deep inside the brain and move unanimously in the opposite direction.

## 4. Discussion

### 4.1 What this shows

The preparation ruler is real, and it is large, in the one design that isolates it (the paired design of Yoshimaru et al., 2024): same brain, same atlas, same lab pipeline — only the state of the brain (alive, versus perfusion-fixed in 4% PFA, dissected and immersed) differs. A ~21% paired shift in the hippocampal formation is not a subtlety of technique; it is the same order as the cross-species effects comparative neuroanatomy argues about, and it is measured here with cohort differences excluded by construction.

### 4.2 What this does not show

This result does not, by itself, explain the cross-species Two Rulers gap (~1.6×, histological compilation values larger than MRI-atlas values). Here, fixation makes MRI volumes *smaller*; the histology side of the Two Rulers comparison involves sectioning and Stephan-style shrinkage correction and rescaling on top of fixation, a different and partly opposing chain of operations. What the paired test adds is a large-n, pre-registered estimate to an existing line of paired evidence (Yoshimaru et al., 2024) that preparation effects are not negligible — and, with it, that discrepancies between archives cannot be waved away as cohort noise: the paired effect is measured, at n = 30, and it is big.

Prior paired evidence, for the record: Yoshimaru et al. (2024) ran this design first (n = 12, own cohort, deformation-field volumetry; compartment ratios ≈ 0.83–0.86, hippocampal formation significantly reduced at ≈ −12% read from their figure); the 2019 Brain/MINDS metric-distortion quantification (arXiv:1805.04975) put the fixation step at a median absolute local scale change of 6.9 ± 2.1% per axis across 15 Brain/MINDS brains, by Jacobian determinants rather than per-label volumes; and a 2025 paired study (*Magnetic Resonance in Medicine*, n = 2) found ~−10% whole-brain volume post-fixation. The present study is the largest paired estimate in that line, the only one on the public paired label set, and the only one by direct native-space label counting — and its hippocampal magnitude is ~9 points larger than Yoshimaru's, a discrepancy between estimators, protocols and cohorts that is itself unreported and unresolved.

### 4.3 Limitations

Four limits are declared. First, the paired n is exactly the registered minimum of 30: the dataset supplies no more labelled pairs, so the estimate's precision is what 30 pairs give. Second, this is one species, one atlas and one pipeline; the structure-dependence of the shift (§3.2) warns against exporting the −21% figure to other structures, species or preparation protocols as a constant. Third, under Amendment A2 the total-brain arm is a labelled-gray-matter total; white matter is outside the test, and the −10.4% figure must be quoted as a gray-matter figure. Fourth, the positive outliers at the frontal/olfactory pole are interpreted, not resolved: they are flagged as probable atlas-warp boundary behaviour, and a label-level re-examination under a different atlas would be needed to settle them. None of these limits touches the headline comparison, which is paired, unanimous in direction, and an order of magnitude above its registered kill bound.

## 5. Data and code availability

The Brain/MINDS marmoset MRI dataset (Hata et al., 2023) is openly available under CC-BY 4.0 at DOI 10.24475/bminds.mri.thj.4624; no registration or login was required. The full pipeline for this study (`pairs_pipeline.py` — pairing from the dataset's own sheets, downloads via the portal media endpoint, nibabel volumetry from per-file header zooms) and all outputs (`outputs/paired_volumes_n30.csv`, `outputs/per_label_volumes_n30.csv`, `outputs/per_structure_shift_n30.csv`) are retained in the lab's project record for this study, together with the pre-registration under which the test was run.

## References

- Hata, J. et al. (2023). Brain/MINDS marmoset MRI dataset (NA216 / eNA91). *Scientific Data* 10:221. Dataset DOI: 10.24475/bminds.mri.thj.4624. CC-BY 4.0.
- Yoshimaru, D., Tsurugizawa, T., Hayashi, N., Hata, J., Shibukawa, S., Hagiya, K., Oshiro, H., Kishi, N., Saito, K., Okano, H. & Okano, H.J. (2024). Relationship between regional volume changes and water diffusion in fixed marmoset brains: an in vivo and ex vivo comparison. *Scientific Reports* 14, 26901. DOI: 10.1038/s41598-024-78246-0.
- Multimodal cross-registration and quantification of metric distortions in whole brain histology of marmoset using diffeomorphic mappings (2019). arXiv:1805.04975.
- Investigating microstructural changes between in vivo and perfused ex vivo marmoset brains using oscillating gradient and b-tensor encoded diffusion MRI at 9.4 T (2025). *Magnetic Resonance in Medicine* 93(2), 788–802. DOI: 10.1002/mrm.30298.
- Atharva Chourey Lab (2026). *Shrinkage-corrected histological compilation values average ~1.6× MRI-atlas values: an audit of a comparative neuroanatomy archive.* Manuscript, Atharva Chourey Lab. https://github.com/atharva-chourey-lab/lost-atlas
