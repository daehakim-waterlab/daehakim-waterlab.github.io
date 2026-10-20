# Figure for the blog post "How much water and carbon does AI use?" (2026-10-20).
# Data: litres of water consumed per kWh, as reported or derived in de Vries-Gao (2026), Patterns 7, 101430,
# doi:10.1016/j.patter.2025.101430:
#   on site (direct): IEA implied WUE 0.56 (2023); weighted average of company reports 0.59 (2024);
#   at the power plant (indirect): IEA implied 1.04 (2023); Meta 3.92 (2024); Apple, Google and Meta US data
#   centers 3.40 (2023); LBNL US data centers 4.52 (2023); Siddik et al. US data centers 5.3 (2018);
#   range of grid water intensity at the US data center locations examined: 0.68-11.98.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-20-water-per-kwh.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
direct, indirect = "#2a78d6", "#d6604d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

rows = [  # label, L/kWh, colour
    ("On site: IEA global estimate (2023)", 0.56, direct),
    ("On site: tech company reports (2024)", 0.59, direct),
    ("Power plant: IEA global estimate (2023)", 1.04, indirect),
    ("Power plant: Apple, Google, Meta\nUS data centers (2023)", 3.40, indirect),
    ("Power plant: Meta, all sites (2024)", 3.92, indirect),
    ("Power plant: LBNL, US data centers (2023)", 4.52, indirect),
    ("Power plant: US data centers (2018)", 5.30, indirect),
]
y = [0, 1, 2.6, 3.6, 4.6, 5.6, 6.6]
fig, ax = plt.subplots(figsize=(9, 6.2), facecolor=surf); ax.set_facecolor(surf)
for (lab, v, c), yy in zip(rows, y):
    ax.barh(yy, v, 0.62, color=c)
    ax.text(v + 0.08, yy, f"{v:.2f}", va="center", fontsize=11.5, color=ink)
ax.text(5.95, 0.5, "Water evaporated in\nthe data center's\ncooling system", ha="right", va="center",
        fontsize=10.5, color=direct)
ax.text(5.95, 3.1, "Water consumed to\ngenerate the electricity", ha="right", va="center",
        fontsize=10.5, color=indirect)
ax.axhline(1.8, color=grid, lw=1.2)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=10.5)
ax.invert_yaxis()
ax.set_xlim(0, 6)
ax.set_xlabel("Litres of water consumed per kWh", color=ink2)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.suptitle("Most of a data center's water is used at the power plant, not on site",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.text(0.985, 0.012, "At individual US sites, grid water intensity ranged from 0.68 to 11.98 L/kWh",
         ha="right", fontsize=9.5, color=ink2)
fig.tight_layout(rect=(0, 0.03, 1, 1))
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-water-per-kwh.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-water-per-kwh.png")
