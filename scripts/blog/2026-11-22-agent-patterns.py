# Figure for the blog post "Building effective AI agents: start simple" (2026-11-22).
# Six patterns described in Anthropic's "Building effective agents" (Schluntz & Zhang, 2024),
# redrawn from scratch as simple box diagrams. Blue boxes are LLM calls, grey boxes are ordinary
# code, white boxes are inputs, outputs, people or the outside world. Drawn by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-11-22-agent-patterns.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
llm, code, io = "#d6e6f5", "#e8e6e1", "#ffffff"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def box(ax, x, y, text, fc, w=1.9, h=0.9):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                fc=fc, ec=ink2, lw=1.1, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=8.6, color=ink, zorder=3, linespacing=1.05)


def arrow(ax, a, b, rad=0.0, dashed=False, color=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=10, lw=1.1, color=color or ink2,
                                 connectionstyle=f"arc3,rad={rad}", ls="--" if dashed else "-", zorder=1,
                                 shrinkA=2, shrinkB=2))


fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.6), facecolor=surf)
for ax in axes.flat:
    ax.set_facecolor(surf); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    ax.add_patch(plt.Rectangle((0.05, 0.05), 9.9, 5.9, fc="none", ec=grid, lw=1))

# (a) prompt chaining
a = axes[0, 0]
a.set_title("(a) Prompt chaining", loc="left", fontsize=10.5, color=ink)
ys = 3.4
box(a, 1.1, ys, "In", io, w=1.2); box(a, 3.2, ys, "LLM\nstep 1", llm, w=1.6)
box(a, 5.3, ys, "Check\n(gate)", code, w=1.6); box(a, 7.4, ys, "LLM\nstep 2", llm, w=1.6)
box(a, 9.0, ys, "Out", io, w=1.0)
for p, q in [(1.7, 2.4), (4.0, 4.5), (6.1, 6.6), (8.2, 8.5)]: arrow(a, (p, ys), (q, ys))
box(a, 5.3, 1.4, "Stop or\nretry", io, w=1.6); arrow(a, (5.3, ys - 0.45), (5.3, 1.85))
a.text(5.45, 2.35, "fail", fontsize=8, color=ink2)
a.text(0.4, 5.2, "Fixed sequence of easier steps", fontsize=8.6, color=ink2)

# (b) routing
b = axes[0, 1]
b.set_title("(b) Routing", loc="left", fontsize=10.5, color=ink)
box(b, 1.0, 3.0, "In", io, w=1.1); box(b, 3.1, 3.0, "LLM\nrouter", llm, w=1.6)
for y, t in [(4.5, "Handler A"), (3.0, "Handler B"), (1.5, "Handler C")]:
    box(b, 6.0, y, t, llm, w=2.0); arrow(b, (3.9, 3.0), (5.0, y)); arrow(b, (7.0, y), (8.4, 3.0))
box(b, 9.0, 3.0, "Out", io, w=1.0); arrow(b, (1.55, 3.0), (2.3, 3.0))
b.text(0.4, 5.2, "Classify, then send to a specialist", fontsize=8.6, color=ink2)

# (c) parallelization
c = axes[0, 2]
c.set_title("(c) Parallelization", loc="left", fontsize=10.5, color=ink)
box(c, 1.0, 3.0, "In", io, w=1.1)
for y in (4.4, 3.0, 1.6):
    box(c, 3.7, y, "LLM", llm, w=1.5); arrow(c, (1.55, 3.0), (2.95, y)); arrow(c, (4.45, y), (5.6, 3.0))
box(c, 6.5, 3.0, "Combine\n(code)", code, w=1.7); box(c, 9.0, 3.0, "Out", io, w=1.0)
arrow(c, (7.35, 3.0), (8.5, 3.0))
c.text(0.4, 5.2, "Split into parts, or ask several times", fontsize=8.6, color=ink2)
c.text(0.4, 0.45, "sectioning: different parts   voting: same task", fontsize=7.8, color=ink2)

