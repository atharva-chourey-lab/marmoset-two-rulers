# Sources Map — One Brain, Two Rulers (marmoset paired fixation test)

Author: Atharva Chourey
Affiliation: Atharva Chourey Lab (independent research lab)

*Manuscript in preparation — not yet peer-reviewed.*

This file maps every key number, verdict and reference in `paper.md` to the source file it was taken from. Nothing in the paper was taken from a source outside this list. Where a source gives a verdict without a number, the paper reports the verdict without a number.

## Primary sources

- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/PREREGISTRATION.md` — the registered test: committed 2026-11-17 BEFORE any data download. Decide-test (≥30 pairs; LIVE if median paired shift > 5% total brain or > 10% hippocampal formation), kill conditions K1–K3, 10 GB download cap.
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/RESULTS.md` — the run record: verdict, Phase 0 verification (pairing, labels, access route, file sizes), Amendments A1/A2, all headline and per-structure numbers, confound check, and the "what this does and does not show" assessment the paper's §4 follows.
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/outputs/paired_volumes_n30.csv` — per-pair total labelled gray-matter and hippocampal-formation volumes and shifts (30 rows). The paper's headline medians were recomputed from this file during the publication build and match RESULTS.md (−21.0%, −10.4%, n = 30).
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/outputs/per_structure_shift_n30.csv` — median/IQR shift per structure across all 104 labels (source of §3.2).
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/outputs/per_label_volumes_n30.csv` — per-pair volumes for all 104 labels.
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/pairs_pipeline.py` — the full pipeline (pairing from the dataset's own sheets; portal media-endpoint downloads; nibabel volumes from per-file header zooms).
- `~/workspace/brain-scan-comparison/projects/marmoset-pairs/meta/` — Label052 region list and both individual-information sheets (the pairing source).

## Key numbers and their sources

| Claim in paper | Value | Source file |
|---|---|---|
| Paired labelled animals | n = 30 (of 91 ex-vivo scans; 50 with Label052 images) | RESULTS.md, Amendments A1 |
| Hippocampal formation median paired shift | −21.0% (IQR −23.1 to −17.6; 30/30 pairs negative; mean −20.7%; range −31.0% to −6.4%) | RESULTS.md, Numbers; paired_volumes_n30.csv (recomputed) |
| Hippocampal formation median volumes | 0.272 cm³ in vivo → 0.217 cm³ ex vivo; left −20.3%, right −21.0% | RESULTS.md, Numbers |
| Total labelled gray matter median paired shift | −10.4% (IQR −12.3 to −7.3; 28/30 pairs negative; mean −9.0%; range −16.0% to +7.0%) | RESULTS.md, Numbers; paired_volumes_n30.csv (recomputed) |
| Total labelled gray matter median volumes | 4.46 cm³ in vivo → 4.00 cm³ ex vivo | RESULTS.md, Numbers |
| Subiculum median shift | left −8.3%, right −11.6% | RESULTS.md, Numbers |
| Registered thresholds | LIVE if median shift > 5% (total) or > 10% (hippocampal formation) | PREREGISTRATION.md, Decide-test |
| Kill conditions | K1 pairing unresolved — not triggered; K2 shift < 2% everywhere — not triggered; K3 login gate — not triggered | RESULTS.md, verdict block |
| Label counts by shift band | 72/104 labels median < −2%; 15 within ±2%; 17 larger ex vivo | RESULTS.md, Numbers (per-structure pattern) |
| Largest shrinkages | substantia nigra −29/−26%; thalamus −28/−28%; amygdala −27/−25%; insular cortex −26/−26%; septal nucleus −23%; entorhinal cortex −22% | RESULTS.md, Numbers |
| Positive outliers | olfactory bulb R +31%; olfactory nucleus +17/+20%; ventral lateral PFC +21/+22%; orbitofrontal +10/+11% — flagged in the source as most plausibly atlas-warp boundary behaviour | RESULTS.md, Numbers |
| Age gap (confound check) | median 0.13 yr, max 1.36 yr; all animals adult | RESULTS.md, Numbers |
| Grids | in vivo 0.27 mm isotropic; ex vivo 0.10 mm isotropic; volumes from each file's own header zooms | RESULTS.md, Amendments |
| Download size | 60 label files + metadata = 31 MB (registered cap 10 GB) | RESULTS.md, Phase 0 verification |
| Dataset identity | Brain/MINDS marmoset MRI NA216/eNA91; Hata et al. 2023, *Sci Data* 10:221; DOI 10.24475/bminds.mri.thj.4624; CC-BY 4.0 | RESULTS.md, header |
| Two Rulers context (~1.6×, 343 species) | the lab's archive audit | RESULTS.md, "What this does and does not show"; lost-atlas manuscript |

## Novelty and framing notes

- The paper claims a paired, pre-registered measurement of the in-vivo→ex-vivo shift in this dataset — nothing wider. It does **not** claim to explain the cross-archive Two Rulers gap; §4.2 carries the source record's own scoping (fixation shrinks MRI volumes; the histology side involves sectioning plus shrinkage correction/rescaling).
- Amendment A2 is carried in the paper wherever the gray-matter total is quoted: the −10.4% figure is a labelled-gray-matter total, and white matter is outside the test.
- The frontal/olfactory positive outliers are reported with the source record's caveat attached, not silently dropped.
