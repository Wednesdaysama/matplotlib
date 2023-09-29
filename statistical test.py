import numpy as np
from scipy import stats

# Define your data for groups A and B
group_A_data = [
    [0.02669,	0.02298,	0.038103










]
]

group_B_data = [
    [0.68,	0.66,	0.58








]
]

# Flatten the data to 1D arrays
data_A = np.concatenate(group_A_data)
data_B = np.concatenate(group_B_data)

# Perform the two-sample t-test
t_statistic, p_value = stats.ttest_ind(data_A, data_B)

# Print the results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")