# Figure for the blog post "Will the Atlantic overturning tip, and how fast would we feel it?" (2026-10-19).
# Sources of the numbers:
#   RAPID record 2004-2024: Dijkstra & van Westen (2026), Annu. Rev. Mar. Sci. 18, 23-46.
#   Statistical estimate 2057 (2025-2095): Ditlevsen & Ditlevsen (2023), Nat. Commun. 14, 4254 (contested).
#   CESM collapse onset ~2060 (RCP8.5) and ~2110 (RCP4.5), recovery under RCP2.6, very weak AMOC
#   through model year 2500: van Westen, Boerner & Dijkstra (2026), Nat. Clim. Change 16, 1195-1206.
#   "Collapse unfolds within ~100 years": Dijkstra & van Westen (2026).
# The bars are a schematic of these published numbers, not a new projection. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-19-amoc-timescales.py
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BOX = dict(facecolor="#fcfcfb", edgecolor="none", pad=1.5)
from matplotlib.patches import Rectangle

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, orange, green = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})
fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=surf); ax.set_facecolor(surf)
X0, X1, H = 2000, 2520, 0.42

# a lifetime: someone born in 2026
ax.axvspan(2026, 2106, color=grid, alpha=0.55, zorder=0, lw=0)
ax.text(2066, 5.45, "a lifetime\n(born 2026)", ha="center", fontsize=9.5, color=ink2)
ax.axvline(2100, color=ink2, lw=0.9, ls=(0, (4, 3)), zorder=1)
ax.text(2104, -0.78, "2100: IPCC AR6, medium confidence\nno abrupt collapse before this", fontsize=9, color=ink2, va="bottom")

def bar(y, a, b, color, alpha=1.0, hatch=None):
    ax.add_patch(Rectangle((a, y - H / 2), b - a, H, color=color, alpha=alpha, lw=0, hatch=hatch, zorder=2))

def collapse(y, onset, color):
    # decline phase drawn as a fading gradient over ~100 years, then a long weak state
    for i, x in enumerate(np.linspace(onset, onset + 100, 40)[:-1]):
        bar(y, x, x + 100 / 39 + 0.3, color, alpha=0.25 + 0.75 * i / 39)
    bar(y, onset + 100, 2500, color, alpha=1.0)
    ax.scatter([onset], [y], marker="v", s=90, color=ink, zorder=4)
    ax.annotate("", xy=(X1 - 2, y), xytext=(2500, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2, mutation_scale=14))

rows = ["Direct observations\n(RAPID, 26°N)", "Statistical estimate\nof onset (contested)",
        "One model, high\nemissions (RCP8.5)", "One model, moderate\nemissions (RCP4.5)",
        "One model, low\nemissions (RCP2.6)"]
ys = [4.6, 3.5, 2.4, 1.3, 0.2]

bar(ys[0], 2004, 2024, ink2)
ax.text(2030, ys[0], "only ~20 years of record; large natural variability", va="center", fontsize=9.5, color=ink2, bbox=BOX)

bar(ys[1], 2025, 2095, ink2, alpha=0.3)
ax.scatter([2057], [ys[1]], s=60, color=ink2, zorder=4)
ax.text(2101, ys[1], "2057 (90% range 2025–2095), disputed because of data uncertainty",
        va="center", fontsize=9.5, color=ink2, bbox=BOX)

collapse(ys[2], 2060, orange)
ax.text(2062, ys[2] + 0.36, "onset ≈2060 at +2.8 °C → decline over ~a century → weak for centuries",
        fontsize=9.3, color=orange, bbox=BOX)
collapse(ys[3], 2110, orange)
ax.text(2112, ys[3] + 0.36, "onset ≈2110 at +2.2 °C → weak to 2500 and beyond",
        fontsize=9.3, color=orange, bbox=BOX)
bar(ys[4], 2006, 2500, green, alpha=0.45)
ax.text(2112, ys[4] + 0.36, "weakens, then recovers", fontsize=9.3, color=green, bbox=BOX)

ax.set_yticks(ys); ax.set_yticklabels(rows, fontsize=10)
ax.set_xlim(X0, X1); ax.set_ylim(-0.85, 5.95)
ax.set_xticks([2000, 2050, 2100, 2200, 2300, 2400, 2500])
ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.set_title("If the AMOC collapses: decades to the trigger, a century to fall, centuries to recover",
             loc="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-19-amoc-timescales.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-19-amoc-timescales.png")
