# Figure for the blog post "Vibe coding, vibe writing, vibe working: what decides whether it works" (2026-10-21).
# How much office and freelance work current agents can do, by benchmark. Each benchmark defines success
# differently, so the rows are NOT comparable. Numbers as reported:
#   Remote Labor Index: best agent at release, Oct 2025, 2.5% (Mazeika et al. 2025, arXiv:2510.26787);
#     best model in 2026, 15.8% (CAIS 2026 blog).
#   TheAgentCompany: best agent in the published version (Gemini 2.5 Pro) completed 30.3% of 175 tasks
#     (Xu et al. 2025, NeurIPS 2025; arXiv:2412.14161 v3).
#   SpreadsheetBench: Excel Agent Mode 57.2% vs a human baseline of 71.3% (Microsoft 2025, chart in the product
#     announcement).
#   GDPval: best model in the paper, wins or ties vs experts 47.6% (Patwardhan et al. 2025, arXiv:2510.04374);
#     GPT-5.2 Thinking, 70.9% (OpenAI 2025, product announcement).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-21-vibe-working.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
rli, rli2, tac, sheet, gdp, gdp2 = "#d6604d", "#eb9a85", "#2a78d6", "#1b9e5a", "#5b5a57", "#a8a6a0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [  # label, %, color
    ("Remote Labor Index: freelance projects\nacceptable to the client (Oct 2025)", 2.5, rli),
    ("Remote Labor Index\n(best model, 2026)", 15.8, rli2),
    ("TheAgentCompany: workplace tasks\ncompleted on its own (2025)", 30.3, tac),
    ("SpreadsheetBench: Excel agent\n(developer-reported, 2025)", 57.2, sheet),
    ("GDPval: at least as good as an\nexpert's (best model in paper, 2025)", 47.6, gdp),
    ("GDPval (developer announcement,\nDec 2025)", 70.9, gdp2),
]
fig, ax = plt.subplots(figsize=(9, 5.6), facecolor=surf); ax.set_facecolor(surf)
for i, (lab, v, c) in enumerate(rows):
    ax.barh(i, v, 0.6, color=c)
    ax.text(v + 1, i, f"{v:g}%", va="center", fontsize=11.5, color=ink)
i_sb = 3
ax.plot([71.3, 71.3], [i_sb - 0.36, i_sb + 0.36], color=ink, lw=2)
ax.text(72.5, i_sb, "human\n71.3%", va="center", fontsize=10, color=ink2)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5)
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Success rate as defined by each benchmark (%)", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.suptitle("The closer the task is to a whole job, the lower the success rate",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-vibe-working.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-vibe-working.png")