# (d) orchestrator-workers
d = axes[1, 0]
d.set_title("(d) Orchestrator-workers", loc="left", fontsize=10.5, color=ink)
box(d, 0.85, 3.0, "In", io, w=0.9); box(d, 2.75, 3.0, "LLM\norchestrator", llm, w=2.2)
for y in (4.4, 3.0, 1.6):
    box(d, 5.6, y, "Worker", llm, w=1.4); arrow(d, (3.85, 3.0), (4.9, y)); arrow(d, (6.3, y), (6.95, 3.0))
d.text(5.6, 0.4, "number of workers decided on the fly", ha="center", fontsize=7.8, color=ink2)
box(d, 7.95, 3.0, "LLM\nsynthesizer", llm, w=2.0); arrow(d, (1.3, 3.0), (1.65, 3.0))
box(d, 9.4, 4.8, "Out", io, w=0.9); arrow(d, (7.9, 3.45), (9.2, 4.35))
d.text(0.4, 5.2, "A planner splits work it cannot foresee", fontsize=8.6, color=ink2)

# (e) evaluator-optimizer
e = axes[1, 1]
e.set_title("(e) Evaluator-optimizer", loc="left", fontsize=10.5, color=ink)
box(e, 1.0, 3.0, "In", io, w=1.1); box(e, 3.6, 3.0, "LLM\ngenerator", llm, w=1.8)
box(e, 7.0, 3.0, "LLM\nevaluator", llm, w=1.8); arrow(e, (1.55, 3.0), (2.7, 3.0))
arrow(e, (4.5, 3.3), (6.1, 3.3), rad=-0.35); arrow(e, (6.1, 2.7), (4.5, 2.7), rad=-0.35)
e.text(5.3, 4.15, "draft", ha="center", fontsize=8, color=ink2)
e.text(5.3, 1.65, "feedback", ha="center", fontsize=8, color=ink2)
box(e, 9.1, 4.8, "Out", io, w=1.0); arrow(e, (7.6, 3.45), (8.7, 4.35))
e.text(8.45, 3.55, "pass", fontsize=7.8, color=ink2, ha="left")
e.text(0.4, 5.2, "Write, critique, revise", fontsize=8.6, color=ink2)

# (f) agent
f = axes[1, 2]
f.set_title("(f) Agent", loc="left", fontsize=10.5, color=ink)
box(f, 1.3, 3.0, "Person", io, w=1.6); box(f, 5.0, 3.0, "LLM", llm, w=1.6)
box(f, 8.55, 3.0, "Tools and\nenvironment", io, w=2.5)
arrow(f, (2.1, 3.25), (4.2, 3.25)); arrow(f, (4.2, 2.75), (2.1, 2.75))
f.text(3.15, 3.45, "task", ha="center", fontsize=8, color=ink2)
f.text(3.15, 2.25, "questions,\nresult", ha="center", fontsize=7.8, color=ink2)
arrow(f, (5.6, 3.35), (7.3, 3.35), rad=-0.35); arrow(f, (7.3, 2.65), (5.6, 2.65), rad=-0.35)
f.text(6.6, 4.25, "action", ha="center", fontsize=8, color=ink2)
f.text(6.6, 1.5, "feedback\n(ground truth)", ha="center", fontsize=7.8, color=ink2)
box(f, 5.0, 0.9, "Stop: done or\nstep limit", code, w=2.5); arrow(f, (5.0, 2.55), (5.0, 1.35))
f.text(0.4, 5.2, "The model decides its own next step", fontsize=8.6, color=ink2)

fig.suptitle("Six building patterns, from fixed workflows (a–e) to an autonomous agent (f)",
             x=0.012, ha="left", color=ink, fontsize=12.5)
fig.text(0.012, 0.925, "blue: LLM call   grey: ordinary code   white: input, output, person or outside world",
         fontsize=9, color=ink2)
fig.tight_layout(rect=(0, 0, 1, 0.93))
os.makedirs("assets/img/blog", exist_ok=True)
out = "assets/img/blog/2026-11-22-agent-patterns.png"
fig.savefig(out, dpi=170, facecolor=surf)
print("saved", out)
