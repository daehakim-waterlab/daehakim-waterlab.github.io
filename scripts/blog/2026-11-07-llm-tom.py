# Figure for the blog post "How the brain invented learning, part IV: mentalizing in A Brief History of Intelligence"
# (2026-11-07). Share of 40 false-belief tasks solved by language models, as reported by Kosinski (2024),
# PNAS 121, e2405460121 (https://doi.org/10.1073/pnas.2405460121): older models solved none; GPT-3-davinci-003
# (November 2022) and ChatGPT-3.5-turbo (March 2023) 20%; ChatGPT-4 (June 2023) 75%, matching the performance of
# six-year-old children in past studies. A task counted as solved only if all eight of its scenarios were answered
# correctly.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-07-llm-tom.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("Older models", 0, "#c9d9f0"), ("GPT-3 davinci-003\n(Nov 2022)", 20, "#8fb0dc"),
        ("ChatGPT-3.5-turbo\n(Mar 2023)", 20, "#8fb0dc"), ("ChatGPT-4\n(Jun 2023)", 75, "#2a78d6")]
fig, ax = plt.subplots(figsize=(6.6, 4.2), facecolor=surf); ax.set_facecolor(surf)
for i, (name, v, c) in enumerate(rows):
    ax.barh(i, max(v, 0.6), 0.6, color=c)
    ax.text(v + 1.5, i, f"{v}%", va="center", fontsize=10.5, color=ink)
ax.axvline(75, color="#b4532a", lw=1.2, ls=(0, (4, 3)))
ax.text(74, -0.62, "six-year-old children", ha="right", va="center", fontsize=9.5, color="#b4532a")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5); ax.invert_yaxis()
ax.set_xlim(0, 100); ax.set_ylim(3.5, -1.0)
ax.set_xlabel("Share of 40 false-belief tasks solved (%)", color=ink2, fontsize=11)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Language models learned to pass false-belief tests in a year", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-07-llm-tom.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-07-llm-tom.png")
