# Figure for the blog post "A short history of AI, part 3: transformers and large language models (2017-2026)"
# (2026-10-22). A timeline of milestones discussed in the post, with dates from the cited papers and from the
# official announcements (company announcements are marked as such in the post's reference list).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-ai-timeline-3.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
res, prod, sci = "#2a78d6", "#d6604d", "#1b9e5a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

events = [  # date label, text, kind
    ("Jun 2017", "Transformer", res),
    ("2018-19", "GPT, BERT, GPT-2: pre-training", res),
    ("2020", "Scaling laws; GPT-3 (175 B)", res),
    ("Jul 2021", "AlphaFold 2", sci),
    ("Mar 2022", "InstructGPT; Chinchilla", res),
    ("Nov 2022", "ChatGPT", prod),
    ("2023", "LLaMA, GPT-4, Claude, Gemini", prod),
    ("Dec 2023", "GraphCast weather forecasts", sci),
    ("Mar 2024", "AI flood forecasts, ungauged basins", sci),
    ("Sep 2024", "o1: models that reason longer", res),
    ("Oct 2024", "Nobel Prizes for AI research", sci),
    ("Jan 2025", "DeepSeek-R1, open weights", res),
    ("May 2025", "Claude Code: coding agents", prod),
    ("Jun 2026", "Claude Fable 5", prod),
    ("Sep 2026", "Claude Opus 5.5; Gemini 4 Argon", prod),
]
fig, ax = plt.subplots(figsize=(6.6, 8.6), facecolor=surf); ax.set_facecolor(surf)
n = len(events)
ax.plot([0.06, 0.06], [-0.5, n - 0.5], color=ink2, lw=1.2, zorder=1)
for i, (d, lab, c) in enumerate(events):
    ax.scatter([0.06], [i], s=70, color=c, zorder=3, edgecolor=surf, linewidth=1.2)
    ax.text(0.10, i, d, ha="left", va="center", fontsize=11, color=ink2, fontweight="bold")
    ax.text(0.30, i, lab, ha="left", va="center", fontsize=11, color=ink)
ax.set_ylim(n - 0.5, -1.4)
ax.set_xlim(0, 1)
ax.set_xticks([]); ax.set_yticks([])
for sp in ("top", "right", "bottom", "left"): ax.spines[sp].set_visible(False)
from matplotlib.lines import Line2D
handles = [Line2D([], [], marker="o", ls="", color=c, markersize=8, label=l)
           for c, l in [(res, "Research and methods"), (prod, "Products people use"), (sci, "Science and the Earth")]]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.09), ncol=2, frameon=False, fontsize=10.5,
          handletextpad=0.3, columnspacing=1.0)
fig.suptitle("From the Transformer to today's models, 2017-2026", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-ai-timeline-3.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-ai-timeline-3.png")
