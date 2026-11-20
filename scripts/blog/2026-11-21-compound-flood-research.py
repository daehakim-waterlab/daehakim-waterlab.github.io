# Figure 2 for the blog post "When floods team up: a review of compound flooding" (2026-11-21).
# What the 378 studies reviewed by Mohseni et al. (2027) focus on, and where they come from.
# Numbers are typed in from the text of the review (Sections 2.2.1 and 2.2.3):
#   research application: methodological advancement 118, hazard analysis 91, risk assessment 46,
#   frequency analysis 42, projection 35, impact assessment 18, forecasting 17, non-stationary modeling 11
#   country: USA 119, China 54, UK 37, Netherlands 17, Canada 14 (global studies excluded in the paper's map)
# Bar charts drawn by Daeha Kim; no figure from the review is reproduced.
# Run from the repository root: python scripts/blog/2026-11-21-compound-flood-research.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, light = "#2a78d6", "#a9c6ea"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

apps = [("Methods development", 118), ("Hazard analysis", 91), ("Risk assessment", 46),
        ("Frequency analysis", 42), ("Future projections", 35), ("Impact assessment", 18),
        ("Forecasting", 17), ("Changing (non-stationary)\nconditions", 11)]
countries = [("USA", 119), ("China", 54), ("UK", 37), ("Netherlands", 17), ("Canada", 14)]
N = 378

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 6.6), facecolor=surf,
                           gridspec_kw={"height_ratios": [8, 5]})
for ax, rows, title, hi in ((a, apps, "a  What the studies are about", {"Impact assessment", "Forecasting"}),
                            (b, countries, "b  Where the studies are from (top five countries)", set())):
    ax.set_facecolor(surf)
    names = [r[0] for r in rows][::-1]; vals = [r[1] for r in rows][::-1]
    cols = [blue if (n in hi or not hi) else light for n in names]
    if hi:
        cols = [blue if n in hi or n.startswith("Changing") else light for n in names]
    ax.barh(range(len(vals)), vals, color=cols, height=0.66, zorder=2)
    for i, v in enumerate(vals):
        ax.text(v + 2, i, f"{v}  ({100 * v / N:.0f}%)", va="center", fontsize=9.2, color=ink2)
    ax.set_yticks(range(len(vals)), names, fontsize=9.6)
    ax.set_xlim(0, 150); ax.set_xticks([])
    ax.set_title(title, loc="left", fontsize=11, color=ink)
    for sp in ("top", "right", "bottom"): ax.spines[sp].set_visible(False)
a.text(148, 1.0, "impacts, forecasts and\nchanging conditions get\nthe least attention",
       ha="right", va="center", fontsize=9, color=blue, linespacing=1.15)
fig.suptitle("378 studies of compound flooding, 1961–2025", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-21-compound-flood-research.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-21-compound-flood-research.png")
