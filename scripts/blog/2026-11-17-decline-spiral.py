# Figure for the blog post "Ageing pipes, ageing people: the double ageing of water infrastructure" (2026-11-17).
# Schematic by Daeha Kim of the self-reinforcing loop between ageing water infrastructure and an ageing, shrinking
# community, following the "infrastructure-society ageing decline spiral" described in words by Vahedifard et al.
# (2026), Nature Water 4, 1062-1067, https://doi.org/10.1038/s44221-026-00711-z.
# Run from the repository root: python scripts/blog/2026-11-17-decline-spiral.py
import os, math, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
acc = "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

steps = [("Old pipes and plants", "past their design life"), ("More breaks", "and supply interruptions"),
         ("Young people move away", "to better-served places"), ("Fewer, older residents", "use less water"),
         ("Less money", "from water bills"), ("Repairs postponed", "to stay solvent")]
n = len(steps)
fig, ax = plt.subplots(figsize=(6.6, 6.4), facecolor=surf)
ax.set_xlim(-5.1, 5.1); ax.set_ylim(-4.4, 4.4); ax.set_aspect("equal"); ax.axis("off")
R = 3.55
pos = [(R * math.sin(2 * math.pi * k / n), R * math.cos(2 * math.pi * k / n)) for k in range(n)]
w, h = 3.5, 1.15
for (x, y), (head, sub) in zip(pos, steps):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#ffffff", ec=acc, lw=1.5))
    ax.text(x, y + 0.2, head, ha="center", va="center", fontsize=9.4, color=acc, fontweight="bold")
    ax.text(x, y - 0.24, sub, ha="center", va="center", fontsize=8.8, color=ink)

def exit_dist(dx, dy, m=0.18):
    tx = (w / 2) / abs(dx) if dx else 1e9
    ty = (h / 2) / abs(dy) if dy else 1e9
    return min(tx, ty) + m

for k in range(n):
    (x0, y0), (x1, y1) = pos[k], pos[(k + 1) % n]
    L = math.hypot(x1 - x0, y1 - y0); dx, dy = (x1 - x0) / L, (y1 - y0) / L
    t0 = exit_dist(dx, dy); t1 = exit_dist(dx, dy)
    ax.add_patch(FancyArrowPatch((x0 + dx * t0, y0 + dy * t0), (x1 - dx * t1, y1 - dy * t1), arrowstyle="-|>",
                                 mutation_scale=15, color=ink2, lw=1.4))
ax.text(0, 0.35, "Each consequence\nbecomes the next cause", ha="center", va="center", fontsize=10.5, color=ink,
        linespacing=1.3)
ax.text(0, -0.65, "breaking the loop needs\noutside investment or new plans", ha="center", va="center", fontsize=9.2,
        color=ink2, style="italic", linespacing=1.3)
fig.suptitle("How ageing pipes and an ageing town can drag each other down", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-17-decline-spiral.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-17-decline-spiral.png")
