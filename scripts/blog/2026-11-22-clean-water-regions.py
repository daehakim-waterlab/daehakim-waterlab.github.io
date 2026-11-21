# Figure 2 for the blog post "Clean water scarcity: counting quality as well as quantity" (2026-11-22).
# Data: Table 2 of Jones, Bierkens & van Vliet (2024), Nature Climate Change 14, 629-635.
# Share of each region's population exposed to clean water scarcity (WSq) in at least one month
# per year: historical (2005-2020) and end of century (2081-2100) under three scenarios.
# Values are means over five climate models. Drawn by Daeha Kim. Run from the repository root:
#   python scripts/blog/2026-11-22-clean-water-regions.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})

# region: historical, 2081-2100 SSP1-RCP2.6, SSP3-RCP7.0, SSP5-RCP8.5
rows = {
    "Middle East & North Africa": (72.9, 79.2, 85.1, 77.4),
    "Southern Asia": (66.9, 69.7, 73.5, 67.8),
    "East Asia & Pacific": (61.7, 57.9, 61.3, 60.2),
    "World": (55.4, 57.4, 63.8, 59.6),
    "Western Europe": (50.0, 54.5, 54.6, 67.5),
    "North America": (48.4, 59.5, 49.5, 66.0),
    "Latin America & Caribbean": (48.3, 39.6, 57.6, 47.6),
    "Eastern Europe & Central Asia": (45.4, 45.2, 59.7, 56.1),
    "Sub-Saharan Africa": (26.3, 46.3, 53.7, 43.6),
}
sc = [("SSP1–RCP2.6 (sustainable)", "#2a9d8f", "o"), ("SSP3–RCP7.0 (regional rivalry)", "#c0392b", "s"),
      ("SSP5–RCP8.5 (fossil-fueled growth)", "#e08a1e", "D")]

fig, ax = plt.subplots(figsize=(8.4, 5.6), facecolor=surf)
ax.set_facecolor(surf)
names = list(rows)
for i, name in enumerate(names):
    y = len(names) - 1 - i
    h, *fut = rows[name]
    ax.plot([min(h, *fut), max(h, *fut)], [y, y], color=grid, lw=6, solid_capstyle="round", zorder=1)
    ax.scatter(h, y, s=70, color="white", edgecolor=ink, lw=1.6, zorder=3)
    for v, dy, (lab, col, mk) in zip(fut, (0.17, 0, -0.17), sc):  # small offsets so overlapping markers stay visible
        ax.scatter(v, y + dy, s=46, color=col, marker=mk, zorder=4)
    w = "bold" if name == "World" else "normal"
    ax.text(18.5, y, name, ha="right", va="center", fontsize=10, color=ink, fontweight=w)
ax.scatter([], [], s=70, color="white", edgecolor=ink, lw=1.6, label="2005–2020")
for lab, col, mk in sc:
    ax.scatter([], [], s=46, color=col, marker=mk, label="2081–2100, " + lab)
ax.set_xlim(19, 90); ax.set_ylim(-0.7, len(names) - 0.3)
ax.set_yticks([])
ax.set_xticks(range(20, 91, 10), [f"{v}%" for v in range(20, 91, 10)])
ax.tick_params(colors=ink2, labelsize=9.5)
ax.grid(axis="x", color=grid, lw=0.8, zorder=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.spines["bottom"].set_color(ink2)
ax.set_xlabel("Share of population facing clean water scarcity at least one month a year", color=ink2, fontsize=10)
ax.legend(frameon=False, fontsize=8.8, loc="lower center", bbox_to_anchor=(0.42, -0.30), ncol=2, labelcolor=ink)
fig.suptitle("Where clean water scarcity is heading by 2081–2100", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.subplots_adjust(left=0.30, right=0.97, top=0.92, bottom=0.23)
os.makedirs("assets/img/blog", exist_ok=True)
out = "assets/img/blog/2026-11-22-clean-water-regions.png"
fig.savefig(out, dpi=170, facecolor=surf)
print("saved", out)
