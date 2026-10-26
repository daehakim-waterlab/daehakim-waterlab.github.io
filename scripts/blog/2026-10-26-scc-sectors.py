# Figure for the blog post "Heat-stressed workers add about $41 to the social cost of carbon" (2026-10-26).
# Mean 2025 social cost of carbon (US$ per ton CO2, 2020 dollars, 2% near-term discount rate) reported in
# Moore et al. (2026), Nature Climate Change 16, 1170-1177, https://doi.org/10.1038/s41558-026-02749-z:
#   previous GIVE model: total 204, agriculture 95, mortality 98, no labour;
#   revised: total 179, agriculture 29, labour 41, mortality 98.
# Energy and sea-level rise (unchanged between versions) are shown as the remainder, 204 - 95 - 98 = 11 and
# 179 - 29 - 41 - 98 = 11; means are additive, so the remainder is the mean of those two sectors combined.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-26-scc-sectors.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
colors = {"Mortality": "#8a3b2f", "Agriculture": "#c4813a", "Labour (heat stress)": "#d6604d",
          "Energy and sea-level rise": "#a8a6a0"}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

bars = [("Previous estimate", {"Mortality": 98, "Agriculture": 95, "Labour (heat stress)": 0,
                               "Energy and sea-level rise": 11}, 204),
        ("This study", {"Mortality": 98, "Agriculture": 29, "Labour (heat stress)": 41,
                        "Energy and sea-level rise": 11}, 179)]
fig, ax = plt.subplots(figsize=(6.6, 4.4), facecolor=surf); ax.set_facecolor(surf)
for i, (name, parts, total) in enumerate(bars):
    left = 0
    for k in ["Mortality", "Agriculture", "Labour (heat stress)", "Energy and sea-level rise"]:
        v = parts[k]
        if v == 0:
            continue
        ax.barh(i, v, 0.58, left=left, color=colors[k], label=k if i == 1 else None)
        if v >= 20:
            ax.text(left + v / 2, i, f"{v}", ha="center", va="center", fontsize=11, color="#ffffff")
        left += v
    ax.text(total + 3, i, f"${total}", ha="left", va="center", fontsize=12, color=ink, fontweight="bold")
ax.set_yticks([0, 1]); ax.set_yticklabels([b[0] for b in bars], fontsize=11); ax.invert_yaxis()
ax.set_xlim(0, 235)
ax.set_xlabel("Social cost of carbon in 2025 (US$ per ton of CO₂, mean)", color=ink2, fontsize=11)
ax.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, frameon=False, fontsize=10, handlelength=1.2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Labour enters, agriculture shrinks: the new social cost of carbon", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-26-scc-sectors.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-26-scc-sectors.png")
