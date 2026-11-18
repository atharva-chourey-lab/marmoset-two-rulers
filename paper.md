# One Brain, Two Rulers: The Hippocampal Formation Measures 21% Smaller After Perfusion Fixation in the Same Marmoset Brains

Author: Atharva Chourey
Affiliation: Atharva Chourey Lab (independent research lab)

*Manuscript in preparation — not yet peer-reviewed.*

## Abstract

Comparative neuroanatomy pools brain volumes measured in different states of the same organ — alive, fixed, sectioned — as if the state were immaterial. This paper tests that assumption in the one design that isolates it: the same brain, scanned in vivo and again ex vivo after perfusion fixation, with the same atlas and the same pipeline. Using the Brain/MINDS marmoset MRI dataset (Hata et al., 2023; NA216/eNA91), we pre-registered a paired test with fixed thresholds before any download, and measured all 30 animals that carry both an in-vivo and an ex-vivo label image under the shipped Label052 (Hashikawa) atlas. The hippocampal formation reads a median 21.0% smaller in the fixed brain (IQR −23.1% to −17.6%; all 30 pairs negative), against a registered threshold of 10%; total labelled gray matter reads 10.4% smaller (IQR −12.3% to −7.3%; 28 of 30 pairs negative), against a registered threshold of 5%. Both registered thresholds were crossed, and none of the registered kill conditions fired. The shift is structure-dependent, not a uniform scale factor: 72 of 104 labels shrink by more than 2% at the median, while 17 read larger ex vivo, concentrated at the frontal/olfactory pole. A paired preparation effect of ~21% in the hippocampal formation is the same order as the cross-archive discrepancies the field argues about; it cannot be dismissed as cohort noise.

*Keywords:* marmoset; Brain/MINDS; perfusion fixation; hippocampal formation; MRI volumetry; pre-registration; measurement

## 1. Introduction: the state of the brain is part of the measurement

Brain volumes enter comparative neuroanatomy as if they were properties of species. They are, in fact, properties of specimens in particular states, measured by particular pipelines: an MRI of a living brain, an MRI of the same brain after perfusion fixation and dissection, a histological series after sectioning and shrinkage correction. The lab's audit of a comparative neuroanatomy archive (Atharva Chourey Lab, 2026, *Lost Atlas*) found that the two great compilations of hippocampus volumes — the shrinkage-corrected histological lineage and the MRI atlas — disagree by a factor of ~1.6× across 343 paired species. A disagreement of that size invites two readings. It may be biology. Or it may be the rulers: the possibility that preparation and measurement state move a volume by as much as the effects the field debates.

Cross-archive comparisons cannot separate those readings, because the archives differ in cohort, species sampling, era and pipeline all at once. What separates them is a paired design: the same brain measured in two states, everything else held constant. If the preparation ruler is negligible, paired in-vivo and ex-vivo volumes should agree to within a few percent. If it is not, the paired shift measures it directly, with cohort differences excluded by construction.

The Brain/MINDS marmoset programme makes that design possible. Its open MRI dataset (Hata et al., 2023) contains both an in-vivo cohort (NA216) and an ex-vivo cohort (eNA91) of common marmosets, with per-individual label images under a single shipped atlas, and an explicit in-vivo/ex-vivo pairing in the dataset's own individual-information sheets. This paper pre-registered a paired test on that dataset — thresholds, kill conditions, and scope amendments declared under the registration's own rules — and measured every animal the dataset pairs.

The result is that the same marmoset brains, scanned alive and after perfusion fixation, do not agree: the hippocampal formation reads ~21% smaller in the fixed brain, and total labelled gray matter ~10% smaller. Section 2 describes the dataset, the pairing and the registered test. Section 3 reports the headline shifts and the per-structure pattern. Section 4 states carefully what this does and does not show — in particular, what it does not do is explain the cross-archive Two Rulers gap, whose direction and mechanism are different; what it kills is the dismissal that preparation effects are negligible.

## 2. Methods

### 2.1 Data: Brain/MINDS marmoset MRI (NA216 / eNA91)

The data are the Brain/MINDS marmoset MRI dataset of Hata et al. (2023, *Scientific Data* 10:221): in-vivo cohort NA216 and ex-vivo cohort eNA91, dataset DOI 10.24475/bminds.mri.thj.4624, CC-BY 4.0. The dataset is a git-annex repository at datasets.brainminds.jp; per-individual label files were served directly by the portal's media endpoint with no registration or login at any point. The whole project download — 60 label files plus metadata — was 31 MB, against a registered cap of 10 GB.

Labels are the dataset's shipped Label052 images: the Hashikawa atlas merged to 52 regions per hemisphere (104 labels), warped into each animal's native structural space. The hippocampal formation is labels 38 (left) and 90 (right); the subiculum (labels 25/77) is shipped separately and is kept separate throughout. In-vivo labels live on a 0.27 mm isotropic grid and ex-vivo labels on a 0.10 mm isotropic grid; every volume was computed from its own file's header zooms, identically on both sides — the lab's standing rule for cross-grid volumetry.

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

