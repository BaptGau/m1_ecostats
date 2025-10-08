import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

variable = np.random.normal(0, 1, 100)
variable_2 = np.random.normal(5, 1, 100)

sns.set_style(style="darkgrid")

plt.figure(figsize=(12, 8))
plt.title("Density plot")
sns.kdeplot(variable, color="dodgerblue", label="fumeur")
sns.kdeplot(variable_2, fill=True, color="orangered", label="non fumeur")
plt.xlabel("Esperance de vie (age)")
plt.ylabel("Density")
plt.legend()
plt.show()
