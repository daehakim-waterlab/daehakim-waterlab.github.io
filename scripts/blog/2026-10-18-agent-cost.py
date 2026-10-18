# Figure for the blog post "From chatbot to coworker" (2026-10-18).
# Data: Table A1 of Li et al. (2026), J. Hydrol. 679, 136358 (cost of one representative successful run
# per LLM and task group). Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-18-agent-cost.py
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
cost = {  # USD per successful end-to-end modelling run (5 task groups)
 "Qwen-Plus":         [0.085, 0.081, 0.093, 0.046, 0.090],
 "DeepSeek-V3.2":     [0.099, 0.066, 0.088, 0.066, 0.135],
 "Claude Sonnet 4.5": [1.821, 2.833, 1.842, 2.269, 2.550],
 "Gemini 2.5 Pro":    [3.807, 3.926, 4.089, 2.150, 4.337],
 "GPT-5.5":           [3.193, 3.054, 8.130, 2.578, 5.604],
}
ink, ink2, grid, surf, c = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})
fig, ax = plt.subplots(figsize=(9, 4), facecolor=surf); ax.set_facecolor(surf)
names = list(cost)
for i, n in enumerate(names):
    v = np.array(cost[n]); y = len(names) - 1 - i
    ax.plot([v.min(), v.max()], [y, y], color=c, lw=2, alpha=0.35, solid_capstyle="round")
    ax.scatter(v, np.full(5, y), s=46, color=c, edgecolor=surf, linewidth=1.5, zorder=3)
    m = np.median(v)
    ax.text(v.max() * 1.18, y, f"median ${m:.2f}", va="center", fontsize=9.5, color=ink2)
ax.set_xscale("log"); ax.set_xlim(0.03, 30)
ax.set_xticks([0.05, 0.1, 0.5, 1, 5, 10]); ax.set_xticklabels(["$0.05", "$0.10", "$0.50", "$1", "$5", "$10"])
ax.set_yticks(range(len(names))); ax.set_yticklabels(names[::-1])
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("API cost of one successful end-to-end modelling run (USD, log scale)", color=ink2)
ax.set_title("Same agentic workflow, a 25–45× difference in cost", loc="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-18-agent-cost.png", dpi=170, facecolor=surf)
