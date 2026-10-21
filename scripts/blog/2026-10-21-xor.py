# Figure for the blog post "A short history of AI, part 1: from Turing to Deep Blue (1936-1997)" (2026-10-21).
# Why a single perceptron cannot learn XOR: AND and OR can be separated by one straight line, XOR cannot.
# The hidden-layer panel shows one standard two-line solution (x1 + x2 > 0.5 and x1 + x2 < 1.5).
# Illustrative only; no data. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-21-xor.py
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
one, zero, line = "#2a78d6", "#d6604d", "#5b5a57"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

pts = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
cases = [
    ("AND: one straight line\nseparates the 1s from the 0s", [0, 0, 0, 1], [(1.5, None)]),
    ("OR: one straight line\nseparates the 1s from the 0s", [0, 1, 1, 1], [(0.5, None)]),
    ("XOR: no single straight line\ncan do it", [0, 1, 1, 0], []),
    ("XOR with a hidden layer:\ntwo lines (two units) do it", [0, 1, 1, 0], [(0.5, None), (1.5, None)]),
]
fig, axes = plt.subplots(2, 2, figsize=(8.4, 8.0), facecolor=surf)
xs = np.linspace(-0.4, 1.4, 50)
for ax, (title, out, lines) in zip(axes.ravel(), cases):
    ax.set_facecolor(surf)
    if title.startswith("XOR with"):
        ax.fill_between(xs, 0.5 - xs, 1.5 - xs, color=one, alpha=0.12, lw=0)
    for c in [v for v, _ in lines]:
        ax.plot(xs, c - xs, color=line, lw=1.8, ls=(0, (5, 3)))
    for (x, y), o in zip(pts, out):
        ax.scatter([x], [y], s=260, color=one if o else zero, edgecolor=surf, linewidth=1.5, zorder=3)
        ax.text(x, y, str(o), ha="center", va="center", color="white", fontsize=11, fontweight="bold", zorder=4)
    ax.set_xlim(-0.4, 1.4); ax.set_ylim(-0.4, 1.4)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xlabel("input x₁", color=ink2, fontsize=10.5); ax.set_ylabel("input x₂", color=ink2, fontsize=10.5)
    ax.set_aspect("equal")
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.set_title(title, loc="left", color=ink, fontsize=11.5)

fig.suptitle("The problem that stalled the perceptron", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout(h_pad=1.8)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-xor.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-xor.png")
