import numpy as np
from scipy import stats

# Define your data for groups A and B
group_A_data = [
    [0.38, 0.76, 0.72],
    [0.34, 0.22, 0.42],
    [0.84, 0.72, 0.78],
    [0.38, 0.48, 0.64],
    [0.66, 0.54, 0.52]
]


data_A = np.concatenate(group_A_data)

mean_A = np.mean(data_A)
std_dev_A = np.std(data_A)

group_B_data = [
    [0.034115, 0.035814, 0.03498],
    [0.02669, 0.02298, 0.038103]
]


data_A = np.concatenate(group_A_data)
data_B = np.concatenate(group_B_data)

t_statistic, p_value = stats.ttest_ind(data_A, data_B)
mean_A = np.mean(data_A)
std_dev_A = np.std(data_A)
mean_B = np.mean(data_B)
std_dev_B = np.std(data_B)

print(f"Group A - Mean: {mean_A}, Standard Deviation: {std_dev_A}")
print(f"Group B - Mean: {mean_B}, Standard Deviation: {std_dev_B}")

#print(f"T-statistic: {t_statistic}")

print(f"P-value: {p_value}")

