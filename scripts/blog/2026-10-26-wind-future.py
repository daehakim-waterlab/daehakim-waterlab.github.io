# Figure for the blog post "Wind makes ecosystems spend more water per unit of carbon" (2026-10-26).
# CMIP6 results reported in Wang et al. (2026), Nature Climate Change, https://doi.org/10.1038/s41558-026-02781-z
# (Table 1 and text), historical 1995-2014 and SSP scenarios 2081-2100, mean over land grid cells:
# (a) trend in near-surface wind speed (x 1e-3 m s-1 yr-1): historical -0.723, SSP1-2.6 +0.009, SSP2-4.5 -0.616,
#     SSP5-8.5 -1.140;
# (b) trend in WUE caused by wind-speed change, dWUE/dWind x wind trend (x 1e-3 gC kg-1 H2O yr-2):
#     historical 0.172, SSP1-2.6 0.034, SSP2-4.5 -0.003, SSP5-8.5 0.169.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-26-wind-future.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
cols = ["#8a8780", "#7fa9de", "#e0a35a", "#b4532a"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

labels = ["Historical\n1995–2014", "SSP1-2.6\n2081–2100", "SSP2-4.5\n2081–2100", "SSP5-8.5\n2081–2100"]
wind = [-0.723, 0.009, -0.616, -1.140]
wue = [0.172, 0.034, -0.003, 0.169]
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 5.0), facecolor=surf, sharey=True)
for ax, vals, title, xlab, fmt in [(a, wind, "a  Trend in wind speed", "×10⁻³ m/s per year", "{:+.2f}"),
                                   (b, wue, "b  WUE change caused by wind", "×10⁻³ gC/kg per year²", "{:+.3f}")]:
    for i, v in enumerate(vals):
        ax.barh(i, v, 0.6, color=cols[i])
        off = 0.04 * (max(vals) - min(vals) + 0.2)
        ax.text(v + (off if v >= 0 else -off), i, fmt.format(v).replace("-", "−"), ha="left" if v >= 0 else "right",
                va="center", fontsize=10, color=ink)
    ax.axvline(0, color=ink2, lw=1)
    ax.set_title(title, loc="left", fontsize=11.5, color=ink)
    ax.set_xlabel(xlab, color=ink2, fontsize=10)
    ax.set_facecolor(surf); ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
a.set_xlim(-1.75, 0.45); b.set_xlim(-0.09, 0.27)
a.set_yticks(range(4)); a.set_yticklabels(labels, fontsize=10); a.invert_yaxis()
fig.suptitle("How much stilling lifts WUE depends on emissions", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-26-wind-future.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-26-wind-future.png")
