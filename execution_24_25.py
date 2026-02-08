import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Arial"


# Data
categories = [
    "KIDPII",
    "Spanish Debt\nSwap",
    "Global Fund",
    "GAVI",
    "UCREPP",
    "Total Projects"
]

percent_release = [100, 100, 100, 100, 100, 100]
percent_spent = [96.6, 81.0, 55.8, 32.8, 84.0, 58.0]

# Positions
x = np.arange(len(categories))
width = 0.35

# IGC colours (approximate)
igc_purple = "#5B2C83"
igc_yellow = "#F2C300"

# Figure
fig, ax = plt.subplots(figsize=(12, 4))

bars1 = ax.bar(
    x - width/2,
    percent_release,
    width,
    label="% Released",
    color=igc_purple
)

bars2 = ax.bar(
    x + width/2,
    percent_spent,
    width,
    label="% of Release Spent",
    color=igc_yellow
)

# Title (bold, larger)
ax.set_title(
    "Budget Performance for Externally Financed Health Projects\n"
    "FY 2024/25 Uganda Budget",
    fontsize=14,
    fontweight="bold",
    pad=18
)

# Axis labels
ax.set_ylabel("Percentage", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.set_ylim(0, 110)

# Legend positioned next to title (top right)
ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.01, 1.15),
    frameon=False
)

# Annotate bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{height:.1f}%" if height != 100 else "100%",
            ha="center",
            va="bottom",
            fontsize=9
        )

plt.tight_layout()
plt.show()
