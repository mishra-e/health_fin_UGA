import matplotlib.pyplot as plt
import numpy as np

# 1. Styling & Font
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'figure.figsize': (14, 11)
})

# 2. Data
years = np.array([2026, 2027, 2028, 2029, 2030])

us_spending = np.array([566.7, 453.3, 340.0, 226.7, 113.3])
uganda_base = np.array([38, 76, 114, 152, 190])
addition_millions = 881.318558
uganda_spending = uganda_base + addition_millions

total_spending = us_spending + uganda_spending

# 3. Create Plot
fig, ax = plt.subplots()

bar_width = 0.65

# Stacked bars
ax.bar(
    years,
    us_spending,
    width=bar_width,
    label="United States",
    color='purple'
)

ax.bar(
    years,
    uganda_spending,
    width=bar_width,
    bottom=us_spending,
    label="Uganda",
    color='#FFD700'
)

# 4. Numerical Labels
for i, year in enumerate(years):
    # US label (centered in US bar)
    ax.text(
        year,
        us_spending[i] / 2,
        f'${us_spending[i]:,.1f}',
        ha='center',
        va='center',
        fontsize=13,
        fontweight='bold',
        color='white'
    )

    # Uganda label (centered in Uganda stack)
    ax.text(
        year,
        us_spending[i] + uganda_spending[i] / 2,
        f'${uganda_spending[i]:,.1f}',
        ha='center',
        va='center',
        fontsize=13,
        fontweight='bold',
        color='#5A4A00'
    )

    # Total label (above bar)
    ax.text(
        year,
        total_spending[i] + 40,
        f'${total_spending[i]:,.1f}',
        ha='center',
        fontsize=14,
        fontweight='bold'
    )

# 5. Titles and Axes
ax.set_xlabel("Year", fontsize=18, labelpad=15)
ax.set_ylabel("Spending (USD millions)", fontsize=18, labelpad=15)

ax.set_title(
    "US–Uganda Health Financing Commitments (2026–2030)",
    fontsize=24,
    pad=25,
    fontweight='bold'
)

ax.tick_params(axis='both', labelsize=14)
ax.set_xticks(years)
ax.set_ylim(0, max(total_spending) + 250)

# 6. Legend
ax.legend(
    loc='upper right',
    bbox_to_anchor=(1.02, 1),
    fontsize=14,
    frameon=True
)

# Layout
plt.subplots_adjust(bottom=0.22, top=0.88, left=0.12, right=0.90)

# Save
plt.savefig('US_Uganda_Financing_Stacked.png', dpi=700, bbox_inches='tight')
plt.show()
