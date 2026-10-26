# Figure for the blog post "Wind makes ecosystems spend more water per unit of carbon" (2026-10-26).
# Numbers reported in Wang et al. (2026), Nature Climate Change, https://doi.org/10.1038/s41558-026-02781-z,
# from 146 eddy-covariance sites (growing season, daily mean temperature > 0 °C):
# (a) partial correlation between WUE and wind speed (controlling for Ta, P, CO2, SR, VPD): significantly negative at
#     79.5% of sites, significantly positive at 5.5%, not significant at the remaining 15%.
# (b) sensitivity of WUE to wind speed, dWUE/dWind in gC kg-1 H2O (m s-1)-1, median and interquartile range:
#     all sites -0.26 (-0.45 to -0.11); evergreen needleleaf forests -0.38 (-0.54 to -0.17);
#     shrublands -0.10 (-0.22 to 0.03); humid sites -0.34 (-0.51 to -0.16); arid sites -0.0003 (-0.13 to 0.05).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-26-wind-wue-obs.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
neg, pos, ns, dot = "#2a78d6", "#d6604d", "#d8d6d0", "#1f5fa8"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 6.4), facecolor=surf, gridspec_kw={"height_ratios": [1, 2.4]})

parts = [("Lower WUE in windy weather", 79.5, neg), ("No significant link", 15.0, ns), ("Higher WUE", 5.5, pos)]
left = 0
for name, v, c in parts:
    a.barh(0, v, 0.55, left=left, color=c)
    left += v
a.text(39.75, 0, "79.5%: lower WUE when windier", ha="center", va="center", fontsize=11, color="#ffffff")
a.text(87, 0, "15%", ha="center", va="center", fontsize=10.5, color=ink)
a.annotate("5.5%: higher WUE", (97.2, -0.28), xytext=(80, -0.95), fontsize=10.5, color=ink, ha="center",
           arrowprops=dict(arrowstyle="-", color=ink2, lw=0.9))
a.set_xlim(0, 100); a.set_ylim(-1.25, 0.6); a.axis("off")
a.set_title("a  146 flux towers: how WUE responds to day-to-day wind", loc="left", fontsize=11.5, color=ink)

rows = [("All sites", -0.26, -0.45, -0.11), ("Evergreen needleleaf\nforests", -0.38, -0.54, -0.17),
        ("Shrublands", -0.10, -0.22, 0.03), (None, 0, 0, 0), ("Humid climates", -0.34, -0.51, -0.16),
        ("Arid climates", -0.0003, -0.13, 0.05)]
labels = []
for i, (name, med, lo, hi) in enumerate(rows):
    labels.append(name or "")
    if name is None:
        continue
    b.plot([lo, hi], [i, i], color=dot, lw=2.4, solid_capstyle="round")
    b.plot(med, i, "o", color=dot, ms=8)
    b.text(hi + 0.02, i, f"{med:.2f}".replace("-", "−") if abs(med) >= 0.005 else "≈0", ha="left", va="center",
           fontsize=11, color=ink)
b.axvline(0, color=ink2, lw=1)
b.set_yticks(range(len(rows))); b.set_yticklabels(labels, fontsize=10.5); b.invert_yaxis()
b.set_xlim(-0.62, 0.2)
b.set_xlabel("Change in WUE per 1 m/s more wind\n(gC per kg of water; median and interquartile range)", color=ink2,
             fontsize=10.5)
b.set_title("b  Strongest in conifer forests and humid climates", loc="left", fontsize=11.5, color=ink)
b.grid(axis="x", color=grid, lw=0.8); b.set_axisbelow(True); b.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): b.spines[sp].set_visible(False)

for ax in (a, b):
    ax.set_facecolor(surf)
fig.suptitle("Windier days, lower water use efficiency", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-26-wind-wue-obs.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-26-wind-wue-obs.png")
