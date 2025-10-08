import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# création des données
sns.set_style("darkgrid")

temps = np.arange(0, 100, 1)
variable = temps + np.random.normal(1, 1, 100)

# affichage d'un graphique avec deux sous graphiques
# un avec le temps et un avec la densité
fig, ax = plt.subplots(figsize=(13, 6), nrows=2, ncols=1)
ax[0].plot(temps, variable, label="Variable", color="dodgerblue")
ax[0].fill_between(
    x=temps,
    y1=variable,
    y2=[0] * len(temps),
    alpha=0.3,
    color="dodgerblue",
)
ax[0].set_title("Evolution de la variable dans le temps")
ax[0].set_xlabel("Temps")
ax[0].set_ylabel("Amplitude")
ax[0].legend()

sns.kdeplot(variable, fill=True, color="dodgerblue", alpha=0.3, ax=ax[1])
ax[1].set_xlabel("Variable")
ax[1].set_ylabel("Densité")
ax[1].legend()
ax[1].set_title("Densité")
fig.suptitle(
    "Distribution de la variable dans le temps & densité",
    fontweight="bold",
    fontsize=14,
)
plt.show()
