# Figure for the blog post "An AI that reasons like a physician: the Science study and what has changed since"
# (2026-11-06). Two later results on medical tasks:
#   (a) HealthBench (Arora et al. 2025, arXiv 2505.08775), 5,000 realistic health conversations scored with
#       physician-written rubrics: GPT-3.5 Turbo 16%, GPT-4o 32%, o3 60%.
#   (b) Sequential Diagnosis Benchmark (Nori et al. 2025, arXiv 2506.22405), 304 NEJM clinicopathological
#       cases worked through step by step: generalist physicians 20% (average), MAI-DxO with o3 80%,
#       MAI-DxO at maximum-accuracy setting 85.5%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-06-healthbench.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 5.6), facecolor=surf)
ra = [("GPT-3.5 Turbo (2023)", 16, "#c9d9f0"), ("GPT-4o (2024)", 32, "#8fb0dc"), ("o3 (2025)", 60, "#2a78d6")]
rb = [("Generalist physicians", 20, "#b4532a"), ("MAI-DxO with o3", 80, "#2a78d6"),
      ("MAI-DxO, max. accuracy", 85.5, "#1f5fa8")]
for ax, rows, title in [(a, ra, "a  HealthBench: realistic health conversations"),
                        (b, rb, "b  Hard NEJM cases solved step by step (304 cases)")]:
    ax.set_facecolor(surf)
    for i, (name, v, c) in enumerate(rows):
        ax.barh(i, v, 0.62, color=c)
        ax.text(v + 1.2, i, f"{v:g}%", va="center", fontsize=10.5, color=ink)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5); ax.invert_yaxis()
    ax.set_xlim(0, 100); ax.set_title(title, loc="left", fontsize=11, color=ink)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
b.set_xlabel("Score or accuracy (%)", color=ink2, fontsize=10.5)
fig.suptitle("Medical AI kept improving after o1", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-06-healthbench.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-06-healthbench.png")
