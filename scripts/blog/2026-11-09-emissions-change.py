# Figure for the blog post "Global fossil CO2 emissions may fall in 2026, and not because of a pandemic" (2026-11-09).
# Annual change in global CO2 emissions from fossil fuels and industry, 1960-2026.
# 1959-2024: annual emissions (MtCO2, excluding land-use change) from the Global Carbon Budget 2025 as distributed by
#   Our World in Data (owid-co2-data.csv, column "co2", country "World"; https://github.com/owid/co2-data),
#   downloaded 9 November 2026.
# 2025: projection of +1.0% (range 0.2 to 1.7%) from Friedlingstein et al. (2026), Global Carbon Budget 2025,
#   Earth System Science Data 18, 3211-3288, https://doi.org/10.5194/essd-18-3211-2026.
# 2026: estimate of about -0.5% from Carbon Brief (Evans, 16 September 2026), based on IEA fuel-demand forecasts.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-09-emissions-change.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
up, down, est = "#c9c6bf", "#2a78d6", "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

mt = [8855, 9387, 9415, 9747, 10267, 10824, 11311, 11863, 12237, 12905, 13762, 14899, 15504, 16225, 17077, 16998,
      16988, 17862, 18358, 19025, 19509, 19410, 18880, 18730, 18902, 19457, 20145, 20438, 21106, 21919, 22200,
      22732, 23206, 22520, 22750, 22975, 23517, 24233, 24380, 24296, 24838, 25511, 25693, 26265, 27653, 28610,
      29599, 30594, 31499, 32050, 31513, 33318, 34480, 34955, 35276, 35466, 35404, 35393, 35975, 36734, 37087,
      35158, 36867, 37528, 38094, 38599]  # 1959-2024
years = list(range(1960, 2025))
chg = [100 * (mt[i + 1] / mt[i] - 1) for i in range(len(years))]

fig, ax = plt.subplots(figsize=(6.6, 4.6), facecolor=surf); ax.set_facecolor(surf)
ax.bar(years, chg, 0.8, color=[down if c < 0 else up for c in chg])
ax.bar(2025, 1.0, 0.8, color="none", edgecolor=ink2, hatch="////", lw=0.8)
ax.bar(2026, -0.5, 0.8, color=est)
ax.axhline(0, color=ink2, lw=0.8)
notes = [(1981, -2.73, "Second oil\nshock"), (1992, -2.95, "End of the\nSoviet Union"),
         (2009, -1.67, "Financial\ncrisis"), (2020, -5.2, "Covid-19")]
for y, v, t in notes:
    ax.text(y, v - 0.35, t, ha="center", va="top", fontsize=8.6, color=down, linespacing=1.1)
ax.annotate("2026: Hormuz\ncrisis (estimate)", (2026, -0.5), xytext=(2027.5, 6.4), fontsize=8.6, color=est,
            ha="right", va="center", linespacing=1.1, arrowprops=dict(arrowstyle="-", color=est, lw=0.9))
ax.set_xlim(1958, 2028); ax.set_ylim(-7.3, 7.5)
ax.set_ylabel("Change from previous year (%)", color=ink2, fontsize=10.5)
ax.tick_params(axis="both", labelsize=9.5)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Global fossil CO2 has rarely fallen, and almost always in a crisis", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-09-emissions-change.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-09-emissions-change.png")
