# Figure for the blog post "More compute, better AI: how much better?" (2026-10-29).
# Accuracy versus inference-time compute (number of samples per problem, log scale):
#   OpenAI o1 on AIME 2024 (OpenAI 2024, "Learning to reason with LLMs"): 74% with 1 sample, 83% with consensus of
#   64 samples, 93% re-ranking 1,000 samples with a learned scorer (GPT-4o: 12%).
#   OpenAI o3 (preview) on the ARC-AGI-1 semi-private set (ARC Prize, December 2024): 75.7% with 6 samples,
#   87.5% with 1,024 samples (about 172x the compute).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-29-scaling-inference.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig, ax = plt.subplots(figsize=(6.6, 4.8), facecolor=surf); ax.set_facecolor(surf)
o1 = ([1, 64, 1000], [74, 83, 93])
o3 = ([6, 1024], [75.7, 87.5])
ax.plot(*o1, "-o", color="#2a78d6", lw=2.4, ms=7, label="o1 on AIME 2024 (math competition)")
ax.plot(*o3, "-s", color="#b4532a", lw=2.4, ms=7, label="o3 on ARC-AGI-1 (abstract puzzles)")
for x, y in zip(*o1):
    ax.annotate(f"{y}%", (x, y), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=10, color="#2a78d6")
for x, y in zip(*o3):
    ax.annotate(f"{y}%", (x, y), xytext=(0, -16), textcoords="offset points", ha="center", fontsize=10,
                color="#b4532a")
ax.set_xscale("log"); ax.set_xlim(0.7, 2000); ax.set_ylim(65, 100)
ax.set_xlabel("Samples per problem (inference compute, log scale)", color=ink2, fontsize=11)
ax.set_ylabel("Accuracy (%)", color=ink2, fontsize=11)
ax.legend(loc="lower right", frameon=False, fontsize=10)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Thinking longer helps, but each step costs about 10–100× more", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-29-scaling-inference.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-29-scaling-inference.png")
