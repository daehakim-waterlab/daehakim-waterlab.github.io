# Figure for the blog post "An abrupt shift to a hotter, drier climate in the Western Eurasian Steppe" (2026-10-22).
# Soil moisture-atmosphere (SA) coupling experiment in Piao et al. (2026), Nature Geoscience,
# https://doi.org/10.1038/s41561-026-02125-8: seven CMIP6 models run fully coupled and with soil moisture prescribed
# to climatology (LS3MIP LFMIP-pdLC). In five of the seven models, interactive SA coupling explains about 24-44%
# of the warming trend and 37-68% of the PET increase over the Western Eurasian Steppe; a significant post-1990
# regime shift in summer SPEI appears in 5 of 7 coupled runs and in 0 of 7 runs with soil moisture prescribed.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-steppe-coupling.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
loop, off = "#b4532a", "#c9c7c1"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 5.6), facecolor=surf, gridspec_kw={"height_ratios": [1, 1]})

rng = [("Warming trend", 24, 44), ("Rise in evaporative\ndemand (PET)", 37, 68)]
for i, (name, lo, hi) in enumerate(rng):
    a.barh(i, hi - lo, 0.5, left=lo, color=loop)
    a.text(lo - 1.5, i, f"{lo}%", ha="right", va="center", fontsize=11, color=ink)
    a.text(hi + 1.5, i, f"{hi}%", ha="left", va="center", fontsize=11, color=ink)
a.set_yticks(range(len(rng))); a.set_yticklabels([r[0] for r in rng], fontsize=11); a.invert_yaxis()
a.set_xlim(0, 100); a.set_ylim(1.6, -0.6)
a.set_xlabel("Share explained by the soil moisture feedback (%)", color=ink2, fontsize=11)
a.set_title("a  Contribution of the feedback (5 of 7 models)", loc="left", fontsize=11.5, color=ink)
a.grid(axis="x", color=grid, lw=0.8)

runs = [("Soil moisture\ninteractive", 5, loop), ("Soil moisture\nfixed", 0, off)]
for i, (name, n, c) in enumerate(runs):
    for k in range(7):
        b.add_patch(plt.Rectangle((k + 0.12, i - 0.3), 0.76, 0.6, fc=c if k < n else "#ffffff", ec=c if n else ink2,
                                  lw=1.2))
    b.text(7.3, i, f"{n} of 7", ha="left", va="center", fontsize=11, color=ink)
b.set_xlim(0, 8.4); b.set_ylim(1.6, -0.6)
b.set_yticks(range(len(runs))); b.set_yticklabels([r[0] for r in runs], fontsize=11)
b.set_xticks([])
b.set_title("b  Models that show a post-1990 abrupt drying shift", loc="left", fontsize=11.5, color=ink)

for ax in (a, b):
    ax.set_facecolor(surf); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
b.spines["bottom"].set_visible(False)
fig.suptitle("Switch off the soil moisture feedback and the abrupt shift disappears", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-steppe-coupling.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-steppe-coupling.png")
