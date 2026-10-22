# Figure for the blog post "An abrupt shift to a hotter, drier climate in the Western Eurasian Steppe" (2026-10-22).
# Summer (June-August) SPEI trends per decade reported in Piao et al. (2026), Nature Geoscience,
# https://doi.org/10.1038/s41561-026-02125-8:
#   (a) drying hotspots, 1991-2020 (CRU): Western Eurasian Steppe -0.43, North America -0.29, Mongolia -0.22;
#   (b) 1992-2010: observed mean -0.33; ensemble means MPI-GE (n = 100) -0.18, MIROC6 (n = 50) -0.14, CMIP6 (n = 18) -0.19.
# The ensemble mean is the externally forced response; the gap to the observed trend is attributed to internal variability.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-steppe-drying.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
dry, mid, forced = "#b4532a", "#d9a37f", "#8a8780"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 6.6), facecolor=surf, gridspec_kw={"height_ratios": [3, 4]})

hot = [("Western Eurasian\nSteppe", -0.43, dry), ("North America", -0.29, mid), ("Mongolia", -0.22, mid)]
for i, (name, v, c) in enumerate(hot):
    a.barh(i, v, 0.62, color=c)
    a.text(v - 0.01, i, f"{v:.2f}".replace("-", "\u2212"), ha="right", va="center", fontsize=11, color=ink)
a.set_yticks(range(len(hot))); a.set_yticklabels([h[0] for h in hot], fontsize=11); a.invert_yaxis()
a.set_title("a  Northern Hemisphere drying hotspots, 1991–2020", loc="left", fontsize=11.5, color=ink)

ens = [("Observed", -0.33, dry), ("MPI-GE\n(100 runs)", -0.18, forced), ("MIROC6\n(50 runs)", -0.14, forced),
       ("CMIP6\n(18 runs)", -0.19, forced)]
for i, (name, v, c) in enumerate(ens):
    b.barh(i, v, 0.62, color=c)
    b.text(v - 0.01, i, f"{v:.2f}".replace("-", "\u2212"), ha="right", va="center", fontsize=11, color=ink)
b.set_yticks(range(len(ens))); b.set_yticklabels([e[0] for e in ens], fontsize=11); b.invert_yaxis()
b.set_title("b  Abrupt drying, 1992–2010: observed vs forced response", loc="left", fontsize=11.5, color=ink)
b.text(-0.49, 2.0, "Ensemble means = forced response\n(42–58% of the observed trend);\nthe rest is internal variability",
       ha="left", va="center", fontsize=10, color=ink2, linespacing=1.35)

for ax in (a, b):
    ax.set_facecolor(surf); ax.set_xlim(-0.5, 0)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
b.set_xlabel("Trend in summer SPEI (per decade; negative = drier)", color=ink2, fontsize=11)
fig.suptitle("Where summers are drying fastest, and why", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-steppe-drying.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-steppe-drying.png")
