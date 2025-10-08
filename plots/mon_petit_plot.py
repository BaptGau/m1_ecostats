import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# création des données
temps = np.arange(0, 100, 1)
variable = temps + np.random.normal(0, 5, 100)
variable_2 = temps + np.random.normal(0, 10, 100)

# plot
sns.set_style(style="darkgrid")
width, height = 12, 8
plt.figure(figsize=(width, height))
# plt.scatter(temps, variable) # nuage de points
plt.plot(temps, variable, color="#2a9d8f", marker="o", label="variable_1")  # courbe
# plt.plot(temps, variable_2, color="orangered", label="variable_2") # courbe

plt.title(label="Evolution of <variable> over <time>", fontweight="bold")
plt.xlabel("Temps")
plt.ylabel("Variable")
plt.grid(True)
plt.legend()
plt.show()
