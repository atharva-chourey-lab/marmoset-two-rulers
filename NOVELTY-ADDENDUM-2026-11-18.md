# NOVELTY ADDENDUM — 2026-11-18: Yoshimaru et al. 2024

Scrub run 2026-11-18 (prompted by an external reviewer's critique), per the
lab's research-novelty-scrub protocol. Verdict first, then the prior, then
the seam.

## Verdict

**The reviewer's citation is real, and it lands.** Yoshimaru et al. (2024,
*Scientific Reports*) ran the paired same-brain in vivo / ex vivo marmoset
design before us — n = 12, the same Hashikawa 52-region atlas family,
hippocampal formation included and significantly shrunk — and published
numerical whole-brain / gray-matter / white-matter / cerebellum shrinkage
ratios. The phenomenon, the paired design, and a hippocampal-formation
result in the same direction are **already published**. Our paper
(*One Brain, Two Rulers*, marmoset-two-rulers) does not cite it anywhere;
the README statement that novelty was checked and priors cited is, for
this prior, not true. What survives is a larger-n (30 vs 12),
public-dataset, pre-registered re-measurement by a different estimator,
whose hippocampal magnitude (−21.0%) is substantially larger than the
~−12% readable from Yoshimaru's Fig. 3 — an incremental measurement
contribution, not a first discovery. The reviewer's "downgrade —
incremental, not a discovery" verdict is **fair** as applied to the
headline as currently framed.

## The claim (as registered and published)

In the Brain/MINDS marmoset MRI dataset (Hata et al. 2023, NA216/eNA91),
30 marmosets scanned in vivo and again ex vivo after perfusion fixation —
same brains, same shipped Label052 (Hashikawa) atlas, same pipeline — the
hippocampal formation reads a median 21.0% smaller ex vivo (30/30 pairs
negative), total labelled gray matter 10.4% smaller; the shift is
structure-dependent (thalamus / amygdala / substantia nigra ≈ −26 to
−28%); direction is shrinkage, so it does not explain the Two Rulers 1.6×
direction; its registered force is to kill the "preparation effects are
negligible / cohort noise" dismissal.

## Closest prior — verified at source

**Yoshimaru, D., Tsurugizawa, T., Hayashi, N., Hata, J., Shibukawa, S.,
Hagiya, K., Oshiro, H., Kishi, N., Saito, K., Okano, H. & Okano, H.J.
(2024). "Relationship between regional volume changes and water diffusion
in fixed marmoset brains: an in vivo and ex vivo comparison."
*Scientific Reports* 14, 26901. DOI 10.1038/s41598-024-78246-0.
Received 22 Nov 2023; published 6 Nov 2024. Open access (CC BY 4.0);
verified in the journal full text and PMC11541870.**

What it actually did and found:

- **Design: paired, same individual.** 12 common marmosets (1 male,
  11 female; 6.2 ± 2.1 yr) scanned in vivo and ex vivo at 9.4T after
  transcardial perfusion with 4% PFA — explicitly to exclude
  inter-individual differences. This is the design our paper presents as
  "the one design that isolates it."
- **Cohort: NOT the public Brain/MINDS paired dataset.** Their own RIKEN
  cohort (RIKEN BSI animal committee H27-2-307; animals also used in
  other experiments; mean in vivo → fixation interval 58.4 ± 38.2 days;
  brains then incubated in PFA 24 h, stored in PBS 14.1 ± 11.7 days,
  scanned in Fluorinert). Funded under the Brain/MINDS programme and
  co-authored by Junichi Hata — same programme umbrella, different
  animals, different (non-public) data, different pipeline.
- **Atlas: the same family as ours.** Regional volumes used "a predefined
  52 left and right brain structure atlas" citing Hashikawa, Nakatomi &
  Iriki (2015) — the Hashikawa atlas of which our Label052 (52
  regions/hemisphere) is the shipped Brain/MINDS merge. Volumes were
  computed from registration deformation fields (ANTs) with ITK-SNAP,
  not by direct voxel counting of shipped per-animal labels.
- **Numerical results (text):** ex vivo / in vivo volume ratios —
  whole brain 0.84 ± 0.24, gray matter 0.84 ± 0.23, white matter
  0.86 ± 0.24, cerebellum 0.83 ± 0.23 (i.e. ≈ −14 to −17%, with very
  large SDs), described as "homogeneous across the different brain
  regions" at this compartment level. All four compartments
  significantly reduced.
