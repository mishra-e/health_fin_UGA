import matplotlib.pyplot as plt
import numpy as np
## Extract numbers from 24-25 AHS Report
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
plt.figure(figsize=(12, 4))

bars1 = plt.bar(
    x - width/2,
    percent_release,
    width,
    label="% Released",
    color=igc_purple
)

bars2 = plt.bar(
    x + width/2,
    percent_spent,
    width,
    label="% of Release Spent",
    color=igc_yellow
)

# Title and labels
plt.title(
    "Budget Performance for Externally Financed Health Projects\n"
    "FY 2024/25 Uganda Budget",
    fontsize=12,
    fontweight='bold'
)
plt.ylabel("Percentage", fontsize=12)
plt.xticks(x, categories, fontsize=10)
plt.ylim(0, 110)

# Legend outside plot
plt.legend(
    loc="upper right",
    bbox_to_anchor=(1.02, 0.5),
    frameon=False
)

# Annotate bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{height:.1f}%" if height != 100 else "100%",
            ha="center",
            va="bottom",
            fontsize=9
        )

plt.tight_layout()
plt.show()
