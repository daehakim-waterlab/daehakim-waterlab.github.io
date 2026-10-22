# Figure for the blog post "Heat and the mind: what an umbrella review says about climate change and mental health" (2026-10-22).
# Credibility classes of the 237 associations between air pollution or climate change hazards and mental health
# outcomes in Radua et al. (2024), World Psychiatry 23, 244-256, https://doi.org/10.1002/wps.21219:
# class I (convincing) 1, class II (highly suggestive) 11, class III (suggestive) 24, class IV (weak) 65,
# not significant 136. Of the 237, 195 concern air pollution and 42 climate change hazards (35 of them temperature).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-mental-evidence.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

classes = [("Class I\nconvincing", 1, "#1f5fa8"), ("Class II\nhighly suggestive", 11, "#2a78d6"),
           ("Class III\nsuggestive", 24, "#7fa9de"), ("Class IV\nweak", 65, "#b9cbe3"),
           ("Not\nsignificant", 136, "#c9c7c1")]
fig, ax = plt.subplots(figsize=(6.6, 4.6), facecolor=surf); ax.set_facecolor(surf)
for i, (name, n, c) in enumerate(classes):
    ax.barh(i, n, 0.64, color=c)
    ax.text(n + 2, i, f"{n}  ({n / 237:.1%})", ha="left", va="center", fontsize=11, color=ink)
ax.set_yticks(range(len(classes))); ax.set_yticklabels([c[0] for c in classes], fontsize=11); ax.invert_yaxis()
ax.set_xlim(0, 175)
ax.set_xlabel("Number of exposure–outcome associations (total 237)", color=ink2, fontsize=11)
ax.text(172, 1.5, "195 on air pollution\n42 on climate hazards\n(35 on temperature)", ha="right", va="center",
        fontsize=10.5, color=ink2, linespacing=1.4)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("Only 12 of 237 associations pass the strictest evidence tests", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-mental-evidence.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-mental-evidence.png")
