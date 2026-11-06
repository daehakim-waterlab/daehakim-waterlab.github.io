# Figure for the blog post "How fast will AI spread, and how many chips will it need?" (2026-11-07).
# Illustrative stock-flow model by Daeha Kim (not a forecast), following the specification in the accompanying
# research report:
#   token growth in year y: g(y) = 7^((1 - d)^(y - 2026)); 7x is Google's token growth from May 2025 to May 2026
#     (480 trillion to 3.2 quadrillion tokens per month, Google I/O 2026); d sets how fast growth slows;
#   required compute capacity: K(y) = max(K(y-1), K(y-1) * g(y) / e), with net efficiency gain e = 2.5 per year
#     (more tokens per unit of installed capacity);
#   chip purchases: P(y) = K(y) - 0.8 K(y-1) (five-year life); cost per unit of capacity falls 1.4x per year;
#   spending indexed to 2026 = 1 (roughly 400 billion US dollars of AI silicon in 2026, an estimate from NVIDIA,
#   Broadcom and AMD data-center revenue).
# Together, e and the cost decline mean about 3.5x more tokens per dollar of new hardware each year, so spending
# rises only while token growth stays above about 3.5x per year.
# Run from the repository root: python scripts/blog/2026-11-07-chip-cycle.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

def run(d, e=2.5):
    K = {2025: 1.0}; S = {}; G = {}
    for y in range(2026, 2036):
        g = 7 ** ((1 - d) ** (y - 2026)); G[y] = g
        K[y] = max(K[y - 1], K[y - 1] * g / e)
        S[y] = (K[y] - 0.8 * K[y - 1]) * 1.4 ** -(y - 2026)
    s0 = S[2026]
    return G, {y: S[y] / s0 for y in S}

cases = [("Token growth slows fast", 0.2, "#8a8780", -16), ("Consensus-like path", 0.1, "#2a78d6", 8),
         ("Agent boom", 0.05, "#b4532a", 8)]
fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 7.0), facecolor=surf, sharex=True)
years = list(range(2026, 2036))
for name, d, c, off in cases:
    G, S = run(d)
    a.plot(years, [G[y] for y in years], "-o", color=c, lw=2.2, ms=4, label=name)
    b.plot(years, [S[y] for y in years], "-o", color=c, lw=2.2, ms=4, label=name)
    pk = max(S, key=S.get)
    b.annotate(f"peak {pk}", (pk, S[pk]), xytext=(14, off), textcoords="offset points", ha="center", fontsize=9.5,
               color=c)
a.axhspan(3.2, 4.1, color="#efe9dd", zorder=0, label="Break-even for chip spending (≈3.5×/yr)")
a.set_ylim(1, 7.5); a.set_ylabel("Token growth\n(× per year)", color=ink2, fontsize=10.5)
a.set_title("a  How fast AI usage keeps growing (assumed)", loc="left", fontsize=11, color=ink)
a.legend(loc="upper right", frameon=False, fontsize=9.5)
b.set_ylim(0, 8.3); b.set_ylabel("Annual AI chip spending\n(2026 = 1, about US$400B)", color=ink2, fontsize=10.5)
b.set_title("b  What that means for chip purchases (model)", loc="left", fontsize=11, color=ink)
b.set_xticks([2026, 2028, 2030, 2032, 2034])
for ax in (a, b):
    ax.set_facecolor(surf); ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Chip demand peaks when usage growth slows, not when usage stops", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-07-chip-cycle.png", dpi=170, facecolor=surf)
for name, d, c, off in cases:
    G, S = run(d); pk = max(S, key=S.get)
    print(name, "peak", pk, round(S[pk], 2), "growth 2027", round(G[2027], 1), "2030", round(G[2030], 1))
print("saved assets/img/blog/2026-11-07-chip-cycle.png")
