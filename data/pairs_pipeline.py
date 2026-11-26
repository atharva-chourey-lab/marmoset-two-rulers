#!/usr/bin/env python
"""Target 3 — marmoset same-brain ruler test (Brain/MINDS NA216/eNA91).

Downloads Label052 label NIfTIs for every ex vivo animal that (a) has a
label image and (b) has a documented in vivo counterpart in the dataset's
own individual-information sheets, computes per-label volumes on both
sides from each file's own header zooms, and writes paired-shift tables.

Route: datasets.brainminds.jp Gitea media endpoint (the /raw/ endpoint
serves git-annex pointer text; /media/ serves content). No login needed.
"""
import io, os, re, sys, time
import urllib.request
import numpy as np
import pandas as pd
import nibabel as nib

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
META = os.path.join(ROOT, "meta")
OUT = os.path.join(ROOT, "outputs")
for d in (DATA, META, OUT):
    os.makedirs(d, exist_ok=True)

MEDIA = "https://datasets.brainminds.jp/brainminds/MRI-NA216/media/branch/master"

def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as r:
        blob = r.read()
    if len(blob) < 1000 or blob[:2] != b"\x1f\x8b":
        raise RuntimeError(f"bad download {url}: {len(blob)} bytes, head={blob[:40]!r}")
    with open(dest, "wb") as f:
        f.write(blob)
    return dest

def label_volumes(path):
    im = nib.load(path)
    d = np.asanyarray(im.dataobj).astype(np.int32)
    vox = float(np.prod(im.header.get_zooms()[:3]))
    vals, counts = np.unique(d, return_counts=True)
    return {int(v): float(c) * vox / 1000.0 for v, c in zip(vals, counts) if v > 0}, vox

def main():
    ex = pd.read_excel(os.path.join(META, "individual_information_exvivo.xlsx"))
    inv = pd.read_excel(os.path.join(META, "Individual_information_invivo.xlsx"))
    inv_label = dict(zip(inv["In vivo Database Number"].astype(int), inv["Label Image"]))
    inv_age = dict(zip(inv["In vivo Database Number"].astype(int), inv["Age"]))

    pairs = []
    for _, row in ex.iterrows():
        excode = str(row["ex vivo Database Number"]).strip()
        if int(row["Label Image"]) != 1:
            continue
        iv = str(row["in vivo Data"]).strip()
        m = re.fullmatch(r"i(\d+)", iv)
        if not m:
            continue
        icode = int(m.group(1))
        if int(inv_label.get(icode, 0)) != 1:
            continue
        pairs.append((excode, icode, float(row["Age"]), inv_age.get(icode)))
    pairs.sort(key=lambda p: p[0])
    print(f"pairs with labels on both sides: {len(pairs)}")

    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(pairs)
    pairs = pairs[:limit]

    rows = []
    per_label = []
    for excode, icode, ex_age, in_age in pairs:
        exnum = excode[2:]
        # ex vivo filename: plain, or with _iNNN suffix (suffix == sheet mapping)
        ex_file = os.path.join(DATA, f"Label052_{excode}.nii.gz")
        if not os.path.exists(ex_file):
            suffixed = os.path.join(DATA, f"Label052_{excode}_i{icode:03d}.nii.gz")
            try:
                fetch(f"{MEDIA}/exvivo/e_Label052/Label052_{excode}_i{icode:03d}.nii.gz", suffixed)
                ex_file = suffixed
            except Exception:
                fetch(f"{MEDIA}/exvivo/e_Label052/Label052_{excode}.nii.gz", ex_file)
        in_file = os.path.join(DATA, f"Label052_{icode:03d}.nii.gz")
        fetch(f"{MEDIA}/invivo/i_Label052/Label052_{icode:03d}.nii.gz", in_file)

        ex_vols, ex_vox = label_volumes(ex_file)
        in_vols, in_vox = label_volumes(in_file)
        assert len(ex_vols) == 104 and len(in_vols) == 104, (excode, len(ex_vols), len(in_vols))

        tot_ex = sum(ex_vols.values()); tot_in = sum(in_vols.values())
        hip_ex = ex_vols.get(38, 0) + ex_vols.get(90, 0)
        hip_in = in_vols.get(38, 0) + in_vols.get(90, 0)
        rows.append(dict(ex=excode, i=icode, ex_age=ex_age, in_age=in_age,
                         gm_ex_cm3=tot_ex, gm_in_cm3=tot_in,
                         gm_shift_pct=100 * (tot_ex - tot_in) / tot_in,
                         hip_ex_cm3=hip_ex, hip_in_cm3=hip_in,
                         hip_shift_pct=100 * (hip_ex - hip_in) / hip_in if hip_in else np.nan))
        for lab in range(1, 105):
            per_label.append(dict(ex=excode, i=icode, label=lab,
                                  ex_cm3=ex_vols.get(lab, 0.0), in_cm3=in_vols.get(lab, 0.0)))
        print(f"{excode} (i{icode:03d}): GM in={tot_in:.3f} ex={tot_ex:.3f} "
              f"shift={rows[-1]['gm_shift_pct']:+.1f}%  HIP in={hip_in:.4f} ex={hip_ex:.4f} "
              f"shift={rows[-1]['hip_shift_pct']:+.1f}%")
        time.sleep(0.2)

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT, f"paired_volumes_n{len(df)}.csv"), index=False)
    pd.DataFrame(per_label).to_csv(os.path.join(OUT, f"per_label_volumes_n{len(df)}.csv"), index=False)
    print("\nn =", len(df))
    for col in ("gm_shift_pct", "hip_shift_pct"):
        s = df[col]
        print(f"{col}: median {s.median():+.2f}%  IQR [{s.quantile(.25):+.2f}, {s.quantile(.75):+.2f}]  "
              f"mean {s.mean():+.2f}%  range [{s.min():+.2f}, {s.max():+.2f}]")
    print("age gap (ex - in, yr): median", float((df.ex_age - df.in_age).median()))

if __name__ == "__main__":
    main()
