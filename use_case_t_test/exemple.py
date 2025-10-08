import numpy as np
from scipy.stats import ttest_ind

x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)

stat, p_val = ttest_ind(x, y)

print(stat, p_val)
