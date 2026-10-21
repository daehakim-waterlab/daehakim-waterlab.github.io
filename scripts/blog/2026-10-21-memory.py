# Figure for the blog post "A short history of AI, part 2: data, GPUs and deep learning (1997-2017)" (2026-10-21).
# Illustration (no data) of why plain recurrent networks forget and LSTM networks can remember: the share of an
# input signal that survives k steps when it is multiplied by a constant factor at every step. A plain recurrent
# network with an effective factor of 0.8 keeps almost nothing after a month of daily steps; an LSTM cell whose
# forget gate stays open (factor 0.99) keeps most of it. The factors are chosen for illustration; in real networks
# they are learned and vary over time. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-21-memory.py
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
rnn, lstm = "#d6604d", "#2a78d6"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

k = np.arange(0, 91)
fig, ax = plt.subplots(figsize=(8.6, 5.0), facecolor=surf); ax.set_facecolor(surf)
ax.plot(k, 0.8 ** k * 100, color=rnn, lw=2.6, label="plain recurrent network (factor 0.8 per step)")
ax.plot(k, 0.99 ** k * 100, color=lstm, lw=2.6, label="LSTM with its forget gate open (factor 0.99)")
for kk in (30, 90):
    ax.scatter([kk], [0.99 ** kk * 100], s=40, color=lstm, zorder=3)
    ax.text(kk + 1.5, 0.99 ** kk * 100 + 2, f"{0.99 ** kk * 100:.0f}%", fontsize=10.5, color=lstm)
ax.text(31.5, 4, f"{0.8 ** 30 * 100:.2f}%", fontsize=10.5, color=rnn)
ax.scatter([30], [0.8 ** 30 * 100], s=40, color=rnn, zorder=3)
ax.set_xlim(0, 95); ax.set_ylim(0, 105)
ax.set_xlabel("Steps back in time (for example, days since a rainfall event)", color=ink2)
ax.set_ylabel("Share of the input signal that survives (%)", color=ink2)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
ax.legend(loc="upper right", frameon=False, fontsize=10.5)
fig.suptitle("Why LSTM networks can remember last month's rain", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-memory.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-memory.png")
