# Figure for the blog post "A short history of AI, part 1: from Turing to Deep Blue (1936-1997)" (2026-10-21).
# A timeline of milestones discussed in the post. Dates are publication or event years from the cited sources.
# The two "AI winters" are shown as approximate periods (about 1974-1980 and 1987-1993); historians date them
# differently, so the shading is indicative only. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-21-ai-timeline-1.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
sym, net, gen, winter = "#2a78d6", "#d6604d", "#5b5a57", "#e9e7e2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

events = [  # year, label, kind
    (1936, "Turing: a universal machine on paper", gen),
    (1943, "McCulloch & Pitts: neurons as logic units", net),
    (1950, "Turing: the imitation game", gen),
    (1955, "Dartmouth proposal names \"AI\"", sym),
    (1956, "Logic Theorist proves theorems", sym),
    (1958, "Rosenblatt: the perceptron", net),
    (1959, "Samuel: checkers program that learns", net),
    (1966, "Weizenbaum: ELIZA", sym),
    (1969, "Minsky & Papert: limits of perceptrons", net),
    (1973, "Lighthill report (UK)", gen),
    (1982, "R1/XCON expert system at DEC", sym),
    (1986, "Backpropagation popularized", net),
    (1995, "Neural networks for rainfall-runoff", net),
    (1997, "Deep Blue defeats Kasparov", sym),
]

# Evenly spaced rows (not to scale in time) so that close years stay readable; the two winters get their own
# shaded rows in chronological order.
rows = []
for y, lab, c in events:
    rows.append(("event", y, lab, c))
    if y == 1973:
        rows.append(("winter", None, "about 1974-1980: first \"AI winter\"", None))
    if y == 1986:
        rows.append(("winter", None, "about 1987-1993: second \"AI winter\"", None))

fig, ax = plt.subplots(figsize=(6.6, 8.8), facecolor=surf); ax.set_facecolor(surf)
n = len(rows)
ax.plot([0.06, 0.06], [-0.5, n - 0.5], color=ink2, lw=1.2, zorder=1)
for i, (kind, y, lab, c) in enumerate(rows):
    if kind == "winter":
        ax.axhspan(i - 0.42, i + 0.42, color=winter, zorder=0, lw=0)
        ax.text(0.10, i, lab, ha="left", va="center", fontsize=11, color=ink2, style="italic")
    else:
        ax.scatter([0.06], [i], s=70, color=c, zorder=3, edgecolor=surf, linewidth=1.2)
        ax.text(0.10, i, f"{y}", ha="left", va="center", fontsize=11, color=ink2, fontweight="bold")
        ax.text(0.235, i, lab, ha="left", va="center", fontsize=11, color=ink)
ax.set_ylim(n - 0.5, -1.4)
ax.set_xlim(0, 1)
ax.set_xticks([]); ax.set_yticks([])
for sp in ("top", "right", "bottom", "left"): ax.spines[sp].set_visible(False)
from matplotlib.lines import Line2D
handles = [Line2D([], [], marker="o", ls="", color=c, markersize=8, label=l)
           for c, l in [(sym, "Symbolic AI (rules and search)"), (net, "Neural networks and learning"), (gen, "Foundations and policy")]]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.09), ncol=2, frameon=False, fontsize=10.5,
          handletextpad=0.3, columnspacing=1.0)
fig.suptitle("Sixty years of AI, from Turing to Deep Blue", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-ai-timeline-1.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-ai-timeline-1.png")