In absolute volumes, the medians across the 30 pairs move from 4.46 cm³ in vivo to 4.00 cm³ ex vivo for total labelled gray matter (median paired shift −10.4%, mean −9.0%, range −16.0% to +7.0%), and from 0.272 cm³ to 0.217 cm³ for the hippocampal formation (median paired shift −21.0%, mean −20.7%, range −31.0% to −6.4%). The hippocampal result is unanimous in direction: every one of the 30 animals reads smaller after fixation, left (−20.3%) and right (−21.0%) alike. The separately shipped subiculum shifts less (left −8.3%, right −11.6% at the median).

### 3.2 The shift is structure-dependent, not a scale factor

Across all 104 labels, the shift is not a uniform shrinkage that a single correction constant could undo: 72 of 104 labels have a median shift below −2%, 15 sit within ±2%, and 17 read *larger* ex vivo. The largest shrinkages are subcortical and medial: substantia nigra (−29%/−26%), thalamus (−28%/−28%), amygdala (−27%/−25%), insular cortex (−26%/−26%), septal nucleus (−23%) and entorhinal cortex (−22%). The positive outliers cluster at the frontal/olfactory pole (olfactory bulb right +31%, olfactory nucleus +17%/+20%, ventral lateral prefrontal cortex +21%/+22%, orbitofrontal cortex +10%/+11%). We flag these as most plausibly atlas-warp boundary behaviour at the brain's edge in the ex-vivo space rather than tissue growth; this is the main label-level caveat of the study, and it does not touch the headline structures, which sit deep inside the brain and move unanimously in the opposite direction.

## 4. Discussion

### 4.1 What this shows

The preparation ruler is real, and it is large, in the one design that isolates it: same brain, same atlas, same lab pipeline — only the state of the brain (alive, versus perfusion-fixed in 4% PFA, dissected and immersed) differs. A ~21% paired shift in the hippocampal formation is not a subtlety of technique; it is the same order as the cross-species effects comparative neuroanatomy argues about, and it is measured here with cohort differences excluded by construction.

### 4.2 What this does not show

This result does not, by itself, explain the cross-species Two Rulers gap (~1.6×, histological compilation values larger than MRI-atlas values). Here, fixation makes MRI volumes *smaller*; the histology side of the Two Rulers comparison involves sectioning and Stephan-style shrinkage correction and rescaling on top of fixation, a different and partly opposing chain of operations. What the paired test removes is a premise, not a conclusion: the premise that preparation effects are negligible, or that discrepancies between archives can be waved away as cohort noise. They cannot — the paired effect is measured, and it is big.

### 4.3 Limitations

Four limits are declared. First, the paired n is exactly the registered minimum of 30: the dataset supplies no more labelled pairs, so the estimate's precision is what 30 pairs give. Second, this is one species, one atlas and one pipeline; the structure-dependence of the shift (§3.2) warns against exporting the −21% figure to other structures, species or preparation protocols as a constant. Third, under Amendment A2 the total-brain arm is a labelled-gray-matter total; white matter is outside the test, and the −10.4% figure must be quoted as a gray-matter figure. Fourth, the positive outliers at the frontal/olfactory pole are interpreted, not resolved: they are flagged as probable atlas-warp boundary behaviour, and a label-level re-examination under a different atlas would be needed to settle them. None of these limits touches the headline comparison, which is paired, unanimous in direction, and an order of magnitude above its registered kill bound.

## 5. Data and code availability

The Brain/MINDS marmoset MRI dataset (Hata et al., 2023) is openly available under CC-BY 4.0 at DOI 10.24475/bminds.mri.thj.4624; no registration or login was required. The full pipeline for this study (`pairs_pipeline.py` — pairing from the dataset's own sheets, downloads via the portal media endpoint, nibabel volumetry from per-file header zooms) and all outputs (`outputs/paired_volumes_n30.csv`, `outputs/per_label_volumes_n30.csv`, `outputs/per_structure_shift_n30.csv`) are retained in the lab's project record for this study, together with the pre-registration under which the test was run.

## References

- Hata, J. et al. (2023). Brain/MINDS marmoset MRI dataset (NA216 / eNA91). *Scientific Data* 10:221. Dataset DOI: 10.24475/bminds.mri.thj.4624. CC-BY 4.0.
- Atharva Chourey Lab (2026). *Shrinkage-corrected histological compilation values average ~1.6× MRI-atlas values: an audit of a comparative neuroanatomy archive.* Manuscript, Atharva Chourey Lab. https://github.com/atharva-chourey-lab/lost-atlas
