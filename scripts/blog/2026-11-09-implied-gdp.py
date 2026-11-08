# Figure for the blog post "What the public and AI insiders expect from AI" (2026-11-09).
# Model-implied US GDP growth in 2030 from Sacher, Cotter, Jones, Korinek and McCrory (2026), The AI Expectations
# Gap, The Anthropic Institute (https://www.anthropic.com/research/ai-expectations-gap): each respondent's answers on
# capabilities, adoption, autonomy, time savings and re-employment were run through the model of Korinek et al. (2026),
# Economic Scenarios for Transformative AI. Medians: US adults 5.4% (3,259 respondents), website quiz visitors 12.5%
# (23,075), Anthropic staff 17.1% (1,093). Reference scenarios from the same model: Modest 2.4%, Substantial 5.4%,
# Extreme 15.4%. Doubling time of GDP at growth rate g: ln 2 / ln(1 + g).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-09-implied-gdp.py
import os, math, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("US adults", 5.4, "#8a8780"), ("Website quiz\nvisitors", 12.5, "#c98a5c"), ("Anthropic staff", 17.1, "#b4532a")]
fig, ax = plt.subplots(figsize=(6.6, 3.9), facecolor=surf); ax.set_facecolor(surf)
for i, (name, g, c) in enumerate(rows):
    ax.barh(i, g, 0.55, color=c)
    dbl = math.log(2) / math.log(1 + g / 100)
    ax.text(g + 0.3, i, f"{g}%  (GDP doubles in {dbl:.1f} years)", va="center", fontsize=9.6, color=ink,
            bbox=dict(fc=surf, ec="none", pad=1.5))
for x, lab, ha in [(2.4, "Modest ", "right"), (5.4, " Substantial", "left"), (15.4, " Extreme", "left")]:
    ax.axvline(x, color=ink2, lw=0.9, ls=(0, (3, 3)), zorder=0)
    ax.text(x, -0.62, lab, ha=ha, va="bottom", fontsize=9, color=ink2)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=10); ax.invert_yaxis()
ax.set_xlim(0, 30); ax.set_ylim(2.5, -0.85); ax.tick_params(axis="x", labelsize=9.5)
ax.set_xlabel("Median model-implied US GDP growth in 2030 (% per year)", color=ink2, fontsize=10)
ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("What each group's answers imply for the economy", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-09-implied-gdp.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-09-implied-gdp.png")
