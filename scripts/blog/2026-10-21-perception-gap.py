# Figure for the blog post on using LLMs for writing and coding (2026-10-21).
# Data: Becker, Rush, Barnes & Rein (2025), "Measuring the impact of early-2025 AI on experienced
# open-source developer productivity", arXiv:2507.09089. Randomized trial, 16 developers, 246 tasks.
# Change in task completion time when AI tools were allowed (negative = faster):
#   experts' prediction: economics -39%, machine learning -38%; developers' forecast -24%;
#   developers' estimate after the study -20%; measured +19%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-21-perception-gap.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
belief, measured = "#a9c8ec", "#d6604d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [
    ("Economists' prediction", -39, belief),
    ("Machine-learning experts' prediction", -38, belief),
    ("Developers' forecast before the study", -24, belief),
    ("Developers' estimate after the study", -20, belief),
    ("Measured in the randomized trial", 19, measured),
]
fig, ax = plt.subplots(figsize=(9, 4.8), facecolor=surf); ax.set_facecolor(surf)
for i, (lab, v, c) in enumerate(rows):
    ax.barh(i, v, 0.6, color=c)
    ax.text(v + (1.2 if v > 0 else -1.2), i, f"{v:+d}%", va="center", ha="left" if v > 0 else "right",
            fontsize=12, color=ink, fontweight="bold" if v > 0 else "normal")
ax.axvline(0, color=ink2, lw=1.2)
ax.axhline(3.5, color=grid, lw=1.2)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=11.5)
ax.invert_yaxis()
ax.set_xlim(-50, 30)
ax.set_xticks([-40, -30, -20, -10, 0, 10, 20])
ax.set_xlabel("Change in task completion time with AI tools (%)", color=ink2)
ax.text(-49, 4.62, "← faster", fontsize=10.5, color=ink2, va="center")
ax.text(29, 4.62, "slower →", fontsize=10.5, color=ink2, va="center", ha="right")
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_ylim(4.95, -0.6)
fig.suptitle("Everyone expected AI to speed experienced developers up; it slowed them down",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-perception-gap.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-perception-gap.png")
