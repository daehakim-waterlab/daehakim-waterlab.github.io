# Figure for the blog post on using LLMs for writing and coding (2026-10-21).
# Data: stance of essays answering "Does money lead to happiness?" in a randomized study (N = 100), as
# classified in Abdulhai, White et al. (2026), "How LLMs distort our written language", arXiv:2603.18161:
#   no LLM (n = 45): for 32.6%, against 27.9%, neutral 39.5%;
#   LLM used for advice or search only ("LLM-influenced"): for 31.0%, against 24.1%, neutral 44.8%;
#   LLM used to generate most of the text: for 22.2%, against 11.1%, neutral 66.7%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-21-llm-stance.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
c_for, c_against, c_neutral = "#2a78d6", "#d6604d", "#bdbbb5"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

groups = ["Wrote without an LLM", "Used the LLM for\nadvice or search only", "Let the LLM write\nmost of the text"]
data = [(32.6, 27.9, 39.5), (31.0, 24.1, 44.8), (22.2, 11.1, 66.7)]
fig, ax = plt.subplots(figsize=(9, 4.6), facecolor=surf); ax.set_facecolor(surf)
for i, (f, a, n) in enumerate(data):
    left = 0
    for v, c, lab in [(f, c_for, "For"), (a, c_against, "Against"), (n, c_neutral, "Neutral")]:
        ax.barh(i, v, 0.6, left=left, color=c, edgecolor=surf, linewidth=1.5, label=lab if i == 0 else None)
        ax.text(left + v / 2, i, f"{v:.0f}%", ha="center", va="center", fontsize=11.5,
                color="white" if c != c_neutral else ink, fontweight="bold")
        left += v
ax.set_yticks(range(3)); ax.set_yticklabels(groups, fontsize=11.5)
ax.invert_yaxis()
ax.set_xlim(0, 100); ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0", "25", "50", "75", "100%"])
ax.set_xlabel("Share of essays by stance on \"Does money lead to happiness?\"", color=ink2)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), frameon=False, fontsize=11)
fig.suptitle("Heavy LLM use turned opinions into fence-sitting", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-llm-stance.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-llm-stance.png")
