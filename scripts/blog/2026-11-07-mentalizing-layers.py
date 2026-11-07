# Figure for the blog post "How the brain invented learning, part IV: mentalizing in A Brief History of Intelligence"
# (2026-11-07). Schematic by Daeha Kim summarizing the models described in parts III and IV, following the argument
# of Bennett (2023): a model of the world (sensory neocortex), a model of one's own body and intent (agranular
# prefrontal cortex, early mammals) and a model of one's own mind (granular prefrontal cortex, early primates),
# which can be projected into another individual or into one's future self.
# Run from the repository root: python scripts/blog/2026-11-07-mentalizing-layers.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
mam, pri = "#2a78d6", "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

fig, ax = plt.subplots(figsize=(6.6, 7.8), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0.8, 13); ax.axis("off")

def box(x, y, w, h, head, body, c, fill="#ffffff"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=fill, ec=c, lw=1.7))
    ax.text(x, y + h / 2 - 0.42, head, ha="center", va="center", fontsize=10.8, color=c, fontweight="bold")
    ax.text(x, y - 0.22, body, ha="center", va="center", fontsize=9.6, color=ink, linespacing=1.3)

def arrow(p, q, c):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, color=c, lw=1.5))

ax.text(0.2, 12.55, "Early mammals (part III)", fontsize=10, color=mam, fontweight="bold")
box(5, 11.5, 9.4, 1.45, "Model of the world", "sensory neocortex: what is out there\nand what would happen if…", mam)
box(5, 9.55, 9.4, 1.45, "Model of my body and intent", "agranular prefrontal cortex: what I am doing\nand why", mam)
arrow((5, 10.78), (5, 10.32), ink2)
ax.text(0.2, 8.35, "Early primates (part IV)", fontsize=10, color=pri, fontweight="bold")
box(5, 7.35, 9.4, 1.45, "Model of my own mind", "granular prefrontal cortex: what I know,\nwant and believe", pri, fill="#f8ece6")
arrow((5, 8.83), (5, 8.12), ink2)

kids = [(1.75, "Theory of mind", "project it into\nanother mind:\ntheir intent and\nknowledge"),
        (5.0, "Imitation learning", "project it into\nanother body:\ntheir skills"),
        (8.25, "Anticipating\nfuture needs", "project it into\nmy future self:\nwants I will have")]
for x, head, body in kids:
    arrow((5 + (x - 5) * 0.25, 6.6), (x, 4.9), pri)
    ax.add_patch(FancyBboxPatch((x - 1.5, 1.9), 3.0, 2.85, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#ffffff", ec=pri, lw=1.5))
    ax.text(x, 4.2, head, ha="center", va="center", fontsize=10.2, color=pri, fontweight="bold", linespacing=1.15)
    ax.text(x, 2.95, body, ha="center", va="center", fontsize=9.4, color=ink, linespacing=1.3)
ax.text(5, 1.25, "One new model, three uses", ha="center", fontsize=10.5, color=ink2, style="italic")
fig.suptitle("Models within models: from mammals to primates", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-07-mentalizing-layers.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-07-mentalizing-layers.png")
