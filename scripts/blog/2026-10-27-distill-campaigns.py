# Figure for the blog post "Model distillation: how AI models learn from each other, and what they lose" (2026-10-27).
# Exchanges with Claude attributed by Anthropic to distillation campaigns by three AI labs, as reported in
# Anthropic (2026), "Detecting and preventing distillation attacks", 23 February 2026
# (https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks): DeepSeek over 150,000,
# Moonshot AI over 3.4 million, MiniMax over 13 million; in total over 16 million exchanges through about 24,000
# fraudulent accounts. These are Anthropic's attributions; the labs have not confirmed them.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-27-distill-campaigns.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

labs = [("MiniMax", 13.0), ("Moonshot AI (Kimi)", 3.4), ("DeepSeek", 0.15)]
fig, ax = plt.subplots(figsize=(6.6, 3.4), facecolor=surf); ax.set_facecolor(surf)
for i, (name, v) in enumerate(labs):
    ax.barh(i, v, 0.6, color="#b4532a")
    ax.text(v + 0.25, i, f">{v:g} million" if v >= 1 else ">150,000", va="center", fontsize=10.5, color=ink)
ax.set_yticks(range(3)); ax.set_yticklabels([l[0] for l in labs], fontsize=11); ax.invert_yaxis()
ax.set_xlim(0, 16)
ax.set_xlabel("Exchanges with Claude (millions), as reported by Anthropic", color=ink2, fontsize=10.5)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("16 million conversations, 24,000 fake accounts (Anthropic, Feb 2026)", x=0.012, ha="left", color=ink,
             fontsize=12)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-27-distill-campaigns.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-27-distill-campaigns.png")
