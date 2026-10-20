# Figure for the blog post "How much water and carbon does AI use?" (2026-10-20).
# Data from de Vries-Gao (2026), Patterns 7, 101430, doi:10.1016/j.patter.2025.101430:
#   AI systems in 2025 (9.4 GW at end-2024 to 23 GW at end-2025): 32.6-79.7 MtCO2 and 312.5-764.6 billion L;
#   comparison values quoted there: New York City 52.2 MtCO2 (2023); global bottled water 446 billion L per year;
#   all data centers (IEA): 182 MtCO2 (2024); 560 billion L water consumption (2023, incl. 47 billion L for
#   hardware manufacturing); de Vries-Gao's alternative for 2023: 140 billion L direct + 1,225 billion L
#   indirect (3.40 L/kWh x 360 TWh) = 1,365 billion L.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-20-ai-footprint.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
ai, dc, ref = "#d6604d", "#5b5a57", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink})

fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 6.6), facecolor=surf)

def panel(ax, title, items, xmax, unit):
    ax.set_facecolor(surf)
    for i, (lab, lo, hi, c) in enumerate(items):
        if hi is None:
            ax.barh(i, lo, 0.55, color=c)
            ax.text(lo + xmax * 0.012, i, f"{lo:,.1f}" if lo < 100 else f"{lo:,.0f}", va="center", fontsize=11.5, color=ink)
        else:
            ax.barh(i, hi - lo, 0.55, left=lo, color=c, alpha=0.85)
            ax.text(hi + xmax * 0.012, i, f"{lo:,.1f}–{hi:,.1f}" if hi < 100 else f"{lo:,.0f}–{hi:,.0f}",
                    va="center", fontsize=11.5, color=ink)
    ax.set_yticks(range(len(items))); ax.set_yticklabels([it[0] for it in items], fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(0, xmax)
    ax.set_xlabel(unit, color=ink2)
    ax.set_title(title, loc="left", color=ink, fontsize=12.5)
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", length=0)

panel(a1, "Carbon: AI in 2025 is in the range of New York City",
      [("AI systems, 2025 (estimate)", 32.6, 79.7, ai),
       ("New York City, 2023", 52.2, None, ref),
       ("All data centers, 2024 (IEA)", 182, None, dc)],
      230, "Million tonnes of CO₂ per year")
panel(a2, "Water: AI in 2025 is in the range of the world's bottled water",
      [("AI systems, 2025 (estimate)", 312.5, 764.6, ai),
       ("Global bottled water", 446, None, ref),
       ("All data centers, 2023 (IEA)", 560, None, dc),
       ("All data centers, 2023 (alternative)", 1365, None, dc)],
      1700, "Billion litres of water consumed per year")
fig.tight_layout(h_pad=2.2)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-20-ai-footprint.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-20-ai-footprint.png")
