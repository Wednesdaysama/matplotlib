import numpy as np
from scipy import stats

# Define data for groups A, B, C, and D
group_A_data = np.array([
    0.00149, 0.00155, 0.00158,
    0.00130, 0.00155, 0.00149,
    0.00124, 0.00180, 0.00140,
    0.00161, 0.00186, 0.00174,
    0.00146, 0.00174, 0.00124,
    0.00211, 0.00205, 0.00180
])

group_B_data = np.array([
    0.00126, 0.00104, 0.00096,
    0.00143, 0.00126, 0.00117,
    0.00105, 0.00090, 0.00071,
    0.00118, 0.00105, 0.00090
])

group_C_data = np.array([
    0.00055, 0.00078, 0.00096,
    0.00040, 0.00096, 0.00071,
    0.00130, 0.00084, 0.00087,
    0.00115, 0.00090, 0.00071,
    0.00090, 0.00124, 0.00133
])

group_D_data = np.array([
    0.00118, 0.00236, 0.00223,
    0.00105, 0.00068, 0.00130,
    0.00261, 0.00223, 0.00242,
    0.00118, 0.00149, 0.00199,
    0.00205, 0.00168, 0.00161
])

# Perform t-tests and print results
groups = [group_A_data, group_B_data, group_C_data, group_D_data]
group_names = ['Group A', 'Group B', 'Group C', 'Group D']

for i in range(len(groups)):
    for j in range(i + 1, len(groups)):
        t_statistic, p_value = stats.ttest_ind(groups[i], groups[j])
        print(f"Comparison between {group_names[i]} and {group_names[j]}:")
        print(f"  T-statistic: {t_statistic}")
        print(f"  P-value: {p_value}")
        print("\n")