- **52 regions:** per-region in vivo vs ex vivo volumes are plotted in
  their Fig. 3 (no per-region numbers in text or tables; the word
  "hippocampus" appears nowhere in the article). The 10 regions named
  as *non*-significant are piriform cortex, entorhinal cortex, dorsal
  lateral prefrontal cortex, septal nucleus, gustatory cortex, secondary
  somatosensory cortex, superior temporal rostral area, posterior
  parietal area, caudate nucleus, superior colliculus — the
  **hippocampal formation is not among them, so its reduction was
  significant**, and it is plotted in Fig. 3 (right panel). Reading the
  Fig. 3 bars (figure-read estimate, not a reported value): hippocampal
  formation ≈ 137 mm³ in vivo → ≈ 121 mm³ ex vivo per hemisphere,
  **≈ −12%**; amygdala and thalamus likewise ≈ −10%. Their in vivo
  hippocampal-formation volume (≈137 mm³/hemisphere) matches ours
  (0.272 cm³ both hemispheres) almost exactly; the ex vivo values are
  where the studies diverge.
- **Aim:** the volumetry was in service of a diffusion question — axial
  diffusivity (AD) correlated with regional volume change in 40 of 52
  regions. No hippocampal-formation percentage is stated anywhere, and
  no connection is drawn to cross-archive / comparative-neuroanatomy
  volume compilations.

## Per-part grades

| Part | Grade | Prior that forces it |
|---|---|---|
| (a) Perfusion fixation shrinks marmoset brain regions at all | **Already published** | Yoshimaru et al. 2024 (paired, n = 12, all compartments significant); behind it Haga et al. 2019 and the rodent fixation literature Yoshimaru cites |
| (b) The specific paired same-brain −21.0% hippocampal-formation estimate at n = 30 | **Narrowed but open** | Yoshimaru 2024 holds the paired design, the atlas and a significant hippocampal-formation shrinkage (≈ −12% by Fig. 3) — the design and the direction are theirs. No prior states a hippocampal-formation % for the public Brain/MINDS paired label set, at any n; ours is n = 30 (2.5×), direct native-space label counting, pre-registered, and its magnitude is ~9 points larger — a discrepancy between estimators/protocols that is itself unreported |
| (c) Structure-dependence pattern across the labelled set | **Narrowed but open** | Non-uniformity as a qualitative fact is published (Yoshimaru's 10 non-significant regions; de Guzman et al.'s nonuniform mouse shrinkage, cited by Yoshimaru). Yoshimaru's compartment-level framing is actually "homogeneous," which sits in tension with our spread. Our quantitative 104-label pattern — subcortical ≈ −26 to −28%, 17 labels larger ex vivo at the frontal/olfactory pole — has not been reported |
| (d) Methodological implication for cross-archive comparisons (Two Rulers context) | **Open** | No prior connects paired fixation shrinkage to the histology-vs-MRI archive disagreement; Yoshimaru's frame is diffusion microstructure, the 2019 distortion paper's frame is histology reconstruction. This is an implication, not a measurement — its force narrows with (b), and it was never the part the headline sold |

## Other priors found on the widened search (one widening, per protocol)

- **O'Callaghan / Amos et al. line — "Multimodal cross-registration and
  quantification of metric distortions in whole brain histology of
  marmoset using diffeomorphic mappings"** (arXiv:1805.04975, 2019;
  RIKEN Brain/MINDS data, 15 brains): quantified the perfusion/fixation
  step on Brain/MINDS brains as a median absolute local scale change of
  6.9 ± 2.1% per axis, unidirectional shrinkage, via Jacobian
  determinants. Same-dataset-family fixation distortion, quantified in
  2019 — but Jacobian scale change, not per-label volumes, and no
  hippocampal-formation figure. Reinforces grade (a)/(b) narrowing.
- **"Investigating microstructural changes between in vivo and perfused
  ex vivo marmoset brains using oscillating gradient and b-tensor
  encoded diffusion MRI at 9.4 T," *Magnetic Resonance in Medicine*
  93(2):788–802 (2025), DOI 10.1002/mrm.30298:** n = 2, paired;
  structural MRI showed "an average volume reduction of about 10%"
  post-fixation. Whole-brain only; corroborates the phenomenon, touches
  no part of our specific estimates.
