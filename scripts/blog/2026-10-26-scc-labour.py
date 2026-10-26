# Figure for the blog post "Heat-stressed workers add about $41 to the social cost of carbon" (2026-10-26).
# Labour component of the 2025 social cost of carbon (US$ per ton CO2, 2020 dollars, 2% near-term discount rate)
# reported in Moore et al. (2026), Nature Climate Change 16, 1170-1177, https://doi.org/10.1038/s41558-026-02749-z:
# (a) preferred estimate: mean 41, median 32, 90% range 1-108; Lancet response function alone 30, ISO alone 52;
#     Rode et al. (working paper, 2020 SC-CO2, different method) 39.
# (b) largest country contributions: India 9, Nigeria 6, China 4, Pakistan 3 (together 22 of the mean of 41).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-26-scc-labour.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
red, light = "#d6604d", "#efb3a6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 6.2), facecolor=surf, gridspec_kw={"height_ratios": [1.5, 1.1]})

rows = [("Preferred estimate\n(mean of both)", 41), ("Lancet function\n(field data)", 30),
        ("ISO standard\n(physiology)", 52), ("Rode et al.\n(different method)", 39)]
a.plot([1, 108], [0, 0], color=red, lw=2.4, solid_capstyle="round")
a.plot(32, 0, "|", color=ink, ms=14, mew=2)
for i, (name, v) in enumerate(rows):
    a.plot(v, i, "o", color=red if i == 0 else ink2, ms=9 if i == 0 else 7)
    a.text(v + 3, i - 0.28, f"${v}", ha="left", va="center", fontsize=10.5, color=ink)
a.text(108, 0.3, "90% range $1–108", ha="right", va="center", fontsize=9.5, color=ink2)
a.text(32, -0.42, "median $32", ha="center", va="bottom", fontsize=9.5, color=ink2)
a.set_yticks(range(len(rows))); a.set_yticklabels([r[0] for r in rows], fontsize=10.5); a.invert_yaxis()
a.set_xlim(0, 115); a.set_ylim(3.6, -0.8)
a.set_xlabel("Labour damages, US$ per ton of CO₂ emitted in 2025", color=ink2, fontsize=10.5)
a.set_title("a  About $41 per ton, with wide uncertainty", loc="left", fontsize=11.5, color=ink)

parts = [("India", 9), ("Nigeria", 6), ("China", 4), ("Pakistan", 3)]
for k, (name, v) in enumerate(parts):
    b.barh(k, v, 0.6, color=red)
    b.text(v + 0.3, k, f"${v}", ha="left", va="center", fontsize=10.5, color=ink)
b.set_yticks(range(len(parts))); b.set_yticklabels([p[0] for p in parts], fontsize=10.5); b.invert_yaxis()
b.set_xlim(0, 41)
b.set_xlabel("Share of the $41 mean (US$ per ton of CO₂); together $22, or 54%", color=ink2, fontsize=10)
b.set_title("b  Four countries carry more than half of it", loc="left", fontsize=11.5, color=ink)

for ax in (a, b):
    ax.set_facecolor(surf); ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("The labour cost of heat stress", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-26-scc-labour.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-26-scc-labour.png")
