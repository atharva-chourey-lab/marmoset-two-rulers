# Data and code deposit — Marmoset paired in-vivo / ex-vivo volumetry

Atharva Chourey Lab (independent research lab). Deposit prepared 2026-11-25.

Underlying manuscript: "One Brain, Two Rulers: The Hippocampal Formation
Measures 21% Smaller After Perfusion Fixation in the Same Marmoset Brains"
(submission package prepared for *Brain, Behavior and Evolution*).

## Contents

| File | What it is |
|---|---|
| `paired_volumes_n30.csv` | Per-animal paired volumes (n = 30 pairs): total labelled gray matter and hippocampal formation, in vivo vs ex vivo, with signed shift %. |
| `per_label_volumes_n30.csv` | Per-label, per-animal volumes for all labelled structures, both states. |
| `per_structure_shift_n30.csv` | Per-structure median paired shift with quartiles (n = 30). |
| `pairs_pipeline.py` | The single pipeline used for both states: pairing from the dataset's own sheets, downloads via the portal media endpoint, nibabel volumetry from each file's own header zooms. |
| `PREREGISTRATION.md` | The pre-registration dated 2026-11-17, written before any data download, stating the hypothesis, thresholds (10% hippocampus / 5% total) and kill conditions. |

## Source data (not included)

The Brain/MINDS marmoset MRI dataset (Hata et al. 2023) is openly available
under CC BY 4.0 at DOI 10.24475/bminds.mri.thj.4624. The source label files
are not redistributed here; this deposit contains only the lab's derived
volumes, code and pre-registration.

## Headline results (from the deposited outputs)

- Hippocampal formation: median −21.0%, 30/30 pairs negative.
- Total labelled gray matter: median −10.4%, 28/30 pairs negative.
- Both registered thresholds crossed; no kill conditions fired.

## Correction — 2026-11-27 (side convention for per-structure shifts)

In the shipped Brain/MINDS Label052 files, labels 1–52 sit on opposite sides
in the in-vivo and ex-vivo images (verified from the NIfTI headers in all 30
pairs: the world-x centroid of label 38 minus label 90 is negative in every
in-vivo file and positive in every ex-vivo file). Side-specific comparisons
in `per_structure_shift_n30.csv` therefore remap ex-vivo label IDs
(k ↔ k+52), with "left" following the in-vivo header. The originally
deposited version of this file compared matching IDs without the remap;
its side-specific medians are superseded by the corrected file.
`paired_volumes_n30.csv` is unaffected (bilateral sums are invariant
under the swap), and `per_label_volumes_n30.csv` reports volumes per
shipped label ID, exactly as computed from the files.
