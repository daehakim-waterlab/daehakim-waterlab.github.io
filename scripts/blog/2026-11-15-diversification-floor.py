# Figure for the blog post "Carbon at risk: putting a number on how much stored carbon might leak back" (2026-11-15).
# Why correlation limits diversification. For K projects with equal loss variance sigma^2 and common pairwise
# correlation rho, the variance of the portfolio-average loss is sigma^2 (1 - rho) / K + rho sigma^2 (the formula used
# by Lee et al. 2026, Nature Climate Change, https://doi.org/10.1038/s41558-026-02785-9). The figure plots the
# standard deviation of the portfolio-average loss relative to a single project, sqrt((1 - rho) / K + rho).
# rho = 0.07 is the median pairwise correlation of annual burned area between 1-degree cells in California reported in
# the paper. This is an analytical illustration, not a reproduction of the paper's simulations.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-15-diversification-floor.py
import os, matplotlib
import numpy as np
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

K = np.arange(1, 201)
cases = [(0.0, "#8a8780", "independent"), (0.07, "#2e8b57", "ρ = 0.07 (California median)"),
         (0.25, "#2a78d6", "ρ = 0.25"), (0.5, "#b4532a", "ρ = 0.5")]
fig, ax = plt.subplots(figsize=(6.6, 4.4), facecolor=surf); ax.set_facecolor(surf)
for rho, c, lab in cases:
    ax.plot(K, np.sqrt((1 - rho) / K + rho), color=c, lw=2.2, label=lab)
    if rho > 0:
        ax.axhline(np.sqrt(rho), color=c, lw=0.9, ls=(0, (3, 3)))
ax.text(196, np.sqrt(0.07) + 0.035, "floor = √ρ", ha="right", fontsize=9.2, color="#2e8b57")
ax.set_xscale("log"); ax.set_xlim(1, 200); ax.set_ylim(0, 1.05)
ax.set_xticks([1, 2, 5, 10, 20, 50, 100, 200]); ax.set_xticklabels(["1", "2", "5", "10", "20", "50", "100", "200"])
ax.tick_params(labelsize=9.5)
ax.set_xlabel("Number of projects in the portfolio (log scale)", color=ink2, fontsize=10.5)
ax.set_ylabel("Spread of portfolio loss\n(relative to one project)", color=ink2, fontsize=10.5)
ax.legend(frameon=False, fontsize=9.3, loc="upper right")
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Correlated risks put a floor under diversification", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-15-diversification-floor.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-15-diversification-floor.png")
