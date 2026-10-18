# Figure for the blog post "From chatbot to coworker" (2026-10-18). Original schematic by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-18-llm-roles.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, surf = "#0b0b0b", "#52514e", "#fcfcfb"
C = {"human": ("#ecebe7", "#52514e"), "llm": ("#dbe8f8", "#2a78d6"), "code": ("#fde3d6", "#eb6834")}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
fig, ax = plt.subplots(figsize=(12, 6.2), facecolor=surf)
ax.set_xlim(0, 12.2); ax.set_ylim(0, 6.2); ax.axis("off")

def box(x, y, w, h, text, kind, bold=False):
    fc, ec = C[kind]
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.6))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=9.3, color=ink,
            fontweight="bold" if bold else "normal", wrap=True)

def arrow(x1, y1, x2, y2, rad=0.0, color=ink2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12,
                                 lw=1.3, color=color, connectionstyle=f"arc3,rad={rad}"))

cols = [
  (0.3, "2023 · Chatbot", "Foroumandi et al. (2023), WRR",
   [("You ask a question\nor paste an error", "human"), ("LLM writes text\nor a code snippet", "llm"),
    ("You run, debug and\nfact-check everything", "human")],
   "LLM as writer", "Fake citations; answers flip\nwhen challenged"),
  (4.25, "2025 · LLM in the loop", "Zhu et al. (2026), GRL",
   [("You build the loop,\nprompt and model", "human"), ("LLM proposes\nnext parameters", "llm"),
    ("VIC model runs;\nNSE computed", "code")],
   "LLM as decision-maker", "1 of 5 LLMs matched\nSCE-UA, in fewer runs"),
  (8.2, "2026 · Agentic workflow", "Li et al. (2026), J. Hydrol.",
   [("You write the expert\nworkflow and tools", "human"), ("Agents plan, write code,\nrun, debug, evaluate", "llm"),
    ("LSTMs trained on\n531 CAMELS basins", "code")],
   "LLM as orchestrator", "92.8% task success;\n0% without the workflow"),
]
for x0, title, src, steps, role, note in cols:
    ax.text(x0, 5.95, title, fontsize=12.5, color=ink, fontweight="bold", va="top")
    ax.text(x0, 5.55, src, fontsize=9, color=ink2, va="top", style="italic")
    w, h = 3.3, 0.78
    ys = [4.25, 2.95, 1.65]
    for (t, k), y in zip(steps, ys):
        box(x0, y, w, h, t, k)
    arrow(x0 + w/2, ys[0], x0 + w/2, ys[1] + h)
    arrow(x0 + w/2, ys[1], x0 + w/2, ys[2] + h)
    lc = C["code"][1] if x0 > 1 else C["human"][1]
    lab = "feedback" if x0 > 1 else "you iterate"
    arrow(x0 + w + 0.02, ys[2] + h/2, x0 + w + 0.02, ys[1] + h/2, rad=0.45, color=lc)
    ax.text(x0 + w + 0.42, (ys[1] + ys[2]) / 2 + h/2, lab, fontsize=7.5, color=lc, rotation=90, va="center", ha="left")
    ax.text(x0, 1.15, role, fontsize=10.5, color=ink, fontweight="bold", va="top")
    ax.text(x0, 0.78, note, fontsize=9, color=ink2, va="top")

# legend
lx = 0.3
for k, lab in [("human", "Human"), ("llm", "LLM"), ("code", "Code / model")]:
    fc, ec = C[k]
    ax.add_patch(FancyBboxPatch((lx, 0.02), 0.32, 0.2, boxstyle="round,pad=0.01,rounding_size=0.05", fc=fc, ec=ec, lw=1.4))
    ax.text(lx + 0.42, 0.12, lab, va="center", fontsize=9, color=ink2); lx += 1.9
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-18-llm-roles.png", dpi=170, facecolor=surf, bbox_inches="tight")
