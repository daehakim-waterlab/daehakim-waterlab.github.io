# Figure for the blog post "The vanishing frozen reservoirs of the American West" (2026-11-21).
# Glacier area change in the mountain ranges of the conterminous United States, from the historic
# (mid-20th century, mapped 1953-1982) to the recent (~2015) inventory, after Table 1 of
# Fountain et al. (2026, PNAS). Only ranges with at least 2 km2 of historic glacier area are shown.
# (a) percentage change in area by range; (b) rate of area loss compared with other regions,
# as quoted by Fountain et al. (2026) from published studies. Drawn by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-11-21-us-glacier-loss.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
wa_c, other_c = "#2a78d6", "#c0392b"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

# range, state, historic area (km2), recent area (km2)
ranges = [
    ("North Cascades", "WA", 263.42, 176.27),
    ("Olympic Mountains", "WA", 32.24, 23.44),
    ("South Cascades (Mt Rainier)", "WA", 118.16, 95.64),
    ("Cascade Range", "OR", 32.00, 11.90),
    ("Cascade Range (Mt Shasta)", "CA", 5.15, 4.61),
    ("Sierra Nevada", "CA", 12.18, 4.37),
    ("Lewis Range (Glacier NP)", "MT", 34.24, 19.22),
    ("Mission, Swan, Flathead", "MT", 2.05, 1.16),
    ("Beartooth and Absaroka", "MT", 11.37, 4.31),
    ("Absaroka Range", "WY", 2.24, 0.48),
    ("Teton Range", "WY", 2.97, 1.46),
    ("Wind River Range", "WY", 42.85, 22.42),
]
chg = [(f"{n}, {s}", s, 100 * (r - h) / h) for n, s, h, r in ranges]
chg.sort(key=lambda x: x[2], reverse=True)

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 7.6), facecolor=surf,
                           gridspec_kw={"height_ratios": [12, 4.6]})
for ax in (a, b):
    ax.set_facecolor(surf)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(labelsize=9.4)

names = [c[0] for c in chg]; vals = [c[2] for c in chg]
cols = [wa_c if c[1] == "WA" else other_c for c in chg]
a.barh(range(len(vals)), vals, color=cols, height=0.66, zorder=2)
for i, v in enumerate(vals):
    a.text(v - 1.5, i, f"{v:.0f}%", ha="right", va="center", fontsize=8.8, color=ink2,
           bbox=dict(fc=surf, ec="none", pad=0.6), zorder=4)
a.set_yticks(range(len(vals)), names, fontsize=9)
a.invert_yaxis(); a.yaxis.tick_right(); a.spines["right"].set_visible(True); a.spines["left"].set_visible(False)
a.set_xlim(-90, 0)
a.set_xlabel("Change in glacier area, mid-20th century to about 2015 (%)", color=ink2, fontsize=9.8)
a.axvline(-35, color=ink, lw=1.0, ls=(0, (4, 3)), zorder=3)
a.text(-35.8, len(vals) - 0.35, "all US glaciers: -35%", ha="right", va="center", fontsize=8.8, color=ink)
a.set_title("a  Glacier area lost, by mountain range", loc="left", fontsize=11, color=ink)

comp = [("Western US (mid-1900s to 2015)", -8), ("Austrian Alps (1969-98)", -6),
        ("Eastern Himalaya (1962-2006)", -5), ("Norway (1960s-2010s)", -2.5)]
b.barh(range(len(comp)), [c[1] for c in comp], color=[ink, "#a9a6a0", "#a9a6a0", "#a9a6a0"],
       height=0.6, zorder=2)
for i, (n, v) in enumerate(comp):
    b.text(v - 0.15, i, f"{v:g}%", ha="right", va="center", fontsize=8.8, color=ink2)
b.set_yticks(range(len(comp)), [c[0] for c in comp], fontsize=9)
b.invert_yaxis(); b.yaxis.tick_right(); b.spines["right"].set_visible(True); b.spines["left"].set_visible(False)
b.set_xlim(-10, 0)
b.set_xlabel("Glacier area change per decade (%)", color=ink2, fontsize=9.8)
b.set_title("b  Faster than many other mountain regions", loc="left", fontsize=11, color=ink)

fig.suptitle("A third of the West's glacier ice is gone", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout(h_pad=1.8)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-21-us-glacier-loss.png", dpi=170, facecolor=surf)
for n, s, v in chg: print(f"{n:40s} {v:6.1f}")
print("saved assets/img/blog/2026-11-21-us-glacier-loss.png")
