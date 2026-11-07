# Figure for the blog post "How the brain invented learning, part VI: the future of intelligence" (2026-11-08).
# Schematic by Daeha Kim (an interpretation, not a claim of the book): evolution acquired Bennett's (2023) five
# breakthroughs in the order 1 to 5 over about 600 million years; AI systems have been acquiring rough counterparts
# of them in a different order, starting with language, within about a decade. Example systems and years:
#   speaking: GPT-3 (2020) and ChatGPT (2022); steering by good and bad: reinforcement learning from human feedback
#   (InstructGPT, 2022); mentalizing: language models passing false-belief tests (GPT-4, 2023; Kosinski 2024);
#   reinforcing: reasoning models trained with reinforcement learning (OpenAI o1, 2024; DeepSeek-R1, 2025);
#   simulating: interactive world models (Genie 3, 2025).
# Run from the repository root: python scripts/blog/2026-11-08-ai-reverse-order.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
col = {"1": "#8a8780", "2": "#6f8fb8", "3": "#2a78d6", "4": "#7a5195", "5": "#b4532a"}

evo = [("1", "Steering", "600 Ma"), ("2", "Reinforcing", "500 Ma"), ("3", "Simulating", "150 Ma"),
       ("4", "Mentalizing", "65 Ma"), ("5", "Speaking", "2.5 Ma")]
ai = [("5", "Speaking", "GPT-3, ChatGPT", "2020–22"), ("1", "Steering", "Learning from human\nfeedback", "2022"),
      ("4", "Mentalizing", "False-belief tests", "2023"), ("2", "Reinforcing", "Reasoning via RL", "2024–25"),
      ("3", "Simulating", "World models", "2025–")]

fig, ax = plt.subplots(figsize=(6.6, 7.2), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0, 11.6); ax.axis("off")
ax.text(2.3, 11.05, "Evolution", ha="center", fontsize=11.5, color=ink, fontweight="bold")
ax.text(2.3, 10.6, "about 600 million years", ha="center", fontsize=9.6, color=ink2)
ax.text(7.35, 11.05, "AI", ha="center", fontsize=11.5, color=ink, fontweight="bold")
ax.text(7.35, 10.6, "about ten years", ha="center", fontsize=9.6, color=ink2)
for i, (n, name, t) in enumerate(evo):
    y = 9.3 - i * 2.0
    c = col[n]
    ax.add_patch(FancyBboxPatch((0.25, y - 0.62), 4.1, 1.24, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="#ffffff", ec=c, lw=1.6))
    ax.text(0.7, y, n, ha="center", va="center", fontsize=17, color=c, fontweight="bold")
    ax.text(1.2, y + 0.2, name, va="center", fontsize=10.8, color=c, fontweight="bold")
    ax.text(1.2, y - 0.27, t, va="center", fontsize=9.4, color=ink2)
    if i < 4:
        ax.add_patch(FancyArrowPatch((2.3, y - 0.66), (2.3, y - 1.34), arrowstyle="-|>", mutation_scale=12,
                                     color=ink2, lw=1.2))
for i, (n, name, ex, t) in enumerate(ai):
    y = 9.3 - i * 2.0
    c = col[n]
    ax.add_patch(FancyBboxPatch((5.15, y - 0.62), 4.6, 1.24, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="#ffffff", ec=c, lw=1.6))
    ax.text(5.6, y, n, ha="center", va="center", fontsize=17, color=c, fontweight="bold")
    ax.text(6.1, y + 0.3, name, va="center", fontsize=10.8, color=c, fontweight="bold")
    ax.text(9.6, y + 0.3, t, va="center", ha="right", fontsize=9.2, color=ink2)
    ax.text(6.1, y - 0.25, ex, va="center", fontsize=9.2, color=ink, linespacing=1.15)
    if i < 4:
        ax.add_patch(FancyArrowPatch((7.45, y - 0.66), (7.45, y - 1.34), arrowstyle="-|>", mutation_scale=12,
                                     color=ink2, lw=1.2))
fig.suptitle("AI is gathering the same pieces in a different order", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-08-ai-reverse-order.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-08-ai-reverse-order.png")
