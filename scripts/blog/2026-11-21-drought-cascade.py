# Figure for the blog post "Beyond the drought map: monitoring what drought actually does" (2026-11-21).
# A schematic of the drought-related cascading hazards described by AghaKouchak et al. (2023),
# with the Montecito, California example they give (drought 2012-16, fire in December 2017,
# debris flow after intense rain in January 2018), and a comparison of hazard-based and
# impact-based monitoring. Drawn by Daeha Kim; no figure from the paper is reproduced.
# Run from the repository root: python scripts/blog/2026-11-21-drought-cascade.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
cols = ["#b8862b", "#d4602c", "#b5321f", "#2a78d6", "#5b4a8a"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig = plt.figure(figsize=(6.6, 6.0), facecolor=surf)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 10); ax.set_ylim(0.75, 9.85); ax.axis("off")

def box(x, y, w, h, fc, ec, text, tc=ink, fs=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight=weight, linespacing=1.2)

def arrow(x0, y0, x1, y1, c=ink2):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=14,
                                 lw=1.5, color=c, shrinkA=0, shrinkB=0))

ax.text(0.15, 9.5, "a  One drought, a chain of hazards", fontsize=11.5, color=ink, va="center")
chain = [("Drought", "dry soil, less\nevaporation"),
         ("Heatwave", "more of the sun's\nenergy heats the air"),
         ("Wildfire", "dry fuel burns;\nslopes left bare"),
         ("Extreme rain", "falls on burned,\ncracked slopes"),
         ("Debris flow\nor flood", "mud and boulders\nrush downhill")]
x0, w, h, gap = 0.25, 1.72, 1.0, 0.205
y = 8.0
for i, (name, note) in enumerate(chain):
    x = x0 + i * (w + gap)
    box(x, y, w, h, cols[i], cols[i], name, tc="white", fs=9.6, weight="bold")
    ax.text(x + w / 2, y - 0.14, note, ha="center", va="top", fontsize=7.9, color=ink2, linespacing=1.15)
    if i < len(chain) - 1:
        arrow(x + w + 0.02, y + h / 2, x + w + gap - 0.02, y + h / 2)

# Montecito timeline
ax.text(0.15, 6.35, "Example: Montecito, California", fontsize=10.2, color=ink, va="center", fontweight="bold")
ty = 5.6
ax.plot([0.5, 9.5], [ty, ty], color=ink2, lw=1.2)
events = [(0.9, 2.9, "2012–16", "multi-year\ndrought", cols[0]),
          (6.0, 6.0, "Dec 2017", "large\nwildfire", cols[2]),
          (8.6, 8.6, "Jan 2018", "intense rain triggers\na deadly debris flow", cols[4])]
for xa, xb, when, what, c in events:
    if xb > xa:
        ax.plot([xa, xb], [ty, ty], color=c, lw=7, solid_capstyle="butt")
        xm = (xa + xb) / 2
    else:
        ax.plot(xa, ty, "o", ms=11, color=c)
        xm = xa
    ax.text(xm, ty + 0.3, when, ha="center", va="bottom", fontsize=9, color=ink)
    ax.text(xm, ty - 0.3, what, ha="center", va="top", fontsize=8.4, color=ink2, linespacing=1.15)
ax.text(4.4, ty - 0.3, "years apart,\nyet one story", ha="center", va="top", fontsize=8.4,
        color=ink2, style="italic")

# Part b: hazard-based vs impact-based monitoring
ax.text(0.15, 3.95, "b  What a drought monitor reports", fontsize=11.5, color=ink, va="center")
box(0.25, 1.85, 4.4, 1.7, "#efeeea", ink2,
    "Today: hazard-based\n\nHow dry is it?\nrainfall, soil moisture,\nstreamflow, snow", fs=9.2)
box(5.35, 1.85, 4.4, 1.7, "#e8eef6", cols[3],
    "Proposed: impact-based\n\nWhat will it do?\ncrop yield, drinking water,\nhydropower, jobs, fire risk", fs=9.2)
arrow(4.7, 2.7, 5.3, 2.7, c=cols[3])
ax.text(5.0, 1.6, "Needs: impact records, local water-use and storage data,\n"
        "new satellites (such as SWOT) and AI to link them",
        ha="center", va="top", fontsize=8.8, color=ink2, linespacing=1.25)

fig.savefig("assets/img/blog/2026-11-21-drought-cascade.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-21-drought-cascade.png")
