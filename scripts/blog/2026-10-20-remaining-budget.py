# Figure for the blog post "Where our CO2 goes, and how much is left to emit" (2026-10-20).
# Data: remaining carbon budgets from January 2026 (50% likelihood, GtCO2) reported in Section 4 of
# Friedlingstein et al. (2026), Global Carbon Budget 2025, Earth Syst. Sci. Data 18, 3211-3288,
# doi:10.5194/essd-18-3211-2026:
#   IPCC AR6 budget updated for 2020-2025 emissions: 250, 600, 1100 (1.5, 1.7, 2.0 C);
#   Forster et al. (2025) budget updated for 2025 emissions: 90, 450, 1010;
#   GCB2025 average of the two: 170, 525, 1055.
# Total CO2 emissions in 2025 (preliminary): 42.2 GtCO2/yr. A straight-line path to net zero in 2050
# gives cumulative emissions of about 520 GtCO2 over 2025-2050 (same source). Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-20-remaining-budget.py
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
light, mid, dark = "#a9c8ec", "#5b9be0", "#1f5fae"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

targets = ["1.5 °C", "1.7 °C", "2.0 °C"]
ipcc = [250, 600, 1100]
forster = [90, 450, 1010]
avg = [170, 525, 1055]
E2025 = 42.2

fig, ax = plt.subplots(figsize=(9, 5.8), facecolor=surf); ax.set_facecolor(surf)
y = np.arange(3) * 1.25
h = 0.32
ax.barh(y - h, ipcc, h, color=light, label="IPCC AR6, updated to 2026")
ax.barh(y, forster, h, color=mid, label="Forster et al. (2025), updated to 2026")
ax.barh(y + h, avg, h, color=dark, label="Global Carbon Budget 2025 (average)")
for yy, a in zip(y, avg):
    ax.text(a + 25, yy + h, f"{a} GtCO₂\n≈ {a / E2025:.0f} years", va="center", fontsize=11.5, color=ink,
            fontweight="bold")
ax.axvline(520, color="#d6604d", lw=1.6, ls=(0, (5, 3)))
ax.text(530, -0.78, "Straight-line path to net zero\nin 2050 emits about 520 GtCO₂", color="#d6604d",
        fontsize=10.5, va="center")
ax.set_yticks(y); ax.set_yticklabels(targets, fontsize=13)
ax.set_ylim(3.05, -1.15)
ax.set_xlim(0, 1500)
ax.set_xlabel("Remaining CO₂ budget from January 2026 (GtCO₂, 50% chance)", color=ink2)
top = ax.secondary_xaxis("top", functions=(lambda g: g / E2025, lambda t: t * E2025))
top.set_xlabel("Years left at the 2025 emission rate (42.2 GtCO₂ per year)", color=ink2, fontsize=11)
top.tick_params(colors=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("right",): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.86), frameon=False, fontsize=10.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-remaining-budget.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-remaining-budget.png")
