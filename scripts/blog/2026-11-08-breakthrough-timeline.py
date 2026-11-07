# Figure for the blog post "How the brain invented learning, part VI: the future of intelligence" (2026-11-08).
# Timing of the five breakthroughs of Bennett (2023) on the geologic time scale, and the same events on a
# logarithmic scale of years before present together with milestones of human culture and computing.
# Geologic period boundaries (million years ago, rounded) from the International Chronostratigraphic Chart
# (International Commission on Stratigraphy, v2023/09).
# Approximate breakthrough dates as used in this blog series: first bilaterians about 600 Ma, early vertebrates about
# 500 Ma, early mammals about 150 Ma (the figure Bennett gives),
# early primates about 65 Ma (shortly after the end-Cretaceous extinction), genus Homo about 2.5 Ma.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-08-breakthrough-timeline.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

MAMMALS, PRIMATES = 150, 65
periods = [("Ed", 635, 538.8, "#e8d9c4"), ("Cm", 538.8, 485.4, "#d7e3c8"), ("O", 485.4, 443.8, "#c9e1d6"),
           ("S", 443.8, 419.2, "#d9ebe4"), ("D", 419.2, 358.9, "#ead7c0"), ("C", 358.9, 298.9, "#cfdcdc"),
           ("P", 298.9, 251.9, "#f0d6cc"), ("Tr", 251.9, 201.4, "#e2cfe3"), ("J", 201.4, 145.0, "#cfe0ef"),
           ("K", 145.0, 66.0, "#dbe9c8"), ("Pg", 66.0, 23.03, "#f5dcc2"), ("N", 23.03, 2.58, "#f6ebbd"),
           ("Q", 2.58, 0.0, "#f2f0d8")]
bt = [("1", "Steering", 600, "#8a8780"), ("2", "Reinforcing", 500, "#6f8fb8"), ("3", "Simulating", MAMMALS, "#2a78d6"),
      ("4", "Mentalizing", PRIMATES, "#7a5195"), ("5", "Speaking", 2.5, "#b4532a")]

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 7.6), facecolor=surf, gridspec_kw={"height_ratios": [1, 1.25]})
for ax in (a, b):
    ax.set_facecolor(surf)

# (a) linear geologic time
for lab, t0, t1, c in periods:
    a.axvspan(t0, t1, ymin=0, ymax=0.16, color=c, lw=0)
    if t0 - t1 > 30:
        a.text((t0 + t1) / 2, 0.08, lab, ha="center", va="center", fontsize=8.5, color=ink2, transform=a.get_xaxis_transform())
for i, (n, name, t, c) in enumerate(bt):
    y = 0.3 + 0.13 * i
    a.plot([t, t], [0.16, y], color=c, lw=1.4, transform=a.get_xaxis_transform())
    a.plot(t, y, "o", ms=16, color=c, transform=a.get_xaxis_transform(), clip_on=False)
    a.text(t, y, n, ha="center", va="center", fontsize=10, color="white", fontweight="bold",
           transform=a.get_xaxis_transform())
    a.text(t - 14 if t > 30 else t - 14, y, name, ha="left", va="center", fontsize=9.6, color=c,
           transform=a.get_xaxis_transform()) if t > 100 else \
        a.text(t + 14, y, name, ha="right", va="center", fontsize=9.6, color=c, transform=a.get_xaxis_transform())
a.set_xlim(650, -5); a.set_ylim(0, 1); a.set_yticks([])
a.set_xlabel("Million years ago", color=ink2, fontsize=10.5); a.tick_params(axis="x", labelsize=9.5)
a.set_title("a  On the geologic time scale, speaking is a sliver at the end", loc="left", fontsize=11, color=ink)
for sp in ("top", "right", "left"): a.spines[sp].set_visible(False)

# (b) logarithmic years before present
ev = [(6e8, "1 Steering", "#8a8780"), (5e8, "2 Reinforcing", "#6f8fb8"), (MAMMALS * 1e6, "3 Simulating", "#2a78d6"),
      (PRIMATES * 1e6, "4 Mentalizing", "#7a5195"), (2.5e6, "5 Speaking begins (genus Homo)", "#b4532a"),
      (3e5, "Homo sapiens", ink2), (5.2e3, "Writing", ink2), (5.7e2, "Printing press", ink2),
      (8.0e1, "First electronic computers", ink2), (9, "Transformer", "#2e8b57"), (4, "ChatGPT", "#2e8b57")]
for i, (t, lab, c) in enumerate(ev):
    y = len(ev) - i
    b.plot(t, y, "o", ms=7, color=c)
    b.text(t * 0.62, y, lab, va="center", ha="left", fontsize=9.4, color=c)
b.set_xscale("log"); b.set_xlim(2e9, 1); b.set_ylim(0.3, len(ev) + 0.7); b.set_yticks([])
b.set_xticks([1e9, 1e7, 1e5, 1e3, 1e1])
b.set_xticklabels(["1 billion", "10 million", "100,000", "1,000", "10"], fontsize=9.5)
b.set_xlabel("Years ago (logarithmic scale)", color=ink2, fontsize=10.5)
b.set_title("b  On a logarithmic scale, the pace keeps quickening", loc="left", fontsize=11, color=ink)
b.grid(axis="x", color=grid, lw=0.8); b.set_axisbelow(True)
for sp in ("top", "right", "left"): b.spines[sp].set_visible(False)

fig.suptitle("Five breakthroughs in 600 million years", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-08-breakthrough-timeline.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-08-breakthrough-timeline.png")
