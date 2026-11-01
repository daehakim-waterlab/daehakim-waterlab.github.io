# Figure for the blog post "Why climate science and economics talk past each other" (2026-11-02).
# An example of the "layered" presentation recommended by Sherwood et al. (2026, Nature Climate Change,
# https://doi.org/10.1038/s41558-026-02784-w): a headline cost with its conditions attached. The content is the
# labour component of the 2025 social cost of carbon from Moore et al. (2026, Nature Climate Change 16, 1170-1177,
# https://doi.org/10.1038/s41558-026-02749-z): mean US$41 per ton CO2 (90% range 1-108), 2% near-term discount
# rate, average of the ISO (US$52) and Lancet (US$30) response functions, air conditioning used more intensively
# but not spreading, cold benefits and heat illness not counted, damages through 2300, India, Nigeria, China and
# Pakistan together about US$22 of the 41. Layout by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-11-02-gap-card.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
head, layer = "#b4532a", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig, ax = plt.subplots(figsize=(6.6, 7.6), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis("off")

ax.add_patch(FancyBboxPatch((0.2, 9.55), 9.6, 1.85, boxstyle="round,pad=0.02,rounding_size=0.2", fc="#f8ece6",
                            ec=head, lw=1.8))
ax.text(0.55, 10.95, "Headline", fontsize=10, color=head, fontweight="bold", va="center")
ax.text(0.55, 10.15, "Heat stress on workers costs about US$41\nper ton of CO₂ emitted in 2025", fontsize=12.5,
        color=ink, va="center", linespacing=1.3, fontweight="bold")

layers = [("Uncertainty", "90% range US$1–108; US$30 or US$52\ndepending on how heat affects work"),
          ("Key assumptions", "2% discount rate; air conditioning used more,\nbut not spreading to new places"),
          ("Not counted", "benefits of milder winters; heat illness\nand injury; new forms of adaptation"),
          ("Time horizon", "damages from a 2025 emission\nadded up through 2300"),
          ("Who bears it", "India, Nigeria, China and Pakistan carry\nmore than half; Europe almost none")]
for k, (lab, txt) in enumerate(layers):
    y = 8.35 - k * 1.72
    ax.add_patch(FancyBboxPatch((0.2, y - 0.72), 9.6, 1.44, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#ffffff", ec=grid, lw=1.2))
    ax.add_patch(plt.Rectangle((0.2, y - 0.72), 0.12, 1.44, fc=layer, ec="none"))
    ax.text(0.6, y, lab, fontsize=10.5, color=layer, fontweight="bold", va="center")
    ax.text(3.35, y, txt, fontsize=10.2, color=ink, va="center", linespacing=1.3)
fig.suptitle("A climate cost with its conditions attached", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-02-gap-card.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-02-gap-card.png")
