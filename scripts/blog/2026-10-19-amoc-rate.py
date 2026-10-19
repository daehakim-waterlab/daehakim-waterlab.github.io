# Figure for the blog post "Will the Atlantic overturning tip, and how fast would we feel it?" (2026-10-19).
# Data: CO2-ramp experiments with CESM (background hosing FH = 0.45 Sv) reported in
# van Westen, Boerner & Dijkstra (2026), Nature Climate Change 16, 1195-1206, doi:10.1038/s41558-026-02730-w.
# Threshold range +4.0 C (1.4-8 C) as quoted in the same paper. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-19-amoc-rate.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, orange, green = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})
fig, ax = plt.subplots(figsize=(9, 5), facecolor=surf); ax.set_facecolor(surf)

# commonly cited warming threshold and its range
ax.plot([6.12, 6.12], [1.4, 8.0], color=ink2, lw=1.2)
ax.scatter([6.12, 6.12], [1.4, 8.0], marker="_", s=90, color=ink2, linewidths=1.2)
ax.scatter([6.12], [4.0], marker="_", s=260, color=ink2, linewidths=2.5, zorder=3)
ax.text(6.0, 4.0, "commonly cited\nthreshold +4 °C\n(range 1.4–8 °C)", ha="right", va="center",
        fontsize=9.5, color=ink2)

# today's rate of CO2 rise
ax.axvline(2.6, color=ink2, lw=1, ls=(0, (4, 3)), zorder=1)
ax.text(2.68, 7.75, "today: +2.6 ppm/yr\n(Mauna Loa, 2015–2025)", fontsize=9.5, color=ink2, va="top")

# slow ramp: no collapse up to +5.5 C
ax.annotate("", xy=(0.5, 5.6), xytext=(0.5, 0.15),
            arrowprops=dict(arrowstyle="-|>", color=blue, lw=3, mutation_scale=18))
ax.text(0.68, 5.35, "+0.5 ppm/yr:\nAMOC stays strong\nup to +5.5 °C", color=blue, fontsize=10, va="top")

# fast ramps: collapse onset at about +2 C
for x, y in [(2.5, 2.02), (5.0, 1.99)]:
    ax.plot([x, x], [0.15, y], color=orange, lw=3, solid_capstyle="butt")
    ax.scatter([x], [y], marker="X", s=150, color=orange, edgecolor=surf, linewidth=1.2, zorder=4)
ax.text(3.55, 2.55, "+2.5 and +5.0 ppm/yr:\ncollapse begins at about +2 °C", color=orange,
        fontsize=10, ha="center")

ax.set_xlim(0, 6.6); ax.set_ylim(0, 8.3)
ax.set_xticks([0, 0.5, 1, 2, 2.5, 3, 4, 5]); ax.set_xticklabels(["0", "0.5", "1", "2", "2.5", "3", "4", "5"])
ax.set_xlabel("Rate of CO₂ increase in the experiment (ppm per year)", color=ink2)
ax.set_ylabel("Global warming above pre-industrial (°C)", color=ink2)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.set_title("In one climate model, how fast CO₂ rises matters more than how warm it gets",
             loc="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-19-amoc-rate.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-19-amoc-rate.png")
