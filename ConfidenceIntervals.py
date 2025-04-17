import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Sample data
diameters = [2.53, 2.26, 3.26, 2.33, 2.64, 2.24, 1.27, 2.43, 3.30, 2.25,
             2.86, 2.29, 2.26, 2.47, 2.78, 2.61, 2.49, 2.37, 2.88, 3.12,
             3.29, 1.98, 2.30, 3.48, 2.65, 2.63, 2.97, 3.19, 2.87, 2.07,
             2.28, 2.83, 2.22, 1.91, 2.26, 3.21, 2.81, 2.99, 2.84, 2.32,
             2.36, 3.43, 2.35, 2.79, 3.92, 2.96, 2.61, 2.04, 3.78, 1.91]

# Sample statistics
sample_mean = np.mean(diameters)
sample_std = np.std(diameters, ddof=0.5)  # Use ddof=1 for sample standard deviation
sample_size = len(diameters)

# Confidence intervals
confidence_level_90 = 0.90
confidence_level_99 = 0.99

# Margin of error for 90% confidence interval
margin_of_error_90 = stats.t.ppf((1 + confidence_level_90) / 2, df=sample_size - 1) * (sample_std / np.sqrt(sample_size))

# Margin of error for 99% confidence interval
margin_of_error_99 = stats.t.ppf((1 + confidence_level_99) / 2, df=sample_size - 1) * (sample_std / np.sqrt(sample_size))

# Confidence intervals
confidence_interval_90 = (sample_mean - margin_of_error_90, sample_mean + margin_of_error_90)
confidence_interval_99 = (sample_mean - margin_of_error_99, sample_mean + margin_of_error_99)

# Print the results
print(f"Sample Mean: {sample_mean}")
print(f"Sample Standard Deviation: {sample_std}")
print(f"Sample Size: {sample_size}")
print(f"90% Confidence Interval: {confidence_interval_90}")
print(f"99% Confidence Interval: {confidence_interval_99}")

# Histogram
plt.figure(figsize=(10, 5))
plt.hist(diameters, bins=10, edgecolor='black', alpha=0.7)
plt.axvline(sample_mean, color='red', linestyle='--', label=f'Mean = {sample_mean:.2f}')
plt.axvline(confidence_interval_90[0], color='blue', linestyle='--', label='90% CI Lower')
plt.axvline(confidence_interval_90[1], color='blue', linestyle='--', label='90% CI Upper')
plt.title('Histogram of Diameters with 90% Confidence Interval')
plt.xlabel('Diameter')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Confidence interval error bar plot
plt.figure(figsize=(8, 2))
plt.errorbar(x=1, y=sample_mean, y_err=[[sample_mean - confidence_interval_99[0]], [confidence_interval_99[1] - sample_mean]],
             fmt='o', color='black', capsize=10, label='99% CI')
plt.errorbar(x=1.2, y=sample_mean, y_err=[[sample_mean - confidence_interval_90[0]], [confidence_interval_90[1] - sample_mean]],
             fmt='o', color='blue', capsize=10, label='90% CI')
plt.xlim(0.5, 2)
plt.xticks([])
plt.title('Confidence Intervals for Mean Diameter')
plt.ylabel('Diameter')
plt.legend()
plt.grid(True)
plt.show()
