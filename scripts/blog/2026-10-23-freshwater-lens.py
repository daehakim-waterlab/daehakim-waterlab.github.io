# Figure for the blog post "Coastal groundwater and seawater intrusion in a warming world" (2026-10-23).
# Illustrative calculation by Daeha Kim, not a result of Nolte et al. (2026).
# Ghyben-Herzberg sharp-interface approximation: the freshwater-seawater interface lies about
# rho_f / (rho_s - rho_f) ~ 40 times the freshwater head above sea level below sea level (Werner et al. 2013).
# Coast with the "flat" land-sea gradient threshold of Nolte et al. (2026), 1e-3 m/m, so the head is 1e-3 * x.
# Topography-limited case: inland heads cannot rise with the sea, so a sea-level rise d lowers the head above sea
# level by d everywhere. The same head loss results from a groundwater-level decline of 0.1 m/yr (the paper's trend
# threshold) sustained for 3 or 10 years. 0.3-1.0 m is the projected global mean sea-level rise by 2100
# (relative to 1995-2014) quoted in the paper. Steady state, homogeneous aquifer, no mixing zone.
# Run from the repository root: python scripts/blog/2026-10-23-freshwater-lens.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
cols = ["#2a78d6", "#d9a37f", "#b4532a"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

x = np.linspace(0, 3000, 601)            # distance inland (m)
grad, ratio = 1e-3, 40.0
fig, ax = plt.subplots(figsize=(6.6, 6.4), facecolor=surf); ax.set_facecolor(surf)
cases = [(0.0, "Today"), (0.3, "Head 0.3 m lower: sea-level rise 0.3 m,\nor a 0.1 m/yr decline for 3 years"),
         (1.0, "Head 1.0 m lower: sea-level rise 1.0 m,\nor a 0.1 m/yr decline for 10 years")]
for (d, lab), c in zip(cases, cols):
    h = np.clip(grad * x - d, 0, None)
    ax.plot(x / 1000, ratio * h, color=c, lw=2.4, label=lab)
    if d > 0:
        ax.plot([d / grad / 1000], [0], "o", color=c, ms=6)
ax.invert_yaxis()
ax.set_xlim(0, 3.4); ax.set_ylim(130, -8)
ax.set_xlabel("Distance inland from the coast (km)", color=ink2, fontsize=11)
ax.set_ylabel("Depth of the freshwater–seawater\ninterface below sea level (m)", color=ink2, fontsize=11)
ax.text(3.04, 120, "120 m", va="center", fontsize=10.5, color=cols[0])
ax.text(3.04, 80, "80 m", va="center", fontsize=10.5, color=cols[2])
ax.annotate("no freshwater lens:\nseawater within 1 km", (0.65, 0), xytext=(1.85, 9), fontsize=10, color=cols[2],
            arrowprops=dict(arrowstyle="-", color=ink2, lw=0.9))
ax.text(0.06, 124, "Interface depth ≈ 40 × freshwater head above sea level\nGradient 10⁻³ (the paper's 'flat' threshold);"
        " heads cannot rise", fontsize=9.5, color=ink2, va="bottom", linespacing=1.4)
fig.legend(*ax.get_legend_handles_labels(), loc="lower left", frameon=False, fontsize=10, bbox_to_anchor=(0.1, 0.0))
ax.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3]); ax.spines["bottom"].set_bounds(0, 3)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Every 1 m of lost head thins the freshwater lens by about 40 m", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout(rect=(0, 0.2, 1, 1))
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-23-freshwater-lens.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-23-freshwater-lens.png")
