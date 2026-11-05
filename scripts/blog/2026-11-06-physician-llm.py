# Figure for the blog post "An AI that reasons like a physician: the Science study and what has changed since"
# (2026-11-06). Results reported in Brodeur et al. (2026), Science 392, 524-527 (10.1126/science.adz4433):
#   NEJM clinicopathological conferences, same 70 cases, exact or very close diagnosis in the differential:
#     GPT-4 72.9%, o1-preview 88.6%.
#   NEJM Healer cases, share of perfect R-IDEA reasoning scores: o1-preview 78/80, GPT-4 47/80,
#     attending physicians 28/80, residents 16/72.
#   Grey Matters management cases, median score: o1-preview 89%, GPT-4 42%, physicians with GPT-4 41%,
#     physicians with conventional resources 34%.
#   Landmark diagnostic cases, median score: o1-preview 97%, GPT-4 92%, physicians with GPT-4 76%,
#     physicians with conventional resources 74%.
#   Emergency room (76 real cases), exact or very close diagnosis at initial triage: o1 67.1%,
#     attending physician 1 55.3%, attending physician 2 50.0%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-06-physician-llm.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
C = {"o1": "#2a78d6", "gpt4": "#8fb0dc", "doc": "#b4532a", "doc2": "#d9a37f", "res": "#ecc7a8"}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

panels = [
    ("NEJM cases: right diagnosis listed (70 cases)",
     [("o1-preview", 88.6, "o1"), ("GPT-4", 72.9, "gpt4")]),
    ("NEJM Healer: perfect reasoning documentation",
     [("o1-preview", 97.5, "o1"), ("GPT-4", 58.8, "gpt4"), ("Attending physicians", 35.0, "doc"),
      ("Residents", 22.2, "res")]),
    ("Management cases: median score",
     [("o1-preview", 89, "o1"), ("GPT-4", 42, "gpt4"), ("Physicians with GPT-4", 41, "doc2"),
      ("Physicians, usual resources", 34, "doc")]),
    ("ER triage, 76 real patients: right diagnosis",
     [("o1", 67.1, "o1"), ("Attending physician 1", 55.3, "doc"), ("Attending physician 2", 50.0, "doc")]),
]
fig, axes = plt.subplots(len(panels), 1, figsize=(6.6, 8.4), facecolor=surf,
                         gridspec_kw={"height_ratios": [len(p[1]) + 0.6 for p in panels]})
for k, (ax, (title, rows)) in enumerate(zip(axes, panels)):
    ax.set_facecolor(surf)
    for i, (name, v, c) in enumerate(rows):
        ax.barh(i, v, 0.66, color=C[c])
        ax.text(v + 1.2, i, f"{v:g}%", va="center", fontsize=10, color=ink)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10); ax.invert_yaxis()
    ax.set_xlim(0, 110); ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_title(f"{'abcd'[k]}  {title}", loc="left", fontsize=10.5, color=ink)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
    if k < len(panels) - 1:
        ax.set_xticklabels([])
axes[-1].set_xlabel("Percent", color=ink2, fontsize=10.5)
fig.suptitle("o1 against GPT-4 and physicians, 2024–2025", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-06-physician-llm.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-06-physician-llm.png")
