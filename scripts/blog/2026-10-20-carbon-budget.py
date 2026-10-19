# Figure for the blog post "Where our CO2 goes, and how much is left to emit" (2026-10-20).
# Data: decadal mean global carbon budget 2015-2024 (GtC/yr), Table 7 of Friedlingstein et al. (2026),
# Global Carbon Budget 2025, Earth Syst. Sci. Data 18, 3211-3288, doi:10.5194/essd-18-3211-2026:
#   fossil CO2 9.8 (incl. cement carbonation), land-use change 1.4,
#   atmospheric growth 5.6, ocean sink 3.2, land sink 2.4, budget imbalance ~0.
# Converted to GtCO2 with 1 GtC = 3.664 GtCO2. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-20-carbon-budget.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
C = 3.664
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

sources = [("Fossil fuels\nand cement", 9.8, "#5b5a57"), ("Land-use\nchange", 1.4, "#b07a3c")]
sinks = [("Atmosphere", 5.6, "#d6604d"), ("Ocean", 3.2, "#2a78d6"), ("Land", 2.4, "#1b9e5a")]
total = sum(v for _, v, _ in sources)

fig, ax = plt.subplots(figsize=(8.6, 6.4), facecolor=surf); ax.set_facecolor(surf)
W = 0.62
for x, parts in [(0, sources), (1, sinks)]:
    bottom = 0
    for name, v, c in parts:
        g = v * C
        ax.bar(x, g, W, bottom=bottom, color=c, edgecolor=surf, linewidth=2)
        txt = f"{name}\n{g:.1f} GtCO₂/yr"
        if x == 1:
            txt += f"\n{v / total * 100:.0f}% of emissions"
        ax.text(x, bottom + g / 2, txt, ha="center", va="center", color="white", fontsize=11.5,
                fontweight="bold" if g > 6 else "normal", linespacing=1.25)
        bottom += g
ax.annotate("", xy=(0.67, total * C * 0.5), xytext=(0.33, total * C * 0.5),
            arrowprops=dict(arrowstyle="-|>", color=ink2, lw=1.6, mutation_scale=18))
ax.text(0, total * C + 1.2, f"Human emissions\n{total * C:.0f} GtCO₂/yr", ha="center", va="bottom", fontsize=12, color=ink)
ax.text(1, total * C + 1.2, "Where the CO₂ went", ha="center", va="bottom", fontsize=12, color=ink)
ax.set_xlim(-0.55, 1.55); ax.set_ylim(0, 49)
ax.set_xticks([])
ax.set_ylabel("GtCO₂ per year (mean of 2015–2024)", color=ink2)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right", "bottom"): ax.spines[sp].set_visible(False)
ax.set_title("The global carbon budget balances: half stays in the air, half is taken up",
             loc="left", color=ink, fontsize=12.5)
fig.text(0.985, 0.015, "Budget imbalance over 2015–2024: about zero", ha="right", fontsize=10, color=ink2)
fig.tight_layout(rect=(0, 0.03, 1, 1))
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-carbon-budget.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-carbon-budget.png")
