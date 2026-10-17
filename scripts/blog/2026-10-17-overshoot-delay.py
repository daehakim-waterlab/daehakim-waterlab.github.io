# Figure for the blog post "Approaching 1.5°C from above" (2026-10-17).
# Illustrative CO2-budget arithmetic based on numbers reported in UNEP (2026) Limiting Overshoot.
# Run from the repository root: python scripts/blog/2026-10-17-overshoot-delay.py
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

E0, RAMP = 40.0, 30            # GtCO2/yr today; years of linear decline to net zero
BUDGET, T15 = 130.0, 1.5       # remaining 1.5C budget from 2026 (50%), GtCO2
TCRE = dict(best=0.45, lo=0.27, hi=0.63)   # degC per 1000 GtCO2 (IPCC AR6 likely range)
starts = [2026, 2031, 2036]
labels = ["Start cutting in 2026", "Delay 5 years (2031)", "Delay 10 years (2036)"]
cols = ["#2a78d6", "#eb6834", "#1baf7a"]
ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

years = np.arange(2020, 2076)
def path(s):
    e = np.where(years < s, E0, E0*(1-(years-s)/RAMP))
    return np.clip(e, 0, None)
def peak(s, k):
    C = E0*(s-2026) + E0*RAMP/2
    return T15 + (C-BUDGET)*k/1000, C

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":ink2,
    "axes.labelcolor":ink2,"xtick.color":ink2,"ytick.color":ink2})
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios":[1.45,1]}, facecolor=surf)
for ax in (a, b):
    ax.set_facecolor(surf)
    for sp in ("top","right"): ax.spines[sp].set_visible(False)
    ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)

# (a) emissions pathways
for s, l, c in zip(starts, labels, cols):
    a.plot(years, path(s), color=c, lw=2, solid_capstyle="round")
    a.text(s+RAMP+0.6, 1.2, f"{s+RAMP}", color=ink2, fontsize=9, ha="center")
b6 = np.clip(E0*(1-(years-2026)/6.5), 0, None); b6[years<2026]=E0
a.plot(years, b6, color=ink2, lw=1.5, ls=(0,(4,3)))
a.annotate("Staying within the 1.5°C budget\nmeans zero in ~6 years", xy=(2031.2, 8), xytext=(2034, 5),
           color=ink2, fontsize=9, va="center", arrowprops=dict(arrowstyle="-", color=ink2, lw=0.8))
for s, l, c, y in zip(starts, labels, cols, [22, 30, 38]):
    pass
a.legend([plt.Line2D([],[],color=c,lw=2) for c in cols], labels, frameon=False, loc="upper right", fontsize=9.5, labelcolor=ink)
a.set_xlim(2020, 2075); a.set_ylim(0, 46)
a.set_ylabel("Global CO$_2$ emissions (GtCO$_2$ per year)")
a.set_title("(a) Same 30-year decline, different start", loc="left", color=ink, fontsize=12)
a.text(2054.2, 1.2, "net zero:", color=ink2, fontsize=9, ha="right")

# (b) peak warming
for i, (s, c) in enumerate(zip(starts, cols)):
    pb, C = peak(s, TCRE["best"]); pl,_ = peak(s, TCRE["lo"]); ph,_ = peak(s, TCRE["hi"])
    b.plot([i, i], [pl, ph], color=c, lw=2, solid_capstyle="round")
    b.scatter([i], [pb], s=70, color=c, edgecolor=surf, linewidth=2, zorder=3)
    b.text(i+0.12, pb, f"{pb:.2f}°C", va="center", color=ink, fontsize=10)
    b.text(i, 1.33, f"{int(C)} GtCO$_2$\nemitted from 2026", ha="center", va="bottom", color=ink2, fontsize=8)
b.axhline(T15, color=ink2, lw=1.2, ls=(0,(4,3)))
b.text(2.45, T15+0.01, "1.5°C", color=ink2, fontsize=9, ha="right", va="bottom")
b.set_xticks(range(3)); b.set_xticklabels(["2026", "2031", "2036"])
b.set_xlabel("Year emissions start to fall"); b.set_xlim(-0.5, 2.6); b.set_ylim(1.3, 2.1)
b.set_ylabel("Peak warming (°C above 1850–1900)")
b.set_title("(b) Each 5 years of delay ≈ +0.1°C", loc="left", color=ink, fontsize=12)


fig.tight_layout()
import os; os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-17-overshoot-delay.png", dpi=180, facecolor=surf)
for s in starts: print(s, [round(peak(s,TCRE[k])[0],2) for k in ("lo","best","hi")])
