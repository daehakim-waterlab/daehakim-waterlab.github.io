# Figure for the blog post "Does living through extreme weather make people act on climate?" (2026-10-19).
# Data: group values reported in the text of Wyss, Guizar Rosales et al. (2026), Nature Climate Change,
# doi:10.1038/s41558-026-02765-z (final analytic sample, N = 1,451 US adults):
#   share with >= 1 NOAA-recorded extreme weather episode in the home county, 30 days before the study:
#     Republicans 48.2 %, Democrats 43.4 %;
#   self-reported extreme weather experience (log-transformed count): R 2.87 (s.d. 1.01), D 3.06 (s.d. 0.97);
#   subjective attribution of extreme weather to climate change: R 3.94 (s.d. 1.16), D 4.52 (s.d. 0.65).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-19-weather-filter.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, red = "#2a78d6", "#d64545"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})
fig, axes = plt.subplots(3, 1, figsize=(8.6, 7.4), facecolor=surf)
rows = ["Republicans", "Democrats"]
colors = [red, blue]
panels = [
    ("1. Recorded: at least one extreme weather episode in the home county\n    in the 30 days before the study (NOAA Storm Events)",
     [48.2, 43.4], None, (0, 80), "% of participants", "{:.1f} %"),
    ("2. Reported: extreme weather the participants say they experienced\n    (self-report, log-transformed count)",
     [2.87, 3.06], [1.01, 0.97], (1.5, 4.5), "mean ± 1 s.d.", "{:.2f}"),
    ("3. Interpreted: how strongly they attribute extreme weather\n    to climate change",
     [3.94, 4.52], [1.16, 0.65], (2.5, 5.9), "mean ± 1 s.d.", "{:.2f}"),
]
for ax, (title, vals, sds, xlim, xlab, fmt) in zip(axes, panels):
    ax.set_facecolor(surf)
    for i, (v, c) in enumerate(zip(vals, colors)):
        if sds is None:
            ax.barh(i, v, height=0.55, color=c, alpha=0.9)
            ax.text(v + 0.8, i, fmt.format(v), va="center", color=ink, fontsize=12)
        else:
            ax.plot([v - sds[i], v + sds[i]], [i, i], color=c, lw=2.2, solid_capstyle="round")
            ax.scatter([v], [i], s=110, color=c, zorder=3, edgecolor=surf, linewidth=1.2)
            ax.text(v, i - 0.14, fmt.format(v), ha="center", va="bottom", color=ink, fontsize=12)
    ax.set_yticks([0, 1]); ax.set_yticklabels(rows)
    ax.set_ylim(-0.75 if sds is not None else -0.6, 1.5); ax.invert_yaxis()
    ax.set_xlim(*xlim)
    if sds is None: ax.set_xticks(range(0, 61, 10))
    ax.set_xlabel(xlab, color=ink2, fontsize=10.5)
    ax.set_title(title, loc="left", color=ink, fontsize=12, linespacing=1.35)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", length=0)
axes[0].text(79.5, 0.5, "Republicans were slightly\nmore often exposed ...", ha="right", va="center",
             fontsize=10.5, color=ink2)
axes[1].text(4.48, 0.5, "... yet Democrats\nreported more ...", ha="right", va="center",
             fontsize=10.5, color=ink2)
axes[2].text(5.88, 0.5, "... and linked it\nto climate change\nmore strongly", ha="right", va="center",
             fontsize=10.5, color=ink2)
fig.tight_layout(h_pad=1.6)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-19-weather-filter.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-19-weather-filter.png")
