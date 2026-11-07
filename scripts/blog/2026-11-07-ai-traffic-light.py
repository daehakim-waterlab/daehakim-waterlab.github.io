# Figure for the blog post "Green, amber, red: how geoscientists should use AI in research and publishing" (2026-11-07).
# Schematic by Daeha Kim of the three risk levels in the Springer Nature risk-assessment framework for AI use
# (Springer Nature journal policies on artificial intelligence, 2026), which Nature Geoscience adopted in its
# editorial "Responsible use of artificial intelligence" (Nature Geoscience 19, 1257, 2026,
# https://doi.org/10.1038/s41561-026-02149-0). The examples are paraphrased and shortened from the policy.
# Run from the repository root: python scripts/blog/2026-11-07-ai-traffic-light.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})

tiers = [
    ("#2e8b57", "#eaf5ee", "Green: permitted", "Assistive use. AI helps with expression or efficiency\nbut adds no new ideas.",
     ["Polishing language, suggesting structure", "Translating or clarifying review comments",
      "Cleaning and deduplicating data", "Comparing methods, stress-testing questions"],
     "Disclosure encouraged"),
    ("#d08a1c", "#fbf2e2", "Amber: use with care", "Evaluative use. AI adds content that can shape\ninterpretation, so a human must check it.",
     ["Suggesting methods or statistical tests", "Drafting summaries, heavy writing support",
      "Comparing results with the literature", "Spotting patterns, explaining model output"],
     "Verify, keep human control, disclose"),
    ("#c0392b", "#f9e7e5", "Red: not permitted", "AI replaces human judgment, cannot be verified\nor breaks confidentiality.",
     ["AI conclusions presented as your own", "Fabricated data, citations or results",
      "AI as an author; peer review done by an LLM", "Photorealistic fake images"],
     "Not allowed"),
]

fig, ax = plt.subplots(figsize=(6.6, 8.2), facecolor=surf)
ax.set_xlim(0, 10); ax.set_ylim(0.0, 12.2); ax.axis("off")
h, gap, top = 3.75, 0.3, 12.0
for i, (c, fill, head, summ, ex, rule) in enumerate(tiers):
    y0 = top - (i + 1) * h - i * gap
    ax.add_patch(FancyBboxPatch((0.15, y0), 9.7, h, boxstyle="round,pad=0.02,rounding_size=0.18", fc=fill, ec=c, lw=1.6))
    ax.plot(0.85, y0 + h - 0.6, "o", ms=17, color=c)
    ax.text(1.4, y0 + h - 0.6, head, va="center", fontsize=12, color=c, fontweight="bold")
    ax.text(0.55, y0 + h - 1.4, summ, va="center", fontsize=9.6, color=ink, linespacing=1.3)
    for j, e in enumerate(ex):
        ax.text(0.75, y0 + h - 2.15 - j * 0.39, "•  " + e, va="center", fontsize=9.6, color=ink)
    ax.text(9.6, y0 + h - 0.6, rule, va="center", ha="right", fontsize=9.2, color=ink2, style="italic")
fig.suptitle("One framework for authors, reviewers and editors", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-11-07-ai-traffic-light.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-11-07-ai-traffic-light.png")
