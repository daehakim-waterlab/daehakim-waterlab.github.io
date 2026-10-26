# Figure for the blog post "Model distillation: how AI models learn from each other, and what they lose" (2026-10-27).
# Illustrative schematic by Daeha Kim (the probabilities are made up for illustration, not measured).
# Hinton et al. (2015) distil a model by training the student on the teacher's full probability distribution over
# possible outputs ("soft targets"), which carries more information than the single correct answer. A student that
# learns from a commercial chatbot through its interface sees only sampled text: the answer, sometimes the
# reasoning, and increasingly only a summary of the reasoning.
# Run from the repository root: python scripts/blog/2026-10-27-distill-signal.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
blue, pale = "#2a78d6", "#c9d9f0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

fig = plt.figure(figsize=(6.6, 7.4), facecolor=surf)
a = fig.add_axes([0.30, 0.60, 0.62, 0.28]); a.set_facecolor(surf)
words = ["Canberra", "Sydney", "Melbourne", "Perth", "Brisbane"]
p = [0.82, 0.12, 0.04, 0.01, 0.01]
a.barh(range(5), p, 0.62, color=[blue] + [pale] * 4)
for i, v in enumerate(p):
    a.text(v + 0.015, i, f"{v:.2f}", va="center", fontsize=10.5, color=ink)
a.set_yticks(range(5)); a.set_yticklabels(words, fontsize=11); a.invert_yaxis()
a.set_xlim(0, 1.0); a.set_xticks([]); a.tick_params(axis="y", length=0)
for sp in ("top", "right", "bottom"): a.spines[sp].set_visible(False)
fig.text(0.03, 0.915, "a  What the teacher knows (full distribution)", fontsize=11.5, color=ink)
fig.text(0.03, 0.885, "Prompt: \"The capital of Australia is …\"", fontsize=10, color=ink2, style="italic")
a.text(0.30, 2.6, "The small numbers carry information too:\nSydney is a far more plausible mistake\nthan Perth (\"dark knowledge\")", fontsize=9.5, color=ink2,
       va="center", linespacing=1.35)

b = fig.add_axes([0.03, 0.04, 0.94, 0.48]); b.axis("off"); b.set_xlim(0, 10); b.set_ylim(0, 10)
fig.text(0.03, 0.535, "b  What a student model gets to see (schematic)", fontsize=11.5, color=ink)
rows = [("Inside the lab", "All probabilities for every word", "most information", 1.0),
        ("Through a chat interface,\nreasoning visible", "Sampled answer + step-by-step\nreasoning text", "", 0.6),
        ("Through a chat interface,\nreasoning hidden", "Sampled answer only\n(or a summary of the reasoning)", "least information",
         0.3)]
for k, (who, what, note, frac) in enumerate(rows):
    y = 8.2 - k * 3.1
    b.add_patch(FancyBboxPatch((0.1, y - 1.1), 9.8, 2.2, boxstyle="round,pad=0.02,rounding_size=0.15", fc="#ffffff",
                               ec=grid, lw=1.2))
    b.text(0.4, y + 0.35, who, fontsize=10.5, color=ink, va="center", linespacing=1.25, fontweight="bold")
    b.text(0.4, y - 0.6, what, fontsize=10, color=ink2, va="center", linespacing=1.25)
    b.add_patch(plt.Rectangle((6.4, y - 0.3), 3.2, 0.6, fc=grid, ec="none"))
    b.add_patch(plt.Rectangle((6.4, y - 0.3), 3.2 * frac, 0.6, fc=blue, ec="none"))
    if note:
        b.text(8.0, y + 0.65, note, fontsize=9.5, color=ink2, ha="center", va="center")
fig.suptitle("What a student model can learn from", x=0.012, ha="left", color=ink, fontsize=12.5)
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-27-distill-signal.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-27-distill-signal.png")
