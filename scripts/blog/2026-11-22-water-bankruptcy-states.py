# Figure 1 for the blog post "Water bankruptcy: when a water crisis never ends" (2026-11-22).
# A schematic of the three states of concern in human-water systems described by Madani (2026):
# water stress (the system still oscillates around a stable baseline), water crisis (an acute
# shock followed by recovery) and water bankruptcy (persistent overdraft that lowers the baseline
# itself, so the old level cannot be restored). The curves are invented for illustration and do
# not show data. Drawn by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-11-22-water-bankruptcy-states.py
import os, matplotlib
import numpy as np
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, amber, red = "#2a78d6", "#d08a1f", "#c0392b"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

t = np.linspace(0, 60, 601)
rng = np.random.default_rng(3)
noise = np.convolve(rng.normal(0, 1, t.size), np.ones(25) / 25, mode="same")
wiggle = 4 * np.sin(2 * np.pi * t / 7) + 6 * noise

stress = 100 + wiggle
crisis = 100 + wiggle - 38 * np.exp(-((t - 25) / 3.2) ** 2)
decline = np.where(t < 12, 0, -1.25 * (t - 12))
decline = np.maximum(decline, -48)
bankrupt = 100 + 0.6 * wiggle + decline

fig, axes = plt.subplots(3, 1, figsize=(6.6, 7.0), facecolor=surf, sharex=True)
panels = [(stress, blue, "a  Water stress",
           "High pressure, but the system still swings\naround its normal level and can recover"),
          (crisis, amber, "b  Water crisis",
           "An acute shock (a severe drought, say),\nfollowed by recovery"),
          (bankrupt, red, "c  Water bankruptcy",
           "Years of overdraft lower the baseline itself;\nthe old normal cannot be restored")]
for ax, (y, c, title, note) in zip(axes, panels):
    ax.set_facecolor(surf)
    ax.axhline(100, color=ink2, lw=1.0, ls=(0, (4, 3)))
    ax.plot(t, y, color=c, lw=2.3)
    ax.set_ylim(35, 125); ax.set_yticks([])
    ax.set_title(title, loc="left", fontsize=11, color=ink)
    ax.text(59.5, 121, note, ha="right", va="top", fontsize=8.9, color=ink2, linespacing=1.2)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
    ax.spines["bottom"].set_color(ink2)
axes[0].text(0.5, 110, "normal level", fontsize=8.6, color=ink2, va="bottom")
axes[2].annotate("new, lower\n\"normal\"", xy=(55, 53), xytext=(40, 44), fontsize=8.9, color=red,
                 ha="center", va="center", arrowprops=dict(arrowstyle="-|>", color=red, lw=1.2))
axes[2].set_xlabel("Time (decades)", color=ink2, fontsize=10)
axes[2].set_xticks([])
fig.text(0.012, 0.5, "Water available (surface water + groundwater)", rotation=90, va="center",
         ha="left", fontsize=9.6, color=ink2)
fig.suptitle("Stress, crisis, bankruptcy: three different states", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout(rect=(0.03, 0, 1, 1))
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-22-water-bankruptcy-states.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-22-water-bankruptcy-states.png")
