# Figure for the blog post "Why LLMs make things up, and what you can do about it" (2026-10-24).
# AA-Omniscience (Artificial Analysis): hard factual questions answered without web access. For each model,
# accuracy (% correct) and the Omniscience Index (% correct minus % incorrect) give % incorrect = accuracy - index;
# the remainder answered "I don't know" (or gave partial answers). Values as compiled by Suprmind from Artificial
# Analysis model records, snapshot read 4 October 2026 (https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/);
# the top three Index values match artificialanalysis.ai/evaluations/omniscience.
#   model, accuracy, index
#   Gemini 4 Argon (high, not yet public) 49.9, 42.4;  Claude Opus 5.5 (max) 66.2, 46.4;  GPT-6 Astra (max) 62.6, 43.4;
#   Grok 4.7 (xhigh) 47.4, 32.0;  Gemini 3.1 Pro 54.9, 31.9;  Kimi K3 (max) 47.6, 19.7;  DeepSeek V4 Pro 0813 49.1, 0.8;
#   late-2025 models: Claude Opus 4.5 46.6, 14.0;  Gemini 3 Pro 55.8, 15.3.
# Plotted by Daeha Kim. Run from the repository root: python scripts/blog/2026-10-24-hallucination-answers.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
ok, bad, idk = "#2a78d6", "#d6604d", "#d8d6d0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

models = [("Gemini 4 Argon", 49.9, 42.4), ("Claude Opus 5.5", 66.2, 46.4), ("GPT-6 Astra", 62.6, 43.4),
          ("Grok 4.7", 47.4, 32.0), ("Gemini 3.1 Pro", 54.9, 31.9), ("Kimi K3", 47.6, 19.7),
          ("DeepSeek V4 Pro", 49.1, 0.8), (None, 0, 0),
          ("Claude Opus 4.5\n(Nov 2025)", 46.6, 14.0), ("Gemini 3 Pro\n(Nov 2025)", 55.8, 15.3)]
fig, ax = plt.subplots(figsize=(6.6, 6.6), facecolor=surf); ax.set_facecolor(surf)
labels = []
for i, (name, acc, idx) in enumerate(models):
    labels.append(name or "")
    if name is None:
        continue
    wrong = acc - idx
    rest = 100 - acc - wrong
    ax.barh(i, acc, 0.66, color=ok)
    ax.barh(i, wrong, 0.66, left=acc, color=bad)
    ax.barh(i, rest, 0.66, left=acc + wrong, color=idk)
    ax.text(acc / 2, i, f"{acc:.0f}", ha="center", va="center", fontsize=10, color="#ffffff")
    ax.text(acc + wrong / 2, i, f"{wrong:.0f}", ha="center", va="center", fontsize=10, color="#ffffff")
    if rest >= 6:
        ax.text(acc + wrong + rest / 2, i, f"{rest:.0f}", ha="center", va="center", fontsize=10, color=ink)
ax.text(0, 7.05, "Models from a year earlier", fontsize=10.5, color=ink2, va="center")
ax.set_yticks(range(len(models))); ax.set_yticklabels(labels, fontsize=10.5); ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Out of 100 hard factual questions (no web search)", color=ink2, fontsize=11)
ax.tick_params(axis="y", length=0)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=ok, label="Correct"), Patch(color=bad, label="Wrong (hallucinated)"),
                   Patch(color=idk, label="Declined or partial")], loc="lower center", bbox_to_anchor=(0.42, 1.0),
          ncol=3, frameon=False, fontsize=10, handlelength=1.2, columnspacing=1.0)
fig.suptitle("The best models now know when to say \"I don't know\"", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-24-hallucination-answers.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-24-hallucination-answers.png")
