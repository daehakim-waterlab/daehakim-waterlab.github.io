# Figure for the blog post "Heat and the mind: what an umbrella review says about climate change and mental health" (2026-10-22).
# (a) Class II associations between short-term temperature increase and mental health outcomes, per 1°C,
#     from Radua et al. (2024), World Psychiatry 23, 244-256, Table 2, https://doi.org/10.1002/wps.21219:
#     suicide- or mental disorders-related mortality RR 1.024 (1.015-1.033); suicidal behavior 1.012 (1.011-1.014);
#     hospital access, suicidal behavior or mental disorders 1.011 (1.008-1.015); hospital access, mental disorders
#     only 1.009 (1.006-1.012); apparent temperature and suicidal behavior 1.010 (1.009-1.011).
# (b) What the mortality estimate implies if it is scaled with warming: RR^dT - 1, the method of the paper's
#     complementary analysis. The paper estimates ~5% today and ~7% (95% CI 4.2-9.7%) in 2050 relative to the
#     pre-industrial land temperature; the markers are placed where the curve reaches those values.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-22-mental-heat.py
import os, math, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
hot = "#d6604d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 7.6), facecolor=surf, gridspec_kw={"height_ratios": [5, 4]})

rows = [("Deaths from suicide or\nmental disorders", 1.024, 1.015, 1.033),
        ("Suicidal behavior", 1.012, 1.011, 1.014),
        ("Hospital visits: suicidal\nbehavior or mental disorders", 1.011, 1.008, 1.015),
        ("Hospital visits:\nmental disorders only", 1.009, 1.006, 1.012),
        ("Suicidal behavior\n(per 1°C apparent temp.)", 1.010, 1.009, 1.011)]
for i, (name, rr, lo, hi) in enumerate(rows):
    p, pl, ph = (rr - 1) * 100, (lo - 1) * 100, (hi - 1) * 100
    a.plot([pl, ph], [i, i], color=hot, lw=2.2, solid_capstyle="round")
    a.plot(p, i, "o", color=hot, ms=8)
    a.text(ph + 0.12, i, f"+{p:.1f}%", ha="left", va="center", fontsize=11, color=ink)
a.set_yticks(range(len(rows))); a.set_yticklabels([r[0] for r in rows], fontsize=10.5); a.invert_yaxis()
a.set_xlim(0, 4.2); a.axvline(0, color=ink2, lw=1)
a.set_xlabel("Increase in risk per 1°C hotter day (%, with 95% CI)", color=ink2, fontsize=11)
a.set_title("a  Short-term heat (class II evidence)", loc="left", fontsize=11.5, color=ink)

dT = np.linspace(0, 3.2, 200)
b.plot(dT, (1.024 ** dT - 1) * 100, color=hot, lw=2.2)
for val, lab, dx, dy in [(5, "today: ≈5%", 0.2, -2.2), (7, "2050: ≈7%\n(95% CI 4.2–9.7%)", -1.65, 0.4)]:
    x = math.log(1 + val / 100) / math.log(1.024)
    b.plot(x, val, "o", color=ink, ms=7)
    b.annotate(lab, (x, val), xytext=(x + dx, val + dy), fontsize=10.5, color=ink,
               arrowprops=dict(arrowstyle="-", color=ink2, lw=0.9))
b.set_xlim(0, 3.2); b.set_ylim(0, 9)
b.set_xlabel("Land warming since pre-industrial (°C)", color=ink2, fontsize=11)
b.set_ylabel("Extra deaths from\nsuicide or mental disorders", color=ink2, fontsize=10.5)
b.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.0f}%"))
b.set_title("b  Scaled with warming, as in the paper's projection", loc="left", fontsize=11.5, color=ink)

for ax in (a, b):
    ax.set_facecolor(surf); ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
a.tick_params(axis="y", length=0); a.spines["left"].set_visible(False)
b.grid(axis="y", color=grid, lw=0.8)
fig.suptitle("Small effects per degree, multiplied by everyone and every hot day", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-22-mental-heat.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-22-mental-heat.png")
