# Figure for the blog post "How much water and carbon does AI use?" (2026-10-20).
# Data reported in Privette, Barros & Cai (2026), AGU Advances 7, e2025AV002140, doi:10.1029/2025AV002140:
#   US data centers combined: about 0.3% of the public water supply of the contiguous US;
#   Google, Council Bluffs (Iowa), 2023: about 21% of the city's total water use;
#   data centers in The Dalles (Oregon), 2021: about 29% of the city's total water demand;
#   one proposed data center in Mesa (Arizona): up to 1.75 million gallons per day, about two-thirds of the
#   city's daily water supply (projection at full operation).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-20-local-share.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
national, local, proj = "#5b5a57", "#2a78d6", "#a9c8ec"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [
    ("All US data centers\n(share of US public supply)", 0.3, national, "0.3%"),
    ("One Google campus,\nCouncil Bluffs, Iowa (2023)", 21, local, "21%"),
    ("Data centers in\nThe Dalles, Oregon (2021)", 29, local, "29%"),
    ("One proposed data center,\nMesa, Arizona (projected)", 66.7, proj, "about two-thirds"),
]
fig, ax = plt.subplots(figsize=(9, 5.4), facecolor=surf); ax.set_facecolor(surf)
for i, (lab, v, c, txt) in enumerate(rows):
    ax.barh(i, v, 0.6, color=c)
    ax.text(v + 1.2, i, txt, va="center", fontsize=12, color=ink, fontweight="bold")
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=11)
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Share of the relevant water supply (%)", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.suptitle("Small on a national scale, large for the town next door",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-local-share.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-local-share.png")
