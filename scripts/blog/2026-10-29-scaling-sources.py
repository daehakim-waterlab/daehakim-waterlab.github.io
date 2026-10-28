# Figure for the blog post "More compute, better AI: how much better?" (2026-10-29).
# (a) Growth of frontier training compute and its components, median growth factors per year for frontier models
#     after 2018 (Emberson & Owen 2025, Epoch AI, https://epoch.ai/data-insights/training-compute-decomposition):
#     total 4.17x; number of chips 1.69x; training duration 1.53x; FLOP/s per chip 1.41x.
# (b) Algorithmic progress: compute needed for a given language-model performance halves about every 8 months
#     (Ho et al. 2024, arXiv 2403.05812), i.e. 2^(12/8) = 2.8x per year of "effective" compute.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-29-scaling-sources.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("Total training compute", 4.17, "#0b0b0b"), ("More chips", 1.69, "#b4532a"),
        ("Longer training runs", 1.53, "#d9a37f"), ("Faster chips", 1.41, "#2a78d6"), (None, 0, None),
        ("Better algorithms\n(compute-equivalent)", 2.83, "#8a8780")]
fig, ax = plt.subplots(figsize=(6.6, 4.6), facecolor=surf); ax.set_facecolor(surf)
labels = []
for i, (name, v, c) in enumerate(rows):
    labels.append(name or "")
    if name is None:
        continue
    ax.barh(i, v - 1, 0.6, left=1, color=c)
    ax.text(v + 0.06, i, f"×{v:.2f} per year", va="center", fontsize=10.5, color=ink)
ax.set_yticks(range(len(rows))); ax.set_yticklabels(labels, fontsize=10.5); ax.invert_yaxis()
ax.set_xlim(1, 5.3)
ax.set_xticks([1, 2, 3, 4, 5]); ax.set_xticklabels(["×1", "×2", "×3", "×4", "×5"])
ax.set_xlabel("Growth factor per year", color=ink2, fontsize=11)
ax.text(1.05, 4.0, "Faster chips supply only about a quarter of the growth (in log terms)", fontsize=9.5,
        color=ink2, va="center")
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Where the extra compute comes from", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-29-scaling-sources.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-29-scaling-sources.png")
