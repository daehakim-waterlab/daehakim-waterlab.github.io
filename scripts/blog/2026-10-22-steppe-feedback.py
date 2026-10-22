# Figure for the blog post "An abrupt shift to a hotter, drier climate in the Western Eurasian Steppe" (2026-10-22).
# Schematic of the soil moisture-temperature feedback described in Piao et al. (2026), Nature Geoscience,
# https://doi.org/10.1038/s41561-026-02125-8: drier soils suppress evaporative cooling, raise sensible heat flux
# (Bowen ratio), warm the near-surface air and raise evaporative demand; the warmer column reinforces the
# upper-level anticyclone, whose sinking air reduces clouds and rain, drying the soil further.
# External forcing sets the background; an internally generated Eurasian wave train amplified it after the early 1990s.
# Drawn by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-steppe-feedback.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
loop, drive, out = "#b4532a", "#2a78d6", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig, ax = plt.subplots(figsize=(6.6, 7.4), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0, 11.2); ax.axis("off")

def box(x, y, text, color, w=4.0, h=1.15, fill="#ffffff", fs=10.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fill, ec=color, lw=1.6))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=ink, linespacing=1.3)

def arrow(p, q, color, rad=0.0, lw=1.8):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=16, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))

# drivers
box(2.55, 10.3, "Global warming\n(external forcing):\nthe background drying", drive, w=4.3, h=1.3, fill="#eef4fc")
box(7.45, 10.3, "Eurasian wave train\n(internal variability):\namplifier since early 1990s", drive, w=4.3, h=1.3, fill="#eef4fc")

# loop, clockwise from top
P = {"high": (5.0, 8.2), "soil": (7.55, 5.95), "flux": (5.0, 3.7), "air": (2.45, 5.95)}
box(*P["high"], "Stronger upper-level high:\nsinking air, fewer clouds,\nless rain", loop, w=4.4, h=1.3)
box(*P["soil"], "Drier soil", loop, w=3.3, h=0.9)
box(*P["flux"], "Less evaporative cooling,\nmore sensible heat\n(higher Bowen ratio)", loop, w=4.4, h=1.3)
box(*P["air"], "Hotter air,\nhigher evaporative\ndemand (PET)", loop, w=3.3, h=1.3)
arrow((7.2, 7.55), (7.75, 6.45), loop, rad=-0.25)
arrow((7.6, 5.45), (6.9, 4.4), loop, rad=-0.25)
arrow((3.0, 4.4), (2.3, 5.25), loop, rad=-0.25)
arrow((2.35, 6.65), (2.85, 7.55), loop, rad=-0.25)
ax.text(5.0, 5.95, "positive\nfeedback", ha="center", va="center", fontsize=11, color=loop, style="italic")

arrow((2.55, 9.62), (3.6, 8.9), drive)
arrow((7.45, 9.62), (6.4, 8.9), drive)

# outcomes
box(5.0, 1.45, "Outcomes: more heatwave days, flash droughts, grassland ≈5% smaller\nand barren land ≈26% larger (2021–2023 vs pre-2010), lower GPP", out,
    w=9.6, h=1.25, fill="#f3f2ef", fs=10)
arrow((5.0, 3.02), (5.0, 2.12), out)

fig.suptitle("The soil moisture feedback that locks in the dry regime", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-steppe-feedback.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-steppe-feedback.png")
