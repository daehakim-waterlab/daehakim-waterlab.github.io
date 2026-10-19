# Figure for the blog post "Does living through extreme weather make people act on climate?" (2026-10-19).
# Data: odds ratios (95% confidence intervals) for choosing the pro-climate option, as reported in the
# Results of Wyss, Guizar Rosales et al. (2026), Nature Climate Change, doi:10.1038/s41558-026-02765-z.
# Rows 1-5 come from the models that add subjective attribution (Supplementary Table 17 of the paper;
# attribution is mean-centred, so the exposure term is its effect at average attribution).
# Row 6 comes from a separate exploratory model with self-reported experience. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-19-choice-odds.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, orange = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [  # label, odds ratio, lower, upper
    ("Democrat rather than Republican", 1.68, 1.21, 2.33),
    ("Attributes extreme weather to\nclimate change (one point more)", 1.41, 1.19, 1.66),
    ("Extreme weather recorded in the\nhome county (at average attribution)", 0.72, 0.52, 0.98),
    ("Interaction: exposure effect,\nper point of attribution", 0.66, 0.47, 0.90),
    ("Interaction: party gap,\nper point of attribution", 1.64, 1.09, 2.46),
    ("Self-reported extreme weather\nexperience (separate model)", 1.46, 1.25, 1.71),
]
y = [0, 1, 2, 3, 4, 5.35]

fig, ax = plt.subplots(figsize=(9, 6.2), facecolor=surf); ax.set_facecolor(surf)
ax.axvline(1, color=ink2, lw=1.1, zorder=1)
for (lab, o, lo, hi), yy in zip(rows, y):
    c = blue if o > 1 else orange
    ax.plot([lo, hi], [yy, yy], color=c, lw=2.6, solid_capstyle="round", zorder=2)
    ax.scatter([o], [yy], s=120, color=c, edgecolor=surf, linewidth=1.3, zorder=3)
    ax.text(5.9, yy, f"{o:.2f}  ({lo:.2f}–{hi:.2f})", va="center", ha="right", fontsize=11, color=ink2)
ax.axhline(4.68, color=grid, lw=1.2)
ax.set_xscale("log")
ax.set_xticks([0.5, 0.75, 1, 1.5, 2]); ax.set_xticklabels(["0.5", "0.75", "1", "1.5", "2"])
ax.minorticks_off()
ax.set_xlim(0.42, 6.0); ax.set_ylim(5.9, -1.1)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=11)
ax.tick_params(axis="y", length=0)
ax.text(0.97, -0.75, "← less likely to choose\n     the low-carbon option", ha="right", va="center", fontsize=10.5, color=orange)
ax.text(1.03, -0.75, "more likely →", ha="left", va="center", fontsize=10.5, color=blue)
ax.text(5.9, -0.75, "odds ratio (95% CI)", ha="right", va="center", fontsize=10.5, color=ink2)
ax.set_xlabel("Odds ratio for choosing the pro-climate option (log scale)", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.set_title("Beliefs and party predict the low-carbon choice; recorded exposure does not help",
             loc="left", color=ink, fontsize=12.5, x=-0.52)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-19-choice-odds.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-19-choice-odds.png")
