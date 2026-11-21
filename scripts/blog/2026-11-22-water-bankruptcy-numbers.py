# Figure 2 for the blog post "Water bankruptcy: when a water crisis never ends" (2026-11-22).
# Headline shares from "Global Water Bankruptcy in Brief" in the UNU-INWEH report
# (Madani 2026, Global Water Bankruptcy: Living Beyond Our Hydrological Means in the Post-Crisis Era).
# The report states these as approximate values ("more than half", "around 70%", "nearly
# three-quarters", "over 40%"); the bars show the stated round numbers. Red bars mark decline or
# insecurity, blue bars what water use depends on. Drawn by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-11-22-water-bankruptcy-numbers.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
red, blue, grey = "#c0392b", "#2a78d6", "#d9d7d2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

rows = [
    ("World population living in water-insecure\nor critically water-insecure countries", 75, "nearly 3/4"),
    ("Major aquifers with long-term\ndeclining trends", 70, "around 70%"),
    ("Freshwater withdrawals used\nfor agriculture", 70, "roughly 70%"),
    ("Large lakes that have lost water\nsince the early 1990s", 50, "more than half"),
    ("Domestic water supplied\nfrom groundwater", 50, "about 50%"),
    ("Irrigation water supplied\nfrom groundwater", 40, "over 40%"),
]

fig, ax = plt.subplots(figsize=(6.6, 5.6), facecolor=surf)
ax.set_facecolor(surf)
for i, (label, v, txt) in enumerate(rows):
    y = len(rows) - 1 - i
    ax.barh(y, 100, color=grey, height=0.5, zorder=1)
    ax.barh(y, v, color=blue if "groundwater" in label or "agriculture" in label else red,
            height=0.5, zorder=2)
    ax.text(v + 1.5, y, txt, va="center", ha="left", fontsize=9.6, color=ink, fontweight="bold")
    ax.text(0, y + 0.36, label, va="bottom", ha="left", fontsize=9.3, color=ink2, linespacing=1.1)
ax.set_xlim(0, 100); ax.set_ylim(-0.5, len(rows) - 0.05)
ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"], fontsize=9.2, color=ink2)
ax.set_yticks([])
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.spines["bottom"].set_color(ink2)
fig.text(0.012, 0.905, "red: decline or insecurity   blue: what the world relies on", fontsize=9, color=ink2)
fig.suptitle("A world living beyond its water means", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-22-water-bankruptcy-numbers.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-22-water-bankruptcy-numbers.png")
