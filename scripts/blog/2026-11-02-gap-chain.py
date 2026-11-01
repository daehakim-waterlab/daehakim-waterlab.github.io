# Figure for the blog post "Why climate science and economics talk past each other" (2026-11-02).
# Schematic by Daeha Kim of the chain that turns emissions into an economic cost, with the choices that enter at
# each link, following the argument of Sherwood et al. (2026, Nature Climate Change,
# https://doi.org/10.1038/s41558-026-02784-w) that each link should be transparent and its assumptions visible.
# Run from the repository root: python scripts/blog/2026-11-02-gap-chain.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
phys, econ = "#2a78d6", "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

steps = [("Warming", "global mean temperature", "which scenario; climate sensitivity", phys),
         ("Hazards", "heat, humid heat, floods, drought,\nstorms, sea-level rise", "regional patterns, variability,\ntipping and compound events", phys),
         ("Exposure", "people, buildings, farms,\ninfrastructure, ecosystems", "where people and assets\nwill be in the future", ink2),
         ("Adaptation", "what people and firms do", "how much is assumed,\nat what cost", ink2),
         ("Loss", "GDP, capital stocks, health,\nwell-being, inequality", "which losses count; whose;\nnon-market values", econ),
         ("Cost today", "social cost of carbon,\nfinancial risk", "discount rate; time horizon;\nrisk aversion", econ)]
fig, ax = plt.subplots(figsize=(6.6, 8.6), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0, 13.2); ax.axis("off")
ax.text(0.2, 12.75, "Link in the chain", fontsize=10, color=ink2, fontweight="bold")
ax.text(5.55, 12.75, "Choices made here", fontsize=10, color=ink2, fontweight="bold")
for k, (name, what, choice, c) in enumerate(steps):
    y = 11.7 - k * 2.1
    ax.add_patch(FancyBboxPatch((0.2, y - 0.75), 4.9, 1.5, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#ffffff", ec=c, lw=1.7))
    ax.text(0.5, y + 0.33, name, fontsize=11.5, color=c, fontweight="bold", va="center")
    ax.text(0.5, y - 0.3, what, fontsize=9.6, color=ink, va="center", linespacing=1.25)
    ax.text(5.55, y, choice, fontsize=9.8, color=ink2, va="center", linespacing=1.3, style="italic")
    if k < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((2.65, y - 0.78), (2.65, y - 1.32), arrowstyle="-|>", mutation_scale=14,
                                     color=ink2, lw=1.4))
ax.text(9.8, 11.7 - 0.5 * 2.1, "physical\nclimate\nscience", fontsize=9.5, color=phys, ha="right", va="center",
        linespacing=1.2)
ax.text(9.8, 11.7 - 4.5 * 2.1, "economics\nand finance", fontsize=9.5, color=econ, ha="right", va="center",
        linespacing=1.2)
fig.suptitle("Where assumptions enter a climate cost estimate", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-02-gap-chain.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-02-gap-chain.png")
