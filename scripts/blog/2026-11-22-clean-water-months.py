# Figure 1 for the blog post "Clean water scarcity: counting quality as well as quantity" (2026-11-22).
# Data: Table 1 of Jones, Bierkens & van Vliet (2024), Nature Climate Change 14, 629-635.
# Share of the world population exposed to water scarcity in at least n months per year,
# averaged over 2005-2020, for quantity only (WS) and quantity plus quality (WSq).
# Drawn by Daeha Kim. Run from the repository root:
#   python scripts/blog/2026-11-22-clean-water-months.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
c_ws, c_wsq = "#8a8883", "#1f6fb2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})

n = np.arange(1, 13)
ws = np.array([47.3, 42.4, 37.3, 31.7, 24.5, 17.7, 14.0, 11.4, 9.4, 7.7, 6.1, 4.6])
wsq = np.array([55.4, 50.9, 46.3, 41.4, 35.6, 29.6, 25.4, 21.8, 18.7, 15.8, 13.0, 10.3])
ws_bn = np.array([3.26, 2.93, 2.58, 2.19, 1.69, 1.22, 0.97, 0.79, 0.65, 0.53, 0.42, 0.32])
wsq_bn = np.array([3.82, 3.52, 3.19, 2.86, 2.46, 2.04, 1.75, 1.51, 1.29, 1.09, 0.90, 0.71])

fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 4.4), facecolor=surf, gridspec_kw={"width_ratios": [1.35, 1]})
for ax in (a, b):
    ax.set_facecolor(surf)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): ax.spines[sp].set_color(ink2)
    ax.tick_params(colors=ink2, labelsize=9.5)
    ax.grid(axis="y", color=grid, lw=0.8, zorder=0)

a.fill_between(n, ws, wsq, color=c_wsq, alpha=0.12, lw=0, zorder=1)
a.plot(n, ws, "-o", color=c_ws, ms=4.5, lw=2, zorder=3, label="Quantity only")
a.plot(n, wsq, "-o", color=c_wsq, ms=4.5, lw=2, zorder=3, label="Quantity + quality")
a.annotate(f"{wsq[0]:.0f}% ({wsq_bn[0]:.1f} billion)", (1, wsq[0]), (1.6, 58.5), fontsize=9.2, color=c_wsq)
a.annotate(f"{ws[0]:.0f}% ({ws_bn[0]:.1f} billion)", (1, ws[0]), (0.75, 26), fontsize=9.2, color=ink2,
           arrowprops=dict(arrowstyle="-", color=ink2, lw=0.8))
a.annotate(f"every month:\n{wsq[-1]:.1f}% vs {ws[-1]:.1f}%", (12, wsq[-1]), (9.0, 24), fontsize=9.2, color=ink,
           arrowprops=dict(arrowstyle="-", color=ink2, lw=0.8))
a.set_xticks(n); a.set_xlim(0.6, 12.4); a.set_ylim(0, 62)
a.set_xlabel("Scarce in at least n months of the year", color=ink2, fontsize=10)
a.set_ylabel("Share of world population (%)", color=ink2, fontsize=10)
a.legend(frameon=False, fontsize=9.5, loc="upper right", labelcolor=ink)
a.set_title("How many people face scarcity, and how often", loc="left", fontsize=10.5, color=ink)

ratio = wsq / ws
b.bar(n, ratio, color=c_wsq, width=0.62, zorder=2)
b.axhline(1, color=ink2, lw=1, zorder=3)
for i in (0, 5, 11):
    b.text(n[i], ratio[i] + 0.05, f"×{ratio[i]:.1f}", ha="center", fontsize=9.2, color=ink)
b.set_xticks(n); b.set_xlim(0.4, 12.6); b.set_ylim(0, 2.55)
b.set_xlabel("Scarce in at least n months of the year", color=ink2, fontsize=10)
b.set_title("Quality multiplies the count (WSq ÷ WS)", loc="left", fontsize=10.5, color=ink)

fig.suptitle("Adding water quality raises exposure, most of all for year-round scarcity (2005–2020)",
             x=0.012, ha="left", color=ink, fontsize=12)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
out = "assets/img/blog/2026-11-22-clean-water-months.png"
fig.savefig(out, dpi=170, facecolor=surf)
print("saved", out, "ratios", np.round(ratio, 2))
