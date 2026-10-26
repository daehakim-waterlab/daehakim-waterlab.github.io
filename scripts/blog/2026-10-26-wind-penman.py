# Figure for the blog post "Wind makes ecosystems spend more water per unit of carbon" (2026-10-26).
# Illustrative Penman-Monteith calculation by Daeha Kim, not a result of Wang et al. (2026).
#   LE = (Delta*A + rho*cp*D*ga) / (Delta + gamma*(1 + ga/gc))   (Monteith 1965)
# Fixed conditions: available energy A = 150 W m-2, air temperature 20 °C, vapour-pressure deficit D = 1.0 kPa,
# canopy (surface) conductance gc = 10 mm/s for dry canopies and gc -> infinity for a wet canopy (evaporation of
# intercepted rain). Aerodynamic conductance from the logarithmic wind profile under neutral conditions,
#   ga = k^2 u / [ln((z-d)/z0m) ln((z-d)/z0h)],  d = 0.67h, z0m = 0.123h, z0h = 0.1 z0m, k = 0.41,
# grass h = 0.12 m with wind measured at 2 m; conifer forest h = 20 m with wind measured 5 m above the canopy.
# Run from the repository root: python scripts/blog/2026-10-26-wind-penman.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
cg, cf, cw = "#8fb35a", "#2e6b4f", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

T, P, D, A = 20.0, 101.3, 1.0, 150.0
es = 0.6108 * np.exp(17.27 * T / (T + 237.3))
Delta, gamma, rho, cp = 4098 * es / (T + 237.3) ** 2, 0.000665 * P, 1.2, 1013.0

def ga_log(u, h, z):
    d, z0m = 0.67 * h, 0.123 * h
    return 0.41 ** 2 * u / (np.log((z - d) / z0m) * np.log((z - d) / (0.1 * z0m)))

def le(ga, gc):
    return (Delta * A + rho * cp * D * ga) / (Delta + gamma * (1 + ga / gc))

u = np.linspace(1, 5, 81)
cases = [("Grass, dry canopy (transpiration)", le(ga_log(u, 0.12, 2.0), 0.010), cg, "-"),
         ("Conifer forest, dry canopy (transpiration)", le(ga_log(u, 20, 25), 0.010), cf, "-"),
         ("Conifer forest, wet canopy (intercepted rain)", le(ga_log(u, 20, 25), 1e6), cw, "--")]
fig, ax = plt.subplots(figsize=(6.6, 5.6), facecolor=surf); ax.set_facecolor(surf)
for (name, y, c, ls), dy in zip(cases, (7, -7, 0)):
    rel = (y / y[0] - 1) * 100
    ax.plot(u, rel, color=c, lw=2.6, ls=ls, label=name)
    ax.text(5.06, rel[-1] + dy, f"+{rel[-1]:.0f}%", va="center", fontsize=10.5, color=c)
ax.set_xlim(1, 5.6); ax.set_ylim(0, 270)
ax.set_xticks([1, 2, 3, 4, 5]); ax.spines["bottom"].set_bounds(1, 5)
ax.set_xlabel("Wind speed (m/s)", color=ink2, fontsize=11)
ax.set_ylabel("Increase in evaporation\nrelative to 1 m/s (%)", color=ink2, fontsize=11)
ax.legend(loc="upper left", frameon=False, fontsize=10)
ax.text(2.45, 42, "Same weather: 150 W/m² available energy,\n20°C, VPD 1 kPa, canopy conductance 10 mm/s",
        fontsize=9.5, color=ink2, linespacing=1.4)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Wind matters most where the canopy is rough and wet", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-26-wind-penman.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-26-wind-penman.png")
