import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 100 random integers
np.random.seed(42)  # For reproducibility
data = np.random.randint(0, 100, size=100)

# Step 2: Calculate mean and median
mean_value = np.mean(data)
median_value = np.median(data)

# Step 3: Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Subplot 1: Show mean as minimizer of Σ (x - xi)²
x_values = np.linspace(0, 100, 400)
squared_diffs = np.sum((data[:, np.newaxis] - x_values) ** 2, axis=0)

axs[0].plot(x_values, squared_diffs, label='Σ (x - xi)²', color='blue')
axs[0].axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
axs[0].set_title('Mean Minimizes Σ (x - xi)²')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Sum of Squared Differences')
axs[0].legend()

# Subplot 2: Show median as minimizer of Σ |x - xi|
absolute_diffs = np.sum(np.abs(data[:, np.newaxis] - x_values), axis=0)

axs[1].plot(x_values, absolute_diffs, label='Σ |x - xi|', color='green')
axs[1].axvline(median_value, color='orange', linestyle='--', label=f'Median: {median_value:.2f}')
axs[1].set_title('Median Minimizes Σ |x - xi|')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Sum of Absolute Differences')
axs[1].legend()

# Adjust layout
plt.tight_layout()
plt.show()