- **Yoshimaru et al. 2026, *Radiological Physics and Technology*
  19(2):666–673** (same 12 animals): fixation effects on structural
  connectivity; hippocampal formation among the most-affected regions
  (32 changed connections); shrinkage described as region-specific.
  Connectivity, not volumetry — no conflict with (b), support for the
  qualitative half of (c).

No closer prior than Yoshimaru 2024 was found.

## Surviving seam (one sentence)

What survives is the largest paired, pre-registered, direct label-count
estimate of fixation shrinkage on the public Brain/MINDS dataset — n = 30,
hippocampal formation −21.0%, with a quantitative 104-label pattern — as a
re-measurement that *disagrees in magnitude* with Yoshimaru et al. 2024's
deformation-based ≈ −12% at n = 12, not as the first demonstration that
fixation shrinks the marmoset brain or the first paired test of it.

## Exact wording changes required

**Paper (marmoset-two-rulers/paper.md):**

1. Abstract and §1: delete the implication that the paired design is new
   ("tests that assumption in the one design that isolates it" may stay
   as a statement about design logic only if Yoshimaru is cited in the
   same sentence). Insert, in §1 after the paired-design paragraph:
   > "The paired design itself is not new: Yoshimaru et al. (2024,
   > *Scientific Reports* 14, 26901) scanned 12 marmosets in vivo and ex
   > vivo after perfusion fixation, using the Hashikawa 52-region atlas,
   > and reported significant shrinkage in whole brain, gray matter,
   > white matter and cerebellum (ex vivo/in vivo ≈ 0.83–0.86), with a
   > significant hippocampal-formation reduction plotted but not
   > quantified in text (≈ −12% read from their Fig. 3). The present
   > study is a re-measurement at larger n on the public Brain/MINDS
   > paired label set, by direct label counting rather than deformation
   > fields; its hippocampal estimate (−21.0%) is larger than
   > Yoshimaru's, a discrepancy attributable to estimator, protocol and
   > cohort differences that we flag rather than resolve."
2. §4: add Yoshimaru et al. 2024, the 2019 Brain/MINDS metric-distortion
   quantification (arXiv:1805.04975), and the 2025 MRM paired study
   (~−10% whole-brain, n = 2) to the prior-work discussion; the claim
   "what it kills is the dismissal that preparation effects are
   negligible" must be softened to "adds a large-n, pre-registered
   estimate to an existing line of paired evidence (Yoshimaru et al.
   2024) that preparation effects are not negligible."
3. README.md: the sentence "Novelty claims were checked against the
   published literature before release; where a prior work already held
   a claim, the paper says so and cites it" is false for this prior —
   either correct the paper per (1)–(2) so the sentence becomes true, or
   amend the sentence. Correcting the paper is the right fix.

**Site / dashboard (featured finding #4 and profile bullet):**

4. Current text — "Thirty marmosets in the Brain/MINDS dataset were
   scanned in vivo and again ex vivo after perfusion fixation — the same
   brains, the same atlas, the same pipeline — under a test
   pre-registered before any download. The hippocampal formation reads a
   median 21.0% smaller in the fixed brain (all 30 pairs negative)" —
   carries no false "first" claim verbatim, but in context reads as a
   first demonstration. Append one sentence:
   > "Yoshimaru et al. (2024) first ran this paired comparison at n = 12
   > and found significant shrinkage (≈ −12% for the hippocampal
   > formation, read from their Fig. 3); this study re-measures it at
   > n = 30 on the public dataset and finds a larger effect."

**Headline framing:** "One Brain, Two Rulers" and the −21% figure may
stand as *our measurement*; any phrasing of the form "first paired test,"
"first demonstration that fixation shrinks the (marmoset) brain," or
"discovery that the same brain measures smaller after fixation" is
killed by Yoshimaru et al. 2024 and must not be used.

## Reviewer verdict — assessment

Fair. The phenomenon, the design, the atlas and the direction were all
published in 2024 (received Nov 2023 — before this lab existed); our
contribution is a bigger, public, pre-registered re-measurement with a
divergent magnitude and a finer pattern — precisely "incremental, not a
fundamentally new discovery." The one place the reviewer overstates:
"his precise estimates … may constitute an incremental contribution"
underplays that the two hippocampal estimates do not agree (−21.0% vs
≈ −12%) — reconciling *why* (deformation-field volumetry vs direct label
counting; 58-day interval and intervening experiments vs the public
dataset's protocol) is a genuine open question the addendum leaves on
the table, and the only part of this project that could still grow.
