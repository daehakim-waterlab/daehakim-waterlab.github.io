# Figure for the blog post "Push until it breaks: why good research reports where it fails" (2026-11-17).
# A toy "crash test" in the spirit of Klemes (1986) and Andreassian et al. (2009), by Daeha Kim.
# "Truth": mean annual runoff Q = P - E, with evapotranspiration E from Fu's form of the Budyko curve,
#   E/P = 1 + PET/P - (1 + (PET/P)^w)^(1/w), with PET = 1000 mm/yr and w = 2.6.
# "Model": a straight line, Q = a + b P, fitted by least squares to years with P between 1,100 and
#   1,500 mm/yr (the calibration range). The model is then tested over P = 500 to 2,000 mm/yr.
# The numbers are illustrative and do not describe any real catchment.
# Run from the repository root: python scripts/blog/2026-11-17-model-breaking-point.py
import os, matplotlib
import numpy as np
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
true_c, mod_c, bad = "#2a78d6", "#b4532a", "#f6e3dc"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

PET, w = 1000.0, 2.6
def runoff(P):
    phi = PET / P
    E = P * (1 + phi - (1 + phi ** w) ** (1 / w))
    return P - E

P = np.linspace(500, 2000, 301)
Q = runoff(P)
cal = (P >= 1100) & (P <= 1500)
b1, a0 = np.polyfit(P[cal], Q[cal], 1)
Qm = a0 + b1 * P
err = 100 * (Qm - Q) / Q
fails = np.abs(err) > 20

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 6.6), facecolor=surf, sharex=True,
                           gridspec_kw={"height_ratios": [1.15, 1]})
for ax in (a, b):
    ax.set_facecolor(surf)
    ax.axvspan(1100, 1500, color="#e8eef6", zorder=0)
    lo = P[fails & (P < 1100)]
    if lo.size:
        ax.axvspan(500, lo.max(), color=bad, zorder=0)
a.plot(P, Q, color=true_c, lw=2.4, label="Real behaviour (Budyko curve)")
a.plot(P, Qm, color=mod_c, lw=2.2, ls=(0, (5, 3)), label="Simple model fitted to the blue-shaded years")
a.text(1300, 1060, "calibration\nrange", ha="center", va="center", fontsize=9.2, color=true_c, linespacing=1.1)
a.set_ylabel("Annual runoff (mm)", color=ink2, fontsize=10.5)
a.axhline(0, color=ink2, lw=0.8)
a.set_ylim(-150, 1200)
a.legend(frameon=False, fontsize=9.3, loc="upper left", bbox_to_anchor=(0.0, 0.88))
a.set_title("a  Inside the tested range, the model looks excellent", loc="left", fontsize=11, color=ink)

b.plot(P, err, color=mod_c, lw=2.2)
b.axhline(0, color=ink2, lw=0.8)
b.axhline(-20, color=ink2, lw=0.8, ls=(0, (3, 3)))
b.text(1990, -30, "-20% error", ha="right", va="top", fontsize=9, color=ink2)
if lo.size:
    b.text(775, -118, "model breaks\nin drier years", ha="center", va="center", fontsize=9.2,
           color=mod_c, linespacing=1.1)
b.set_ylim(-160, 25)
b.set_xlabel("Annual precipitation (mm)", color=ink2, fontsize=10.5)
b.set_ylabel("Runoff error (%)", color=ink2, fontsize=10.5)
b.set_title("b  Outside it, the error grows quickly", loc="left", fontsize=11, color=ink)
for ax in (a, b):
    ax.tick_params(labelsize=9.5)
    ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("A toy crash test: find where the model breaks", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-17-model-breaking-point.png", dpi=170, facecolor=surf)
print("fit a, b", round(a0, 1), round(b1, 3), "| breaks below P =", round(lo.max()) if lo.size else None,
      "| error at 800 mm:", round(float(np.interp(800, P, err)), 1), "| at 600 mm:", round(float(np.interp(600, P, err)), 1),
      "| max err in cal:", round(float(np.abs(err[cal]).max()), 1), "| at 2000:", round(float(err[-1]), 1))
print("saved assets/img/blog/2026-11-17-model-breaking-point.png")
