# Figure for the blog post "How the brain invented learning, part III: simulating in A Brief History of Intelligence"
# (2026-11-03). Simulation by Daeha Kim of tabular Dyna-Q (Sutton 1990) on the 6 x 9 "Dyna maze" of Sutton & Barto
# (2018, section 8.2): start at row 2, column 0; goal at row 0, column 8 (reward +1, all other steps 0); walls at
# (1,2), (2,2), (3,2), (4,5), (0,7), (1,7), (2,7). Step size 0.1, discount 0.95, epsilon-greedy with epsilon 0.1.
# After every real step the agent replays n imagined steps drawn from its learned model of the maze
# (n = 0 is plain model-free Q-learning). Steps per episode averaged over 30 runs of 50 episodes.
# Run from the repository root: python scripts/blog/2026-11-03-dyna-maze.py
import os, random, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

ROWS, COLS = 6, 9
START, GOAL = (2, 0), (0, 8)
WALLS = {(1, 2), (2, 2), (3, 2), (4, 5), (0, 7), (1, 7), (2, 7)}
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def step(s, a):
    r, c = s[0] + MOVES[a][0], s[1] + MOVES[a][1]
    if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in WALLS:
        r, c = s
    return (r, c), (1.0 if (r, c) == GOAL else 0.0)

def greedy(Q, s, rng):
    q = Q[s]; best = max(q)
    return rng.choice([a for a in range(4) if q[a] == best])

def run(n, episodes, seed, alpha=0.1, gamma=0.95, eps=0.1):
    rng = random.Random(seed)
    Q = {(r, c): [0.0] * 4 for r in range(ROWS) for c in range(COLS)}
    model, steps = {}, []
    for _ in range(episodes):
        s, k = START, 0
        while s != GOAL:
            a = rng.randrange(4) if rng.random() < eps else greedy(Q, s, rng)
            s2, rew = step(s, a)
            Q[s][a] += alpha * (rew + gamma * max(Q[s2]) * (s2 != GOAL) - Q[s][a])
            model[(s, a)] = (s2, rew)
            keys = list(model)
            for _ in range(n):                      # imagined experience from the learned model
                ps, pa = keys[rng.randrange(len(keys))]
                ps2, pr = model[(ps, pa)]
                Q[ps][pa] += alpha * (pr + gamma * max(Q[ps2]) * (ps2 != GOAL) - Q[ps][pa])
            s, k = s2, k + 1
        steps.append(k)
    return steps

E, R = 50, 30
curves = {n: np.mean([run(n, E, seed) for seed in range(R)], axis=0) for n in (0, 5, 50)}
fig, ax = plt.subplots(figsize=(6.6, 4.8), facecolor=surf); ax.set_facecolor(surf)
cols = {0: "#8a8780", 5: "#d9a37f", 50: "#2a78d6"}
labs = {0: "No imagination (model-free Q-learning)", 5: "5 imagined steps per real step",
        50: "50 imagined steps per real step"}
ep = np.arange(1, E + 1)
for n in (0, 5, 50):
    ax.plot(ep[1:], curves[n][1:], color=cols[n], lw=2.4, label=labs[n])
ax.axhline(14, color=ink2, lw=1, ls=(0, (4, 3)))
ax.text(50, 24, "shortest path: 14 steps", ha="right", va="bottom", fontsize=9.5, color=ink2)
ax.set_xlim(2, 50); ax.set_ylim(0, 1200)
ax.set_xlabel("Episode (trip from start to goal)", color=ink2, fontsize=11)
ax.set_ylabel("Steps needed to reach the goal", color=ink2, fontsize=11)
ax.legend(loc="upper right", frameon=False, fontsize=10)
ax.grid(color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.suptitle("Imagined experience speeds up learning", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-03-dyna-maze.png", dpi=170, facecolor=surf)
for n in (0, 5, 50):
    print(n, "episode 2:", round(curves[n][1]), "episode 5:", round(curves[n][4]), "episode 10:", round(curves[n][9]),
          "first episode within 20 steps:", int(np.argmax(curves[n] < 20)) + 1)
print("saved assets/img/blog/2026-11-03-dyna-maze.png")
