# Figure for the blog post "Carbon at risk: putting a number on how much stored carbon might leak back" (2026-11-15).
# 95% carbon at risk (CaR, % of contracted tonnes that may be lost with 5% probability) reported by Lee et al. (2026),
# Nature Climate Change, https://doi.org/10.1038/s41558-026-02785-9:
#   forest, California, single project: about 65% at 100 years, more than 70% at 200 years (plotted as 70);
#   geological storage, well-regulated offshore: 0.15% (200 yr), 0.66% (1,000 yr), 6.3% (10,000 yr);
#   geological storage, poorly regulated onshore: 17% (200 yr), 20% (1,000 yr).
# The shaded band marks the flat 15-20% buffer that the paper cites as an example of a conventional buffer rule.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-15-carbon-at-risk.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
forest, onsh, offs = "#2e8b57", "#b4532a", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("Forest, California\n100 years", 65, forest, ""), ("Forest, California\n200 years", 70, forest, "more than "),
        ("Geological, onshore,\npoorly regulated, 200 yr", 17, onsh, ""),
        ("Geological, onshore,\npoorly regulated, 1,000 yr", 20, onsh, ""),
        ("Geological, offshore,\nwell regulated, 200 yr", 0.15, offs, ""),
        ("Geological, offshore,\nwell regulated, 1,000 yr", 0.66, offs, ""),
        ("Geological, offshore,\nwell regulated, 10,000 yr", 6.3, offs, "")]
fig, ax = plt.subplots(figsize=(6.6, 5.6), facecolor=surf); ax.set_facecolor(surf)
ax.axvspan(15, 20, color="#efe9dd", zorder=0)
ax.text(17.5, -0.85, "flat 15–20%\nbuffer", ha="center", va="center", fontsize=8.8, color=ink2, linespacing=1.1)
for i, (name, v, c, pre) in enumerate(rows):
    ax.barh(i, v - 0.05, 0.6, color=c, left=0.05)
    ax.text(v * 1.12, i, f"{pre}{v:g}%", va="center", fontsize=9.6, color=ink)
ax.set_xscale("log"); ax.set_xlim(0.05, 400)
ax.set_xticks([0.1, 1, 10, 100]); ax.set_xticklabels(["0.1%", "1%", "10%", "100%"], fontsize=9.5)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=9.2); ax.invert_yaxis()
ax.set_ylim(len(rows) - 0.4, -1.4)
ax.set_xlabel("95% carbon at risk (share of contracted CO2, log scale)", color=ink2, fontsize=10)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("The risk of losing stored carbon spans nearly three orders of magnitude", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-15-carbon-at-risk.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-15-carbon-at-risk.png")
