# Figure 1 for the blog post "When floods team up: a review of compound flooding" (2026-11-21).
# A toy calculation, by Daeha Kim, of why the dependence between flood drivers matters.
# Two drivers, say heavy rain and storm surge, each reach their own 10-year level
# (annual exceedance probability 0.1). The chance that both do so in the same event is
# computed with a Gaussian copula for a range of correlation coefficients rho:
#   P(both) = P(X > z, Y > z) for standard normal X, Y with correlation rho and z = 1.28155
#   (the 90th percentile), integrated numerically as the integral over x > z of
#   phi(x) * P(Y > z | X = x), where Y given X = x is normal with mean rho x and variance 1 - rho^2.
# With rho = 0 (independence) this is 0.01, a 100-year joint event. Numbers are illustrative.
# Run from the repository root: python scripts/blog/2026-11-21-compound-flood-odds.py
import os, matplotlib
import numpy as np
from math import erf, sqrt
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, red = "#2a78d6", "#c0392b"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

p_single = 0.1
z = 1.2815515655446004            # standard normal 90th percentile
Phi = np.vectorize(lambda x: 0.5 * (1 + erf(x / sqrt(2))))
xs = np.linspace(z, 9, 20001)
phi = np.exp(-xs ** 2 / 2) / sqrt(2 * np.pi)
def p_both(rho):
    cond = 1 - Phi((z - rho * xs) / sqrt(1 - rho ** 2))
    return np.trapezoid(phi * cond, xs)

rhos = np.linspace(0, 0.9, 46)
T = np.array([1 / p_both(r) for r in rhos])

fig, ax = plt.subplots(figsize=(6.6, 4.4), facecolor=surf)
ax.set_facecolor(surf)
ax.plot(rhos, T, color=blue, lw=2.6)
for r in (0.0, 0.3, 0.6):
    t = 1 / p_both(r)
    ax.plot(r, t, "o", color=red if r else ink2, ms=7, zorder=3)
    ax.annotate(f"once in about\n{t:.0f} years", (r, t), xytext=(12, 4), textcoords="offset points",
                fontsize=9.4, color=red if r else ink2, va="bottom", linespacing=1.1)
ax.axhline(10, color=ink2, lw=0.9, ls=(0, (3, 3)))
ax.text(0.9, 11.5, "each driver alone: once in 10 years", ha="right", va="bottom", fontsize=9, color=ink2)
ax.set_xlim(-0.02, 0.92); ax.set_ylim(0, 110)
ax.set_xlabel("How strongly the two drivers tend to occur together\n(correlation, 0 = independent)",
              color=ink2, fontsize=10.2)
ax.set_ylabel("Return period of both together (years)", color=ink2, fontsize=10.2)
ax.tick_params(labelsize=9.5)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Rain and storm surge, each a 10-year event: how rare is both?", x=0.012, ha="left",
             color=ink, fontsize=12)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-21-compound-flood-odds.png", dpi=170, facecolor=surf)
print({round(r, 1): round(1 / p_both(r), 1) for r in (0.0, 0.3, 0.5, 0.6, 0.9)})
print("saved assets/img/blog/2026-11-21-compound-flood-odds.png")
