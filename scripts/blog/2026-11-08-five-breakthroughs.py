# Figure for the blog post "How the brain invented learning, part V: speaking in A Brief History of Intelligence"
# (2026-11-08). Schematic by Daeha Kim summarizing the five breakthroughs of Bennett (2023) as covered in parts I-V
# of the series, each with the AI counterpart discussed in the corresponding post.
# Run from the repository root: python scripts/blog/2026-11-08-five-breakthroughs.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

rows = [
    ("1", "Steering", "First bilaterians", "Approach the good, avoid the bad", "Reactive robots", "#8a8780"),
    ("2", "Reinforcing", "Early vertebrates", "Learn by trial and error", "Temporal-difference learning", "#6f8fb8"),
    ("3", "Simulating", "Early mammals", "Try things out in imagination", "Model-based RL (Dyna, MuZero)", "#2a78d6"),
    ("4", "Mentalizing", "Early primates", "Model one's own and others' minds", "Inverse RL, theory-of-mind tests", "#7a5195"),
    ("5", "Speaking", "Early humans", "Share simulations between minds", "Large language models", "#b4532a"),
]
fig, ax = plt.subplots(figsize=(6.6, 7.4), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0.2, 11.2); ax.axis("off")
h, gap, top = 1.85, 0.25, 11.0
for i, (n, name, who, what, ai, c) in enumerate(rows):
    y0 = top - (i + 1) * h - i * gap
    x0 = 0.15 + i * 0.35
    ax.add_patch(FancyBboxPatch((x0, y0), 9.7 - i * 0.35, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc="#ffffff", ec=c, lw=1.6 if i < 4 else 2.4))
    ax.text(x0 + 0.5, y0 + h / 2, n, ha="center", va="center", fontsize=20, color=c, fontweight="bold")
    ax.text(x0 + 1.1, y0 + h - 0.42, name, va="center", fontsize=12, color=c, fontweight="bold")
    ax.text(9.6, y0 + h - 0.42, who, va="center", ha="right", fontsize=9.6, color=ink2, style="italic")
    ax.text(x0 + 1.1, y0 + h - 1.0, what, va="center", fontsize=9.8, color=ink)
    ax.text(x0 + 1.1, y0 + h - 1.5, "AI: " + ai, va="center", fontsize=9.6, color=ink2)
fig.suptitle("Five breakthroughs, each built on the last", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-08-five-breakthroughs.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-08-five-breakthroughs.png")
