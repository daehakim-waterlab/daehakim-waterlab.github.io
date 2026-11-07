# Figure for the blog post "How the brain invented learning, part V: speaking in A Brief History of Intelligence"
# (2026-11-08). Language input of children and adults compared with the training data of language models.
# Human estimates from Frank (2023), Trends in Cognitive Sciences 27, 990-992 (https://doi.org/10.1016/j.tics.2023.08.007):
#   by age 5: about 6e6 words (limited-language environment) to 6e7 words (soft upper bound);
#   by age 20: about 3e7 words (lower bound, no reading) to 4e8 words (literate reader).
# Model training data: GPT-3 5e11 tokens and Chinchilla about 1e12 tokens, as cited by Frank (2023);
#   Llama 3 about 15e12 tokens (Grattafiori et al. 2024, The Llama 3 herd of models, arXiv:2407.21783).
# Tokens and words are not identical (a token is roughly three quarters of an English word), which does not matter
# on this logarithmic scale.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-08-language-data-gap.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("Child by age 5", 6e6, 6e7, "#b4532a"), ("Adult by age 20", 3e7, 4e8, "#b4532a"),
        ("GPT-3 (2020)", 5e11, 5e11, "#2a78d6"), ("Chinchilla (2022)", 1e12, 1e12, "#2a78d6"),
        ("Llama 3 (2024)", 1.5e13, 1.5e13, "#2a78d6")]
fig, ax = plt.subplots(figsize=(6.6, 4.4), facecolor=surf); ax.set_facecolor(surf)
for i, (name, lo, hi, c) in enumerate(rows):
    if lo == hi:
        ax.barh(i, hi, 0.55, color=c, left=1e5)
    else:
        ax.barh(i, lo, 0.55, color=c, left=1e5)
        ax.barh(i, hi - lo, 0.55, color=c, left=lo, alpha=0.4)
ax.set_xscale("log"); ax.set_xlim(1e5, 1e14)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5); ax.invert_yaxis()
ax.set_xticks([1e6, 1e8, 1e10, 1e12, 1e14])
ax.set_xticklabels(["1 million", "100 million", "10 billion", "1 trillion", "100 trillion"], fontsize=9.5)
ax.set_xlabel("Words heard or read (people), tokens seen in training (models)", color=ink2, fontsize=10.5)
ax.text(2e9, 0.5, "Models see about 1,000 to\n100,000 times more language", ha="left", va="center", fontsize=9.8,
        color=ink2, linespacing=1.3)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Children learn language from far less data than models", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-08-language-data-gap.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-08-language-data-gap.png")
