# PREREGISTRATION — Target 3: Marmoset same-brain ruler test (Brain/MINDS)

Atharva Chourey Lab · registered 2026-11-17, BEFORE any data download.
Source dataset: Brain/MINDS marmoset MRI (Hata et al. 2023, *Sci Data* 10:221),
dataportal.brainminds.jp, DOI 10.24475/bminds.mri.thj.4624, CC-BY 4.0.
In vivo cohort NA216 (n=455 scanned; 216 standard-brain subset) and ex vivo
cohort eNA91 (n=91), the ex vivo animals drawn from the in vivo cohort.

## Background

The lab's Two Rulers result (Brain Catalogue thread): histological hippocampus
volumes run ~1.6× MRI-label volumes across 343 species — but that comparison is
cross-study and cross-animal, so it can always be dismissed as cohort or
pipeline differences. The Brain/MINDS marmoset collection is, per the sweep,
the only open dataset where the SAME brains were scanned in vivo and ex vivo,
with per-individual label files. That design isolates the preparation ruler
(fixation, extraction, postmortem state) from every other confound.

## Hypothesis

H1: Fixation/preparation shifts measured brain volumes in the same brain by a
systematic, non-trivial amount: the median paired |in-vivo − ex-vivo| shift
exceeds 5% of volume for total brain, or 10% for hippocampus.

H0 (null): paired shifts are small (<2% across regions) — the preparation
ruler is honest and the Two Rulers gap must live elsewhere (sectioning,
shrinkage correction, rescaling), not in fixation state per se.

## Decide-test (registered)

- Pair eNA91 ex vivo individuals to their in vivo scans via the dataset's
  subject identifiers; verify pairing resolves to the same individuals.
- Pilot first: ~5 pairs, end-to-end pipeline (download → nibabel volumes →
  paired shifts), file sizes checked before any bulk pull.
- Main test: ≥30 paired animals. Volumes from the shipped per-individual
  label NIfTIs (volume = nonzero/label voxel count × voxel volume from each
  file's own header), computed identically for in vivo and ex vivo.
- LIVE verdict if median paired shift > 5% (total brain) OR > 10%
  (hippocampus). Report median, IQR, and per-structure signed shifts
  (ex vivo − in vivo, % of in vivo) for every labelled structure, not only
  the headline two.

## Kill conditions (registered)

- K1: Pairing identifiers do not resolve eNA91 animals to the same
  individuals in the in vivo cohort → target dead as designed; report the
  gate, do not substitute a cross-sectional comparison and call it this test.
- K2: Median paired shift < 2% across ALL labelled regions at n ≥ 30 → no
  ruler gap; publish the null, target closed.
- K3 (access): If the portal requires registration/login that cannot be
  completed without the user's credentials, stop at the gate and report it
  precisely. No workarounds.

## Registered contingencies

- If hippocampus is NOT among the shipped per-individual labels, the
  decide-test re-scopes to total brain + the structures that ARE labelled,
  and the change is recorded as a written amendment in RESULTS.md — never
  silently swapped.
- Cross-pipeline discipline: in vivo and ex vivo volumes are compared ONLY
  within this dataset and this pipeline. Nothing here is pooled with Brain
  Catalogue numbers.

## Disk discipline

- Check file sizes before downloading anything beyond metadata.
- Pilot (~5 pairs) before any bulk pull.
- HARD CAP: 10 GB total under this project folder. If the ≥30-pair set
  would exceed it, stop and report rather than exceeding.

## What would make this havoc-grade

Requirement check against BYPASS_THE_LEADERBOARD.md: (1) load-bearing —
marmoset is the field's translational primate model and its published brain
numbers come overwhelmingly from fixed brains; (2) audit-shaped — it checks
the preparation ruler, it does not mint a new atlas; (3) scale — first
same-brain paired test at n≈91 available, vs zero published paired tests;
(4) one-sentence shock, stateable now: "The same 91 brains, scanned alive
and dead, don't agree"; (5) this document, with K1/K2 kills, precedes data.
