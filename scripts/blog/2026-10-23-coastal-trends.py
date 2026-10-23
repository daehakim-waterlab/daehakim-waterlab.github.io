# Figure for the blog post "Coastal groundwater and seawater intrusion in a warming world" (2026-10-23).
# Numbers reported in Nolte et al. (2026), Nature Water 4, 673-682, https://doi.org/10.1038/s44221-026-00619-8:
# (a) share of observations (H3-8 grid cells) with significant groundwater-level trends (|slope| >= 0.1 m/yr) by
#     hydroclimatic cluster: water-limited clusters C1 and C2 34-36%, energy-limited C4 (steep gradient) 12% and
#     C3 (flat gradient) 3%;
# (b) extrapolating recent trends over the next decade, locations in or entering flat-gradient (seawater-intrusion
#     susceptible) conditions: 93.4% persist, 3.5% newly emerge, 3.1% stabilize.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-23-coastal-trends.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
dry, wet = "#c4813a", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 5.8), facecolor=surf, gridspec_kw={"height_ratios": [3, 1.6]})

rows = [("Dry coasts (C1, C2)\nwater-limited", 34, 36, dry), ("Wet coasts, steep\ngradient (C4)", 12, 12, wet),
        ("Wet coasts, flat\ngradient (C3)", 3, 3, wet)]
for i, (name, lo, hi, c) in enumerate(rows):
    a.barh(i, hi, 0.6, color=c)
    a.text(hi + 0.8, i, f"{lo}–{hi}%" if lo != hi else f"{lo}%", ha="left", va="center", fontsize=11, color=ink)
a.set_yticks(range(len(rows))); a.set_yticklabels([r[0] for r in rows], fontsize=11); a.invert_yaxis()
a.set_xlim(0, 42)
a.set_xlabel("Locations with level trends ≥0.1 m per year (%)", color=ink2, fontsize=10.5)
a.set_title("a  Groundwater levels move most on dry coasts", loc="left", fontsize=11.5, color=ink)
a.grid(axis="x", color=grid, lw=0.8); a.set_axisbelow(True); a.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): a.spines[sp].set_visible(False)

parts = [("Persistent", 93.4, "#8a3b2f"), ("Emerging", 3.5, "#d6604d"), ("Stabilizing", 3.1, "#7fa9de")]
left = 0
for name, v, c in parts:
    b.barh(0, v, 0.55, left=left, color=c)
    left += v
b.text(46.7, 0, "Persistent  93.4%", ha="center", va="center", fontsize=11, color="#ffffff")
b.annotate("Emerging 3.5%", (95.2, 0.28), xytext=(70, 0.75), fontsize=10.5, color=ink, ha="center",
           arrowprops=dict(arrowstyle="-", color=ink2, lw=0.9))
b.annotate("Stabilizing 3.1%", (98.5, -0.28), xytext=(82, -0.85), fontsize=10.5, color=ink, ha="center",
           arrowprops=dict(arrowstyle="-", color=ink2, lw=0.9))
b.set_xlim(0, 100); b.set_ylim(-1.2, 1.1); b.axis("off")
b.set_title("b  Susceptible sites over the next decade", loc="left", fontsize=11.5,
            color=ink)

for ax in (a, b):
    ax.set_facecolor(surf)
fig.suptitle("Coastal groundwater, 1990–2024: what ~480,000 monitoring sites show", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-23-coastal-trends.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-23-coastal-trends.png")
