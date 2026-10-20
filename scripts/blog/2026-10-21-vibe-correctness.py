# Figure for the blog post "Vibe coding, vibe writing, vibe working: what decides whether it works" (2026-10-21).
# The same kind of system scores very differently depending on who checks, what counts as correct and how much
# of the task must work. Numbers as reported in the cited sources; the three panels are NOT comparable:
#   SWE-bench (Michels et al. 2026, arXiv:2608.20446): best score on SWE-bench Verified 95%; best
#     developer-reported score on SWE-bench Pro about 80%; independent runs by the maintainer about 60% (59-61%).
#   SusVibes (Zhao et al. 2026, ICML): best configuration 57% functionally correct, 11.8% correct and secure.
#   SciCode (Tian et al. 2024, NeurIPS 2024 version, Table 2): best model, o1-preview, without background:
#     28.5% of subproblems, 7.7% of whole problems.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-21-vibe-correctness.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
dark, mid, light = "#1f5fae", "#5b9be0", "#a9c8ec"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink, "ytick.color": ink2})

groups = [
    ("Who runs the test\n(SWE-bench, 2026)",
     [("Verified", 95.0), ("Pro,\ndeveloper-\nreported", 80.0), ("Pro,\nindependent", 60.0)]),
    ("What counts as correct\n(SusVibes, 2026)",
     [("Functionally\ncorrect", 57.0), ("Correct\nand secure", 11.8)]),
    ("How much must work\n(SciCode, 2024)",
     [("One\nsubproblem", 28.5), ("Whole\nproblem", 7.7)]),
]

fig, axes = plt.subplots(1, 3, figsize=(10, 5.0), sharey=True, facecolor=surf,
                         gridspec_kw={"width_ratios": [3, 2, 2]})
for ax, (title, bars) in zip(axes, groups):
    ax.set_facecolor(surf)
    labels = [b[0] for b in bars]
    vals = [b[1] for b in bars]
    x = range(len(vals))
    ax.bar(x, vals, 0.66, color=[dark, mid, light][:len(vals)])
    for xi, v in zip(x, vals):
        ax.text(xi, v + 2, f"{v:g}%", ha="center", va="bottom", fontsize=11.5, color=ink)
    ax.set_xticks(list(x)); ax.set_xticklabels(labels, fontsize=10)
    ax.set_title(title, fontsize=11, color=ink, loc="center")
    ax.set_ylim(0, 108)
    ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.tick_params(axis="x", length=0)
axes[0].set_ylabel("Share of tasks solved (%)", color=ink2)
fig.suptitle("The same kind of system, very different scores", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-vibe-correctness.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-vibe-correctness.png")
