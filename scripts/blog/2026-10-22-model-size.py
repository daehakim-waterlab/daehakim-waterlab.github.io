# Figure for the blog post "A short history of AI, part 3: transformers and large language models (2017-2026)"
# (2026-10-22). Number of parameters of landmark language models, as stated in the papers that introduced them:
#   Transformer (big), 2017: 213 million (Vaswani et al. 2017, Table 3)
#   BERT-large, 2018: 340 million (Devlin et al. 2019)
#   GPT-2, 2019: 1.5 billion (Radford et al. 2019)
#   GPT-3, 2020: 175 billion (Brown et al. 2020)
#   PaLM, 2022: 540 billion (Chowdhery et al. 2022)
#   Chinchilla, 2022: 70 billion, trained on more data (Hoffmann et al. 2022)
#   LLaMA (largest), 2023: 65 billion (Touvron et al. 2023)
# Most frontier developers stopped disclosing model size from 2023 (for example, the GPT-4 Technical Report gives
# no parameter count), so later models cannot be plotted. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-22-model-size.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
c_main, c_eff = "#2a78d6", "#1b9e5a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

models = [  # year (x position), params, label, color, label offset (points)
    (2017.45, 213e6, "Transformer\n213 M", c_main, (0, 10)),
    (2018.8, 340e6, "BERT-large\n340 M", c_main, (0, 10)),
    (2019.1, 1.5e9, "GPT-2\n1.5 B", c_main, (0, 10)),
    (2020.4, 175e9, "GPT-3\n175 B", c_main, (0, 10)),
    (2022.25, 540e9, "PaLM\n540 B", c_main, (0, 10)),
    (2022.25, 70e9, "Chinchilla\n70 B, more data", c_eff, (-30, -44)),
    (2023.15, 65e9, "LLaMA\n65 B", c_eff, (18, -44)),
]
fig, ax = plt.subplots(figsize=(8.6, 5.6), facecolor=surf); ax.set_facecolor(surf)
ax.axvspan(2023.4, 2026.9, color="#efede8", lw=0, zorder=0)
ax.text(2025.15, 3e11, "frontier models:\nsize no longer\ndisclosed", ha="center", va="center", fontsize=11, color=ink2,
        style="italic")
for x, p, lab, c, off in models:
    ax.scatter([x], [p], s=90, color=c, zorder=3, edgecolor=surf, linewidth=1.2)
    ax.annotate(lab, (x, p), textcoords="offset points", xytext=off, ha="center", va="bottom", fontsize=10.5,
                color=ink)
ax.set_yscale("log")
ax.set_ylim(5e7, 5e12)
ax.set_xlim(2016.8, 2026.9)
ax.set_xticks(range(2017, 2027))
ax.set_ylabel("Number of parameters (log scale)", color=ink2)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=c_main, markersize=8, label="bigger models"),
                   Line2D([], [], marker="o", ls="", color=c_eff, markersize=8, label="smaller models trained on more data")],
          loc="upper left", frameon=False, fontsize=10.5)
fig.suptitle("The scaling era: language models grew about 2,500-fold in five years", x=0.012, ha="left",
             color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-model-size.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-model-size.png")
