# Figure for the blog post "Ageing pipes, ageing people: the double ageing of water infrastructure" (2026-11-17).
# Share of the population aged 65 and over, 1960-2025, for five countries, from the World Bank's World Development
# Indicators (indicator SP.POP.65UP.TO.ZS, based on the UN World Population Prospects; downloaded 16 November 2026
# from https://api.worldbank.org/v2/country/<code>/indicator/SP.POP.65UP.TO.ZS).
# The shaded band marks 1950-1980, the post-war decades of large-scale infrastructure building described by
# Vahedifard et al. (2026), Nature Water 4, 1062-1067, https://doi.org/10.1038/s44221-026-00711-z.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-17-ageing-population.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

data = {
    "KOR": [3.1, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.4, 3.4, 3.5, 3.5, 3.6, 3.6, 3.6, 3.7, 3.7, 3.8, 3.8, 3.9, 4.0, 4.1, 4.1, 4.2, 4.4, 4.5, 4.6, 4.8, 4.9, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9.0, 9.4, 9.9, 10.2, 10.6, 11.0, 11.4, 11.7, 12.1, 12.5, 13.0, 13.4, 13.9, 14.5, 15.1, 15.8, 16.7, 17.5, 18.3, 19.3, 20.3],
    "JPN": [5.7, 5.8, 6.0, 6.1, 6.2, 6.3, 6.5, 6.7, 6.8, 7.0, 7.1, 7.2, 7.4, 7.6, 7.7, 7.9, 8.1, 8.4, 8.6, 8.8, 9.1, 9.3, 9.5, 9.8, 10.0, 10.4, 10.6, 11.0, 11.3, 11.7, 12.2, 12.6, 13.1, 13.6, 14.1, 14.7, 15.2, 15.8, 16.3, 16.9, 17.4, 18.0, 18.6, 19.1, 19.6, 20.3, 21.0, 21.6, 22.3, 22.8, 23.1, 23.7, 24.5, 25.4, 26.2, 26.9, 27.5, 28.0, 28.3, 28.6, 28.9, 29.2, 29.4, 29.6, 29.8, 30.0],
    "USA": [8.8, 8.9, 9.0, 9.1, 9.1, 9.3, 9.4, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.3, 10.4, 10.6, 10.7, 10.9, 11.1, 11.2, 11.3, 11.5, 11.6, 11.7, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.4, 12.3, 12.2, 12.2, 12.1, 12.1, 12.1, 12.1, 12.1, 12.2, 12.3, 12.5, 12.7, 12.8, 13.1, 13.4, 13.7, 14.0, 14.3, 14.6, 14.9, 15.3, 15.7, 16.1, 16.5, 16.9, 17.4, 17.9, 18.4],
    "GBR": [11.7, 11.8, 11.8, 11.9, 12.1, 12.2, 12.4, 12.5, 12.7, 12.9, 13.1, 13.3, 13.5, 13.7, 13.9, 14.1, 14.3, 14.5, 14.7, 14.9, 15.0, 15.1, 15.1, 15.0, 15.0, 15.1, 15.3, 15.5, 15.7, 15.8, 15.9, 15.9, 16.0, 16.0, 16.0, 16.0, 16.0, 16.0, 15.9, 15.9, 15.9, 15.9, 15.9, 15.9, 16.0, 16.0, 15.9, 15.9, 16.0, 16.2, 16.3, 16.6, 17.0, 17.3, 17.6, 17.8, 17.9, 18.1, 18.3, 18.5, 18.6, 18.7, 18.9, 19.2, 19.5, 19.7],
    "CHN": [4.0, 3.9, 3.8, 3.8, 3.7, 3.6, 3.6, 3.6, 3.7, 3.7, 3.7, 3.7, 3.8, 3.8, 3.9, 4.0, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.5, 5.6, 5.7, 5.9, 6.1, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.7, 7.9, 8.1, 8.2, 8.4, 8.5, 8.7, 8.9, 9.1, 9.4, 9.7, 10.1, 10.5, 11.0, 11.5, 12.1, 12.6, 13.2, 13.8, 14.3, 14.7, 14.9],
}
style = {"KOR": ("South Korea", "#b4532a", 2.8), "JPN": ("Japan", "#7a5195", 2.0), "GBR": ("UK", "#8a8780", 2.0),
         "USA": ("USA", "#2a78d6", 2.0), "CHN": ("China", "#2e8b57", 2.0)}
years = list(range(1960, 2026))
fig, ax = plt.subplots(figsize=(6.6, 4.4), facecolor=surf); ax.set_facecolor(surf)
ax.axvspan(1960, 1980, color="#efe9dd", zorder=0)
ax.text(1970, 31.5, "post-war building boom\n(pipes, dams, levees)", ha="center", va="center", fontsize=9, color=ink2,
        linespacing=1.1)
ax.axhline(20, color=ink2, lw=0.9, ls=(0, (3, 3)))
ax.text(1961, 20.6, "20%: 'super-aged' society", fontsize=9, color=ink2)
for c, v in data.items():
    name, col, lw = style[c]
    ax.plot(years, v, color=col, lw=lw)
    off = {"KOR": 1.6, "GBR": -0.5, "USA": -1.5}.get(c, 0.0)
    ax.text(2026.5, v[-1] + off, f"{name} {v[-1]:.0f}%",
            va="center", fontsize=9.3, color=col)
ax.set_xlim(1960, 2042); ax.set_ylim(0, 34)
ax.set_xticks([1960, 1980, 2000, 2020])
ax.set_ylabel("Population aged 65 and over (%)", color=ink2, fontsize=10.5)
ax.tick_params(labelsize=9.5)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("The people that post-war water systems serve have grown old", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-17-ageing-population.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-17-ageing-population.png")
