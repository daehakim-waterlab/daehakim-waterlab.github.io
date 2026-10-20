# Figure for the blog post on using LLMs for writing and coding (2026-10-21).
# Error rates of LLM output reported in published studies (each with its own models, tasks and dates):
#   Walters & Wilder (2023), Sci. Rep. 13, 14045: fabricated citations, GPT-3.5 55%, GPT-4 18%;
#     substantive errors in real citations, GPT-4 24%.
#   Kabir et al. (2024), CHI: ChatGPT answers to 517 Stack Overflow questions with incorrect information 52%.
#   Bastani et al. (2025), PNAS 122, e2422633122: GPT-4-based tutor ("GPT Base") correct only 51% of the time
#     on the practice problems (so 49% not correct).
#   Pearce et al. (2022), IEEE S&P: Copilot programs vulnerable in 89 high-risk scenarios, about 40%.
#   Spracklen et al. (2025), USENIX Security: average rate of hallucinated packages, open-source models 21.7%,
#     commercial models at least 5.2%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-21-llm-error-rates.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
text_c, code_c = "#2a78d6", "#d6604d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [  # label, %, color
    ("Citations fabricated by GPT-3.5", 55, text_c),
    ("ChatGPT answers to Stack Overflow\nquestions with incorrect information", 52, code_c),
    ("Math answers from a GPT-4 tutor\nthat were not correct", 49, text_c),
    ("Copilot programs with a security flaw\n(scenarios chosen to be risky)", 40, code_c),
    ("Real citations with substantive errors\n(GPT-4)", 24, text_c),
    ("Code samples naming a non-existent\npackage (open-source models)", 21.7, code_c),
    ("Citations fabricated by GPT-4", 18, text_c),
    ("Code samples naming a non-existent\npackage (commercial models)", 5.2, code_c),
]
fig, ax = plt.subplots(figsize=(9, 7), facecolor=surf); ax.set_facecolor(surf)
for i, (lab, v, c) in enumerate(rows):
    ax.barh(i, v, 0.62, color=c)
    ax.text(v + 0.8, i, f"{v:g}%", va="center", fontsize=12, color=ink)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5)
ax.invert_yaxis()
ax.set_xlim(0, 65)
ax.set_xlabel("Share of outputs with the error (%)", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=text_c, label="Writing and reasoning"), Patch(color=code_c, label="Code")],
          loc="lower right", frameon=False, fontsize=11)
fig.suptitle("Error rates measured in LLM output vary widely, and none is zero",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-llm-error-rates.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-llm-error-rates.png")
