# Figure for the blog post "How fast will AI spread, and how many chips will it need?" (2026-11-07).
# Adoption by years since launch. Sources:
#   US workers using a computer at work (IBM PC, 1981): 24.6% 1984, 36.8% 1989, 45.8% 1993, 49.4% 1997, 55.5% 2003
#     (Census/CPS via NCES Digest Table 429 and BLS).
#   US households with internet access (web browser, 1993): 18.0% 1997, 41.5% 2000, 50.4% 2001 (Census CPS).
#   EU enterprises (10+ staff) buying cloud services (AWS, 2006): 19% 2014, 21% 2016, 26% 2018, 45.2% 2023 (Eurostat).
#   US adults 18-64 using generative AI (ChatGPT, 30 Nov 2022): 44.6% Aug 2024, 54.6% Aug 2025
#     (Bick, Blandin & Deming, Real-Time Population Survey; St. Louis Fed, Nov 2025).
#   EU enterprises (10+ staff) using AI: 8.0% 2023, 13.5% 2024, 20.0% 2025 (Eurostat).
#   Share of US work hours assisted by generative AI: 4.1% Q3 2024, 6.3% Q2 2026 (FRED Blog, Aug 2026).
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-07-ai-diffusion.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

series = [
    ("PC at work (US workers)", [3, 8, 12, 16, 22], [24.6, 36.8, 45.8, 49.4, 55.5], "#8a8780", "o", "-"),
    ("Internet at home (US households)", [4, 7, 8], [18.0, 41.5, 50.4], "#c4813a", "s", "-"),
    ("Cloud services (EU firms)", [8, 10, 12, 17], [19, 21, 26, 45.2], "#7a5195", "D", "-"),
    ("Generative AI (US adults 18–64)", [1.7, 2.7], [44.6, 54.6], "#2a78d6", "o", "-"),
    ("AI in business (EU firms)", [1.1, 2.1, 3.1], [8.0, 13.5, 20.0], "#2a78d6", "s", "--"),
    ("Work hours assisted by AI (US)", [1.8, 3.6], [4.1, 6.3], "#b4532a", "^", "-"),
]
fig, ax = plt.subplots(figsize=(6.6, 5.6), facecolor=surf); ax.set_facecolor(surf)
for name, x, y, c, m, ls in series:
    ax.plot(x, y, ls=ls, marker=m, color=c, lw=2.2, ms=6, label=name)
ax.set_xlim(0, 23); ax.set_ylim(0, 62)
ax.set_xlabel("Years since launch", color=ink2, fontsize=11)
ax.set_ylabel("Share of adopters (%)", color=ink2, fontsize=11)
ax.annotate("fast breadth", (2.7, 54.6), xytext=(4.6, 58.5), fontsize=10, color="#2a78d6",
            arrowprops=dict(arrowstyle="-", color="#2a78d6", lw=0.9))
ax.annotate("slow depth", (3.6, 6.3), xytext=(5.6, 4.0), fontsize=10, color="#b4532a",
            arrowprops=dict(arrowstyle="-", color="#b4532a", lw=0.9))
ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.07), frameon=False, fontsize=9.5)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("AI spread faster than any office technology, but only on the surface", x=0.012, ha="left", color=ink,
             fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-07-ai-diffusion.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-07-ai-diffusion.png")
