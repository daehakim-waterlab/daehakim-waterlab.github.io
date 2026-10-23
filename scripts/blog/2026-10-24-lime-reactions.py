# Figure for the blog post "Farm lime turns out to be a carbon sink" (2026-10-24).
# Schematic of the two ways agricultural lime (CaCO3) dissolves in soil, following Suhrhoff et al. (2026),
# Nature 658, 113-118, https://doi.org/10.1038/s41586-026-11040-2, and Robertson & Hamilton (2026), Nature 658, 39-41:
#   with strong acids (nitric, sulfuric):  CaCO3 + 2H+ -> Ca2+ + CO2 + H2O   (releases CO2)
#   with carbonic acid from soil CO2:      CaCO3 + CO2 + H2O -> Ca2+ + 2HCO3-  (captures CO2 as bicarbonate)
# Strong acids also release CO2 without lime, by converting bicarbonate in soils and rivers to CO2; that is the
# counterfactual against which the paper measures the effect of lime.
# Drawn by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-24-lime-reactions.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
src, sink, neu = "#b4532a", "#2a78d6", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig, ax = plt.subplots(figsize=(6.6, 7.6), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0, 11.4); ax.axis("off")

def box(x, y, w, h, text, ec, fc="#ffffff", fs=10.5, weight="normal"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fc, ec=ec, lw=1.6))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=ink, linespacing=1.35, fontweight=weight)

def arrow(p, q, color):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=16, color=color, lw=1.8))

box(5, 10.35, 5.2, 0.95, "Agricultural lime (CaCO₃)\nspread on acidic cropland", neu, fc="#f3f2ef", weight="bold")
arrow((3.6, 9.85), (2.6, 9.0), src); arrow((6.4, 9.85), (7.4, 9.0), sink)

box(2.55, 8.2, 4.6, 1.45, "Meets strong acids\n(nitric acid from fertilizer,\nsulfuric acid from pollution)", src)
box(7.45, 8.2, 4.6, 1.45, "Meets carbonic acid\n(CO₂ from roots and microbes\ndissolved in soil water)", sink)
box(2.55, 6.35, 4.6, 1.15, "CaCO₃ + 2H⁺ →\nCa²⁺ + CO₂ + H₂O", src, fs=11)
box(7.45, 6.35, 4.6, 1.15, "CaCO₃ + CO₂ + H₂O →\nCa²⁺ + 2HCO₃⁻", sink, fs=11)
arrow((2.55, 7.45), (2.55, 6.95), src); arrow((7.45, 7.45), (7.45, 6.95), sink)
box(2.55, 4.75, 4.6, 1.0, "CO₂ released\nto the air", src, fc="#f8ece6", weight="bold")
box(7.45, 4.75, 4.6, 1.0, "CO₂ stored as bicarbonate,\ncarried by rivers to the sea", sink, fc="#eaf2fc", weight="bold")
arrow((2.55, 5.75), (2.55, 5.27), src); arrow((7.45, 5.75), (7.45, 5.27), sink)

box(5, 2.35, 9.5, 2.55,
    "The overlooked counterfactual\n\nWithout lime, the same strong acids still release CO₂,\nby turning bicarbonate in soils and rivers into CO₂.\n"
    "So the acid, not the lime, is the source. Measured against\nthat baseline, lime lowers CO₂ emissions over decades.",
    ink2, fc="#ffffff", fs=10.5)
ax.text(5, 0.6, "Which path wins depends on soil pH, which varies even between microsites in the same field.",
        ha="center", va="center", fontsize=9.5, color=ink2, style="italic")

fig.suptitle("Two ways lime dissolves: one releases CO₂, one captures it", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-24-lime-reactions.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-24-lime-reactions.png")
