# Figure for the blog post "Where our CO2 goes, and how much is left to emit" (2026-10-20).
# Data: 2024 fossil CO2 emissions by sector (shares of 36.3 GtCO2, Carbon Monitor) and their change
# from 2023, from Deng et al. (2025), Nat. Rev. Earth Environ. 6, 231-233, doi:10.1038/s43017-025-00658-x.
# Land-use change emissions in 2024 (1.3 GtC/yr = 4.8 GtCO2/yr) from Friedlingstein et al. (2026),
# Global Carbon Budget 2025, doi:10.5194/essd-18-3211-2026; shown separately because it comes from a
# different dataset. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-20-sector-shares.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
fossil, land = "#5b5a57", "#b07a3c"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

TOTAL = 36.3
rows = [  # sector, share of fossil CO2 in 2024 (%)
    ("Power", 38.7),
    ("Industry", 28.5),
    ("Ground transport", 18.7),
    ("Residential", 9.4),
    ("International shipping", 1.9),
    ("International aviation", 1.8),
    ("Domestic aviation", 1.0),
]
fig, ax = plt.subplots(figsize=(9, 6), facecolor=surf); ax.set_facecolor(surf)
for i, (name, s) in enumerate(rows):
    g = TOTAL * s / 100
    ax.barh(i, g, 0.62, color=fossil)
    ax.text(g + 0.2, i, f"{s:.1f}%  ({g:.1f} Gt)", va="center", fontsize=11.5, color=ink)
yl = len(rows) + 0.5
ax.barh(yl, 1.3 * 3.664, 0.62, color=land, hatch="//", edgecolor=surf, linewidth=0)
ax.text(1.3 * 3.664 + 0.2, yl, "4.8 Gt (separate dataset,\nnot in the 36.3 Gt total)", va="center",
        fontsize=10.5, color=ink2)
ax.axhline(len(rows) - 0.25, color=grid, lw=1.2)
ax.set_yticks(list(range(len(rows))) + [yl])
ax.set_yticklabels([r[0] for r in rows] + ["Land-use change"], fontsize=11.5)
ax.invert_yaxis()
ax.set_xlim(0, 19)
ax.set_xlabel("CO₂ emissions in 2024 (GtCO₂)", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.suptitle("Fossil CO₂ by sector in 2024: power and industry are two-thirds of the total",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-sector-shares.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-sector-shares.png")
