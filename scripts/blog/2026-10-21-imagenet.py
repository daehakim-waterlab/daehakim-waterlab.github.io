# Figure for the blog post "A short history of AI, part 2: data, GPUs and deep learning (1997-2017)" (2026-10-21).
# Top-5 classification error of the winning entry in the ImageNet Large Scale Visual Recognition Challenge:
#   2010 NEC 28.2, 2011 XRCE 25.8, 2012 SuperVision (AlexNet) 16.4, 2013 Clarifai 11.7, 2014 GoogLeNet 6.7
#     (Russakovsky et al. 2015, IJCV 115, 211-252, Tables 5-7);
#   2015 ResNet 3.57 (He et al. 2016, CVPR); 2016 winning entry 2.991 and 2017 SENet 2.251 (Hu et al. 2018, CVPR).
# Estimated human error 5.1% (one trained annotator, 1,500 test images; a second annotator scored 12.0%),
# Russakovsky et al. (2015), Table 9. Plotted by Daeha Kim.
# Run from the repository root: python scripts/blog/2026-10-21-imagenet.py
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ink, ink2, grid, surf = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
old, deep, human = "#a8a6a0", "#2a78d6", "#d6604d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.edgecolor": ink2,
                     "xtick.color": ink2, "ytick.color": ink2})

data = [  # year, error %, entry, deep CNN?
    (2010, 28.2, "NEC", False), (2011, 25.8, "XRCE", False), (2012, 16.4, "AlexNet", True),
    (2013, 11.7, "Clarifai", True), (2014, 6.7, "GoogLeNet", True), (2015, 3.57, "ResNet", True),
    (2016, 2.991, "", True), (2017, 2.251, "SENet", True),
]
fig, ax = plt.subplots(figsize=(8.6, 5.6), facecolor=surf); ax.set_facecolor(surf)
for y, e, name, d in data:
    ax.bar(y, e, 0.66, color=deep if d else old)
    ax.text(y, e + 0.6, f"{e:g}%", ha="center", va="bottom", fontsize=11, color=ink)
ax.axhline(5.1, color=human, lw=1.6, ls=(0, (5, 3)))
ax.text(2016.5, 5.6, "one trained human: 5.1%", ha="center", va="bottom", fontsize=10.5, color=human)
ax.set_xticks([d[0] for d in data]); ax.set_xticklabels([f"{d[0]}\n{d[2]}" if d[2] else str(d[0]) for d in data], fontsize=10.5)
ax.tick_params(axis="x", length=0)
ax.set_ylim(0, 32)
ax.set_ylabel("Top-5 error of the winning entry (%)", color=ink2)
ax.grid(axis="y", color=grid, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=old, label="Hand-designed features"), Patch(color=deep, label="Deep convolutional networks")],
          loc="upper right", frameon=False, fontsize=10.5)
fig.suptitle("ImageNet: the year deep learning took over", x=0.012, ha="left", color=ink, fontsize=12.5)
fig.tight_layout()
os.makedirs("assets/img/blog", exist_ok=True)
fig.savefig("assets/img/blog/2026-10-21-imagenet.png", dpi=170, facecolor=surf)
print("saved assets/img/blog/2026-10-21-imagenet.png")
