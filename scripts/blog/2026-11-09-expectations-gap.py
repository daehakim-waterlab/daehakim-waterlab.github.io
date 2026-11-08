# Figure for the blog post "What the public and AI insiders expect from AI" (2026-11-09).
# Data from Sacher, Cotter, Jones, Korinek and McCrory (2026), The AI Expectations Gap: Public and Frontier Lab Views
# on AI's Impact on Work, The Anthropic Institute (https://www.anthropic.com/research/ai-expectations-gap).
# Surveys of 10,980 US adults (Morning Consult, 11-23 Aug 2026, weighted) and 1,334 Anthropic staff (9-12 Aug 2026).
# (a) Public versus staff:
#   AI able to make a Nobel-level discovery by 2030: 39% vs 91%
#   AI able to design, conduct and publish scientific studies by 2027: 38% vs about 90% ("9 in 10")
#   AI able to do at least seven of eight named tasks by 2030: 41% vs 96%
#   Share of feasible work tasks done with AI by 2030: 42% vs 65%
#   AI makes a suitable task take a quarter of the time or less: 26% (US adults who use AI at work) vs 59%
#   Average share of own work hours AI can do by 2030: 28% (US workers) vs 75%
# (b) AI able to do at least seven of eight tasks by 2030, by experience: never used AI 28%, all US adults 41%,
#   regular users at work 56%, Anthropic staff 96%.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-11-09-expectations-gap.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
pub, lab = "#8a8780", "#b4532a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

rows = [("Nobel-level discovery\nby 2030", 39, 91), ("Runs and publishes\nstudies by 2027", 38, 90),
        ("Does 7 of 8 tasks\nby 2030", 41, 96), ("Tasks done with AI\nby 2030", 42, 65),
        ("Task takes a quarter\nof the time or less", 26, 59), ("Share of own work AI\ncan do by 2030", 28, 75)]
ladder = [("Never used AI", 28, pub), ("All US adults", 41, pub), ("Regular users at work", 56, "#c98a5c"),
          ("Anthropic staff", 96, lab)]

fig, (a, b) = plt.subplots(2, 1, figsize=(6.6, 8.4), facecolor=surf, gridspec_kw={"height_ratios": [2.3, 1]})
for ax in (a, b):
    ax.set_facecolor(surf)
for i, (name, p, s) in enumerate(rows):
    a.plot([p, s], [i, i], color=grid, lw=5, solid_capstyle="round", zorder=1)
    a.plot(p, i, "o", ms=11, color=pub, zorder=2)
    a.plot(s, i, "o", ms=11, color=lab, zorder=2)
    a.text(p - 3.5, i, f"{p}%", ha="right", va="center", fontsize=9.6, color=pub)
    a.text(s + 3.5, i, f"{s}%", ha="left", va="center", fontsize=9.6, color=lab)
a.set_yticks(range(len(rows))); a.set_yticklabels([r[0] for r in rows], fontsize=9.8); a.invert_yaxis()
a.set_xlim(0, 112); a.set_xticks([0, 25, 50, 75, 100]); a.set_ylim(len(rows) - 0.4, -1.1)
a.plot(4, -0.85, "o", ms=9, color=pub); a.text(8, -0.85, "US public", va="center", fontsize=9.8, color=pub)
a.plot(40, -0.85, "o", ms=9, color=lab); a.text(44, -0.85, "Anthropic staff", va="center", fontsize=9.8, color=lab)
a.set_xlabel("Share of respondents (%), or average share (last row)", color=ink2, fontsize=10)
a.set_title("a  Far apart on what AI will do by 2030", loc="left", fontsize=11, color=ink)

for i, (name, v, c) in enumerate(ladder):
    b.barh(i, v, 0.6, color=c)
    b.text(v + 1.5, i, f"{v}%", va="center", fontsize=9.6, color=ink)
b.set_yticks(range(len(ladder))); b.set_yticklabels([r[0] for r in ladder], fontsize=9.8); b.invert_yaxis()
b.set_xlim(0, 112); b.set_xticks([0, 25, 50, 75, 100])
b.set_xlabel("Expect AI to do at least 7 of 8 named tasks by 2030 (%)", color=ink2, fontsize=10)
b.set_title("b  Expectations rise with hands-on use", loc="left", fontsize=11, color=ink)
for ax in (a, b):
    ax.grid(axis="x", color=grid, lw=0.8); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=9.5)
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
fig.suptitle("The AI expectations gap", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-09-expectations-gap.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-09-expectations-gap.png")
