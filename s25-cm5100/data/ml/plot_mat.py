import matplotlib as mpl
import matplotlib.pyplot as plt

# ===============================
# Font
# ===============================
mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["font.sans-serif"] = [
    "Arial",
    "Helvetica",
    "DejaVu Sans",
    "Bitstream Vera Sans",
    "sans-serif",
]
mpl.rcParams["font.size"] = 12

# ===============================
# Axes
# ===============================
mpl.rcParams["axes.labelsize"] = 12
mpl.rcParams["axes.titlesize"] = 14
mpl.rcParams["axes.linewidth"] = 0.8
mpl.rcParams["axes.edgecolor"] = "black"
mpl.rcParams["axes.spines.top"] = True
mpl.rcParams["axes.spines.right"] = True
mpl.rcParams["axes.grid"] = False

# ===============================
# Lines and markers
# ===============================
mpl.rcParams["lines.linewidth"] = 1.2
mpl.rcParams["lines.markersize"] = 4

# ===============================
# Ticks
# ===============================
mpl.rcParams["xtick.direction"] = "out"
mpl.rcParams["ytick.direction"] = "out"
mpl.rcParams["xtick.major.size"] = 3
mpl.rcParams["ytick.major.size"] = 3
mpl.rcParams["xtick.major.width"] = 0.8
mpl.rcParams["ytick.major.width"] = 0.8
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12

# ===============================
# Legend
# ===============================
mpl.rcParams["legend.fontsize"] = 12
mpl.rcParams["legend.frameon"] = False

# ===============================
# Figure
# ===============================
mpl.rcParams["figure.dpi"] = 300
mpl.rcParams["savefig.dpi"] = 600
mpl.rcParams["figure.figsize"] = [3.5, 2.5]  # single column JACS figure
mpl.rcParams["figure.facecolor"] = "white"

# ===============================
# Savefig
# ===============================
mpl.rcParams["savefig.transparent"] = False
mpl.rcParams["savefig.bbox"] = "tight"
mpl.rcParams["savefig.pad_inches"] = 0.05

# Optional: Example plot to test
if __name__ == "__main__":
    import numpy as np

    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label="sin(x)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Test Figure")
    plt.legend()
    plt.tight_layout()
    plt.show()
