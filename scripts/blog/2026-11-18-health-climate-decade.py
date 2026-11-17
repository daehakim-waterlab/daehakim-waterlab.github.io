# Figure for the blog post "A decade of tracking climate and health: the 2026 Lancet Countdown report" (2026-11-18).
# Four headline indicators of the 2026 Lancet Countdown report (Romanello et al. 2026), comparing the decade
# before the Paris Agreement entered into force (2006-15) with the decade after it (2016-25). Values are
# typed in from the report text:
#   heat-related deaths per year: 398,400 (2006-15) and 540,800 (2016-23)       indicator 1.1.5
#   heatwave days per person aged 65+ per year: 7.2 and 11.5                     indicator 1.1.1
#   share of land with >= 1 month of extreme drought per year: 28.4% and 41.7%  indicator 1.2.2
#   share of land with >= 1 very extreme (>10-year) daily rainfall: 14.8% and 17.2%  indicator 1.2.3
# Bar charts drawn by Daeha Kim; no figure from the report is reproduced.
# Run from the repository root: python scripts/blog/2026-11-18-health-climate-decade.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
before_c, after_c = "#a9a6a0", "#c0392b"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

panels = [
    ("a  Heat-related deaths per year", 398_400, 540_800, "{:,.0f}", "2016–23", 650_000),
    ("b  Heatwave days per person aged 65+", 7.2, 11.5, "{:.1f} days", "2016–25", 14),
    ("c  Land with at least a month of\n    extreme drought each year", 28.4, 41.7, "{:.1f}%", "2016–25", 50),
    ("d  Land with at least one very\n    extreme daily rainfall each year", 14.8, 17.2, "{:.1f}%", "2016–25", 21),
]

fig, axes = plt.subplots(2, 2, figsize=(6.6, 6.2), facecolor=surf)
for ax, (title, v0, v1, fmt, lab1, top) in zip(axes.flat, panels):
    ax.set_facecolor(surf)
    ax.bar([0, 1], [v0, v1], width=0.6, color=[before_c, after_c], zorder=2)
    for x, v in ((0, v0), (1, v1)):
        ax.text(x, v + top * 0.02, fmt.format(v), ha="center", va="bottom", fontsize=9.6,
                color=ink if x else ink2, fontweight="bold" if x else "normal")
    pct = 100 * (v1 - v0) / v0
    ax.text(0.5, top * 0.93, f"+{pct:.0f}%", ha="center", va="top", fontsize=11, color=after_c, fontweight="bold")
    ax.set_xticks([0, 1], ["2006–15", lab1], fontsize=9.6)
    ax.set_ylim(0, top)
    ax.set_yticks([])
    ax.set_title(title, loc="left", fontsize=10.2, color=ink, linespacing=1.15)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
fig.suptitle("Ten years after Paris: before and after, side by side", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout(h_pad=1.6, w_pad=1.2)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-18-health-climate-decade.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-18-health-climate-decade.png")
