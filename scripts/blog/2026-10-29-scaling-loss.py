# Figure for the blog post "More compute, better AI: how much better?" (2026-10-29).
# Compute-optimal pretraining loss from the Chinchilla parametric fit as corrected by Besiroglu et al. (2024,
# arXiv 2404.10102): L(N, D) = E + A/N^alpha + B/D^beta with E = 1.8172, A = 482.01, B = 2085.43,
# alpha = 0.3478, beta = 0.3658, training compute C = 6 N D. For each C the loss is minimised over N (calculation by
# Daeha Kim). Reference compute levels: GPT-3 3.14e23 FLOP (Brown et al. 2020); GPT-4 about 2e25 FLOP and the
# 2e29 FLOP run judged feasible by 2030 (Sevilla et al. 2024, Epoch AI); Grok 4 about 5e26 FLOP (Epoch AI estimate).
# Stock of public human text about 300 trillion tokens (Villalobos et al. 2024, arXiv 2211.04325).
# The fit describes one family of models and data; it illustrates the shape of the curve, not exact frontier losses.
# Run from the repository root: python scripts/blog/2026-10-29-scaling-loss.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, red = "#2a78d6", "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

E, A, B, a, b = 1.8172, 482.01, 2085.43, 0.3478, 0.3658
C = np.logspace(22, 29.5, 76)
Nn = np.logspace(7, 16, 9001)
L, D = [], []
for c in C:
    d = c / (6 * Nn); l = E + A / Nn ** a + B / d ** b; k = l.argmin()
    L.append(l[k]); D.append(d[k])
L, D = np.array(L), np.array(D)

fig, (ax, bx) = plt.subplots(2, 1, figsize=(6.6, 7.4), facecolor=surf, sharex=True,
                             gridspec_kw={"height_ratios": [1.35, 1]})
ax.plot(C, L, color=blue, lw=2.6)
ax.axhline(E, color=ink2, lw=1.2, ls=(0, (4, 3)))
ax.text(1.3e22, E + 0.008, "irreducible floor (1.82)", fontsize=9.5, color=ink2, va="bottom")
refs = [("GPT-3", 3.14e23), ("GPT-4", 2e25), ("Grok 4", 5e26), ("2030\nfeasible", 2e29)]
for name, c in refs:
    l = np.interp(np.log10(c), np.log10(C), L)
    ax.plot(c, l, "o", color=ink, ms=6)
    ax.annotate(name, (c, l), xytext=(0, 9), textcoords="offset points", ha="center", va="bottom", fontsize=9.5,
                color=ink, linespacing=1.1)
ax.set_ylim(1.78, 2.2)
ax.set_ylabel("Predicted loss (nats per token)", color=ink2, fontsize=10.5)
ax.set_title("a  Each 10× compute removes about a third of what is left to gain", loc="left", fontsize=11.5,
             color=ink)

bx.plot(C, D / 1e12, color=red, lw=2.6)
bx.axhline(300, color=ink2, lw=1.2, ls=(0, (4, 3)))
bx.text(1.3e22, 330, "public human text ≈ 300 trillion tokens", fontsize=9.5, color=ink2, va="bottom")
bx.set_yscale("log"); bx.set_ylim(0.1, 3000)
bx.set_ylabel("Training tokens needed\n(trillions)", color=ink2, fontsize=10.5)
bx.set_xscale("log"); bx.set_xlim(1e22, 3e29)
bx.set_xlabel("Training compute (FLOP)", color=ink2, fontsize=11)
bx.set_title("b  …and needs ever more data", loc="left", fontsize=11.5, color=ink)
for axx in (ax, bx):
    axx.set_facecolor(surf); axx.grid(color=grid, lw=0.8); axx.set_axisbelow(True)
    for sp in ("top", "right"): axx.spines[sp].set_visible(False)
fig.suptitle("What the scaling law predicts for more compute", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-29-scaling-loss.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-29-scaling-loss.png")
