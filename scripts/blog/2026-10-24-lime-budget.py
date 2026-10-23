# Figure for the blog post "Farm lime turns out to be a carbon sink" (2026-10-24).
# Numbers reported in Suhrhoff et al. (2026), Nature 658, 113-118, https://doi.org/10.1038/s41586-026-11040-2,
# for the Mississippi River Basin:
# (a) CO2 emissions from soil acid-base reactions in 1980: ~20 MtCO2/yr with anthropogenic acidity and no lime
#     (reactive transport model SCEPTER), ~15 MtCO2/yr with lime added; lime emissions under the IPCC default
#     method ~7 MtCO2/yr and under the US national inventory ~3.5 MtCO2/yr.
# (b) Cumulative CO2 removal by lime, 1900-2015: ideal potential 0.444 (+/-0.050) GtCO2; realized, from excess river
#     bicarbonate flux, 0.401 (+/-0.091) GtCO2 (about 90%); realized, from SCEPTER, 0.22-0.37 GtCO2 (P to P-ET range).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-24-lime-budget.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
src, sink, acc = "#b4532a", "#2a78d6", "#a8a6a0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 7.2), facecolor=surf, gridspec_kw={"height_ratios": [1.15, 1]})

rows = [("Acid inputs, no lime\n(the counterfactual)", 20, src), ("Acid inputs + lime", 15, sink),
        ("IPCC default method\n(counts lime only)", 7, acc), ("US inventory\n(counts lime only)", 3.5, acc)]
for i, (name, v, c) in enumerate(rows):
    a.barh(i, v, 0.62, color=c)
    a.text(v + 0.3, i, f"≈{v:g}", ha="left", va="center", fontsize=11, color=ink)
a.set_yticks(range(len(rows))); a.set_yticklabels([r[0] for r in rows], fontsize=10.5); a.invert_yaxis()
a.set_xlim(0, 24)
a.set_xlabel("CO₂ from soil acid–base reactions in 1980 (Mt per year)", color=ink2, fontsize=10.5)
a.set_title("a  Lime lowers emissions relative to acid alone", loc="left", fontsize=11.5, color=ink)

cum = [("Ideal potential", 0.444, 0.444, 0.050, acc), ("Realized: river\nbicarbonate record", 0.401, 0.401, 0.091, sink),
       ("Realized: soil\nmodel range", 0.22, 0.37, None, sink)]
for i, (name, lo, hi, err, c) in enumerate(cum):
    if err is None:
        b.barh(i, hi - lo, 0.55, left=lo, color=c, alpha=0.55)
        b.text(hi + 0.012, i, "0.22–0.37", ha="left", va="center", fontsize=11, color=ink)
    else:
        b.barh(i, hi, 0.55, color=c)
        b.errorbar(hi, i, xerr=err, color=ink, capsize=4, lw=1.2)
        b.text(hi + err + 0.012, i, f"{hi:.2f}", ha="left", va="center", fontsize=11, color=ink)
b.set_yticks(range(len(cum))); b.set_yticklabels([c[0] for c in cum], fontsize=10.5); b.invert_yaxis()
b.set_xlim(0, 0.62)
b.set_xlabel("Cumulative CO₂ removed by lime, 1900–2015 (Gt)", color=ink2, fontsize=10.5)
b.set_title("b  About 90% of the potential has been realized", loc="left", fontsize=11.5, color=ink)

for ax in (a, b):
    ax.set_facecolor(surf); ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Liming and CO₂ in the Mississippi River Basin", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-24-lime-budget.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-24-lime-budget.png")
