# Figure for the blog post "Global fossil CO2 emissions may fall in 2026, and not because of a pandemic" (2026-11-09).
# How the International Energy Agency's forecast of the change in global oil demand in 2026 evolved through its
# monthly Oil Market Reports (thousand barrels per day, kb/d):
#   January +930 (as reported by Carbon Brief, 16 September 2026); March +730 (as stated in the April report);
#   April -80; May -420; June -1,100; July -1,000; August -1,600; September -2,500; October -2,600
#   (IEA Oil Market Reports, https://www.iea.org/reports/oil-market-report-<month>-2026). February not shown.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-09-iea-oil-revisions.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

pts = [("Jan", 1, 930), ("Mar", 3, 730), ("Apr", 4, -80), ("May", 5, -420), ("Jun", 6, -1100), ("Jul", 7, -1000),
       ("Aug", 8, -1600), ("Sep", 9, -2500), ("Oct", 10, -2600)]
fig, ax = plt.subplots(figsize=(6.6, 4.0), facecolor=surf); ax.set_facecolor(surf)
x = [p[1] for p in pts]; y = [p[2] / 1000 for p in pts]
ax.axvspan(2.5, 10.5, color="#f6ece4", lw=0, zorder=0)
ax.text(2.65, -3.05, "Hormuz crisis", fontsize=9.2, color="#b4532a", va="center")
ax.axhline(0, color=ink2, lw=0.8)
ax.plot(x, y, "-", color="#b4532a", lw=2.2)
ax.plot(x, y, "o", color="#b4532a", ms=6)
for m, xi, v in pts:
    ax.text(xi, v / 1000 + (0.22 if v > 0 else -0.24), f"{v / 1000:+.1f}", ha="center",
            va="bottom" if v > 0 else "top", fontsize=8.8, color=ink)
ax.set_xticks(x); ax.set_xticklabels([p[0] for p in pts], fontsize=9.5)
ax.set_xlim(0.4, 10.6); ax.set_ylim(-3.3, 1.6)
ax.set_xlabel("Month of the IEA report in 2026", color=ink2, fontsize=10.5)
ax.set_ylabel("Forecast change in 2026\noil demand (million b/d)", color=ink2, fontsize=10.5)
ax.tick_params(axis="y", labelsize=9.5)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("From growth to the steepest fall since Covid, month by month", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-09-iea-oil-revisions.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-09-iea-oil-revisions.png")
